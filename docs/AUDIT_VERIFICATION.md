# Audit verification — 21 October 2026

This register distinguishes evidence that is implemented and tested from gaps that remain. A result is **DEV** when its seed, configuration, or output has already been inspected during development. It is not a post-change held-out headline.

## Verified implementation

| Claim | Status | Evidence |
|---|---|---|
| Exasol Personal is the primary analytic database. | VERIFIED | [`src/load_and_score.py`](../src/load_and_score.py), [`sql/00_schema.sql`](../sql/00_schema.sql) |
| All project data is synthetic. | VERIFIED | [`src/generate.py`](../src/generate.py) creates every input CSV. |
| Detector SQL does not use outcome labels. | VERIFIED | `test_sql_does_not_use_truth` in [`tests/test_engine.py`](../tests/test_engine.py). |
| Two distinct source families are required for priority. | VERIFIED | `V_RANKED_CASES` in [`sql/10_checks.sql`](../sql/10_checks.sql) and two SQL-contract tests. |
| Case-note number validation rejects tampering. | VERIFIED | [`tests/test_notes.py`](../tests/test_notes.py). |
| Follow-up questions are fixed read-only templates. | VERIFIED | [`src/followup.py`](../src/followup.py) and injection-rejection test. |
| Historical full-scale workload artefacts exist. | DEV | [`reports/benchmark_full.json`](../reports/benchmark_full.json); they predate current detector changes. |
| Historical V2 accuracy artefacts exist. | DEV | [`reports/v2_seed_b_results.json`](../reports/v2_seed_b_results.json), [`reports/v2_seed_c_results.json`](../reports/v2_seed_c_results.json). |

## Measured misses

| Area | Status | Reason |
|---|---|---|
| Supplier loops affect priority score. | MEASURED-MISS | The view records loop text but does not change severity or ranking. |
| Normalised entity keys affect priority score. | MEASURED-MISS | The entity table is created but is not joined by scoring views. |
| Clear disposition means documents were verified. | MEASURED-MISS | The current disposition comes from generated operating-change fields; no uploaded-document verification exists. |
| Engine superiority over pandas. | MEASURED-MISS | Stored local measurements show pandas faster on the compared checks. |

## Not implemented or not independently verified

| Area | Status | Required evidence |
|---|---|---|
| Clean separate-machine reproduction | NOT-IMPLEMENTED | Dated setup log from a fresh database installation. |
| Post-change held-out accuracy result | NOT-IMPLEMENTED | New preregistered suite and immutable run artefact. |
| Fair repeated multi-engine benchmark | NOT-IMPLEMENTED | Same workload, repetitions and environment record. |
| Large mixed-workload concurrency test | NOT-IMPLEMENTED | Repeated concurrent-run report with configuration and latency distribution. |
| Verified advanced database extension | NOT-IMPLEMENTED | Successful dated transcript and automated test. |

## Provenance

`git log --reverse` starts at `f015d5b` on 19 October 2026. Repository history has not been rewritten. Earlier inactive advanced-feature code and unsupported claims were removed from the active submission tree; the historical record remains in Git.
