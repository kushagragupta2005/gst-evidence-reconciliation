"""Verify source-linked deliverables and explicit hand-in limits; no fabricated video."""
import hashlib,json,zipfile
from pathlib import Path
from xml.etree import ElementTree as ET
ROOT=Path(__file__).resolve().parents[1]
required=['LICENSE','README.md','PROJECT_STATUS.md','SUBMISSION_CHECKLIST.md','docs/JUDGE_AUDIT.md','docs/demo_script.md','docs/judge_qa.md','data/audit/manifest.json','deliverables/exathon-india-2026-pitch.pptx','deliverables/exathon-india-2026-pitch.pdf']
for name in required:assert (ROOT/name).is_file(),name
problem=(ROOT/'README.md').read_text().split('\n> ',1)[1].split('\n',1)[0]
assert hashlib.sha256(problem.encode()).hexdigest()=='d5b711f68044bdd8079701b61916870971a76d3a20104649a4bd0035c870ba33'
texts=[]
with zipfile.ZipFile(ROOT/required[-2]) as z:
 for i in range(1,6):
  content=ET.fromstring(z.read(f'ppt/slides/slide{i}.xml'))
  texts.extend(e.text for e in content.iter() if e.tag.endswith('}t') and e.text)
assert problem in texts
joined='\n'.join(texts)
for old in ['84.01%','16.58%','58.67%','K=4']:assert old not in joined,old
result=json.loads((ROOT/'reports/v3_c_results.json').read_text())
for value in [result['factory_month']['recall'],result['factory_month']['fpr'],result['factory']['precision']]:assert f'{value*100:.2f}%' in joined
assert 'NOT PROVIDED' in (ROOT/'SUBMISSION_CHECKLIST.md').read_text()
report={'status':'passed','required_files':required,'native_slides':5,'problem_statement_hash':'matched','deck_matches_v3_c_metrics':True,'video':'not supplied; user recording required','portal_submission':'not performed','files':[{'path':name,'bytes':(ROOT/name).stat().st_size,'sha256':hashlib.sha256((ROOT/name).read_bytes()).hexdigest()} for name in required if name.startswith('deliverables/')]}
(ROOT/'reports/submission_file_checks.json').write_text(json.dumps(report,indent=2)+'\n');print('Current submission files verified; missing video and portal submission remain explicit.')
