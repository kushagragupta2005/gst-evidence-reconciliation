# Static-site smoke check — 2026-10-26

## Verified

- Served `website/` at `http://127.0.0.1:8081`.
- Browser-checked Snapshot routes: Queue, factory queue, Cleared, Review-only, Case, Ask, Results, Scale, Activity, and Method.
- Each route rendered its expected heading. The browser reported no console errors.
- The Snapshot Results page rendered V3-B and V3-C held-out metrics from `website/data/evaluation.json`.
- The source-level regression test rejects the retired UI framework token and former port outside `legacy/` and the result changelog.
- `src.api` bound locally on `127.0.0.1:8765`; its health endpoint returned HTTP 503 with a generic `ExaConnectionFailedError` detail when the restricted Exasol connection reset. It did not expose credentials or database details.

## Not verified

- The static API is local only and does not run on GitHub Pages.

## Live verification

- After the supported stop/start repair and a narrow local CORS policy, the browser displayed `Live verified` for Queue, factory queue, Cleared, Review-only, Case, Results, Scale, and Method.
- The browser Ask form returned its fixed SQL template, and Activity displayed the executed-query buffer. No console errors were reported.
