#!/bin/sh
set -eu
PY=${PYTHON:-python3}
valid() { "$1" -c 'import sys;sys.exit(sys.version_info < (3,12))' >/dev/null 2>&1; }
if ! valid "$PY"; then
  for candidate in python3.14 python3.13 python3.12; do
    if command -v "$candidate" >/dev/null 2>&1 && valid "$candidate"; then PY=$candidate;break;fi
  done
fi
if ! valid "$PY";then echo 'Python 3.12+ required. Set PYTHON=/path/to/python3.12';exit 1;fi
if [ ! -x .venv/bin/python ];then "$PY" -m venv .venv;fi
.venv/bin/python -m pip install -r requirements-lock.txt
