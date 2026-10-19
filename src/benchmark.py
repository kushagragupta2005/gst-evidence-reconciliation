"""Measure real Exasol workloads, preserving raw and optimized timings."""
import argparse
import json
import time
from pathlib import Path
from src.db import connect,execute_file
from src.load_and_score import load,VIEWS


def timed(conn,query):
    start=time.perf_counter();rows=conn.execute(query).fetchall()
    return {'seconds':time.perf_counter()-start,'rows':[[float(v) if hasattr(v,'as_tuple') else v for v in row] for row in rows]}

def benchmark(data,label,do_load=True):
    result=load(data,None) if do_load else {'manifest':json.loads((Path(data)/'manifest.json').read_text())}
    if not do_load and Path(f"reports/benchmark_{label}.json").exists():
        previous=json.loads(Path(f"reports/benchmark_{label}.json").read_text())
        for key in ("load_seconds","actual_rows","join_sanity"):
            if key in previous:result[key]=previous[key]
    c=connect()
    c.execute("ALTER SESSION SET QUERY_CACHE='OFF'")
    result["query_result_cache"]="OFF"
    execute_file(c,'sql/10_checks.sql')
    threshold=json.load(open('results.json'))['protocol']['threshold']
    c.execute(f'UPDATE GST_EVIDENCE.SETTINGS SET THRESHOLD={threshold}')
    result['measurement_threshold']=threshold
    result['unoptimised']={}
    queries={view:f'SELECT COUNT(*),SUM(ABS({"TOTAL_ABSOLUTE_GAP" if view=="V_RANKED_CASES" else "GAP"})) FROM GST_EVIDENCE.{view}' for view in VIEWS}
    for view,q in queries.items():
        result['unoptimised'][view]=timed(c,q)
    slowest=max(result['unoptimised'],key=lambda v:result['unoptimised'][v]['seconds'])
    result['slowest']=slowest
    try:
        c.execute("ALTER SESSION SET PROFILE='ON'")
        timed(c,queries[slowest])
        c.execute("ALTER SESSION SET PROFILE='OFF'")
        c.execute('FLUSH STATISTICS')
        columns='STMT_ID,PART_ID,PART_NAME,PART_INFO,OBJECT_NAME,OBJECT_ROWS,OUT_ROWS,DURATION,CPU'
        # SELECT * preserves version-specific profile fields without guessing their schema.
        stmt=c.execute("SELECT * FROM EXA_USER_PROFILE_LAST_DAY WHERE SESSION_ID=CURRENT_SESSION AND SQL_TEXT LIKE 'SELECT COUNT(*),SUM(ABS(%' ORDER BY STMT_ID,PART_ID")
        profile=[dict(zip(stmt.column_names(),row)) for row in stmt.fetchall()]
        Path(f'reports/profile_{label}.json').write_text(json.dumps(profile,indent=2,default=str)+'\n')
        result['profile_rows']=len(profile)
    except Exception as e:
        result['profile_error']=str(e).split('query')[0]
    # Refresh once per batch: removes repeated joins and window sorting from interactive views.
    start=time.perf_counter()
    c.execute('CREATE OR REPLACE TABLE GST_EVIDENCE.LEDGER_CACHE AS SELECT * FROM GST_EVIDENCE.V_LEDGER')
    result['cache_refresh_seconds']=time.perf_counter()-start
    text=Path('sql/10_checks.sql').read_text()
    features=text[text.index('CREATE OR REPLACE VIEW GST_EVIDENCE.V_FEATURES'):].replace('FROM GST_EVIDENCE.V_LEDGER','FROM GST_EVIDENCE.LEDGER_CACHE')
    for statement in features.split(';'):
        if statement.strip():c.execute(statement)
    result['optimised']={}
    for view,q in queries.items():
        result['optimised'][view]=[timed(c,q) for _ in range(3)]
        # Exact same checksums and counts are required before a speed comparison is reported.
        before=result['unoptimised'][view]['rows'][0];after=result['optimised'][view][0]['rows'][0]
        import math
        assert before[0]==after[0] and math.isclose(float(before[1] or 0),float(after[1] or 0),rel_tol=1e-9,abs_tol=.001),view
    try:
        c.execute(Path('sql/30_baseline_udf.sql').read_text().rsplit('/',1)[0])
        udfquery='SELECT GST_EVIDENCE.ROBUST_POWER_BASELINE(FACTORY_ID,PERIOD_MONTH,POWER_KWH/NULLIF(DECLARED_OUTPUT,0)) FROM GST_EVIDENCE.FACTORY_MONTH GROUP BY FACTORY_ID'
        start=time.perf_counter()
        c.execute('CREATE OR REPLACE TABLE GST_EVIDENCE.POWER_BASELINES AS '+udfquery)
        result['udf']={'seconds':time.perf_counter()-start,'output_rows':c.execute('SELECT COUNT(*) FROM GST_EVIDENCE.POWER_BASELINES').fetchval(),'role':'historical-only median/MAD explanation; not used for flags or held-out metrics'}
    except Exception as e:
        result['udf']={'available':False,'error':str(e).split('query')[0]}
    c.close()
    Path(f'reports/benchmark_{label}.json').write_text(json.dumps(result,indent=2,default=str)+'\n')
    r=json.load(open('results.json'));r.setdefault('performance',{})[label]=result
    Path('results.json').write_text(json.dumps(r,indent=2,default=str)+'\n')
    print(json.dumps({k:result[k] for k in ['slowest','cache_refresh_seconds','udf']},indent=2))
    return result

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--data',default='data/generated');p.add_argument('--label',default='small');p.add_argument('--no-load',action='store_true');a=p.parse_args();benchmark(a.data,a.label,not a.no_load)
