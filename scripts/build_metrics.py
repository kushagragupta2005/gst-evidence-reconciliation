"""Build one canonical metrics JSON and byte-equivalent browser/offline bundles."""
import hashlib,json,subprocess
from pathlib import Path
from datetime import datetime,timezone
ROOT=Path(__file__).resolve().parents[1]
FILES={'v3_b':'results.json','v3_c':'reports/v3_c_results.json','dispositions_b':'reports/v3_b_dispositions.json','dispositions_c':'reports/v3_c_dispositions.json','bounds':'reports/wrong_clear_bounds.json','ablation':'reports/site_ablation.json','benchmark':'reports/benchmark_current_reader.json','concurrency':'reports/live_smoke.json','historical':'reports/benchmark_full.json','examples':'reports/site_examples.json'}
def build():
 repo=subprocess.check_output(['git','remote','get-url','origin'],cwd=ROOT,text=True).strip().removesuffix('.git')
 m={'meta':{'generated_at':datetime.now(timezone.utc).isoformat(),'commit':subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip(),'repo':repo,'data_scope':'All evidence and outcomes are synthetic.'},'sources':{},'results':{}}
 for key,file in FILES.items():
  raw=(ROOT/file).read_bytes();v=json.loads(raw)
  commit,date=subprocess.check_output(['git','log','-1','--format=%H|%cI','--',file],cwd=ROOT,text=True).strip().split('|')
  m['sources'][key]={'file':file,'sha256':hashlib.sha256(raw).hexdigest(),'commit':commit,'committed_at':date,'url':repo+'/blob/'+commit+'/'+file,'run_time':v.get('time_utc')}
  if key in ('v3_b','v3_c'):
   m['results'][key]={k:v[k] for k in ['factory_month','factory','dataset','protocol','factory_queue','prevalence_adjusted_precision','evasive','fpr_by_decoy','precision_at_k','misses']}
   m['results'][key]['prevalence_sorted']=sorted(v['prevalence_adjusted_precision'].values(),key=lambda x:x['assumed_prevalence'])
  else:m[key]=v
 m['problem_statement']=(ROOT/'README.md').read_text().split('\n> ',1)[1].split('\n',1)[0]
 # Deployment copies are generated from this single canonical JSON, never independently edited.
 text=json.dumps(m,ensure_ascii=False,indent=2)+'\n';(ROOT/'data').mkdir(exist_ok=True)
 (ROOT/'data/metrics.json').write_text(text)
 (ROOT/'website/data/metrics.json').write_text(text)
 (ROOT/'website/metrics.js').write_text('window.__METRICS__ = '+json.dumps(m,ensure_ascii=False,separators=(',',':')).replace('<','\\u003c')+';\n')
 return m
if __name__=='__main__':build()
