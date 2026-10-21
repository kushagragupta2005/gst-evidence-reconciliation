# Evaluation preregistration — V3, 21 October 2026

This protocol is committed before V3 code changes are evaluated and before any V3 dataset is generated. The immutable original protocol remains in `docs/preregistration.md`. V2 and attribution outputs are development evidence only and may not be used to choose V3 settings.

## Purpose

V3 will evaluate the current reconciliation detector after adding a separately auditable document-verification disposition. The monthly priority rule stays unchanged: a factory-month is prioritised only when at least two source families have severity strictly above the selected threshold. A disposition must not add, remove, or reorder a monthly priority decision.

## Seeds and access order

| Dataset | Seed | Role | Generation and inspection rule |
|---|---:|---|---|
| V3-A | 51001 | Calibration | Generate once after this commit; select threshold and annual queue K here only. |
| V3-B | 51002 | Primary held-out evaluation | Generate once after V3-A settings are recorded; do not alter settings. |
| V3-C | 51003 | Confirmation holdback | Generate only after the V3-B report, then run once with unchanged settings. |

Each set will contain 2,400 factories and 12 months. The generator keeps its declared 30% cheat, 40% honest-decoy and 30% clean-factory assignment at factory level. V3-C will not be used for code, threshold, K, ranking, wording, or test changes before its single run.

## Frozen selection and evaluation rules

1. Evaluate threshold grid `0.025, 0.05, 0.075, 0.10, 0.125, 0.15, 0.20, 0.25, 0.30, 0.40, 0.55` on V3-A only.
2. Select the threshold with lowest factory-month balanced error `(1 - recall + false-positive rate) / 2`; use the larger threshold on a tie.
3. Evaluate annual queue `K = 2, 3, 4` on V3-A only; choose the lowest factory-level balanced error and the larger K on a tie.
4. Rank prioritised rows by source-family count, then weakest fired severity, then estimated synthetic tax exposure, then factory ID.
5. Apply the selected threshold, K and ranking unchanged to V3-B and V3-C.
6. Use 1,000 factory-cluster bootstrap resamples, percentile 95% intervals, seed 721. Selection uncertainty is not included.

## Primary outcomes

- Factory-month and factory-level recall, false-positive rate, precision and confusion counts.
- Recall by cheat type, intensity and evasive status.
- False-positive rate by clean factories, decoy type and fired-source-family combination.
- Precision at review capacities 50 and 200 for each monthly snapshot.
- Discrepancy-class confusion matrix and honest cheat misses with evidence-based reasons.
- Document-disposition outcomes: verified clear, review-only, unsupported document, and wrong-clear rate for planted cheats with deceptive explanations.

## Integrity gates

- Truth labels, scenario, intensity, evasive flag and taxpayer explanation remain outside detection views and dashboard queries.
- Generated document metadata may be used only by the disposition view; the priority SQL must not reference it.
- V3 report generation must label V3-B and V3-C `HELDOUT`; V3-A is `DEV` calibration.
- If a protocol or detector change is needed after V3-B inspection, V3-C becomes development evidence and a new preregistration is required before another held-out result.

## Run log

No V3 dataset has been generated or evaluated at commit time.
