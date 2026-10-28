"""Verify and restore only the allow-listed synthetic audit CSVs."""
import gzip,hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def restore():
 manifest=json.loads((ROOT/'data/audit/manifest.json').read_text())
 allowed={f'{prefix}/{seed}/{name}' for seed in ['v3_a','v3_b','v3_c'] for prefix,name in [('data','features.csv'),('reports','held_out_predictions.csv')]}
 for entry in manifest['files']:
  if entry['source'] not in allowed:raise ValueError('Unexpected evidence destination')
  seed=Path(entry['source']).parts[1]
  if entry['archive']!=f"data/audit/{seed}/{Path(entry['source']).name}.gz":raise ValueError('Unexpected archive path')
  packed=(ROOT/entry['archive']).read_bytes()
  if hashlib.sha256(packed).hexdigest()!=entry['archive_sha256']:raise ValueError('Archive hash mismatch')
  raw=gzip.decompress(packed)
  if hashlib.sha256(raw).hexdigest()!=entry['sha256']:raise ValueError('Evidence hash mismatch')
  dest=ROOT/entry['source'];dest.parent.mkdir(parents=True,exist_ok=True)
  if dest.exists() and dest.read_bytes()!=raw:raise ValueError('Existing CSV differs; preserve it and investigate before restoring')
  if not dest.exists():dest.write_bytes(raw)
 return manifest
if __name__=='__main__':
 r=restore();print(f"Verified {len(r['files'])} archived synthetic audit inputs.")
