"""Preserve the prior seed-B result before a v2 run rewrites results.json."""
import argparse
import json
from pathlib import Path

p=argparse.ArgumentParser();p.add_argument('--input',default='results.json');p.add_argument('--output',default='reports/results_v1_seed_b.json');a=p.parse_args()
source=json.loads(Path(a.input).read_text())
if source.get('protocol',{}).get('held_out_seed') != 20261020:
    raise SystemExit('Expected the committed seed-B result before creating the v1 archive.')
Path(a.output).parent.mkdir(parents=True,exist_ok=True)
Path(a.output).write_text(json.dumps(source,indent=2)+'\n')
