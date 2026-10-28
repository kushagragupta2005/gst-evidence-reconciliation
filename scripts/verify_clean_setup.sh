#!/bin/sh
# A real local clone and isolated venv. Database loading is opt-in and destructive.
set -eu
ROOT=$(pwd)
SCRATCH=$(mktemp -d "${TMPDIR:-/tmp}/gst-clean.XXXXXX")
START=$(date +%s)
PYTHON_BIN=${PYTHON:-$(command -v python3.12 || true)}
if [ -z "$PYTHON_BIN" ] && [ -x "$ROOT/.venv/bin/python" ]; then PYTHON_BIN="$ROOT/.venv/bin/python"; fi
if [ -z "$PYTHON_BIN" ]; then echo 'Python 3.12+ required; set PYTHON.' >&2; exit 1; fi
MODE=${1:---offline}
case "$MODE" in --offline|--with-exasol) ;; *) echo 'Usage: verify_clean_setup.sh [--offline|--with-exasol]' >&2; exit 2;; esac
cleanup() {
 status=$?
 if [ "$status" -ne 0 ]; then
  echo "Clean setup failed; scratch files retained at $SCRATCH" >&2
  [ ! -f "$SCRATCH/setup.log" ] || tail -35 "$SCRATCH/setup.log" >&2
 else rm -rf "$SCRATCH"; fi
}
trap cleanup EXIT
PUBLIC_REMOTE=$(git remote get-url origin)
git clone --quiet --no-hardlinks "$ROOT" "$SCRATCH/project"
cd "$SCRATCH/project"
git remote set-url origin "$PUBLIC_REMOTE"
REVISION=$(git rev-parse HEAD)
PYTHON="$PYTHON_BIN" sh scripts/bootstrap.sh > "$SCRATCH/setup.log" 2>&1
.venv/bin/python -m unittest discover -s tests -v >> "$SCRATCH/setup.log" 2>&1
.venv/bin/python scripts/restore_audit_evidence.py >> "$SCRATCH/setup.log" 2>&1
PYTHONPATH=. .venv/bin/python scripts/audit_site_numbers.py >> "$SCRATCH/setup.log" 2>&1
PYTHONPATH=. .venv/bin/python scripts/site_ablation.py >> "$SCRATCH/setup.log" 2>&1
.venv/bin/python scripts/build_metrics.py >> "$SCRATCH/setup.log" 2>&1
.venv/bin/python scripts/build_pages.py >> "$SCRATCH/setup.log" 2>&1
.venv/bin/python -m compileall -q src scripts >> "$SCRATCH/setup.log" 2>&1
if [ "$MODE" = '--with-exasol' ]; then
 .venv/bin/python -m src.generate --scale small --factories 60 --seed 44001 --out data/clean_smoke >> "$SCRATCH/setup.log" 2>&1
 .venv/bin/python -m src.load_and_score --data data/clean_smoke --features data/clean_smoke/features.csv --report reports/clean_smoke_load.json >> "$SCRATCH/setup.log" 2>&1
fi
END=$(date +%s)
cd "$ROOT"
"$PYTHON_BIN" - "$REVISION" "$((END-START))" "$MODE" <<'PY'
import json,sys
from datetime import datetime,timezone
from pathlib import Path
Path('reports/clean_setup.json').write_text(json.dumps({'status':'passed','source_commit':sys.argv[1],'elapsed_seconds':int(sys.argv[2]),'mode':sys.argv[3],'time_utc':datetime.now(timezone.utc).isoformat(),'scope':'Real local Git clone, new venv, locked dependency install, tests, archived-evidence restoration, numeric audit, ablation replay, static build. Database/runtime installation and second-machine reproduction excluded.'},indent=2)+'\n')
PY
cat reports/clean_setup.json
