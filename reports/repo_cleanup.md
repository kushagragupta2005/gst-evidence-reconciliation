# Repository cleanup audit

Audit performed before moves. References below are literal-name matches in tracked Makefile, workflows, package.json, scripts, tests, website, README and docs (binary assets excluded). Historical references are preserved as dated evidence.

| Item | Referenced by | Decision |
|---|---|---|
| `.git` | `.github/workflows/pages.yml`, `README.md`, `docs/PROJECT_GUIDE.md`, `docs/README.md`, `docs/licences/PYTHON.md`, `scripts/build_metrics.py`, `scripts/build_pages.py`, `scripts/build_submission_manifest.py`, `scripts/export_site_data.py`, `scripts/update_submission_deck.mjs`, `tests/test_engine.py`, `website/404.html`, `website/cases/index.html`, `website/data/index.html`, `website/how-it-works/index.html`, `website/index.html`, `website/limits/index.html`, `website/problem/index.html`, `website/results/index.html`, `website/site.js`, `website/system/index.html` | Keep; source/config/environment or supporting directory |
| `.gitattributes` | No literal references found | Keep; source/config/environment or supporting directory |
| `.github` | `.github/workflows/pages.yml`, `README.md`, `docs/PROJECT_GUIDE.md`, `docs/README.md`, `docs/licences/PYTHON.md`, `scripts/build_pages.py`, `scripts/update_submission_deck.mjs`, `tests/test_engine.py`, `website/404.html`, `website/cases/index.html`, `website/data/index.html`, `website/how-it-works/index.html`, `website/index.html`, `website/limits/index.html`, `website/problem/index.html`, `website/results/index.html`, `website/system/index.html` | Keep; source/config/environment or supporting directory |
| `.gitignore` | No literal references found | Keep; source/config/environment or supporting directory |
| `.pitch_build` | `scripts/build_submission_manifest.py`, `scripts/update_submission_deck.mjs` | Keep; source/config/environment or supporting directory |
| `.pytest_cache` | No literal references found | Keep; source/config/environment or supporting directory |
| `.venv` | `Makefile`, `docs/NUMBERS_AUDIT.md`, `docs/PROJECT_GUIDE.md`, `scripts/audit_site_numbers.py`, `scripts/bootstrap.sh`, `scripts/build_submission_manifest.py`, `scripts/evaluate.sh`, `scripts/evaluate_v2.sh`, `scripts/generate_third_party.sh`, `scripts/verify_clean_setup.sh` | Keep; source/config/environment or supporting directory |
| `00_SUBMISSION` | `README.md`, `docs/PROJECT_GUIDE.md`, `docs/README.md`, `docs/archive/legacy/submission/README.md`, `scripts/build_submission_manifest.py`, `scripts/render_pitch_pdf.py`, `scripts/update_submission_deck.mjs`, `scripts/verify_submission_files.py` | Move to docs/submission; update deliverable checker |
| `LICENSE` | `README.md`, `docs/PROJECT_GUIDE.md`, `docs/README.md`, `scripts/build_pages.py`, `scripts/verify_submission_files.py`, `website/404.html`, `website/cases/index.html`, `website/data/index.html`, `website/how-it-works/index.html`, `website/index.html`, `website/limits/index.html`, `website/problem/index.html`, `website/results/index.html`, `website/system/index.html` | Keep; source/config/environment or supporting directory |
| `Makefile` | `docs/PROJECT_GUIDE.md`, `tests/test_engine.py` | Keep; source/config/environment or supporting directory |
| `README.md` | `README.md`, `docs/JUDGE_AUDIT.md`, `docs/PROJECT_GUIDE.md`, `docs/README.md`, `docs/archive/legacy/app.py`, `scripts/build_judge_audit.py`, `scripts/build_metrics.py`, `scripts/build_pages.py`, `scripts/build_submission_text.py`, `scripts/verify_submission_files.py`, `tests/test_engine.py`, `website/data/index.html`, `website/system/index.html` | Keep; source/config/environment or supporting directory |
| `__pycache__` | No literal references found | Keep; source/config/environment or supporting directory |
| `data` | `.github/workflows/pages.yml`, `.github/workflows/tests.yml`, `Makefile`, `README.md`, `docs/CHANGELOG_RESULTS.md`, `docs/JUDGE_AUDIT.md`, `docs/LICENCE_AUDIT.md`, `docs/NUMBERS_AUDIT.md`, `docs/PROJECT_GUIDE.md`, `docs/README.md`, `docs/archive/AUDIT_VERIFICATION.md`, `docs/archive/PLAN.md`, `docs/archive/PREREGISTRATION_SCORECARD.md`, `docs/archive/legacy/app.py`, `docs/demo_script.md`, `docs/evaluation_protocol.md`, `docs/judge_qa.md`, `docs/licences/AUTHORING.md`, `docs/licences/BROWSER.md`, `docs/licences/PYTHON.md`, `docs/preregistration.md`, `docs/preregistration_v3.md`, `scripts/audit_live_ranking.py`, `scripts/audit_site_numbers.py`, `scripts/benchmark_current_reader.py`, `scripts/build_artifact_index.py`, `scripts/build_judge_audit.py`, `scripts/build_metrics.py`, `scripts/build_pages.py`, `scripts/build_robustness.py`, `scripts/build_site_data.py`, `scripts/build_submission_manifest.py`, `scripts/build_submission_text.py`, `scripts/evaluate.sh`, `scripts/evaluate_v2.sh`, `scripts/export_site_data.py`, `scripts/inventory_datasets.py`, `scripts/live_smoke.py`, `scripts/package_audit_evidence.py`, `scripts/record_site_examples.py`, `scripts/render_preregistration_scorecard.py`, `scripts/restore_audit_evidence.py`, `scripts/serve_site.py`, `scripts/site_ablation.py`, `scripts/site_browser_smoke.mjs`, `scripts/site_lighthouse.mjs`, `scripts/threshold_tradeoff.py`, `scripts/update_submission_deck.mjs`, `scripts/verify_clean_setup.sh`, `scripts/verify_submission_files.py`, `tests/test_audit.py`, `tests/test_engine.py`, `tests/test_site_data.py`, `website/404.html`, `website/README.md`, `website/cases/index.html`, `website/data.js`, `website/data/evaluation.json`, `website/data/index.html`, `website/data/metrics.json`, `website/data/performance.json`, `website/data/snapshot.json`, `website/how-it-works/index.html`, `website/index.html`, `website/limits/index.html`, `website/metrics.js`, `website/problem/index.html`, `website/results/index.html`, `website/site.js`, `website/style.css`, `website/system/index.html` | Keep: compressed evidence and snapshot provenance |
| `docs` | `README.md`, `docs/JUDGE_AUDIT.md`, `docs/LICENCE_AUDIT.md`, `docs/PROJECT_GUIDE.md`, `docs/archive/AUDIT_VERIFICATION.md`, `docs/archive/PLAN.md`, `docs/archive/PREREGISTRATION_SCORECARD.md`, `docs/demo_script.md`, `docs/licences/PYTHON.md`, `docs/preregistration_v3.md`, `scripts/audit_site_numbers.py`, `scripts/build_judge_audit.py`, `scripts/build_pages.py`, `scripts/build_submission_manifest.py`, `scripts/build_submission_text.py`, `scripts/generate_third_party.sh`, `scripts/render_attribution.py`, `scripts/render_pitch_pdf.py`, `scripts/render_preregistration_scorecard.py`, `scripts/site_browser_smoke.mjs`, `scripts/update_submission_deck.mjs`, `scripts/verify_submission_files.py`, `tests/test_engine.py`, `website/404.html`, `website/cases/index.html`, `website/data.js`, `website/data/evaluation.json`, `website/data/index.html`, `website/data/metrics.json`, `website/how-it-works/index.html`, `website/index.html`, `website/limits/index.html`, `website/metrics.js`, `website/problem/index.html`, `website/results/index.html`, `website/system/index.html` | Keep; source/config/environment or supporting directory |
| `node_modules` | `scripts/build_submission_manifest.py` | Keep; source/config/environment or supporting directory |
| `package-lock.json` | `docs/licences/BROWSER.md` | Move to website; preserve dependency versions |
| `package.json` | No literal references found | Move to website; update npm commands |
| `reports` | `.github/workflows/pages.yml`, `Makefile`, `README.md`, `docs/ATTRIBUTION.md`, `docs/JUDGE_AUDIT.md`, `docs/LICENCE_AUDIT.md`, `docs/NUMBERS_AUDIT.md`, `docs/PROJECT_GUIDE.md`, `docs/README.md`, `docs/archive/AUDIT_VERIFICATION.md`, `docs/archive/PREREGISTRATION_SCORECARD.md`, `docs/archive/legacy/app.py`, `docs/archive/legacy/evidence/site_examples_before_threshold_repair.json`, `docs/judge_qa.md`, `docs/preregistration.md`, `scripts/archive_v1.py`, `scripts/attach_concurrency.py`, `scripts/audit_live_ranking.py`, `scripts/audit_site_numbers.py`, `scripts/benchmark_current_reader.py`, `scripts/build_artifact_index.py`, `scripts/build_judge_audit.py`, `scripts/build_metrics.py`, `scripts/build_robustness.py`, `scripts/build_submission_manifest.py`, `scripts/build_submission_text.py`, `scripts/evaluate.sh`, `scripts/evaluate_v2.sh`, `scripts/export_demo_examples.py`, `scripts/export_site_data.py`, `scripts/inventory_datasets.py`, `scripts/live_smoke.py`, `scripts/package_audit_evidence.py`, `scripts/performance_report.py`, `scripts/record_site_examples.py`, `scripts/render_attribution.py`, `scripts/render_preregistration_scorecard.py`, `scripts/report.py`, `scripts/restore_audit_evidence.py`, `scripts/run_judge_tests.py`, `scripts/site_ablation.py`, `scripts/site_browser_smoke.mjs`, `scripts/site_lighthouse.mjs`, `scripts/threshold_tradeoff.py`, `scripts/update_submission_deck.mjs`, `scripts/verify_clean_setup.sh`, `scripts/verify_submission_files.py`, `scripts/wrong_clear_bounds.py`, `tests/test_site_data.py`, `website/data.js`, `website/data/evaluation.json`, `website/data/manifest.json`, `website/data/metrics.json`, `website/data/performance.json`, `website/metrics.js` | Keep: commit-specific hashed source links |
| `requirements-lock.txt` | `.github/workflows/tests.yml`, `docs/PROJECT_GUIDE.md`, `scripts/bootstrap.sh`, `scripts/generate_third_party.sh`, `scripts/requirements/benchmark.txt`, `tests/test_engine.py` | Move to requirements; update CI, bootstrap and tests |
| `requirements.txt` | `tests/test_engine.py` | Keep; source/config/environment or supporting directory |
| `results.json` | `docs/NUMBERS_AUDIT.md`, `docs/PROJECT_GUIDE.md`, `docs/README.md`, `docs/archive/AUDIT_VERIFICATION.md`, `docs/judge_qa.md`, `docs/preregistration.md`, `scripts/archive_v1.py`, `scripts/attach_concurrency.py`, `scripts/audit_site_numbers.py`, `scripts/benchmark_current_reader.py`, `scripts/build_artifact_index.py`, `scripts/build_judge_audit.py`, `scripts/build_metrics.py`, `scripts/build_robustness.py`, `scripts/build_submission_text.py`, `scripts/evaluate.sh`, `scripts/evaluate_v2.sh`, `scripts/export_site_data.py`, `scripts/render_preregistration_scorecard.py`, `scripts/report.py`, `scripts/site_ablation.py`, `scripts/update_submission_deck.mjs`, `scripts/verify_submission_files.py`, `tests/test_audit.py`, `tests/test_site_data.py`, `website/data.js`, `website/data/manifest.json`, `website/data/metrics.json`, `website/metrics.js` | Keep: commit-specific hashed source links |
| `scripts` | `.github/workflows/pages.yml`, `.github/workflows/tests.yml`, `Makefile`, `README.md`, `docs/ATTRIBUTION.md`, `docs/JUDGE_AUDIT.md`, `docs/NUMBERS_AUDIT.md`, `docs/PROJECT_GUIDE.md`, `docs/archive/PREREGISTRATION_SCORECARD.md`, `docs/judge_qa.md`, `package.json`, `scripts/audit_site_numbers.py`, `scripts/build_judge_audit.py`, `scripts/build_pages.py`, `scripts/build_submission_text.py`, `scripts/evaluate.sh`, `scripts/evaluate_v2.sh`, `scripts/generate_third_party.sh`, `scripts/render_attribution.py`, `scripts/render_preregistration_scorecard.py`, `scripts/site_ablation.py`, `scripts/update_submission_deck.mjs`, `scripts/verify_clean_setup.sh`, `scripts/wrong_clear_bounds.py`, `tests/test_audit.py`, `tests/test_engine.py`, `tests/test_site_data.py`, `website/README.md`, `website/system/index.html` | Keep: 41 tracked scripts, not a few files |
| `sql` | `README.md`, `docs/PROJECT_GUIDE.md`, `docs/archive/AUDIT_VERIFICATION.md`, `docs/archive/legacy/app.py`, `docs/archive/legacy/evidence/live_smoke_before_threshold_repair.json`, `docs/archive/legacy/evidence/site_examples_before_threshold_repair.json`, `scripts/benchmark_current_reader.py`, `scripts/build_pages.py`, `scripts/live_smoke.py`, `scripts/site_browser_smoke.mjs`, `tests/test_audit.py`, `tests/test_engine.py`, `tests/test_site_data.py`, `website/data.js`, `website/data/metrics.json`, `website/data/performance.json`, `website/metrics.js`, `website/site.js`, `website/style.css`, `website/system/index.html` | Keep; source/config/environment or supporting directory |
| `src` | `.github/workflows/tests.yml`, `Makefile`, `README.md`, `docs/JUDGE_AUDIT.md`, `docs/PROJECT_GUIDE.md`, `docs/archive/AUDIT_VERIFICATION.md`, `docs/archive/legacy/app.py`, `scripts/audit_live_ranking.py`, `scripts/audit_site_numbers.py`, `scripts/benchmark_current_reader.py`, `scripts/build_judge_audit.py`, `scripts/build_pages.py`, `scripts/evaluate.sh`, `scripts/evaluate_v2.sh`, `scripts/export_demo_examples.py`, `scripts/export_site_data.py`, `scripts/inventory_datasets.py`, `scripts/live_smoke.py`, `scripts/record_site_examples.py`, `scripts/threshold_tradeoff.py`, `scripts/verify_clean_setup.sh`, `tests/test_audit.py`, `tests/test_engine.py`, `tests/test_notes.py`, `tests/test_site_data.py`, `website/404.html`, `website/cases/index.html`, `website/data/index.html`, `website/how-it-works/index.html`, `website/index.html`, `website/limits/index.html`, `website/problem/index.html`, `website/results/index.html`, `website/system/index.html` | Keep; source/config/environment or supporting directory |
| `tests` | `.github/workflows/tests.yml`, `Makefile`, `README.md`, `docs/CHANGELOG_RESULTS.md`, `docs/JUDGE_AUDIT.md`, `docs/PROJECT_GUIDE.md`, `docs/archive/AUDIT_VERIFICATION.md`, `docs/archive/PLAN.md`, `docs/archive/PREREGISTRATION_SCORECARD.md`, `scripts/build_artifact_index.py`, `scripts/build_judge_audit.py`, `scripts/build_pages.py`, `scripts/render_preregistration_scorecard.py`, `scripts/run_judge_tests.py`, `scripts/verify_clean_setup.sh`, `tests/test_engine.py`, `website/limits/index.html`, `website/results/index.html` | Keep; source/config/environment or supporting directory |
| `tmp` | `scripts/verify_clean_setup.sh`, `tests/test_audit.py` | Keep; source/config/environment or supporting directory |
| `website` | `.github/workflows/pages.yml`, `README.md`, `docs/JUDGE_AUDIT.md`, `docs/PROJECT_GUIDE.md`, `scripts/build_judge_audit.py`, `scripts/build_metrics.py`, `scripts/build_pages.py`, `scripts/build_submission_manifest.py`, `scripts/export_site_data.py`, `scripts/serve_site.py`, `scripts/site_browser_smoke.mjs`, `tests/test_engine.py`, `tests/test_site_data.py`, `website/404.html`, `website/cases/index.html`, `website/data/index.html`, `website/how-it-works/index.html`, `website/index.html`, `website/limits/index.html`, `website/problem/index.html`, `website/results/index.html`, `website/system/index.html` | Keep; source/config/environment or supporting directory |

