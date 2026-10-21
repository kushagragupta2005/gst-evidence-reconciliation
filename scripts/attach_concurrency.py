import json
from pathlib import Path
r=json.loads(Path('results.json').read_text());r['concurrency']=json.loads(Path('reports/concurrency.json').read_text())
Path('results.json').write_text(json.dumps(r,indent=2)+'\n')
