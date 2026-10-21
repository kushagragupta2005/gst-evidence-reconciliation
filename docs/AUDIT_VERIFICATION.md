# Audit verification — 21 October 2026

This file verifies the technical claims made in the earlier project audit against
the repository and the locally running Exasol Personal instance. `VERIFIED`
means the cited artifact or command supports the claim. `WRONG` means the
claim conflicts with implementation or measured output. `UNVERIFIABLE` means
the repository has no successful recorded execution that proves it.

## Commands run

```text
git status --short --branch
python3 -m unittest discover -s tests -v
python3 -c "import json; print(json.load(open('results.json')).keys())"
rg -n "GROUND_TRUTH|SCENARIO|TOTAL_ABSOLUTE_GAP|V_STOCK_ROLLFORWARD|mcp|UDF" \
  src sql app.py README.md tests
```

The offline suite passed: 16 tests in 0.085 seconds. The repository was clean
on `main...origin/main`. This is evidence about repository state, not a new
held-out evaluation run.

## Claim register

| Claim | Status | Evidence and finding |
|---|---|---|
| The project uses Exasol Personal as its analytical database. | VERIFIED | `README.md` setup, `src/load_and_score.py`, and `sql/00_schema.sql` create and query `GST_EVIDENCE` objects. |
| Source data is synthetic. | VERIFIED | `src/generate.py` creates every evidence CSV; no real-data connector exists. |
| Seeded 12-month datasets and held-out Seed C metrics exist. | VERIFIED | `src/generate.py`; `data/seed_c/manifest.json`; `results.json`. |
| Detector SQL does not reference truth labels. | VERIFIED | `tests/test_engine.py::test_sql_does_not_use_truth` passed; `sql/10_checks.sql` contains no label reference. |
| Labels are isolated from the detection database. | VERIFIED AFTER REMEDIATION | The original state was wrong: `FACTORIES` had label columns. The rebuilt state has five factory columns, no `GST_EVIDENCE.TRUTH`, 28,800 rows in `GST_EVALUATION.TRUTH`, and dashboard-label access is denied. Evidence: `reports/load_seed_c_label_isolated.json` and the verification command recorded in `docs/CHANGELOG_RESULTS.md`. |
| Two source families are required for priority status. | VERIFIED | `sql/10_checks.sql` creates `STATUS='prioritise'` when `SIGNAL_COUNT >= 2`; tests cover same-family non-corroboration. |
| Stock roll-forward catches generated cases. | VERIFIED AFTER REMEDIATION | Original Seed C had zero stock rows. Pre-registered V2-C has 2,627 stock evidence rows and held-out per-check recall of 88.09%; see `reports/v2_load_seed_c.json` and `reports/v2_seed_c_results.json`. This remains synthetic scenario recovery. |
| Supplier loops affect detection score. | WRONG | `sql/10_checks.sql` records `LOOP_FOUND` text, but it does not change severity or ranking. |
| Normalised entity keys affect detection. | WRONG | `sql/20_entities.sql` creates `ENTITY_KEYS`; no scoring or ranking query references it. |
| Dashboard ranking matches evaluated ranking. | VERIFIED AFTER REMEDIATION | Both use family count, weakest fired normalised gap, estimated INR tax exposure, then factory ID. `test_dashboard_and_evaluator_share_rank_order` enforces this source-level contract. |
| The rank field name accurately describes its contents. | VERIFIED AFTER REMEDIATION | `TOTAL_ABSOLUTE_GAP` was replaced with `TOTAL_SEVERITY`. `ESTIMATED_TAX_EXPOSURE_INR` is separately exposed with documented synthetic formulas. |
| “Cleared” means supporting documents were verified. | WRONG | `V_SINGLE_SIGNAL_DISPOSITIONS` uses machine/product/hours/stock fields only; there is no uploaded-evidence table. |
| A Python UDF result is part of the submission. | WRONG | `results.json.udf.status` is `excluded`; `sql/30_baseline_udf.sql` exists but no successful execution artifact is published. |
| A live Exasol MCP follow-up demo is recorded. | UNVERIFIABLE | The dashboard uses guarded PyExasol templates (`src/followup.py`, `src/db.py`); no successful MCP transcript exists. |
| Case-note numeric validation works. | VERIFIED | `src/case_notes.py`; tamper and swapped-field tests passed in `tests/test_notes.py`. |
| Guarded follow-up queries resist basic injection. | VERIFIED | Fixed templates and ID validation in `src/followup.py`; injection test passed. |
| Full-scale path reaches about 21 million raw evidence rows. | VERIFIED | `results.json.performance.full.manifest.raw_evidence_rows = 20,978,945`; reproduction code is `src/generate.py --scale large`. |
| Full-scale Exasol timing was recorded. | VERIFIED | `results.json.performance.full` and `reports/benchmark_full.json`. These are workload timings on one local MacBook, not comparative production benchmarks. |
| Exasol beats pandas on reported local checks. | WRONG | The saved pandas measurements are lower for every compared check. The report must state that plainly. |
| Eight-query concurrency was measured. | VERIFIED | `results.json.concurrency` and `reports/concurrency.json` record one local run. It is not a 50-session repeated benchmark. |
| Repository provenance starts in the challenge window. | VERIFIED | `git log --reverse` starts at `f015d5b`, dated 2026-10-19, after the 5 October 2026 opening date. |

## Immediate release implications

No submission material may claim working MCP or UDF functionality, verified
supporting documents, real-world fraud accuracy, or stock-check recovery until
there is a dated successful artifact. Existing negative results remain in the
repository and will be carried into `docs/CHANGELOG_RESULTS.md`.
