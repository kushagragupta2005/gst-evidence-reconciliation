"""Write measured timing claims from canonical results.json."""
import json
import statistics
from pathlib import Path
r=json.load(open('results.json'))
lines=['## Exasol workload timings on a MacBook','', 'These are workload timings on the project author\'s MacBook, using Exasol Personal locally. Raw checks aggregate count and absolute gap, forcing evaluation. Optimised queries use a batch-materialised monthly ledger, then run three sequential repetitions (median below, all samples in results.json). Query-result caching was disabled for the comparison. Data pages can be warm; neither cold-page control nor concurrency isolation was enforced. The cache build is reported separately and must rerun after every source update.', '', '| Dataset | Factories | Raw evidence rows | CSV load seconds | Ledger refresh seconds |','|---|---:|---:|---:|---:|']
for label in ['small','full']:
    b=r['performance'].get(label)
    if not b: continue
    if label=='small':
        b['load_seconds']=r['performance']['small_unoptimised']['load_seconds']
    lines.append(f"| {label} | {b['manifest']['factories']:,} | {b['manifest']['raw_evidence_rows']:,} | {sum(b.get('load_seconds',{}).values()):.3f} | {b['cache_refresh_seconds']:.3f} |")
lines+=['','| View | Small raw (s) | Small cached median (s) | Full raw (s) | Full cached median (s) |','|---|---:|---:|---:|---:|']
for view in r['performance']['small']['unoptimised']:
    values=[]
    for label in ['small','full']:
        b=r['performance'].get(label)
        values += [f"{b['unoptimised'][view]['seconds']:.3f}",f"{statistics.median(x['seconds'] for x in b['optimised'][view]):.3f}"] if b else ['pending','pending']
    lines.append('| '+view+' | '+' | '.join(values)+' |')
lines+=['','### pandas comparison','','The two slowest individual checks in each raw SQL run are reproduced in pandas using the same CSVs, threshold, aggregation and gap checksum. CSV read time and computation time are separate. pandas uses host memory; Exasol runs in a local VM and raw SQL also resolves the shared ledger. These are workload timings on the project author\'s MacBook, not an engine superiority claim. pandas is faster on some checks.','','| Dataset / check | CSV read (s) | pandas compute (s) | pandas total (s) | Exasol raw (s) |','|---|---:|---:|---:|---:|']
for label in ['small','full']:
    for view,m in r['performance'].get(label,{}).get('pandas',{}).items():
        lines.append(f"| {label} / {view} | {m['csv_read_seconds']:.3f} | {m['compute_seconds']:.3f} | {m['total_seconds']:.3f} | {m['exasol_raw_seconds']:.3f} |")
lines+=['','### Profile and optimisation','','Saved session profiles: [small](reports/profile_small.json), [full](reports/profile_full.json). The profile exposes repeated grouping, joining and sorting through the shared ledger. Materialising that ledger once amortises this work across the six signals and case ranking. Counts and absolute-gap checksums are asserted unchanged before reporting any timings. [Exasol profiling documentation](https://docs.exasol.com/db/latest/database_concepts/profiling.htm).','','Window functions implement prior-closing continuity and a trailing power baseline. A historical-only median/MAD Python UDF is included in sql/30_baseline_udf.sql, but execution failed because this Exasol installation lacks a Python script-language container. It is optional, not used for flagging, and no UDF speedup is claimed.','','### Why an in-memory analytic database','','This workload repeatedly scans numeric evidence columns, groups shipments and payments by factory and period, joins independent ledgers, and evaluates window functions over annual histories. Exasol keeps these operations close to the primary data and makes the same SQL evidence available to scoring, the dashboard and guarded follow-ups. Batch materialisation makes repeated reads cheaper while preserving a traceable SQL path to raw evidence. The measured local VM results establish feasibility at this synthetic scale; they do not establish a speed advantage over every alternative or production latency.']
Path('results.json').write_text(json.dumps(r,indent=2)+'\n')
text='\n'.join(lines)+'\n';Path('reports/performance.md').write_text(text)
p=Path('README.md');s=p.read_text();marker='<!-- PERFORMANCE START -->'
if marker in s:
    a,z=s.split(marker,1);_,b=z.split('<!-- PERFORMANCE END -->',1);s=a+marker+'\n'+text+'<!-- PERFORMANCE END -->'+b
else:s+='\n'+marker+'\n'+text+'<!-- PERFORMANCE END -->\n'
p.write_text(s)
