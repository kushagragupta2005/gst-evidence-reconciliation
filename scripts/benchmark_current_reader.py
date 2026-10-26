"""Stamped current-view timings and equivalent DuckDB checks; Exasol SELECT only."""
import hashlib,json,math,platform,statistics,subprocess,time
from datetime import datetime,timezone
from pathlib import Path
import duckdb
from src.db import connect
ROOT=Path(__file__).resolve().parents[1]
data=ROOT/'data/v3_c'
threshold=json.loads((ROOT/'results.json').read_text())['protocol']['threshold']
report={'time_utc':datetime.now(timezone.utc).isoformat(),'git_sha':subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip(),'detector_sql_sha256':hashlib.sha256((ROOT/'sql/10_checks.sql').read_bytes()).hexdigest(),'hardware':{'platform':platform.platform(),'machine':platform.machine(),'processor':subprocess.check_output(['sysctl','-n','machdep.cpu.brand_string'],text=True).strip(),'memory_bytes':int(subprocess.check_output(['sysctl','-n','hw.memsize'],text=True))},'scope':'Current V3-C dataset, not a new full-scale run. Read-only Exasol view execution vs equivalent DuckDB checks on CSV-loaded tables; includes client execution/fetch, excludes Exasol ingestion. Three sequential warm-capable repeats; no cold-cache claim.','threshold':threshold,'duckdb_version':duckdb.__version__,'data_manifest':json.loads((data/'manifest.json').read_text()),'csv_sha256':{},'checks':{}}
queries={
'stock_rollforward':'''WITH m AS (SELECT *, LAG(closing_stock) OVER(PARTITION BY factory_id ORDER BY period_month) previous_closing FROM factory_month), f AS (SELECT opening_stock+purchases_finished+declared_output-declared_dispatch-closing_stock gap, GREATEST(ABS(opening_stock+purchases_finished+declared_output-declared_dispatch-closing_stock)-ABS(raw_stock_change),ABS(opening_stock-COALESCE(previous_closing,opening_stock))-ABS(raw_stock_change),0)/NULLIF(declared_output,0) severity FROM m) SELECT COUNT(*),SUM(ABS(gap)) FROM f WHERE severity>{threshold}''',
'supplier_chain':'''WITH p AS (SELECT buyer_factory_id,period_month,SUM(quantity) qty FROM purchase_invoices GROUP BY buyer_factory_id,period_month), f AS (SELECT p.qty-COALESCE(r.declared_sales_kg,0) gap, ABS(p.qty-COALESCE(r.declared_sales_kg,0))/NULLIF(p.qty,0) severity FROM p JOIN suppliers s ON s.owner_factory_id=p.buyer_factory_id LEFT JOIN supplier_returns r ON r.supplier_id=s.supplier_id AND r.period_month=p.period_month) SELECT COUNT(*),SUM(ABS(gap)) FROM f WHERE severity>{threshold}'''}
duck=duckdb.connect();duck.execute("SET memory_limit='1GB'");duck.execute('SET threads=4')
start=time.perf_counter()
for name in ['factory_month','purchase_invoices','suppliers','supplier_returns']:
 path=data/(name+'.csv');report['csv_sha256'][name]=hashlib.sha256(path.read_bytes()).hexdigest()
 duck.execute(f"CREATE TABLE {name} AS SELECT * FROM read_csv_auto(?, sample_size=-1)",[str(path)])
report['benchmark_script_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
report['working_tree_dirty']=bool(subprocess.check_output(['git','status','--porcelain'],text=True).strip())
report['duckdb_threads']=4
report['duckdb_memory_limit']='1GB'
report['duckdb_csv_load_seconds']=time.perf_counter()-start
c=connect(readonly=True)
try:
 c.execute("ALTER SESSION SET QUERY_CACHE='OFF'");report['exasol_query_result_cache']='OFF'
 report['current_factory_months'],report['current_factories']=c.execute('SELECT COUNT(*), COUNT(DISTINCT FACTORY_ID) FROM GST_EVIDENCE.V_RANKED_CASES').fetchone()
 report['current_feature_rows']=c.execute('SELECT COUNT(*) FROM GST_EVIDENCE.V_FEATURES').fetchval()
 for check,query in queries.items():
  eq=f"SELECT COUNT(*),SUM(ABS(GAP)) FROM GST_EVIDENCE.V_FEATURES WHERE CHECK_FAMILY='{check}' AND SEVERITY>{threshold}"
  dq=query.format(threshold=threshold); item={'exasol_sql':eq,'duckdb_sql':dq,'exasol_seconds':[],'duckdb_seconds':[]}
  for _ in range(3):
   start=time.perf_counter();a=c.execute(eq).fetchone();item['exasol_seconds'].append(time.perf_counter()-start)
   start=time.perf_counter();b=duck.execute(dq).fetchone();item['duckdb_seconds'].append(time.perf_counter()-start)
   assert a[0]==b[0] and math.isclose(float(a[1] or 0),float(b[1] or 0),rel_tol=1e-8,abs_tol=.01),(check,a,b)
  item['exasol_median_seconds']=statistics.median(item['exasol_seconds']);item['duckdb_median_seconds']=statistics.median(item['duckdb_seconds'])
  item.update({'matched_flagged_rows':int(a[0]),'matched_abs_gap_sum':float(a[1] or 0),'equivalent_counts_and_gaps':True});report['checks'][check]=item
finally:c.close();duck.close()
report['full_scale_status']='Not run: current restricted Exasol account cannot load a new full-scale dataset. Existing full-scale artifact remains historical.'
(ROOT/'reports/benchmark_current_reader.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'status':'passed','feature_rows':report['current_feature_rows'],'checks':report['checks']},indent=2))