## Path and integrity constraints

- `tests/test_engine.py` and `tests/test_site_data.py`: exact problem-statement SHA-256; lock-file path in retired-framework scan.
- `tests/test_site_data.py`: results bundle equality, canonical source paths, benchmark detector SQL hash, every canonical source resolved with `git show commit:path` and SHA-256 checked.
- `tests/test_audit.py`: archived compressed/raw hashes, frozen threshold, extracted evidence destination paths.
- `data/audit/manifest.json`: compressed/raw hashes and extraction destinations; `scripts/restore_audit_evidence.py` verifies both before writing.
- `scripts/build_metrics.py`: result/report source paths, Git commit URLs and SHA-256 provenance. These source files stay in place.
- `scripts/site_ablation.py`: frozen features SHA-256 against result provenance.
- `scripts/verify_submission_files.py`: required document/deck paths, exact problem hash and slide metrics. Update this checker with submission/doc moves.
- `scripts/verify_clean_setup.sh`: new-clone bootstrap, root-relative source paths, tests, audit and build commands. Update dependency path through bootstrap.
- `reports/SUBMISSION_MANIFEST.json`, `reports/ARTIFACT_INDEX.json`, dataset inventories, benchmark script/SQL/input hashes and dated verification reports: historical records, not rewritten to pretend the new tree was measured then.
- Deck exporter uses `docs/archive/legacy/submission/pre_v3_pitch.pptx`; retain that template. Before-repair evidence is historical audit evidence, not disposable cache.

