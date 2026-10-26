# Single-page redesign verification

Snapshot loading fix: commit ca1c697. Pages workflow 40286187576 passed its public Chromium check.

The page now uses the existing local serve command and GitHub Pages deployment with a plain bundled data script, relative assets, a 1.5-second local API probe, and snapshot fallback. Public/file contexts do not contact a localhost API.

Case examples were recorded through the restricted local API; source evaluation labels select examples but are never used in detection or queried through the API. See site_examples.json for recording date, source hash, source SHA, actual SQL/results and timings. Notes are deterministic fallback, validated against the displayed month's evidence.

The ablation is a new post-hoc replay of both frozen held-out feature files. Feature hashes and full-check confusion matrices match committed evaluation artifacts exactly. It supplies point estimates only. No thresholds or detector logic changed.

Verification: 30 Python tests and 119 subtests passed. Browser checks cover both seed controls, three cases, three guarded question chips, metric provenance, overflow and keyboard focus at 1440 and 390 pixels. Accessibility scanning covers WCAG A/AA rules on HTTP; axe itself tries an XHR for CSS on file URLs, so that scan is omitted for file URLs. Application file-URL console/network checks remain enabled. See site_browser_smoke.json for actual observations. Automated accessibility checks do not substitute for a full assistive-technology audit.

Public verification runs after deployment in Pages CI; its report is attached to that workflow. No new fresh-clone or second-machine reproduction is claimed by this redesign.
