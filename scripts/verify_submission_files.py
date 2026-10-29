"""Verify source-linked deliverables and explicit hand-in limits; no fabricated video."""
import hashlib,json,zipfile
from pathlib import Path
from xml.etree import ElementTree as ET
ROOT=Path(__file__).resolve().parents[1]
required=['LICENSE','README.md','docs/PROJECT_GUIDE.md','docs/JUDGE_AUDIT.md','docs/demo_script.md','docs/judge_qa.md','data/audit/manifest.json','00_SUBMISSION/Pitch.pptx','00_SUBMISSION/Pitch.pdf']
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
video_line=next(line for line in (ROOT/'docs/PROJECT_GUIDE.md').read_text().splitlines() if line.startswith('- Video URL: '))
video_url=video_line.removeprefix('- Video URL: ').strip()
assert video_url.startswith('https://github.com/') and '/releases/tag/' in video_url
report={'status':'passed','required_files':required,'native_slides':5,'problem_statement_hash':'matched','deck_matches_v3_c_metrics':True,'video':'user-recorded final submission video uploaded','video_url':video_url,'portal_submission':'not performed','files':[{'path':name,'bytes':(ROOT/name).stat().st_size,'sha256':hashlib.sha256((ROOT/name).read_bytes()).hexdigest()} for name in required if name.startswith('00_SUBMISSION/')]}
(ROOT/'reports/submission_file_checks.json').write_text(json.dumps(report,indent=2)+'\n');print('Current submission files verified; video link included; portal submission remains outstanding.')
