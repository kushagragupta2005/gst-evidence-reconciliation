.NOTPARALLEL:
.PHONY: all bootstrap provision-dashboard reproduce reproduce-dev dashboard test scale-dev verify-clean
PY = .venv/bin/python
all: test
bootstrap:
	sh scripts/bootstrap.sh
provision-dashboard: bootstrap
	$(PY) -m src.provision_dashboard_reader
reproduce: bootstrap provision-dashboard
	$(PY) -m src.generate --scale medium --seed 51003 --out data/v3_c --fake-explanations
	$(PY) -m src.load_and_score --data data/v3_c --features data/v3_c/features.csv --report reports/reproduction_v3_c_load.json
	$(PY) -c "from src.db import connect; c=connect(readonly=True); assert c.execute('SELECT COUNT(*) FROM GST_EVIDENCE.V_RANKED_CASES').fetchval()==28800; c.close()"
reproduce-dev: bootstrap
	sh scripts/evaluate_v2.sh
	$(PY) -m scripts.export_demo_examples
	$(PY) scripts/performance_report.py

dashboard:
	.venv/bin/streamlit run app.py --server.address 127.0.0.1

test: bootstrap
	$(PY) -m unittest discover -s tests -v

scale-dev: bootstrap
	$(PY) -m src.generate --scale large --seed 20261021 --out data/full
	$(PY) -m src.benchmark --data data/full --label full
	$(PY) -m src.pandas_baseline --data data/full --label full
	$(PY) -m src.load_and_score --data data/generated --features data/generated/features.csv --report reports/load_demo_restore.json
	$(PY) -m src.benchmark --label small --no-load
	$(PY) -m src.pandas_baseline
	$(PY) scripts/performance_report.py

verify-clean:
	sh scripts/verify_clean_setup.sh
