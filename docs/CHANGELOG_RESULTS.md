# Result change log

This log preserves the interpretation of recorded artefacts. A result labelled **DEV** is a development observation, not a new held-out submission claim.

## 21 October 2026 — baseline cleanup

- Removed inactive advanced-feature code and unsupported claims from the active submission tree. No successful execution artefact existed for those paths.
- Replaced stale README headline metrics with links to the underlying **DEV** artefacts.
- Made the dashboard require an explicitly configured restricted database account; the account can access only label-free views.
- Reworked the release checklist so a separate-machine reproduction and a new preregistered post-change held-out suite remain open requirements.

## 21 October 2026 — label isolation

- Detection input `FACTORIES` has five identity columns only. Truth labels load into evaluator-only storage.
- Offline tests block truth references in detector SQL and dashboard source.
- This is an engineering integrity change. It does not constitute a new accuracy measurement.

## 21 October 2026 — V2 stock and ranking work

- The stock scenario revision, ranking alignment, threshold trade-off and fixed-seed attribution experiment are recorded in [`ATTRIBUTION.md`](ATTRIBUTION.md) and the V2 JSON artefacts.
- Their results are **DEV** because the data and outputs have already been used for development and inspection.
- The attribution study found that the earlier false-positive-rate reduction came from threshold selection. The planted stock mechanism changed synthetic recall at a fixed threshold; it is not real-world validation.
