"""Run real offline regression tests and record their outcome without hardcoded counts."""
import json,subprocess,time,unittest
from datetime import datetime,timezone
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
started=time.perf_counter();suite=unittest.defaultTestLoader.discover(str(ROOT/'tests'))
with (ROOT/'reports/judge_tests.log').open('w') as log:result=unittest.TextTestRunner(stream=log,verbosity=2).run(suite)
report={'time_utc':datetime.now(timezone.utc).isoformat(),'source_commit':subprocess.check_output(['git','rev-parse','HEAD'],text=True,cwd=ROOT).strip(),'working_tree_dirty':bool(subprocess.check_output(['git','status','--porcelain'],text=True,cwd=ROOT).strip()),'tests_run':result.testsRun,'failures':len(result.failures),'errors':len(result.errors),'skipped':len(result.skipped),'elapsed_seconds':time.perf_counter()-started,'status':'passed' if result.wasSuccessful() else 'failed','scope':'Offline Python regression tests; SQL compatibility smoke uses SQLite, not a replacement for live Exasol checks.'}
(ROOT/'reports/judge_tests.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2));raise SystemExit(0 if result.wasSuccessful() else 1)
