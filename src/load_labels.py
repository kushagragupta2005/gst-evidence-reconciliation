"""Evaluator-only label loader. Never invoke this from detector setup."""
import argparse
from pathlib import Path
from src.access_control import ensure_evaluator_access
from src.db import connect, execute_file


def load_labels(data):
    data = Path(data)
    truth = data / 'truth.csv'
    if not truth.exists():
        raise FileNotFoundError(f'No evaluator truth file at {truth}')
    conn = connect()
    try:
        execute_file(conn, 'sql/01_evaluation_schema.sql')
        ensure_evaluator_access(conn)
        conn.import_from_file(str(truth), ('GST_EVALUATION', 'TRUTH'), import_params={'skip': 1})
        return conn.execute('SELECT COUNT(*) FROM GST_EVALUATION.TRUTH').fetchval()
    finally:
        conn.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--data', default='data/generated')
    args = parser.parse_args()
    print(f'Loaded evaluator-only labels: {load_labels(args.data)}')
