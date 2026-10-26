"""Record real restricted-API responses; selection labels come from offline evaluation."""
import csv, hashlib, json, time, urllib.request, subprocess
from datetime import datetime, timezone
from pathlib import Path
from src.case_notes import build_case_note, validate_note
ROOT=Path(__file__).resolve().parents[1]
def request(path, body=None):
    req=urllib.request.Request('http://127.0.0.1:8765'+path, data=json.dumps(body).encode() if body else None, headers={'Content-Type':'application/json'})
    start=time.perf_counter()
    with urllib.request.urlopen(req, timeout=40) as response: value=json.load(response)
    return value, (time.perf_counter()-start)*1000
out={'time_utc':datetime.now(timezone.utc).isoformat(),'git_sha':subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip(),'selection_source':'reports/v3_c/held_out_predictions.csv','examples':[],'questions':[]}
prediction_path=ROOT/out['selection_source']
out['selection_sha256']=hashlib.sha256(prediction_path.read_bytes()).hexdigest()
with prediction_path.open() as file:
    predictions={(r['factory_id'],r['period_month']):r for r in csv.DictReader(file)}
for factory,month,kind in [('F000902','2026-05','caught'),('F000016','2026-04','cleared'),('F000025','2026-08','missed')]:
    label=predictions[(factory,month)]
    assert bool(int(label['is_cheat'])) == (kind!='cleared')
    assert (label['flagged'].lower()=='true') == (kind=='caught')
    payload,_=request('/case/'+factory)
    evidence=[r for r in payload['evidence'] if r['period_month']==month]
    disposition=[r for r in payload['dispositions'] if r['period_month']==month]
    note=build_case_note(factory,evidence)
    out['examples'].append({'factory_id':factory,'month':month,'kind':kind,'evidence':evidence,'dispositions':disposition,'timeline':payload['timeline'],'note':note,'validated':validate_note(note,evidence),'note_mode':'deterministic fallback'})
for intent in ['dispatch','timeline','evidence']:
    question=f'show {intent} for factory F000902'
    result,ms=request('/ask',{'question':question,'factory_id':'F000902'})
    out['questions'].append({'question':question,'intent':intent,'response':result,'latency_ms':ms})
(ROOT/'reports/site_examples.json').write_text(json.dumps(out,indent=2)+'\n')
print([(e['kind'],len(e['evidence']),e['dispositions'],e['validated']) for e in out['examples']])
