"""Hash the actual publishable project files; exclude runtime/cache/private data."""
import hashlib,json,subprocess
from pathlib import Path
from datetime import datetime,timezone
ROOT=Path(__file__).resolve().parents[1]
files=subprocess.check_output(['git','ls-files','--cached','--others','--exclude-standard','-z'],cwd=ROOT).decode().split('\0')
index=json.loads((ROOT/'reports/ARTIFACT_INDEX.json').read_text());classifications={x['path']:x['classification'] for x in index['files']}
rows=[]
for name in sorted(set(files)):
 p=ROOT/name
 if not name or not p.is_file() or name=='reports/SUBMISSION_MANIFEST.json' or p.suffix=='.log':continue
 if name.startswith(('.git/','.venv/','node_modules/','.pitch_build/','wheelhouse/')):continue
 if p.stat().st_size>90_000_000:raise ValueError('Oversized generated file must not be uploaded: '+name)
 role=classifications.get(name,'PROJECT_SOURCE_OR_DOCUMENTATION')
 if name.startswith('docs/archive/'):role='HISTORICAL_DO_NOT_SUBMIT'
 elif name.startswith('data/audit/'):role='SYNTHETIC_REPRODUCTION_INPUT'
 elif name.startswith('00_SUBMISSION/'):role='CURRENT_SUBMISSION_MATERIAL'
 elif name.startswith('website/'):role='CURRENT_STATIC_SITE_OR_RETAINED_EXPORT'
 rows.append({'path':name,'role':role,'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
manifest={'generated_at_utc':datetime.now(timezone.utc).isoformat(),'source_commit':subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip(),'state':'AUDITED_PROTOTYPE_PORTAL_PENDING','author':'Kushagra Gupta','licence':'MIT for project source; third-party/runtime terms documented separately.','excluded':'Credentials, environments, DB images, package caches and large regenerated raw datasets.','fresh_clone_scope':json.loads((ROOT/'reports/clean_setup.json').read_text()),'file_count':len(rows),'total_bytes':sum(x['bytes'] for x in rows),'files':rows}
(ROOT/'reports/SUBMISSION_MANIFEST.json').write_text(json.dumps(manifest,indent=2)+'\n');print('Manifest:',len(rows),'files;',manifest['total_bytes'],'bytes.')
