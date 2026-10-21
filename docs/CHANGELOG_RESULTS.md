# Change log of results

This log preserves measured results and records when engineering changes alter
or do not alter the detector. A “not rerun” entry is never presented as a new
evaluation result.

## 2026-10-21 — label isolation

- **Change:** removed factory label columns and the legacy `GST_EVIDENCE.TRUTH`
  table from the detector schema. Created evaluator-only `GST_EVALUATION.TRUTH`
  and role `GST_EVALUATOR`. Revoked `SELECT ANY TABLE` and `USE ANY SCHEMA`
  from `MCP_READONLY`; granted only four evidence views.
- **Verification:** after `python -m src.load_and_score --data data/seed_c`,
  `GST_EVIDENCE.FACTORIES` had five columns, `GST_EVIDENCE.TRUTH` count was
  zero, `GST_EVALUATION.TRUTH` had 28,800 rows, the dashboard account read
  `V_RANKED_CASES` and was denied `GST_EVALUATION.TRUTH`.
- **Tests:** 18 offline tests passed.
- **Metrics:** not rerun. This changes label handling and permissions only;
  detector inputs, views, threshold, and held-out predictions are unchanged.
  The prior Seed C metrics remain historical until a preregistered rerun.
