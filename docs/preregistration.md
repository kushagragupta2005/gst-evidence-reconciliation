# Evaluation preregistration — version 1, 21 October 2026

This protocol is committed before modifying the detection generator and before
executing any new held-out result. Its purpose is to prevent tuning to Seeds B
or C.

## Dataset split and access

- **Calibration only:** Seed A (`20261019`).
- **Frozen held-out sets:** Seed B (`20261020`) and Seed C (`20261022`).
- **Future held-out sets:** new seeds will be generated once, named in the run
  log before their first evaluation, and never used for threshold selection.
- Every dataset has 2,400 factories and 12 months unless a run log says
  otherwise. Full-scale data is a performance workload, not an accuracy set.
- Ground truth lives outside the detection database in evaluator-only files.

## Predeclared detector selection

1. Generate a calibration dataset using Seed A.
2. Evaluate the threshold grid `0.025, 0.05, 0.075, 0.10, 0.125, 0.15, 0.20,
   0.25, 0.30, 0.40, 0.55` on Seed A only.
3. Select the threshold minimising factory-month balanced error
   `(1 - recall + false_positive_rate) / 2`; choose the larger threshold on a
   tie.
4. Evaluate annual queue rules `K = 2, 3, 4` on Seed A only. Select the rule
   with the lowest balanced error; report queue size as a decision consequence.
5. Apply the selected threshold and K unchanged to every held-out seed.
6. The hard gate remains at least two source families. A source family is a
   grouping of production, movement, supplier, or financial evidence; this is
   a policy rule, not a proof of statistical independence.

## Primary metrics

- Factory-month recall, false-positive rate, precision, and 95% factory-cluster
  bootstrap confidence intervals.
- Factory-level recall, false-positive rate, precision, queue size, and 95%
  factory-cluster bootstrap confidence intervals.
- Recall by cheat type, intensity, and evasive/non-evasive status.
- False-positive rate by decoy type and by clean versus decoy factory.
- Wrong-clear rate: cheats that submit forged, irrelevant, or unmatched
  supporting evidence yet are cleared by the evidence-verification rule.
- Per-check recall and leave-one-family-out ablation.

## Ranking and operations metrics

- The deployed and evaluated sort key must be identical: source-family count,
  weakest fired normalised gap, estimated INR tax exposure, then factory ID.
- Weekly queue simulation uses only April–December, when planted fraud can be
  active. January–March are reported separately as a no-active-cheat baseline.
- Report precision, recall at fixed capacity, queue size, and median
  time-to-detection for capacity budgets declared in the run configuration.

## Robustness and prevalence

- For noise variants, calibrate only on a corresponding Seed-A noise variant;
  never use B/C for recalibration.
- Missingness must be independently generated per document type; correlated
  missingness is a separate scenario.
- Realistic-prevalence precision must be measured by deterministic resampling
  or regenerated populations, not analytic adjustment alone.
- All confidence intervals use 1,000 factory-cluster bootstrap resamples with
  a recorded random seed. Threshold/K selection uncertainty is not included.

## Success criteria and decision rules

There is no target accuracy required for release. A change is retained only if
it improves integrity, fixes a material defect, or has a disclosed operational
trade-off. A metric decline is retained and documented if it results from
removing label leakage or other unrealistic assumptions. No held-out result is
deleted or replaced.

## Run log

| Date | Dataset | Purpose | Calibration changed? | Result artifact |
|---|---|---|---|---|
| 2026-10-21 | No new run | Protocol committed before rebuild | No | This file |
