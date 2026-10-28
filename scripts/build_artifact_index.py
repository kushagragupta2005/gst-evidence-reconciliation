"""Classify reports explicitly without rewriting historical result values."""
import hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
current={'v3_b_results.json':'HELDOUT_PRIMARY','v3_c_results.json':'HELDOUT_CONFIRMATION','v3_b_dispositions.json':'HELDOUT_PRIMARY_DISPOSITIONS','v3_c_dispositions.json':'HELDOUT_CONFIRMATION_DISPOSITIONS','v3_a_calibration.json':'DEV_CALIBRATION','site_ablation.json':'CURRENT_POSTHOC_POINT_ESTIMATES','wrong_clear_bounds.json':'CURRENT_SYNTHETIC_CONDITIONAL_BOUND','benchmark_current_reader.json':'RECORDED_CURRENT_DATA_COMPARISON_NOT_FULL_SCALE','live_smoke.json':'CURRENT_POST_REPAIR_LIVE_SMOKE','site_examples.json':'CURRENT_RECORDED_EXAMPLES','judge_tests.json':'CURRENT_AUDIT_TESTS','judge_database_audit.json':'CURRENT_RESTRICTED_DATABASE_AUDIT','threshold_repair.json':'AUTHORISED_CONFIG_REPAIR','security_inventory.json':'CURRENT_HEURISTIC_SCAN','dataset_inventory.json':'CURRENT_DATA_INVENTORY_PLUS_HISTORICAL_MANIFESTS','ranking_alignment_audit.json':'CURRENT_POSTHOC_ORDER_DIAGNOSTIC','licence_review.json':'CURRENT_DOCUMENT_INSPECTION','submission_file_checks.json':'CURRENT_DELIVERABLE_CHECK','clean_setup.json':'CLONE_CHECK_READ_SCOPE','site_browser_smoke.json':'BROWSER_CHECK_READ_DATE','pages_browser_smoke.json':'PUBLIC_BROWSER_CHECK_READ_DATE','lighthouse_public.json':'RECORDED_PUBLIC_LIGHTHOUSE_READ_DATE','lighthouse_local.json':'RECORDED_LOCAL_LIGHTHOUSE_READ_DATE','public_pages.json':'PUBLIC_HTTP_CHECK_READ_DATE'}
files=[]
for p in sorted((ROOT/'reports').rglob('*')):
 if not p.is_file() or p.name=='ARTIFACT_INDEX.json' or p.suffix=='.log':continue
 status=current.get(p.name,'HISTORICAL_OR_DEV_NOT_CURRENT_HELDOUT')
 if p.suffix=='.json':
  try:
   v=json.loads(p.read_text())
   embedded=v.get('result_status') if isinstance(v,dict) else None
  except ValueError:embedded='INVALID_JSON'
 else:embedded=None
 files.append({'path':str(p.relative_to(ROOT)),'classification':status,'embedded_status':embedded,'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
(ROOT/'reports/ARTIFACT_INDEX.json').write_text(json.dumps({'scope':'Explicit current/historical index. Historical records are retained as audit trails and must not be used as current V3 claims. Dates and scopes within each artifact still apply.','files':files},indent=2)+'\n')
print('Classified',len(files),'report artifacts.')
