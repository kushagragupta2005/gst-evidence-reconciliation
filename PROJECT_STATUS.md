# Project status — audit of 28 October 2026; video added 29 October

**A working synthetic decision-support prototype. The final submission video has been uploaded; the portal form still needs to be submitted.** This register is based on code and recorded verification, not a checklist completion claim.

| Component | Status | Evidence / limit |
|---|---|---|
| Public repo, MIT, sole author | VERIFIED | GitHub PUBLIC; LICENSE; git history; author Kushagra Gupta |
| Required problem statement | VERIFIED | Verbatim hash test; README and Problem page |
| Synthetic generator | VERIFIED | Deterministic tests; reports/dataset_inventory.json; three cheat types, three intensities, six decoy types, twelve months |
| Exasol Personal primary database | LIVE VERIFIED after repair | reports/judge_database_audit.json; restricted reader; 2,400 factories, 28,800 factory-months, 172,800 features |
| Frozen threshold and queue | VERIFIED | 0.05 and K=3 chosen on V3-A; reports/threshold_repair.json; all 28,800 live signals/flags match V3-C |
| Six SQL checks / four source families | VERIFIED | sql/10_checks.sql; SQL smoke and hand-case tests; two-family rule |
| Supplier loop tracing | IMPLEMENTED AS CONTEXT | Loop indicator appears in evidence; loop-only trigger, general rings and graph scoring are not implemented |
| Ranking tie-breaker | OPEN ALIGNMENT ITEM | SQL sums firing-family exposure maxima; frozen evaluator uses a global maximum. See reports/ranking_alignment_audit.json; do not claim identical tertiary semantics |
| Entity normalisation | IMPLEMENTED, batch SQL | sql/20_entities.sql; no validated cross-factory entity-resolution model |
| B/C scoring, intervals, decoys, evasive metrics | VERIFIED OFFLINE | results.json and reports/v3_c_results.json; scripts/audit_site_numbers.py reproduces saved metrics |
| Ablation | VERIFIED POINT ESTIMATES | Frozen feature hashes and baseline matrices checked; ablation intervals unmeasured |
| Wrong-clear result | CONDITIONAL SYNTHETIC RESULT | Zero events; factory-level approximate rule-of-three bound. Verification status is generator metadata; no forger test or cluster-bootstrap wrong-clear CI |
| Note validator and fallback | VERIFIED | tests/test_notes.py; current live smoke; numeric field binding is checked, not full semantic/legal validity |
| Optional LLM-written notes | IMPLEMENTED, NOT LIVE DEMONSTRATED | src/case_notes.py; no API-key-backed run is claimed; LLM never decides flags |
| Guarded follow-up SQL | LIVE VERIFIED | Three fixed SELECT intents, allow-list, row limit, timeout, rate limit; injection rejected |
| Real MCP / Python UDF demo | NOT IMPLEMENTED / NOT DEMONSTRATED | No claim of a working MCP or UDF is made |
| Current Exasol vs DuckDB | RECORDED COMPARISON | Current small V3-C dataset; matching counts/gaps; DuckDB faster; ingestion/physical-plan differences disclosed |
| 20.98M-row scale | HISTORICAL DEV | Predates current detector; not a fresh current full-scale claim |
| Current concurrency | LIVE VERIFIED, EIGHT REQUESTS | reports/live_smoke.json; includes frozen-protocol check overhead; no 50-session result |
| Eight-page site | DEPLOYED SNAPSHOT | GitHub Pages; recorded cases/answers/metrics; local API can execute follow-ups live |
| Reproducible audit evidence | PACKAGED | data/audit/*/*.gz + manifest; exact synthetic features/predictions restored and verified |
| Fresh-clone setup | OFFLINE CLONE VERIFIED | Source 91b53c51b0ff0344f8c51204f9b6a7c87323a4c3; real clone, new venv, pinned cached wheels, tests, calibration/metric replay and static build; 22 seconds; no runtime installation or second machine |
| Current PPTX/PDF/script/Q&A | UPDATED V3 | deliverables/ and docs/; previous V2 deck moved to legacy/submission/ |
| Demo video | UPLOADED | [Final submission video](https://github.com/kushagragupta2005/gst-evidence-reconciliation/releases/tag/walkthrough-2026-10-29); original user-recorded MP4, unchanged |
| Portal submission | USER ACTION REQUIRED | No form submission is claimed |
| Real taxpayer validation | NOT DONE | No taxpayer records; lawful data access, privacy and field validation remain future work |

See [judge audit](docs/JUDGE_AUDIT.md), [submission checklist](SUBMISSION_CHECKLIST.md), and [limits](LIMITATIONS.md). Historical reports remain for traceability. “VERIFIED” means the named check passed in the stated environment; it does not certify real-world accuracy.
