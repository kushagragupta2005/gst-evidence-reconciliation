import csv,hashlib,json
from pathlib import Path
from scripts.restore_audit_evidence import restore
restore()
out={'method':'Approximate one-sided 95% rule-of-three upper bound (3/N) after zero wrong-clear factories. Unit: factory with at least one active cheat month. Assumes independent factory outcomes; conditional on this synthetic generator, not a real-world safety bound. Not a cluster-bootstrap confidence interval.','seeds':{}}
for seed in ['v3_b','v3_c']:
 p=Path(f'reports/{seed}/held_out_predictions.csv');d=json.loads(Path(f'reports/{seed}_dispositions.json').read_text())
 with p.open() as f: active={r['factory_id'] for r in csv.DictReader(f) if r['is_cheat']=='1'}
 assert d['wrong_clears_active_cheat_months']==0
 out['seeds'][seed]={'wrong_clear_factories':0,'active_cheat_factories':len(active),'approximate_upper_95':3/len(active),'active_cheat_months':d['active_cheat_months'],'predictions_sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
Path('reports/wrong_clear_bounds.json').write_text(json.dumps(out,indent=2)+'\n')
print(out)
