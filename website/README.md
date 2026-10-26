# Static judge site

Eight pages share `style.css`, `site.js` and `metrics.js`. The only active numeric
source is repository `data/metrics.json`; the browser script wraps exactly that
JSON for file-URL and offline use. `scripts/build_metrics.py` attaches artifact
hashes, commit dates and recorded run dates without inventing missing timestamps.
`scripts/build_pages.py` creates the shared navigation, metadata and page content.

Run `npm run site:build` to rebuild from committed artifacts or `make site` to
rebuild and serve at http://127.0.0.1:8081. Run `make api` separately for guarded
local live queries on Cases. Every public page works without a backend.

`npm run site:smoke` checks all pages, responsive layouts, light/dark themes,
internal links and file-URL use. `npm run site:lighthouse` measures each page.
Pages CI builds first, deploys, then checks the actual public pages.
