#!/bin/sh
# Fresh source checkout + fresh venv. Uses the same machine's existing Exasol installation.
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
# Include the reviewable working tree, excluding ignored generated data, local credentials and venvs.
git ls-files --cached --others --exclude-standard -z | tar --null -T - -cf "$SCRATCH/source.tar"
mkdir "$SCRATCH/project"
tar -xf "$SCRATCH/source.tar" -C "$SCRATCH/project"
cd "$SCRATCH/project"
PYTHON="$PYTHON_BIN" sh scripts/bootstrap.sh > "$SCRATCH/setup.log" 2>&1
.venv/bin/python -m unittest discover -s tests -v >> "$SCRATCH/setup.log" 2>&1
if [ "${1:-}" != '--offline' ];then
  sh scripts/evaluate.sh >> "$SCRATCH/setup.log" 2>&1
  .venv/bin/python -m scripts.export_demo_examples >> "$SCRATCH/setup.log" 2>&1
  .venv/bin/python scripts/performance_report.py >> "$SCRATCH/setup.log" 2>&1
  .venv/bin/python -c 'from src.db import connect;c=connect(readonly=True);assert c.execute("SELECT COUNT(*) FROM GST_EVIDENCE.V_RANKED_CASES").fetchval()==28800;c.close()' >> "$SCRATCH/setup.log" 2>&1
fi
END=$(date +%s)
cd "$ROOT"
printf '{"status":"passed","elapsed_seconds":%s,"scope":"fresh source tree and venv on same machine; existing Exasol runtime reused","offline":%s}\n' "$((END-START))" "$([ "${1:-}" = '--offline' ] && echo true || echo false)" > reports/clean_setup.json
cp "$SCRATCH/setup.log" reports/clean_setup.log
tail -8 reports/clean_setup.log
cat reports/clean_setup.json
