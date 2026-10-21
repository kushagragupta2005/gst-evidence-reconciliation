#!/bin/sh
set -eu
PY=${PYTHON:-.venv/bin/python}
if [ ! -f reports/results_v1_seed_b.json ]; then
  "$PY" scripts/archive_v1.py --input results.json --output reports/results_v1_seed_b.json
fi

# Seed C is generated once as the new held-out scenario set. Its fake taxpayer
# explanations are written only to truth.csv and never imported into Exasol.
"$PY" -m src.generate --scale medium --seed 20261022 --out data/seed_c --fake-explanations
"$PY" -m src.load_and_score --data data/seed_c --features data/seed_c/features.csv --report reports/load_seed_c.json
"$PY" -m src.evaluate_v2 --train data/train --test data/seed_c --v1 reports/results_v1_seed_b.json --output results.json

# Controlled robustness datasets use the same scenario seed but altered observation process.
"$PY" -m src.generate --scale medium --seed 20261022 --out data/robust_noise_1_5x --fake-explanations --noise-multiplier 1.5
"$PY" -m src.load_and_score --data data/robust_noise_1_5x --features data/robust_noise_1_5x/features.csv --report reports/load_robust_noise_1_5x.json
"$PY" -m src.evaluate_v2 --train data/train --test data/robust_noise_1_5x --v1 reports/results_v1_seed_b.json --output reports/robustness_noise_1_5x.json

"$PY" -m src.generate --scale medium --seed 20261022 --out data/robust_noise_2x --fake-explanations --noise-multiplier 2
"$PY" -m src.load_and_score --data data/robust_noise_2x --features data/robust_noise_2x/features.csv --report reports/load_robust_noise_2x.json
"$PY" -m src.evaluate_v2 --train data/train --test data/robust_noise_2x --v1 reports/results_v1_seed_b.json --output reports/robustness_noise_2x.json

"$PY" -m src.generate --scale medium --seed 20261022 --out data/robust_missing_documents_10pct --fake-explanations --missing-documents-rate 0.10
"$PY" -m src.load_and_score --data data/robust_missing_documents_10pct --features data/robust_missing_documents_10pct/features.csv --report reports/load_robust_missing_documents_10pct.json
"$PY" -m src.evaluate_v2 --train data/train --test data/robust_missing_documents_10pct --v1 reports/results_v1_seed_b.json --output reports/robustness_missing_documents_10pct.json

# Restore seed C in Exasol and in the dashboard artifacts after the variants.
"$PY" -m src.load_and_score --data data/seed_c --features data/seed_c/features.csv --report reports/load_seed_c_restore.json
"$PY" -m src.evaluate_v2 --train data/train --test data/seed_c --v1 reports/results_v1_seed_b.json --output results.json
"$PY" scripts/build_robustness.py
"$PY" -c 'import json; from src.db import connect; c=connect(); c.execute("UPDATE GST_EVIDENCE.SETTINGS SET THRESHOLD="+str(json.load(open("results.json"))["protocol"]["threshold"])); c.close()'
"$PY" -m src.cache
"$PY" scripts/report.py
