# Static-site smoke check — 2026-10-26

## Verified

- Served `website/` at `http://127.0.0.1:8081`.
- Browser-checked Snapshot routes: Queue, factory queue, Cleared, Review-only, Case, Ask, Results, Scale, Activity, and Method.
- Each route rendered its expected heading. The browser reported no console errors.
- The Snapshot Results page rendered V3-B and V3-C held-out metrics from `website/data/evaluation.json`.
- The source-level regression test rejects the retired UI framework token and former port outside `legacy/` and the result changelog.

## Not verified

- Live-mode browser routes, case evidence, note generation, activity, and read-only database access were not verified because the local Exasol endpoint reset the restricted-account connection.
- The static API is local only and does not run on GitHub Pages.
