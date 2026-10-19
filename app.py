"""Bounded read-only Exasol dashboard with auditable evidence and follow-ups."""
import json
import os
import re
from pathlib import Path
import pandas as pd
import streamlit as st
from src.db import connect
from src.case_notes import build_case_note,generate_llm_note,validate_note,numbers_match_evidence
from src.followup import plan_question,execute_followup

st.set_page_config(page_title='GST Evidence Reconciliation',layout='wide')
st.title('GST Evidence Reconciliation')
st.caption('Kushagra Gupta · solo project · synthetic evidence · human review required')

@st.cache_data(ttl=30)
def query(sql):
    c=connect(readonly=True)
    try:
        stmt=c.execute(sql)
        return pd.DataFrame(stmt.fetchall(),columns=[x.lower() for x in stmt.column_names()])
    finally:c.close()

@st.cache_data
def demo_presets():
    p=pd.read_csv('reports/held_out_predictions.csv')
    never=set(p.groupby('factory_id').flagged.max().loc[lambda x:~x].index)
    selections={
      'Planted cheat':p[(p.is_cheat==1)&p.flagged&(p.scenario=='hidden_production')&(p.intensity==.3)&(p.evasive==0)],
      'Honest decoy':p[p.factory_id.isin(never)&(p.signals==1)&(p.intensity==0)&(p.scenario!='honest')&(p.period_month>='2026-04')],
      'Missed cheat':p[(p.is_cheat==1)&~p.flagged],
    }
    return {k:g.iloc[0].to_dict() for k,g in selections.items() if len(g)}

results=json.loads(Path('results.json').read_text())
presets=demo_presets()
mode=st.sidebar.radio('Inspect a recorded example',list(presets)+['Manual factory'])
st.sidebar.caption('Curated examples from held-out labels. Labels select demo examples only; SQL determines flags.')
if mode=='Manual factory':
    fid=st.sidebar.text_input('Factory ID','F000006').upper()
    month=st.sidebar.selectbox('Month',[f'2026-{i:02}' for i in range(1,13)])
    demo=None
else:
    demo=presets[mode];fid=demo['factory_id'];month=demo['period_month']
if not re.fullmatch(r'F\d{6}',fid):st.error('Use F followed by six digits.');st.stop()

case_tab,ask_tab,results_tab,problem_tab=st.tabs(['Factory case','Ask a follow-up','Evaluation & scale','Problem & limits'])
try:
    timeline=query(f"SELECT PERIOD_MONTH,SIGNAL_COUNT,TOTAL_ABSOLUTE_GAP,STATUS FROM GST_EVIDENCE.V_RANKED_CASES WHERE FACTORY_ID='{fid}' ORDER BY PERIOD_MONTH LIMIT 12")
    evidence=query(f"SELECT FACTORY_ID,PERIOD_MONTH,CHECK_FAMILY,SOURCE_FAMILY,EXPECTED,OBSERVED,GAP,SEVERITY,EVIDENCE,DISCREPANCY_CLASS FROM GST_EVIDENCE.V_ALL_EVIDENCE WHERE FACTORY_ID='{fid}' AND PERIOD_MONTH='{month}' ORDER BY CHECK_FAMILY LIMIT 20")
    features=query(f"SELECT PERIOD_MONTH,CHECK_FAMILY,SOURCE_FAMILY,SEVERITY FROM GST_EVIDENCE.V_FEATURES WHERE FACTORY_ID='{fid}' ORDER BY PERIOD_MONTH,CHECK_FAMILY LIMIT 100")
except Exception as error:
    st.error('Start Exasol and run make reproduce to load data. Configure an existing read-only account as described in README.')
    st.caption(type(error).__name__);st.stop()

