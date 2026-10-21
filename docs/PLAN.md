# Submission plan — 21 October 2026

Ordered by expected judging value divided by effort. Phase 1 is the submission
build due by 25 October 2026 at 18:00 IST; Phase 2 starts only after submission.

## Phase 1 — submission build

| Rank | Task | Rubric value | Effort | Completion evidence |
|---:|---|---|---|---|
| 1 | Isolate labels into evaluator-only storage; prove detector and dashboard cannot access them. | High: integrity/Q&A | Medium | Schema, privileges, negative-access tests |
| 2 | Fix stock scenarios and add verified-document evidence for clears, wrong clears, INR exposure. | High: impact/technical | High | Generator, SQL, tests, held-out report |
| 3 | Align deployed ranking with evaluation; test it. | High: UX/integrity | Medium | Shared ranking SQL/function and test |
| 4 | Submission compliance: README, run guide, deck alignment, video script, checklist. | High: documentation | Medium | Script-generated artifacts and checklist |
| 5 | Obtain one verified Exasol advanced feature: Python UDF or successful MCP transcript; otherwise remove all claims. | High: Exasol | Medium | Executed SQL/MCP transcript and test |
| 6 | Optimise ranked cases using profile evidence and record before/after full-scale results. | High: Exasol | Medium | Profile, benchmark artifact, reproducible query |
| 7 | Fair repeated benchmark: Exasol, pandas, DuckDB; state losses. | Medium: technical | Medium | Identical workload harness and report |
| 8 | Evaluation repairs: evasive recall, weekly queue, ablation, realistic prevalence, PR/ROC/Brier. | High: integrity | High | Frozen held-out run log/results |
| 9 | Officer demo safety: pre-warm, clear/escalate details, what-if controls. | Medium: live demo | Medium | Screenshots and smoke test |
| 10 | Clean-checkout, Exasol setup, small end-to-end smoke test in CI. | High: reproducibility | Medium | CI log and clean-run artifact |
| 11 | 50-session mixed-workload concurrency test. | Medium: Exasol | Medium | Repeated latency report |

## Phase 2 — finalist build after submission

1. Factory-specific median/MAD baseline with structural-break handling.
2. Transparent likelihood-ratio evidence combination and comparison-only GBDT.
3. Scored supplier loops and shared-entity rings.
4. Adaptive adversaries and feedback-loop simulation.
5. Real-data adapter specification, roles/audit log/threat model, and live-demo
   Q&A preparation.

## Guardrails

- No held-out run before its configuration is recorded in `docs/preregistration.md`.
- Every change runs offline tests; changes that alter detector behaviour also run
  calibration and held-out evaluation and append results to
  `docs/CHANGELOG_RESULTS.md`.
- Negative or weaker results remain visible.
