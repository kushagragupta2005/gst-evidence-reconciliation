"""Load detection-only inputs; labels never enter the GST_EVIDENCE schema."""
import argparse
import csv
import json
import tempfile
import time
from pathlib import Path
from src.db import connect, execute_file
from src.generate import TABLES

VIEWS = ('V_MATERIAL_OUTPUT','V_DISPATCH_INVOICE','V_STOCK_ROLLFORWARD','V_SUPPLIER_LOOP','V_RANKED_CASES','V_SINGLE_SIGNAL_DISPOSITIONS')

def detector_input(data, table):
    """Return a label-free import file, also supporting pre-isolation CSVs."""
    source = data / f'{table}.csv'
    expected = TABLES[table].split(',')
    with source.open(newline='') as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames == expected:
            return str(source), None
        if table != 'factories' or not set(expected).issubset(reader.fieldnames or []):
            raise ValueError(f'Unexpected columns in {source}: {reader.fieldnames}')
        temp = tempfile.NamedTemporaryFile(mode='w', newline='', suffix='.csv', delete=False)
        writer = csv.DictWriter(temp, fieldnames=expected, lineterminator='\n')
        writer.writeheader()
        writer.writerows({name: row[name] for name in expected} for row in reader)
        temp.close()
        return temp.name, Path(temp.name)

def load(data, features=None):
    data=Path(data)
    conn=connect()
    report={'manifest':json.loads((data/'manifest.json').read_text()),'load_seconds':{},'views':{}}
    temporary_files=[]
    try:
        execute_file(conn,'sql/00_schema.sql')
        for table in TABLES:
            if table=='truth':
                continue
            start=time.perf_counter()
            source, temporary = detector_input(data, table)
            if temporary:
                temporary_files.append(temporary)
            conn.import_from_file(source,('GST_EVIDENCE',table.upper()),import_params={'skip':1})
            report['load_seconds'][table]=time.perf_counter()-start
            print(f'Loaded {table}: {report["load_seconds"][table]:.3f}s',flush=True)
        execute_file(conn,'sql/20_entities.sql')
        threshold=json.loads(Path('results.json').read_text())['protocol']['threshold']
        if not isinstance(threshold,(int,float)) or not 0<threshold<1:raise ValueError('Invalid frozen threshold')
        conn.execute(f'UPDATE GST_EVIDENCE.SETTINGS SET THRESHOLD={threshold}')
        assert float(conn.execute('SELECT THRESHOLD FROM GST_EVIDENCE.SETTINGS').fetchval())==threshold
        report['frozen_threshold']=threshold
        execute_file(conn,'sql/10_checks.sql')
        execute_file(conn,'sql/02_readonly_grants.sql')
        for view in VIEWS:
            start=time.perf_counter()
            # Aggregate values as well as COUNT so optimizer cannot skip computations.
            column='TOTAL_SEVERITY' if view=='V_RANKED_CASES' else ('SIGNAL_COUNT' if view=='V_SINGLE_SIGNAL_DISPOSITIONS' else 'GAP')
            row=conn.execute(f'SELECT COUNT(*),SUM(ABS({column})) FROM GST_EVIDENCE.{view}').fetchone()
            report['views'][view]={'seconds':time.perf_counter()-start,'rows':row[0],'checksum':float(row[1] or 0)}
        if features:
            conn.export_to_file(features,'SELECT * FROM GST_EVIDENCE.V_FEATURES',export_params={'with_column_names':True})
        report['actual_rows']={t:conn.execute(f'SELECT COUNT(*) FROM GST_EVIDENCE.{t.upper()}').fetchval() for t in TABLES if t!='truth'}
        for t,n in report['actual_rows'].items():
            assert n==report['manifest']['rows'][t],(t,n)
        report['join_sanity']={
          'duplicate_months':conn.execute('SELECT COUNT(*) FROM (SELECT FACTORY_ID,PERIOD_MONTH FROM GST_EVIDENCE.FACTORY_MONTH GROUP BY FACTORY_ID,PERIOD_MONTH HAVING COUNT(*)<>1)').fetchval(),
          'orphan_months':conn.execute('SELECT COUNT(*) FROM GST_EVIDENCE.FACTORY_MONTH m LEFT JOIN GST_EVIDENCE.FACTORIES f ON f.FACTORY_ID=m.FACTORY_ID WHERE f.FACTORY_ID IS NULL').fetchval()}
        assert not any(report['join_sanity'].values())
    finally:
        conn.close()
        for temporary in temporary_files:
            temporary.unlink(missing_ok=True)
    return report

if __name__=='__main__':
    p=argparse.ArgumentParser()
    p.add_argument('--data',default='data/generated')
    p.add_argument('--features',default='data/generated/features.csv')
    p.add_argument('--report',default='reports/load_small.json')
    a=p.parse_args(); r=load(a.data,a.features)
    Path(a.report).write_text(json.dumps(r,indent=2)+'\n')
    print(json.dumps(r,indent=2))
