"""Recompute current site headline metrics and inventory every displayed numeric value."""
import hashlib,json,math,statistics
from pathlib import Path
import pandas as pd
import numpy as np
from src.evaluate import clustered_metrics
from src.evaluate_v2 import factory_queue,choose_threshold,monthly_frame,calibration_queue
ROOT=Path(__file__).resolve().parents[1]
from scripts.restore_audit_evidence import restore
restore()
def load(p):return json.loads((ROOT/p).read_text())
rows=[];checks=[]
def walk(x,source,pointer='',status='Artifact value; no new timing run'):
 if isinstance(x,bool):return
 if isinstance(x,(int,float)):
  rows.append((source,pointer,repr(x),status))
 elif isinstance(x,dict):
  for k,v in x.items():walk(v,source,pointer+'/'+str(k),status)
 elif isinstance(x,list):
  for i,v in enumerate(x):walk(v,source,pointer+'/'+str(i),status)
a_result=load('reports/v3_a_calibration.json')
a_frame=pd.read_csv(ROOT/'reports/v3_a/held_out_predictions.csv').set_index(['factory_id','period_month'])
a_features=pd.read_csv(ROOT/'data/v3_a/features.csv');a_features.columns=a_features.columns.str.lower()
a_matrix=a_features.pivot_table(index=['factory_id','period_month'],columns='source_family',values='severity',aggfunc='max').fillna(0).reindex(a_frame.index)
selected,curve=choose_threshold(a_frame,a_matrix)
assert selected==a_result['protocol']['threshold'] and curve==a_result['protocol']['calibration']
a_truth=a_frame[['is_cheat','scenario','intensity','evasive','discrepancy_class','explanation','taxpayer_explanation']]
a_monthly,_=monthly_frame(a_truth,a_matrix,a_features,selected)
selected_k,k_curve=calibration_queue(a_monthly)
assert selected_k==a_result['factory_queue']['k'] and k_curve==a_result['factory_queue']['seed_a_calibration']
checks.append('v3_a: threshold 0.05 and K=3 recomputed from calibration inputs only; B/C were not used to choose them.')
for seed,path in [('v3_b','results.json'),('v3_c','reports/v3_c_results.json')]:
 r=load(path);frame=pd.read_csv(ROOT/f'reports/{seed}/held_out_predictions.csv')
 for level,df in [('factory_month',frame),('factory',factory_queue(frame,r['factory_queue']['k']))]:
  actual=clustered_metrics(df)
  assert actual==r[level],(seed,level)
  walk(r[level],path,'/'+level,'Recomputed counts, ratios and factory-cluster bootstrap intervals')
 for key,p in r['prevalence_adjusted_precision'].items():
  prev=p['assumed_prevalence'];value=r['factory_month']['recall']*prev/(r['factory_month']['recall']*prev+r['factory_month']['fpr']*(1-prev))
  assert math.isclose(value,p['precision'],rel_tol=1e-12)
  walk(p,path,'/prevalence_adjusted_precision/'+key,'Recomputed analytic reweighting')
 for key in ['dataset','protocol','factory_queue']:
  if key=='protocol':walk({k:r[key][k] for k in ['threshold','months_per_factory','train_seed','held_out_seed']},path,'/'+key,'Frozen protocol / source manifest')
  elif key=='factory_queue':walk({'k':r[key]['k'],'queue_size':r[key]['queue_size']},path,'/'+key,'Recomputed queue agrees')
  else:walk(r[key],path,'/'+key,'Generator manifest; not real data')
 d=load(f'reports/{seed}_dispositions.json');b=load('reports/wrong_clear_bounds.json')['seeds'][seed]
 assert int(frame.loc[frame.is_cheat==1,'factory_id'].nunique())==b['active_cheat_factories']
 assert int(frame.is_cheat.sum())==d['active_cheat_months']==b['active_cheat_months']
 assert d['wrong_clears_active_cheat_months']==b['wrong_clear_factories']==0
 assert b['approximate_upper_95']==3/b['active_cheat_factories']
 checks.append(f'{seed}: monthly and factory confusion matrices, all displayed CIs, prevalence precision and denominator counts reproduce exactly.')
for file in ['reports/v3_b_dispositions.json','reports/v3_c_dispositions.json','reports/wrong_clear_bounds.json','reports/site_ablation.json','reports/benchmark_current_reader.json','reports/live_smoke.json','reports/site_examples.json']:
 walk(load(file),file)
# Historical scale headline only; no new claim about its elapsed-time provenance.
walk(load('reports/benchmark_full.json')['manifest']['raw_evidence_rows'],'reports/benchmark_full.json','/manifest/raw_evidence_rows','Historical DEV manifest only; not a fresh scale run')
a=load('reports/site_ablation.json')
for seed in a['seeds']:
 r=load('results.json' if seed=='v3_b' else 'reports/v3_c_results.json')
 assert a['seeds'][seed]['checks']['all_checks']['recall']==r['factory_month']['recall']
 for check,v in a['seeds'][seed]['checks'].items():
  assert v['recall']==v['tp']/(v['tp']+v['fn']) and v['fpr']==v['fp']/(v['fp']+v['tn'])
