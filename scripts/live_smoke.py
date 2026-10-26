"""Exercise the local read-only API against a running restricted Exasol account."""
from __future__ import annotations

import json
import os
import statistics
import subprocess
import sys
import time
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0,str(ROOT))
PORT=int(os.getenv('GST_SMOKE_API_PORT','8876'))
BASE=f'http://127.0.0.1:{PORT}'

def request(path,method='GET',body=None):
    data=None if body is None else json.dumps(body).encode()
    headers={} if data is None else {'Content-Type':'application/json'}
    req=urllib.request.Request(BASE+path,data=data,headers=headers,method=method)
    try:
        with urllib.request.urlopen(req,timeout=35) as response:
            return response.status,json.load(response)
    except urllib.error.HTTPError as error:
        return error.code,json.load(error)

def wait_for_health():
    for _ in range(30):
        try:
            status,payload=request('/health')
            if status==200:return payload
        except (urllib.error.URLError,ConnectionError):
            pass
        time.sleep(.2)
    raise RuntimeError('local API did not become healthy')

def main():
    from src.db import connect
    report={'time_utc':time.strftime('%Y-%m-%dT%H:%M:%SZ',time.gmtime()),'base_url':BASE}
    try:
        connection=connect(readonly=True)
        connection.execute('SELECT 1').fetchval()
        connection.close()
    except Exception as error:
        report.update(status='skipped',reason='restricted Exasol account unavailable',detail=type(error).__name__)
        print('SKIPPED: restricted Exasol account is unavailable.')
        (ROOT/'reports/live_smoke.json').write_text(json.dumps(report,indent=2)+'\n')
        return 0
    environment=os.environ.copy();environment['GST_API_PORT']=str(PORT)
    process=subprocess.Popen([sys.executable,'-m','src.api'],cwd=ROOT,env=environment,stdout=subprocess.DEVNULL,stderr=subprocess.PIPE,text=True)
    try:
        health=wait_for_health()
        status,queue=request('/queue?view=monthly')
        assert status==200 and queue['rows'],'queue failed'
        factory_id=queue['rows'][0]['factory_id']
        outcomes={}
        for path in [f'/case/{factory_id}',f'/note/{factory_id}']:
            status,payload=request(path);assert status==200,path
            if path.startswith('/note/'):
                assert payload['validated'],'note validator rejected deterministic note'
                outcomes[path]={'status':status,'validated':payload['validated'],'evidence_rows':payload['evidence_rows']}
            else:
                outcomes[path]={'status':status,'evidence_rows':len(payload.get('evidence',[]))}
        questions={'dispatch':f'show the dispatch gap by month for factory {factory_id}','timeline':f'show timeline for factory {factory_id}','evidence':f'show evidence for factory {factory_id}'}
        for intent,question in questions.items():
            status,payload=request('/ask','POST',{'factory_id':factory_id,'question':question})
            assert status==200 and payload['intent']==intent,intent;outcomes[f'ask_{intent}']={'status':status,'rows':len(payload['rows']),'sql':payload['sql']}
        status,payload=request('/ask','POST',{'factory_id':factory_id,'question':'show evidence; DROP TABLE GST_EVALUATION'})
        assert status==400,'injection was not rejected';outcomes['injection']={'status':status,'error':payload['error']}
        status,payload=request('/ask','POST',{'factory_id':factory_id,'question':'what is fraud?'})
        assert status==400,'unknown intent was not rejected';outcomes['unknown_intent']={'status':status,'error':payload['error']}
        def parallel_call(_):
            started=time.perf_counter();status,payload=request('/ask','POST',{'factory_id':factory_id,'question':questions['dispatch']});assert status==200;return time.perf_counter()-started,len(payload['rows'])
        with ThreadPoolExecutor(max_workers=8) as pool:
            parallel=list(pool.map(parallel_call,range(8)))
        latencies=sorted(item[0] for item in parallel)
        status,activity=request('/activity');assert status==200 and activity['rows'],'activity failed'
        report.update(status='passed',health=health,factory_id=factory_id,outcomes=outcomes,
                      parallel_ask={'queries':8,'latencies_seconds':latencies,'p50_seconds':statistics.median(latencies),'p95_seconds':statistics.quantiles(latencies,n=20,method='inclusive')[18],'rows_each':[item[1] for item in parallel]},
                      activity_rows=len(activity['rows']))
        print(json.dumps(report,indent=2))
        (ROOT/'reports/live_smoke.json').write_text(json.dumps(report,indent=2)+'\n')
        return 0
    except Exception as error:
        report.update(status='failed',error=repr(error))
        (ROOT/'reports/live_smoke.json').write_text(json.dumps(report,indent=2)+'\n')
        raise
    finally:
        process.terminate()
        try:process.wait(timeout=5)
        except subprocess.TimeoutExpired:process.kill()

if __name__=='__main__':
    raise SystemExit(main())
