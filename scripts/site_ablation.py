"""Post-hoc leave-one-check-out replay of frozen held-out feature files."""
import hashlib,json
from pathlib import Path
import pandas as pd
ROOT=Path(__file__).resolve().parents[1]
out={'scope':'Post-hoc diagnostic; frozen threshold and two-family rule, no retuning. Point estimates only; no ablation confidence intervals.','seeds':{}}
for seed,path in [('v3_b','results.json'),('v3_c','reports/v3_c_results.json')]:
 r=json.loads((ROOT/path).read_text()); f=ROOT/f'data/{seed}/features.csv'
 assert hashlib.sha256(f.read_bytes()).hexdigest()==r['provenance']['feature_sha256']
 features=pd.read_csv(f); pred=pd.read_csv(ROOT/f'reports/{seed}/held_out_predictions.csv'); idx=['factory_id','period_month']
 truth=pred.set_index(idx).is_cheat.astype(bool)
 measured={}
 for omit in [None]+sorted(features.CHECK_FAMILY.unique().tolist()):
  rows=features[(features.SEVERITY>r['protocol']['threshold']) & (features.CHECK_FAMILY!=omit)]
  counts=rows.groupby(['FACTORY_ID','PERIOD_MONTH']).SOURCE_FAMILY.nunique(); counts.index.names=idx
  flags=counts.reindex(truth.index,fill_value=0)>=2
  tp=int((flags & truth).sum()); fp=int((flags & ~truth).sum()); fn=int((~flags & truth).sum()); tn=int((~flags & ~truth).sum())
  measured[omit or 'all_checks']={'tp':tp,'fp':fp,'fn':fn,'tn':tn,'recall':tp/(tp+fn),'fpr':fp/(fp+tn)}
 assert all(measured['all_checks'][k]==r['factory_month'][k] for k in ['tp','fp','fn','tn'])
 out['seeds'][seed]={'feature_sha256':r['provenance']['feature_sha256'],'checks':measured}
(ROOT/'reports/site_ablation.json').write_text(json.dumps(out,indent=2)+'\n')
print('Both baseline confusion matrices match committed results exactly.')
