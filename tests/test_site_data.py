import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from src.api import require_factory
from src.followup import plan_question


class SiteDataTests(unittest.TestCase):
    def test_snapshot_export_has_audited_evaluation_sources(self):
        with tempfile.TemporaryDirectory() as folder:
            output=Path(folder)
            subprocess.run([sys.executable,'scripts/export_site_data.py','--out',str(output)],check=True)
            manifest=json.loads((output/'manifest.json').read_text())
            evaluation=json.loads((output/'evaluation.json').read_text())
        self.assertIn('results_sha256',manifest)
        self.assertEqual(evaluation['heldout_v3_b']['result_status'],'HELDOUT')
        self.assertEqual(evaluation['heldout_v3_c']['result_status'],'HELDOUT')
        self.assertIn('not_measured',evaluation)

    def test_plain_script_bundle_matches_the_json_sources(self):
        with tempfile.TemporaryDirectory() as folder:
            output=Path(folder)/'data'
            subprocess.run([sys.executable,'scripts/export_site_data.py','--out',str(output)],check=True)
            text=(output.parent/'data.js').read_text()
            self.assertTrue(text.startswith('window.__SNAPSHOT__ = '))
            bundle=json.loads(text.removeprefix('window.__SNAPSHOT__ = ').removesuffix(';\n'))
            self.assertEqual(bundle['evaluation']['heldout_v3_b'],json.loads(Path('results.json').read_text()))
            self.assertEqual(bundle['performance'],json.loads((output/'performance.json').read_text()))
        index=Path('website/index.html').read_text()
        self.assertLess(index.index('src="data.js"'),index.index('src="site.js"'))
        self.assertNotIn('data/${n}.json',Path('website/site.js').read_text())

    def test_api_factory_ids_and_followup_remain_bounded(self):
        self.assertEqual(require_factory('F000001'),'F000001')
        for invalid in ['F1',"F000001' OR 1=1",'truth']:
            with self.subTest(invalid=invalid):
                with self.assertRaises(ValueError):
                    require_factory(invalid)
        with self.assertRaises(ValueError):
            plan_question('show evidence; DROP TABLE GST_EVALUATION','F000001')

    def test_api_uses_only_the_restricted_connection(self):
        api=Path('src/api.py').read_text()
        self.assertIn('connect(readonly=True)',api)
        self.assertNotIn('connect(readonly=False)',api)
        self.assertIn('RATE_LIMIT = 60',api)
        self.assertIn('TIMEOUT_SECONDS = 30',api)
        self.assertIn('SITE_ORIGIN = "http://127.0.0.1:8081"',api)
