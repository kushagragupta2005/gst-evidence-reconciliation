"""Measure eight simultaneous bounded read-only follow-up queries against Exasol."""
import concurrent.futures
import json
import statistics
import time
from pathlib import Path
from src.db import connect
from src.followup import compile_plan, execute_followup

def one(factory_id):
    sql=compile_plan({'intent':'dispatch','factory_id':factory_id})
    started=time.perf_counter(); conn=connect(readonly=True)
    try: rows=execute_followup(conn,sql)
    finally: conn.close()
    return {'factory_id':factory_id,'seconds':time.perf_counter()-started,'rows':len(rows),'sql':sql}

def run():
    ids=[f'F{i:06}' for i in range(1,9)]
    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as pool:
        results=list(pool.map(one,ids))
    latency=sorted(row['seconds'] for row in results)
    report={'queries':8,'parallel_workers':8,'intent':'dispatch gap by month','latencies_seconds':results,
            'p50_seconds':statistics.median(latency),'p95_seconds':latency[round(.95*(len(latency)-1))],
            'definition':'One simultaneous guarded SELECT per connection, including connect, query and result fetch. Local workload timing on a MacBook; not an isolated server benchmark.'}
    Path('reports/concurrency.json').write_text(json.dumps(report,indent=2)+'\n')
    return report

if __name__=='__main__': print(json.dumps(run(),indent=2))
