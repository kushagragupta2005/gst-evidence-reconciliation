"""Compare frozen offline queue order with current SQL; no tuning or DB writes."""
import json
from pathlib import Path
from datetime import datetime,timezone
import pandas as pd
from src.db import connect
from src.evaluate_v2 import ordered_queue
ROOT=Path(__file__).resolve().parents[1]
c=connect(readonly=True)
try:rows=c.execute("SELECT FACTORY_ID,PERIOD_MONTH,SIGNAL_COUNT,WEAKEST_LINK_NORMALISED_GAP,ESTIMATED_TAX_EXPOSURE_INR FROM GST_EVIDENCE.V_RANKED_CASES WHERE STATUS='prioritise'").fetchall()
finally:c.close()
actual=pd.DataFrame(rows,columns=['factory_id','period_month','signals','weakest_link_normalised_gap','estimated_tax_exposure_inr']);actual['flagged']=True
frozen=pd.read_csv(ROOT/'reports/v3_c/held_out_predictions.csv')
comparisons=[]
for month,group in frozen.groupby('period_month'):
 keys=['signals','weakest_link_normalised_gap','estimated_tax_exposure_inr','factory_id']
 old=ordered_queue(group,keys);new=ordered_queue(actual[actual.period_month==month],keys)
 for k in [50,200]:
  a=old.head(k).factory_id.tolist();b=new.head(k).factory_id.tolist();labels=group.set_index('factory_id').is_cheat
  comparisons.append({'month':month,'k':k,'same_order':a==b,'common_ids':len(set(a)&set(b)),'offline_returned':len(a),'live_returned':len(b),'offline_true_cheats':int(labels.loc[a].sum()),'live_true_cheats':int(labels.loc[b].sum())})
r={'time_utc':datetime.now(timezone.utc).isoformat(),'scope':'Diagnostic replay after threshold repair, not a new held-out evaluation. Truth read only from local evaluator CSV, not database.','formula_finding':'SQL uses sum of maxima among firing source families; frozen evaluator uses maximum exposure across all feature rows. Primary family-count and weakest-link keys agree, but tertiary ranking semantics are not unified.','comparisons':comparisons}
(ROOT/'reports/ranking_alignment_audit.json').write_text(json.dumps(r,indent=2)+'\n');print('Compared live/offline monthly top-50/200 queues; differing orders:',sum(not x['same_order'] for x in comparisons))
