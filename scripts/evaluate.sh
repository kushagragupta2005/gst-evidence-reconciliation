#!/bin/sh
set -eu
PY=${PYTHON:-.venv/bin/python}
"$PY" -m src.generate --scale medium --seed 20261019 --out data/train
"$PY" -m src.load_and_score --data data/train --features data/train/features.csv --report reports/load_train.json
"$PY" -m src.generate --scale medium --seed 20261020 --out data/generated
"$PY" -m src.load_and_score --data data/generated --features data/generated/features.csv --report reports/load_small.json
"$PY" -m src.evaluate
"$PY" -c 'import json; from src.db import connect; c=connect(); c.execute("UPDATE GST_EVIDENCE.SETTINGS SET THRESHOLD="+str(json.load(open("results.json"))["protocol"]["threshold"])); c.close()'
"$PY" -m src.cache
"$PY" scripts/report.py
