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

## 2026-10-21 — stock-integrity generator revision

- **Pre-registration:** V2-A/Seed 31001 was calibration only; V2-B/31002 and
  V2-C/31003 were registered as frozen held-out datasets before generation in
  `docs/preregistration.md`. Original Seeds B/C and their artifacts remain
  unchanged.
- **Change:** active hidden-production cases retain concealed physical output in
  closing stock; active ITC cases falsify the closing balance; active e-way
  reuse cases physically dispatch more than they declare. The stock SQL now
  deducts a documented raw-stock-change tolerance from stock severity.
- **Tests:** 19 offline tests passed, including a generator test that all three
  active cheat types break a stock identity. V2-C load produced 2,627 stock
  evidence rows; original Seed C had zero.
- **V2-B held-out:** threshold 0.05, K=2. Monthly recall 82.74% (95% CI
  80.46%–84.88%), FPR 2.22% (2.04%–2.43%), precision 85.29%
  (83.66%–86.75%). Stock-check recall 88.95%. Evasive monthly recall 57.24%.
- **V2-C held-out replication:** threshold 0.05, K=2. Monthly recall 79.71%
  (77.22%–82.18%), FPR 2.18% (1.98%–2.39%), precision 85.51%
  (83.79%–87.08%). Factory queue: 711 factories, recall 85.69%, FPR 5.60%,
  precision 86.78%. Stock-check recall 88.09%; evasive monthly recall 49.14%.
- **Interpretation:** this is a new synthetic-generator version, not an
  improvement over the original Seed C experiment. The stronger metrics follow
  from a new observable stock mechanism and must not be compared as a
  like-for-like gain. Full-scale timing has not yet been rerun for V2.

## 2026-10-21 — ranking/exposure alignment

- **Change:** replaced the misleading dimensionless `TOTAL_ABSOLUTE_GAP` field
  with `TOTAL_SEVERITY`. `V_RANKED_CASES` now exposes source-family count,
  weakest fired severity, and `ESTIMATED_TAX_EXPOSURE_INR`; the dashboard and
  evaluator use the same lexicographic order.
- **Exposure assumption:** unreported production/dispatch and stock gaps use
  120 INR per synthetic unit × 18%; supplier gaps use 90 INR × 18%; bank gaps
  use the positive unexplained rupee difference × 18%. This is an ordering
  estimate, never an assessed tax demand.
- **Verification:** reloaded frozen V2-A/B/C input through revised views and
  reran both held-out evaluators. The two-signal decisions and headline
  recall/FPR stayed unchanged; V2-C Precision@50 is 75.00% and Precision@200
  is 74.96% under the aligned order. 20 offline tests passed.
