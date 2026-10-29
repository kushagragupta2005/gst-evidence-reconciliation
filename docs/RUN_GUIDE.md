# Setup, reproduction and verification

[Project overview](../README.md) · [Implementation status](../PROJECT_STATUS.md) · [Limitations](../LIMITATIONS.md)

## Recorded demo and offline audit

Prerequisites: Git, Make, Python 3.12+ and network access for the first dependency installation. No Exasol instance or LLM API key is needed for this mode.

```sh
git clone https://github.com/kushagragupta2005/gst-evidence-reconciliation.git
cd gst-evidence-reconciliation
sh scripts/bootstrap.sh
make all
make site
```

Open http://127.0.0.1:8081/. Stop the server with Ctrl+C. The public equivalent is the [GitHub Pages site](https://kushagragupta2005.github.io/gst-evidence-reconciliation/).

Expected output: regression tests pass; archived A/B/C features and predictions restore with matching hashes; calibration, held-out metrics and ablation replay; the static pages build. The offline pipeline does not contact or replace Exasol. The site displays its mode, source commit and recorded timestamps. All examples are synthetic.

Measured reproduction scope: a real local clone and fresh venv passed in 22 seconds using cached pinned wheels on the author's machine at commit `91b53c51b0ff0344f8c51204f9b6a7c87323a4c3`. First-time downloads and database setup take additional time; their duration is not measured by that result. No second-machine verification is claimed. [Report](../reports/clean_setup.json).

## Local live Exasol queries

Install and start Exasol Personal using its [official instructions](https://github.com/exasol/exasol-personal#-get-started). Verify `SELECT 1;` using your local credentials. Do not put credentials in Git.

If the V3-C schema and restricted reader already exist:

```sh
make api
# In another terminal:
make site
# In a third terminal, to check the API:
make live-smoke
```

The API binds 127.0.0.1:8765; the site binds 127.0.0.1:8081. `EXASOL_DSN`, `EXASOL_RO_USER` and `EXASOL_RO_SECRET` configure the restricted reader. The default local reader is DASHBOARD_READER, with its secret kept outside the repo. Grant only CREATE SESSION, schema USAGE and explicit SELECT on the four label-free views in [sql/02_readonly_grants.sql](../sql/02_readonly_grants.sql).

Live queries use three fixed SELECT intents, a 200-row limit, a 30-second database timeout and a rate limit. They cannot submit arbitrary SQL or read truth. The API checks the frozen rule before enabling Live responses. Without a reachable API, the site keeps the recorded snapshot. The curated example evidence remains recorded even when follow-ups are live.

The [28 October live smoke](../reports/live_smoke.json) and [database audit](../reports/judge_database_audit.json) record actual scope, commit, guard checks and latency. They are dated results, not a claim the database is currently running.

## Generate and load V3-C

These commands need the loader's write-capable account. They are separate from read-only runtime queries. **`make reproduce` drops and recreates GST_EVIDENCE and replaces its data.** Run only against an authorised local demo database.

```sh
make provision-reader
make reproduce
```

The first command creates/repairs the local reader account using loader credentials and stores its secret outside the repo with owner-only permissions. Set `EXASOL_RO_SECRET` first to supply a secret yourself. The loader reapplies restricted grants after creating the views. The reproduction target generates seed 51003, loads label-free tables, fixes the threshold to the published protocol, checks joins/counts and exports features. Expected output: 28,800 ranked monthly rows and the report `reports/reproduction_v3_c_load.json`. Evaluator truth stays outside the detection schema.

## Commands

| Command | Purpose |
|---|---|
| `make test` | Offline regression tests and generated-data SQL smoke |
| `make restore-audit` | Restore exact compressed synthetic scoring inputs |
| `make audit` | Recompute calibration, B/C metrics and ablation |
| `make all` | Tests, audit and static export |
| `make site` / `make api` | Recorded site / restricted local API |
| `make live-smoke` | API endpoints, guards and eight parallel requests; clear skip if DB unavailable |
| `sh scripts/verify_clean_setup.sh --offline` | New local clone, new venv, pinned install and offline pipeline |
| `make export-site-data` | Refresh snapshot from result/report artifacts |

`verify_clean_setup.sh --with-exasol` also replaces local evidence data; it is explicitly opt-in. Historical V2 and scale-development commands remain in Makefile for traceability, not as current held-out claims. The original submit-candidate-1 tag is historical; its older verification does not certify later changes.

## Unreliable package network

Use the bootstrap's retry options or prepare an OS/Python-compatible local wheelhouse:

```sh
python3 -m pip download --retries 10 --timeout 60 -r requirements-lock.txt -d wheelhouse
PIP_NO_INDEX=1 PIP_FIND_LINKS="$PWD/wheelhouse" sh scripts/verify_clean_setup.sh --offline
```

Do not upload wheels, venvs, database images or credentials.

## Browser and numeric checks

```sh
npm ci
npx playwright install chromium
npm run site:smoke -- --url https://kushagragupta2005.github.io/gst-evidence-reconciliation/
PYTHONPATH=. .venv/bin/python scripts/audit_site_numbers.py
```

The browser check covers eight pages at three widths in both themes, source-linked numbers, case controls, accessibility and console/network failures. Local mode also checks file URLs. GitHub Pages repeats the public check after deployment. Lighthouse results are recorded environment-specific measurements, not guaranteed scores.

## Performance and provenance

Current small V3-C comparison: [benchmark_current_reader.json](../reports/benchmark_current_reader.json), 2,400 factories and 172,800 check rows. Matching stock/supplier counts and gap checksums were verified. DuckDB was faster; ingestion and physical plans differ. Install requirements-benchmark.txt and run `PYTHONPATH=. .venv/bin/python scripts/benchmark_current_reader.py` to repeat it with V3-C already loaded. This uses only the reader.

The 20.98-million-row run is historical DEV, predating the current detector. It is not fresh current-scale proof. Current eight-request latency includes protocol-guard work; use the latest live_smoke artifact instead of older figures. No MCP, UDF or 50-session demonstration is claimed.

The repaired live threshold mismatch and open tertiary ranking-key difference are documented in [the audit](JUDGE_AUDIT.md). [SUBMISSION_MANIFEST.json](../SUBMISSION_MANIFEST.json) hashes publishable files; [ARTIFACT_INDEX.json](../reports/ARTIFACT_INDEX.json) separates current from historical results. Detailed formulas and evaluation tables remain in the audit rather than being repeated on the front page.
