"""Batch refresh for dashboard views. Run after loading updated source tables."""
from pathlib import Path
from src.db import connect

def refresh(conn):
    conn.execute('CREATE OR REPLACE TABLE GST_EVIDENCE.LEDGER_CACHE AS SELECT * FROM GST_EVIDENCE.V_LEDGER')
    sql=Path('sql/10_checks.sql').read_text()
    sql=sql[sql.index('CREATE OR REPLACE VIEW GST_EVIDENCE.V_FEATURES'):].replace('FROM GST_EVIDENCE.V_LEDGER','FROM GST_EVIDENCE.LEDGER_CACHE')
    for statement in sql.split(';'):
        if statement.strip():conn.execute(statement)
if __name__=='__main__':
    c=connect();refresh(c);c.close()
