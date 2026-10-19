#!/bin/sh
set -eu
PYTHON=${PYTHON:-python3}
supports_runtime() {
  "$1" -c 'import sys; sys.exit(0 if sys.version_info >= (3, 11) else 1)' >/dev/null 2>&1
}
if ! supports_runtime "$PYTHON"; then
  for candidate in python3.13 python3.12 python3.11; do
    if command -v "$candidate" >/dev/null 2>&1 && supports_runtime "$candidate"; then
      PYTHON=$candidate
      break
    fi
  done
fi
if ! supports_runtime "$PYTHON"; then
  echo "Python 3.11+ is required. Install it or set PYTHON=/path/to/python3.11+" >&2
  exit 1
fi

"$PYTHON" -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
sh scripts/evaluate.sh
exec .venv/bin/streamlit run app.py