## Before (local root)

```text
.git/
.gitattributes
.github/
.gitignore
.pitch_build/
.pytest_cache/
.venv/
00_SUBMISSION/
LICENSE
Makefile
README.md
__pycache__/
data/
docs/
node_modules/
package-lock.json
package.json
reports/
requirements-lock.txt
requirements.txt
results.json
scripts/
sql/
src/
tests/
tmp/
website/
```

## After (tracked root)

```text
.gitattributes
.github/
.gitignore
LICENSE
Makefile
README.md
data/
docs/
reports/
requirements.txt
requirements/
results.json
scripts/
sql/
src/
tests/
website/
```

## Moves and retained exceptions

- `00_SUBMISSION/` → `docs/submission/`; PDF/PPTX bytes unchanged, links and the deliverable checker updated.
- Node package and lock → `website/`; browser entry points → `website/tools/`, keeping repository-root working-directory semantics. Pages CI uses the moved lock and commands.
- Python lock → `requirements/requirements-lock.txt`; bootstrap, CI and tests updated; dependency versions unchanged.
- Seven supporting documents → `docs/reference/`; current links and authoring paths updated. Five Markdown files remain directly in `docs/`.
- `results.json`, `reports/` and `data/` stay in place: published commit:path URLs and hashes must remain verifiable. No provenance checks were weakened.
- `scripts/` stays: 41 files at audit time, with reproducible audit/build entry points; folding them into Makefile would obscure rather than simplify them.
- Historical report/manifest paths describe the tree when measured. They are not rewritten; use this move map for current paths. Two snapshot disposition-scope strings name the original preregistration path; its current location is `docs/reference/preregistration_v3.md`.
- Historical before-repair evidence and archived implementation stay because they are inventoried audit artifacts. The archived PPTX is also an active deck-export input.

