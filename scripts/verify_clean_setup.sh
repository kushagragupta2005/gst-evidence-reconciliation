#!/bin/sh
# Rebuild an isolated source tree and virtual environment.  The default mode
# also loads a small generated dataset into a configured local Exasol runtime.
set -eu
ROOT=$(pwd)
SCRATCH=$(mktemp -d "${TMPDIR:-/tmp}/gst-clean.XXXXXX")
START=$(date +%s)
PYTHON_BIN=${PYTHON:-$(command -v python3.12 || true)}
if [ -z "$PYTHON_BIN" ] && [ -x "$ROOT/.venv/bin/python" ]; then PYTHON_BIN="$ROOT/.venv/bin/python"; fi
if [ -z "$PYTHON_BIN" ]; then echo 'Python 3.12+ not found; set PYTHON to its absolute path.' >&2; exit 1; fi
cleanup() {
  status=$?
  if [ "$status" -ne 0 ]; then
    echo "Clean setup failed; scratch files kept at $SCRATCH" >&2
    [ ! -f "$SCRATCH/setup.log" ] || tail -40 "$SCRATCH/setup.log" >&2
  else
    rm -rf "$SCRATCH"
  fi
}
trap cleanup EXIT

git ls-files --cached --others --exclude-standard -z | "$PYTHON_BIN" -c 'import os,sys; paths=[p for p in sys.stdin.buffer.read().split(bytes([0])) if p and os.path.exists(p)]; sys.stdout.buffer.write(bytes([0]).join(paths)+(bytes([0]) if paths else b""))' | tar --null -T - -cf "$SCRATCH/source.tar"
mkdir "$SCRATCH/project"
tar -xf "$SCRATCH/source.tar" -C "$SCRATCH/project"
cd "$SCRATCH/project"
PYTHON="$PYTHON_BIN" sh scripts/bootstrap.sh > "$SCRATCH/setup.log" 2>&1
.venv/bin/python -m unittest discover -s tests -v >> "$SCRATCH/setup.log" 2>&1
.venv/bin/python -m compileall -q src scripts app.py >> "$SCRATCH/setup.log" 2>&1

OFFLINE=false
if [ "${1:-}" = '--offline' ]; then
  OFFLINE=true
else
  .venv/bin/python -m src.generate --scale small --factories 60 --seed 44001 --out data/clean_smoke >> "$SCRATCH/setup.log" 2>&1
  .venv/bin/python -m src.load_and_score --data data/clean_smoke --features data/clean_smoke/features.csv --report reports/clean_smoke_load.json >> "$SCRATCH/setup.log" 2>&1
  .venv/bin/python - <<'PY' >> "$SCRATCH/setup.log" 2>&1
from src.db import connect
conn = connect(readonly=True)
assert conn.execute('SELECT COUNT(*) FROM GST_EVIDENCE.V_RANKED_CASES').fetchval() == 720
conn.close()
PY
fi

END=$(date +%s)
cd "$ROOT"
mkdir -p reports
printf '{"status":"passed","elapsed_seconds":%s,"scope":"fresh source tree and venv; %s","offline":%s}\n' \
  "$((END-START))" \
  "$([ "$OFFLINE" = true ] && echo 'offline SQL compatibility smoke only' || echo 'configured existing Exasol runtime with 60-factory smoke load')" \
  "$OFFLINE" > reports/clean_setup.json
cp "$SCRATCH/setup.log" reports/clean_setup.log
tail -8 reports/clean_setup.log
cat reports/clean_setup.json
