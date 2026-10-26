# Live-mode connection diagnosis — 2026-10-26

## Cause

`exakit status --json` reported a **conflict**: the Exasol launcher was listening on `127.0.0.1:8563`, while `exasol status` reported `database_connection_failed`. The deployment metadata said `running`, but the database was not accepting sessions, so PyExasol received a connection reset. This was a stale/stuck local deployment, not a restricted-account privilege or TLS problem.

## Evidence checked

- Deployment information: `127.0.0.1:8563`, Exasol Personal, self-signed TLS.
- Before fix: `exasol status` reported `database_connection_failed`; `exakit` supplied `exakit start` as the remedy after clearing the port conflict.
- Restricted-account minimal login after the fix: `SELECT 1` succeeded; system privileges were `CREATE SESSION`; object privileges were `SELECT` and `USAGE`; `GST_EVALUATION.TRUTH` access was denied.
- The project connection uses self-signed local TLS with certificate validation disabled only for local hosts in `src/db.py`, and sets a 30-second session query timeout.

## Fix

Used the supported lifecycle commands only: `exakit stop`, then `exakit start`. The post-fix status was `running` and `database_ready`; label-free reconciliation views contained 28,800 factory-month rows.

## Verification

`reports/live_smoke.json` is the executed endpoint and concurrency record. It starts a local API process, exercises the allow-listed endpoints, checks rejected requests, and records its eight-query latency distribution. It is skipped with a clear message when the restricted account is unavailable.
