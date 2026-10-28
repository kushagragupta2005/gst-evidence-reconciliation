"""Commit compact synthetic scoring inputs so numeric audits work after cloning."""
import gzip,hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
manifest={'scope':'Synthetic A calibration and B/C held-out features and evaluator predictions only; no taxpayer data or credentials. Features are detector outputs; labels remain evaluator-only.','files':[]}
for seed in ['v3_a','v3_b','v3_c']:
 for source in [f'data/{seed}/features.csv',f'reports/{seed}/held_out_predictions.csv']:
  p=ROOT/source;raw=p.read_bytes();out=ROOT/'data/audit'/seed/(p.name+'.gz');out.parent.mkdir(parents=True,exist_ok=True)
  out.write_bytes(gzip.compress(raw,mtime=0))
  manifest['files'].append({'source':source,'archive':str(out.relative_to(ROOT)),'sha256':hashlib.sha256(raw).hexdigest(),'archive_sha256':hashlib.sha256(out.read_bytes()).hexdigest(),'rows':raw.count(b'\n')-1,'bytes':len(raw),'compressed_bytes':out.stat().st_size})
(ROOT/'data/audit/manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
print('Packaged',sum(x['compressed_bytes'] for x in manifest['files']),'bytes of synthetic audit evidence.')