## Removed files

No tracked content deleted. Moves use `git mv`. No unreferenced duplicate was proven safe to delete independently of the audit inventory. Local environments/build caches remain ignored; `.pytest_cache/` and `wheelhouse/` are now explicitly ignored.

## Validation

- Both move groups: `make all` passed (37 tests, 665-field audit, both baseline confusion matrices), followed by `npm --prefix website run site:build`.
- Submission verifier passed after its required paths were updated. PDF/PPTX hashes are unchanged. Relative Markdown links in current README/docs resolve locally.
- Snapshot generation was exercised, then timestamp-only generated changes were discarded to preserve the committed recorded artifacts.
- Byte-for-byte SHA-256 comparison passed for all 119 original tracked files under src/, sql/, reports/, data/audit/ and results.json.
- Fresh clone `20619cdbe1dca9c21238fc752821520b01be5a25`: separate directory and new venv; README bootstrap and `make site` passed (HTTP 200), plus CI-equivalent offline checks and Node install/build. Playwright: 48 successful checks, 64 internal-link checks, no console/HTTP/request errors. See [browser record](repo_cleanup_browser.json).
- Initial sandbox-only install failed DNS access to PyPI; retry with network permission passed. This is author-machine verification, not second-machine or live Exasol verification.
- GitHub-hosted CI status is checked after publication; local verification above is not a claim about a remote run.
