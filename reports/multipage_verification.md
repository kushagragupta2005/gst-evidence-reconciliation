# Multi-page site verification

## Numeric audit

`docs/NUMBERS_AUDIT.md` inventories 664 numeric fields in the previously displayed metrics and records. Monthly and factory confusion matrices, rates and displayed factory-cluster intervals reproduced exactly from held-out prediction files for both seeds. Prevalence precision, zero-event denominators, ablation ratios, benchmark medians and concurrent p95 arithmetic were checked. No thresholds or labels changed.

Corrections: label factory versus month denominators; sort prevalence numerically and format it as percentages; explain ablation as conditional contribution; preserve check-specific gap signs; distinguish artifact commit dates from run dates. Historical timing provenance remains unavailable where the source lacks it.

## Site architecture

Eight static pages share navigation, footer, CSS and JavaScript. Repository `data/metrics.json` is canonical. The build copies this JSON to the site and wraps the identical object in metrics.js for file/offline use. Pages CI rebuilds from source artifacts before deployment. The deployed snapshot stamp therefore describes its own build commit. No runtime frameworks or external font/CDN requests are used.

The immutable problem text is on Problem. Home uses an actual recorded dispatch/invoice series. Cases provides the three recorded outcomes and guarded questions. Results names the seed, units and artifact links. System preserves the honest engine comparison and historical scale limitation. Data and Limits disclose generated verification, lawful-access requirements and unresolved work.

## Local verification

- 33 Python tests and 149 subtests passed, including canonical-data equality, artifact hashes, immutable statement and reader/SQL guard contracts.
- 56 Chromium page configurations passed: every page at three widths in both light/dark themes, plus offline file URLs.
- Internal-link checks recorded 64 successful HTTP responses in the local run.
- Accessibility checks cover WCAG A/AA automation in both themes. This is not a full assistive-technology audit.
- Lighthouse 13.5.0 scored every page 100/100/100/100 in the final local run, after fixing inline-link visibility, hover contrast, heading order and deferred-content layout shifts. See lighthouse_local.json for the actual environment and run timestamp. Scores vary by environment; no universal guarantee is claimed.

Public browser checks run after deployment in the Pages workflow. Public Lighthouse results will be recorded separately. Database evaluation, full-scale loading, a sophisticated-forger test, ablation intervals and second-machine reproduction were not performed by this presentation task. No new fresh-clone claim is made.