with case_tab:
    st.subheader(f'{fid} · {month}')
    selected=timeline[timeline.period_month==month]
    if selected.empty:st.warning('No rows for this factory and month.');st.stop()
    state=selected.iloc[0];a,b,c=st.columns(3)
    a.metric('SQL status',state['status']);b.metric('Source families',int(state.signal_count));c.metric('Calibrated ratio threshold',str(results['protocol']['threshold']))
    st.caption('Production combines material, power and stock. Movement, supplier and financial evidence count separately. Severity is a discrepancy ratio, not a probability of fraud.')
    if demo:
        st.info('Synthetic scenario: '+demo['scenario'].replace('_',' '))
    if mode=='Honest decoy':
        st.success('Why this honest factory was not prioritised: only a single source family crosses the threshold in this month; no month reaches the required corroboration rule. The planted operating change is legitimate. It remains reviewable, not legally cleared.')
        st.caption(str(demo['explanation']))
    if mode=='Missed cheat':
        st.warning('Known miss: the planted cheat is absent from this monthly priority queue because fewer than two source families exceed the frozen threshold. Ground truth is shown for evaluation only.')
    st.markdown('**Evidence rows returned by Exasol**')
    if not evidence.empty:
        display=evidence.copy();display['unit']=display.check_family.map(lambda x:'INR' if x.startswith('bank_') else 'kg')
        st.dataframe(display.drop(columns=['factory_id','period_month']),hide_index=True,width='stretch')
        rows=evidence.rename(columns={'period_month':'month'}).to_dict('records')
        note=build_case_note(fid,rows);note_mode='Deterministic fallback (no LLM API call)'
        use_llm=bool(os.getenv('OPENAI_API_KEY'))
        if st.button('Write note with LLM',disabled=not use_llm):
            try:
                note=generate_llm_note(rows);note_mode='LLM note, numerically validated'
            except Exception as error:st.warning(str(error));note_mode='Deterministic fallback after LLM failure'
        st.markdown('**Evidence-based case note**');st.caption(note_mode)
        if validate_note(note,rows):
            st.success('Validator PASS · every number matches its evidence field');st.write(note)
        else:st.error('Validator REJECT · note withheld')
        if st.button('Demonstrate tampered-note rejection'):
            tampered=note+' Unsupported amount 987654321.123.'
            if not validate_note(tampered,rows):st.error('Validator REJECT · tampered amount is unsupported. Original evidence is unchanged.')
            else:st.error('Unexpected validator result; investigate before use.')
    else:st.info('No discrepancy exceeds the calibrated threshold in this month.')
    st.markdown('**Evidence timeline**')
    st.dataframe(timeline,hide_index=True,width='stretch')
    contributions=features.copy();contributions['severity']=pd.to_numeric(contributions.severity)
    chart=contributions.groupby(['period_month','source_family']).severity.max().unstack(fill_value=0)
    st.line_chart(chart)
    with st.expander('Per-signal contributions, including signals below threshold'):
        st.dataframe(contributions,hide_index=True,width='stretch')
    with st.expander('Ranked monthly queue (up to 50 factories)'):
        st.dataframe(query(f"SELECT FACTORY_ID,PERIOD_MONTH,SIGNAL_COUNT,TOTAL_ABSOLUTE_GAP,STATUS FROM GST_EVIDENCE.V_RANKED_CASES WHERE PERIOD_MONTH='{month}' AND STATUS='prioritise' ORDER BY TOTAL_ABSOLUTE_GAP DESC,FACTORY_ID LIMIT 50"),hide_index=True,width='stretch')

with ask_tab:
    st.subheader('Ask a follow-up')
    st.caption('Guarded read-only Exasol SQL tool · fixed SELECT templates · allow-listed views · maximum 200 rows')
    question=st.text_input('Question',f'show the dispatch gap by month for factory {fid}',key='question_'+fid)
    enable_llm=st.checkbox('Use LLM to interpret and summarise',disabled=not bool(os.getenv('OPENAI_API_KEY')))
    if not os.getenv('OPENAI_API_KEY'):st.info('Deterministic fallback active. No LLM or MCP call is claimed; this uses the permitted guarded SQL alternative.')
    if st.button('Run follow-up'):
        try:
            sql=plan_question(question,fid,enable_llm)
            c=connect(readonly=True)
            try:answer=execute_followup(c,sql)
            finally:c.close()
            st.code(sql,language='sql');st.dataframe(answer,hide_index=True,width='stretch')
            if enable_llm:
                from openai import OpenAI
                response=OpenAI().responses.create(model=os.getenv('OPENAI_MODEL','gpt-6-astra'),store=False,instructions='Summarise only the returned evidence table in a short neutral sentence. Use no numbers or additional facts. Do not decide fraud or flagging.',input=json.dumps(answer,default=str))
                if numbers_match_evidence(response.output_text,answer):st.write(response.output_text)
                else:st.warning('Summary withheld by number validator. The SQL table remains authoritative.')
            else:st.write('Returned the requested evidence directly from Exasol. The SQL ranking is unchanged.')
        except Exception as error:st.error(str(error))

with results_tab:
    st.subheader('Held-out results, including errors')
    x,y,z=st.columns(3);x.metric('Monthly recall',f"{results['factory_month']['recall']:.2%}");y.metric('Monthly FPR',f"{results['factory_month']['fpr']:.2%}");z.metric('Missed cheat months',results['misses']['factory_months'])
    st.warning(f"Annual factory FPR is {results['factory']['fpr']:.2%}. This operating point is unsuitable for operational taxpayer targeting. Results are synthetic scenario recovery only.")
    st.caption('Threshold selected on seed A; results reported on seed B. Monthly review queues approximate a weekly workload. Confidence intervals do not capture generator bias.')
    full=results.get('performance',{}).get('full')
    if full:
        st.metric('Raw evidence rows measured in Exasol',f"{full['manifest']['raw_evidence_rows']:,}")
        st.caption(f"CSV import: {sum(full.get('load_seconds',{}).values()):.2f} s. Scale run is separate from the held-out evaluation; demo database has been restored to seed B.")
        st.dataframe([{'view':k,'raw_seconds':v['seconds'],'ledger_seconds':full['optimised'][k][0]['seconds']} for k,v in full['unoptimised'].items()],hide_index=True,width='stretch')
    st.image('reports/recall_fpr.png');st.dataframe(pd.DataFrame(results['misses']['examples']),hide_index=True)
    with st.expander('All recorded metrics and confidence intervals'):st.json(results)

with problem_tab:
    st.subheader('The problem')
    problem=Path('README.md').read_text().split('\n> ',1)[1].split('\n',1)[0];st.write(problem)
    st.subheader('Limits and next validation')
    st.write('Synthetic data only. Human review is required. Power and bank records require lawful, authorised access and privacy safeguards. Distinct data sources can still be correlated. The model never decides flags. AI coding assistants helped build the implementation and submission materials.')
    st.write('Germany: a proposed adaptation of evidence reconciliation, requiring local tax rules and independent validation. No German statistics or deployment are claimed.')
