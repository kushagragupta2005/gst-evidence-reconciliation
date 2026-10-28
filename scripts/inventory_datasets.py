"""Inventory actual current CSVs and distinguish older manifest-only records."""
import csv,hashlib,json
from pathlib import Path
from src.generate import TABLES
ROOT=Path(__file__).resolve().parents[1]
report={'scope':'Current V3 CSV headers, counts and hashes inspected locally; historical entries are manifests only, not freshly executed. Every dataset is synthetic.','current':{},'historical':{}}
for seed in ['v3_a','v3_b','v3_c']:
 folder=ROOT/'data'/seed;manifest=json.loads((folder/'manifest.json').read_text());items={}
 for table in TABLES:
  path=folder/(table+'.csv');raw=path.read_bytes();header=next(csv.reader([raw.split(b'\n',1)[0].decode()]))
  count=raw.count(b'\n')-1;assert count==manifest['rows'][table]
  assert header==TABLES[table].split(',')
  items[table]={'rows':count,'columns':header,'column_count':len(header),'sha256':hashlib.sha256(raw).hexdigest(),'bytes':len(raw)}
 with (folder/'truth.csv').open() as f:truth=list(csv.DictReader(f))
 distributions={}
 for level,data in [('factory_month',truth),('factory',list({r['factory_id']:r for r in truth}.values()))]:
  # Factory scenario/intensity/evasive are constant; active is_cheat varies by month.
  for field in ['scenario','intensity','evasive']:
   tally={}
   for row in data:tally[row[field]]=tally.get(row[field],0)+1
   distributions[level+'.'+field]=tally
 active_by_month={}
 for row in truth:
  active_by_month[row['period_month']]=active_by_month.get(row['period_month'],0)+int(row['is_cheat'])
 report['current'][seed]={'manifest':manifest,'tables':items,'distributions':distributions,'active_cheat_months_by_period':active_by_month}
for folder in (ROOT/'data').iterdir():
 path=folder/'manifest.json'
 if folder.is_dir() and folder.name not in report['current'] and folder.name!='audit' and path.exists():report['historical'][folder.name]={'status':'historical/dev manifest only','manifest':json.loads(path.read_text())}
(ROOT/'reports/dataset_inventory.json').write_text(json.dumps(report,indent=2)+'\n')
print('Validated V3-A/B/C raw table headers and row counts; inventoried historical manifests separately.')
