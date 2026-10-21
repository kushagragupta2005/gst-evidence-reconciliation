"""Export only public, measured result fields used by the static landing page."""
import json
from pathlib import Path
r=json.loads(Path('results.json').read_text())
data={
 'monthly_recall':r['factory_month']['recall'], 'monthly_fpr':r['factory_month']['fpr'],
 'queue_k':r['factory_queue']['k'], 'queue_size':r['factory_queue']['queue_size'],
 'queue_precision':r['factory_queue']['seed_c']['precision'],
 'top50_precision':r['precision_at_k']['50']['macro_precision'],
 'top200_precision':r['precision_at_k']['200']['macro_precision'],
 'seed':r['dataset']['seed'], 'factories':r['dataset']['factories'],
 'evidence_rows':r['performance']['full']['manifest']['raw_evidence_rows'],
 'ranked_raw_seconds':r['performance']['full']['unoptimised']['V_RANKED_CASES']['seconds'],
 'ranked_ledger_seconds':r['performance']['full']['optimised']['V_RANKED_CASES'][0]['seconds'],
 'robustness':{k:{'recall':v['factory_month']['recall'],'fpr':v['factory_month']['fpr']} for k,v in r['robustness']['variants'].items()},
}
Path('website/data.js').write_text('window.EVALUATION = '+json.dumps(data,indent=2)+';\n')
