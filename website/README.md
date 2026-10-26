# Static officer interface

Run `make site` and open `http://127.0.0.1:8081`. It serves the committed
Snapshot interface only. Run `make api` in another terminal for the local,
restricted-account Live mode. `scripts/export_site_data.py` writes the
committed `data/*.json` snapshot from `results.json` and `reports/*.json`.
