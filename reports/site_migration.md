# Static site migration inventory

**Recorded:** 2026-10-26  
**Scope:** tracked references to `streamlit`, `8501`, `app.py`, or `dashboard` in the README, docs, deck sources, scripts, CI, dependency files, Makefile, and existing site.

## Findings

| Location | Reference | Migration action |
|---|---|---|
| `app.py` | Current Streamlit front end | Move to `legacy/app.py`; retain only as historical implementation. |
| `Makefile` | `dashboard`, `provision-dashboard` targets | Replace the UI target with `site` and add `api`; retain only account provisioning under a neutral name. |
| `README.md` | Dashboard setup, command, dependency, architecture and release-checklist references | Describe the static site and local API; remove Streamlit. |
| `requirements.txt` / `requirements-lock.txt` | `streamlit==1.66.0` | Remove it and its unused UI dependency chain. |
| `.github/workflows/tests.yml` | Compiles root `app.py` | Compile the API and site export instead. |
| `scripts/verify_clean_setup.sh` | Compiles root `app.py` | Compile the API and export script instead. |
| `scripts/evaluate_v2.sh` | Historical dashboard-artifact comment | Rename wording; keep its development-only status. |
| `scripts/export_demo_examples.py` | Dashboard wording | Rename wording; preserve label-isolation constraint. |
| `scripts/render_preregistration_scorecard.py` | Dashboard wording | Rename wording; preserve the test claim. |
| `docs/CHANGELOG_RESULTS.md`, `docs/PLAN.md`, `docs/PREREGISTRATION_SCORECARD.md`, `docs/demo_script.md`, `docs/preregistration_v3.md` | Dashboard references | Update only the product name and launch instructions; do not change evaluation claims. |
| `website/` | Existing static landing page has no old UI links | Extend this design into the sole front end. |
| `deliverables/*.pptx`, `.pitch_build/*.pptx` | No matching old-UI strings found in slide XML | Keep under review when the deck is refreshed. |

The initial grep did not find a `:8501` literal. It found no old-UI string in the scanned PowerPoint slide XML.

## `app.py` parity checklist

The replacement site and its local read-only API must provide each item below before the old application is retired.

- [ ] Ranked queue: monthly priority list and factory queue using the frozen `K=3` rule.
- [ ] Factory case timeline across 12 months.
- [ ] Evidence rows with expected, observed, gap, source family, and discrepancy class.
- [ ] Per-family signal contributions, including sub-threshold evidence.
- [ ] Cleared and review-only tabs with verified-document disposition and reason.
- [ ] Evidence-only case note with explicit validator result and tamper rejection.
- [ ] Guarded follow-up: exactly three intent routes, fixed allow-listed `SELECT` templates, row cap, and timeout.
- [ ] Held-out evaluation and limits, sourced from committed artifacts only.
- [ ] Scale and performance information, labelled by its source and status.

## Non-negotiable migration constraints

- The exact problem statement remains unchanged and continues to be covered by its regression hash test.
- The static site receives no evaluator truth labels. The restricted database account may read only label-free views.
- The language-model layer, if configured, may phrase a validated note or summarize returned evidence; it does not change ranking or flags.
