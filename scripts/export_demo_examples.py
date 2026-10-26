"""Evaluator-only selection of label-free IDs for the static-site demo."""
import json
from pathlib import Path
import pandas as pd
from src.db import connect
p=pd.read_csv('reports/held_out_predictions.csv')
never=set(p.groupby('factory_id').flagged.max().loc[lambda x:~x].index)
candidates={
 'cheat':p[(p.is_cheat==1)&p.flagged&(p.scenario=='hidden_production')&(p.intensity==.3)&(p.evasive==0)],
 'decoy':p[p.factory_id.isin(never)&(p.signals==1)&(p.intensity==0)&(p.scenario!='honest')&(p.period_month>='2026-04')],
 'miss':p[(p.is_cheat==1)&~p.flagged]}
c=connect(readonly=True);examples={}
for kind,frame in candidates.items():
    row=frame.iloc[0].to_dict();fid,month=row['factory_id'],row['period_month']
    statement=c.execute(f"SELECT * FROM GST_EVIDENCE.V_ALL_EVIDENCE WHERE FACTORY_ID='{fid}' AND PERIOD_MONTH='{month}' ORDER BY CHECK_FAMILY LIMIT 20")
    evidence=[dict(zip([x.lower() for x in statement.column_names()],r)) for r in statement.fetchall()]
    # The officer interface receives identifiers and SQL evidence only. Evaluation labels
    # used to select these cases remain in this evaluator process.
    examples[kind]={'factory_id':fid,'period_month':month,'evidence':evidence}
c.close()
Path('reports/demo_cases.json').write_text(json.dumps(examples,indent=2,default=str)+'\n')
print({k:(v['factory_id'],v['period_month']) for k,v in examples.items()})
