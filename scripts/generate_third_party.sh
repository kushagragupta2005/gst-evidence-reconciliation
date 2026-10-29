#!/bin/sh
set -eu

.venv/bin/python - <<'PY'
from pathlib import Path
import subprocess
# Inventory the project's pinned dependencies, not unrelated leftovers in a reused venv.
packages=[]
for filename in ('requirements-lock.txt','scripts/requirements/benchmark.txt'):
    packages.extend(line.split('==',1)[0] for line in Path(filename).read_text().splitlines() if '==' in line and not line.startswith('#'))
with Path('docs/licences/PYTHON.md').open('w') as output:
    subprocess.run(['.venv/bin/pip-licenses','--format=markdown','--with-urls','--with-description','--packages',*packages],stdout=output,check=True)
PY
