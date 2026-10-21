"""Remove stale pre-SLC UDF failures from published timing results."""
import json
from pathlib import Path
r=json.loads(Path('results.json').read_text())
for label in ('small','full'):
    r.get('performance',{}).get(label,{}).pop('udf',None)
r['udf']={'status':'excluded','reason':'Python 3.12 SLC installed, but no successful UDF execution is published in this submission.'}
Path('results.json').write_text(json.dumps(r,indent=2)+'\n')