bench=load('reports/benchmark_current_reader.json')
for v in bench['checks'].values():
 for engine in ['exasol','duckdb']:assert statistics.median(v[engine+'_seconds'])==v[engine+'_median_seconds']
live=load('reports/live_smoke.json')['parallel_ask']
for name,q in [('p50_seconds',.5),('p95_seconds',.95)]:assert math.isclose(float(np.quantile(live['latencies_seconds'],q)),live[name],rel_tol=1e-12)
intro='''# Site numbers audit

Scope: current displayed metrics, both seed selections, all recorded case/follow-up evidence and measured API artifacts. The single-page-to-multi-page audit began at db0e649; sources refreshed by the later threshold-repair audit are inventoried at their current values. The inventory below preserves original precision; page formatting is a separate concern. Numeric strings in recorded SQL rows are listed too. Layout dimensions and dates are not measurements.

## Findings and corrections

- No mismatch was found in the monthly/factory confusion matrices, ratios, displayed bootstrap intervals, prevalence formula, ablation ratios, median comparison timings or concurrent p95 arithmetic.
- V3-B and V3-C are separate real saved runs. Rounded C values (81.2%, 2.3%, 85.0%) must not be attributed to B (81.1%, 2.2%, 85.6%). Every result group now names its seed.
- Zero of 720 counts factories with at least one active cheat month. Zero of 3,950 counts active cheat months in V3-C; V3-B has 3,981. These are different units, not conflicting results. The 3/N approximate upper bound uses factories and assumes their outcomes are independent. It is not a measured cluster-bootstrap interval or real-world safety guarantee.
- The prevalence table was ordered by object keys, not probability, and its old generic numeric formatter hid differences by rounding probabilities/precision to two decimals. Sort by numeric assumed prevalence and display probabilities as percentages. Analytic reweighting assumes recall/FPR transfer across prevalence; it is not a regenerated low-prevalence experiment.
- Leave-one-check-out ablation is a post-hoc conditional contribution with the other checks still present. Small loss after removing material/output does not mean that evidence is useless: other production checks and families can still satisfy the threshold. Intervals are unmeasured.
- The case caption once used one gap sign for every check. Bank checks use flows minus invoices; other displayed checks use expected minus observed. The corrected wording is retained.
- Current benchmark medians and concurrency p95 reproduce from recorded repeats; elapsed timings cannot be regenerated from arithmetic. They remain measured artifacts from their stated dates and machines, not new runs during this audit. Exasol/DuckDB counts and gap checksums were previously matched; physical plans and ingestion coverage differ. DuckDB was faster in the recorded comparison.
- Historical 20,978,945 rows come from an older DEV manifest. Its run timestamp/source SHA are unavailable; do not substitute a later artifact commit date. It remains historical, not fresh.
- Case/evidence values and note validation are recorded observations. The new home line chart uses the complete recorded dispatch response for one factory, not interpolated or invented evidence.
- Per-artifact commit/date metadata describe when a file was committed. Explicit run timestamps are shown separately where the artifact contains one. Missing run timestamps stay unavailable.

## Reproduction

`PYTHONPATH=. .venv/bin/python scripts/audit_site_numbers.py` recomputes monthly/factory confidence intervals from the local held-out prediction CSVs (factory-cluster bootstrap, fixed seed and iterations), ratios, denominator counts and timing summaries. `scripts/site_ablation.py` separately replays the frozen feature files; its feature hashes and baseline matrices were checked. No detector thresholds were changed. Those local CSVs are intentionally not needed to render the deployed site.

## Verified groups

'''
intro+='\n'.join('- '+x for x in checks)
intro+='\n\n## Complete numeric inventory\n\nSource file | JSON field | Exact value | Verification scope\n---|---|---|---\n'
# Include numeric strings inside recorded row payloads, as the DB serialiser can preserve DECIMAL text.
def numeric_strings(x,source,pointer=''):
 if isinstance(x,str):
  try:float(x)
  except ValueError:return
  rows.append((source,pointer,x,'Recorded decimal string; original value preserved'))
 elif isinstance(x,dict):
  for k,v in x.items():numeric_strings(v,source,pointer+'/'+str(k))
 elif isinstance(x,list):
  for i,v in enumerate(x):numeric_strings(v,source,pointer+'/'+str(i))
numeric_strings(load('reports/site_examples.json'),'reports/site_examples.json')
intro+='\n'.join(f'`{s}` | `{p}` | {v} | {status}' for s,p,v,status in rows)+'\n'
(ROOT/'docs/NUMBERS_AUDIT.md').write_text(intro)
print(f'All recomputed groups match. Inventoried {len(rows)} numeric fields.')
