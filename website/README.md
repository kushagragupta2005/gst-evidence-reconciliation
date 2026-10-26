# Judge-facing single-page site

Run `make site` and open http://127.0.0.1:8081. Run `make api` separately for
restricted-account live follow-ups. Metrics and selected cases are recorded.
The local API probe expires after 1.5 seconds; unavailable API means Snapshot.

`data.js` embeds the committed results and reports through a plain script tag.
No snapshot fetch is needed, including on file URLs and Pages subpaths.
`scripts/export_site_data.py` rebuilds it without a database connection.
`reports/site_examples.json` records real restricted-API responses and explicitly
separates offline evaluation labels used to select the three examples.

`npm run site:smoke` checks localhost and file URLs at both requested widths.
The Pages workflow runs the same checks against the deployed public URL.
