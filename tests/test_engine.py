import contextlib
import csv
import hashlib
import io
import json
import sqlite3
import re
import tempfile
import unittest
from pathlib import Path
from src.generate import generate,TABLES
from src.evaluate import rates
from src.followup import compile_plan,guard_sql,plan_question

class GeneratorTests(unittest.TestCase):
    def test_seed_determinism_and_months(self):
        with tempfile.TemporaryDirectory() as folder:
            a,b,c=[Path(folder)/s for s in 'abc']
            with contextlib.redirect_stdout(io.StringIO()):
                generate('small',a,123,60);generate('small',b,123,60);generate('small',c,124,60)
            for name in TABLES:self.assertEqual((a/(name+'.csv')).read_bytes(),(b/(name+'.csv')).read_bytes())
            self.assertNotEqual((a/'factory_month.csv').read_bytes(),(c/'factory_month.csv').read_bytes())
            m=json.loads((a/'manifest.json').read_text());self.assertEqual(m['rows']['factory_month'],60*12)
            self.assertEqual(m['raw_evidence_rows'],sum(v for k,v in m['rows'].items() if k not in ('truth','factories','suppliers','machines')))
    def test_problem_statement_unchanged(self):
        problem=Path('README.md').read_text().split('\n> ',1)[1].split('\n',1)[0]
        self.assertEqual(hashlib.sha256(problem.encode()).hexdigest(),'d5b711f68044bdd8079701b61916870971a76d3a20104649a4bd0035c870ba33')
    def test_sql_does_not_use_truth(self):
        detector_sql=(Path('sql/00_schema.sql').read_text()+Path('sql/10_checks.sql').read_text()).upper()
        for name in ['GROUND_TRUTH','SCENARIO','GST_EVALUATION']:
            self.assertNotIn(name,detector_sql)
        self.assertNotIn('CREATE OR REPLACE TABLE GST_EVIDENCE.TRUTH',detector_sql)
    def test_detection_factory_input_has_no_labels(self):
        fields=TABLES['factories'].upper()
        self.assertNotIn('GROUND_TRUTH',fields)
        self.assertNotIn('SCENARIO',fields)
    def test_active_cheats_break_a_stock_identity(self):
        with tempfile.TemporaryDirectory() as folder:
            path=Path(folder)
            with contextlib.redirect_stdout(io.StringIO()):
                generate('small',path,31001,120)
            with (path/'truth.csv').open() as handle:
                truth={(r['factory_id'],r['period_month']):r for r in csv.DictReader(handle)}
            detected=set()
            with (path/'factory_month.csv').open() as handle:
                for row in csv.DictReader(handle):
                    label=truth[(row['factory_id'],row['period_month'])]
                    if label['is_cheat']=='1':
                        expected=float(row['opening_stock'])+float(row['purchases_finished'])+float(row['declared_output'])-float(row['declared_dispatch'])
                        if abs(expected-float(row['closing_stock']))>1e-3:
                            detected.add(label['scenario'])
            self.assertEqual(detected,{'hidden_production','itc_inflation','eway_reuse'})
    def test_dashboard_source_does_not_read_evaluation_labels(self):
        dashboard=Path('app.py').read_text().upper()
        for token in ['HELD_OUT_PREDICTIONS','IS_CHEAT','.SCENARIO','GST_EVALUATION','TRUTH.CSV']:
            self.assertNotIn(token,dashboard)
        plans=Path('src/followup.py').read_text().upper()
        self.assertNotIn('GST_EVALUATION',plans)

class SQLTests(unittest.TestCase):
    def setUp(self):
        self.c=sqlite3.connect(':memory:')
        self.c.execute("ATTACH DATABASE ':memory:' AS GST_EVIDENCE")
        self.c.create_function('GREATEST',-1,lambda *v:max(v) if all(x is not None for x in v) else None)
        # Same view SQL; SQLite shim uses REAL for Exasol DECIMAL division and portable CREATE syntax.
        for filename in ['sql/00_schema.sql','sql/10_checks.sql']:
            sql=Path(filename).read_text().replace('CREATE SCHEMA IF NOT EXISTS GST_EVIDENCE;','').replace('CREATE OR REPLACE','CREATE')
            sql=re.sub(r'DECIMAL\(\d+,\d+\)','REAL',sql)
            self.c.executescript(sql)
        self.c.execute("INSERT INTO GST_EVIDENCE.FACTORY_MONTH VALUES ('F000001','2026-01','steel_rod',100,100,10,80,50,130,320,160,0)")
    def tearDown(self):self.c.close()
    def test_hand_computed_stock(self):
        # 100 + 10 + 80 - 50 = 140 expected, actual 130, gap 10.
        row=self.c.execute('SELECT EXPECTED,OBSERVED,GAP FROM GST_EVIDENCE.V_STOCK_ROLLFORWARD').fetchone()
        self.assertEqual(row,(140,130,10))
    def test_two_checks_same_source_not_two_signals(self):
        self.c.execute('UPDATE GST_EVIDENCE.FACTORY_MONTH SET DECLARED_OUTPUT=60')
        row=self.c.execute('SELECT SIGNAL_COUNT,STATUS FROM GST_EVIDENCE.V_RANKED_CASES').fetchone()
        self.assertEqual(row,(1,'review only'))
    def test_independent_movement_corroborates(self):
        self.c.execute("INSERT INTO GST_EVIDENCE.EWAY_BILLS VALUES ('E1','F000001','2026-01',50,'KA01')")
        self.assertEqual(self.c.execute('SELECT SIGNAL_COUNT,STATUS FROM GST_EVIDENCE.V_RANKED_CASES').fetchone(),(2,'prioritise'))
    def test_window_checks_stock_continuity(self):
        self.c.execute("INSERT INTO GST_EVIDENCE.FACTORY_MONTH VALUES ('F000001','2026-02','steel_rod',150,100,0,80,50,180,320,160,0)")
        row=self.c.execute("SELECT SEVERITY FROM GST_EVIDENCE.V_STOCK_ROLLFORWARD WHERE PERIOD_MONTH='2026-02'").fetchone()
        self.assertEqual(row,(.25,))

class GuardAndMetricsTests(unittest.TestCase):
    def test_template_select(self):
        sql=plan_question('show dispatch gap by month for factory F000012','F000001')
        self.assertEqual(guard_sql(sql),compile_plan({'intent':'dispatch','factory_id':'F000012'}))
        self.assertTrue(sql.endswith('LIMIT 200'))
    def test_injection_rejected(self):
        sql=compile_plan({'intent':'dispatch','factory_id':'F000012'})
        for attack in [sql+'; DROP TABLE X',sql+' -- comment',sql.replace('LIMIT 200','LIMIT 999'),sql.replace('V_FEATURES','FACTORIES'),'SELECT 1','DELETE FROM X']:
            with self.subTest(attack=attack),self.assertRaises(ValueError):guard_sql(attack)
        with self.assertRaises(ValueError):compile_plan({'intent':'dispatch','factory_id':"F000001' OR 1=1"})
    def test_confusion_counts(self):
        m=rates([1,1,0,0],[1,0,1,0]);self.assertEqual((m['tp'],m['fp'],m['fn'],m['tn']),(1,1,1,1))
        self.assertEqual(m['recall'],.5);self.assertEqual(m['fpr'],.5)
    def test_no_positive_labels(self):self.assertIsNone(rates([0,0],[0,0])['recall'])
