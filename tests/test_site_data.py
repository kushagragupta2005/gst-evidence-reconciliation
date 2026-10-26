import json
import subprocess
import sys
import unittest
from pathlib import Path

from src.api import require_factory
from src.followup import plan_question


class SiteDataTests(unittest.TestCase):
    def test_snapshot_export_has_audited_evaluation_sources(self):
        subprocess.run([sys.executable,'scripts/export_site_data.py'],check=True)
        manifest=json.loads(Path('website/data/manifest.json').read_text())
        evaluation=json.loads(Path('website/data/evaluation.json').read_text())
        self.assertIn('results_sha256',manifest)
        self.assertEqual(evaluation['heldout_v3_b']['result_status'],'HELDOUT')
        self.assertEqual(evaluation['heldout_v3_c']['result_status'],'HELDOUT')
        self.assertIn('not_measured',evaluation)

    def test_api_factory_ids_and_followup_remain_bounded(self):
        self.assertEqual(require_factory('F000001'),'F000001')
        for invalid in ['F1',"F000001' OR 1=1",'truth']:
            with self.subTest(invalid=invalid):
                with self.assertRaises(ValueError):
                    require_factory(invalid)
        compiled=plan_question('show evidence; DROP TABLE GST_EVALUATION','F000001')
        self.assertNotIn('DROP',compiled)
        self.assertTrue(compiled.endswith('LIMIT 200'))

    def test_api_uses_only_the_restricted_connection(self):
        api=Path('src/api.py').read_text()
        self.assertIn('connect(readonly=True)',api)
        self.assertNotIn('connect(readonly=False)',api)
        self.assertIn('RATE_LIMIT = 60',api)
        self.assertIn('TIMEOUT_SECONDS = 30',api)
