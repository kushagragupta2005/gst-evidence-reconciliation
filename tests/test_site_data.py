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
        self.assertLess(index.index('src="./metrics.js"'),index.index('src="./site.js"'))
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

    def test_page_preserves_problem_and_has_no_forbidden_hues(self):
        import colorsys
        import hashlib
        import re
        page=Path('website/problem/index.html').read_text()
        statement=re.search(r'<p id="problem-statement">(.*?)</p>',page).group(1)
        self.assertEqual(hashlib.sha256(statement.encode()).hexdigest(),'d5b711f68044bdd8079701b61916870971a76d3a20104649a4bd0035c870ba33')
        css=Path('website/style.css').read_text()
        self.assertNotRegex(css.lower(),r'pink|magenta|lime|monospace')
        for token in re.findall(r'#[0-9a-fA-F]{3,6}\b',css):
            h=token[1:]; h=''.join(c*2 for c in h) if len(h)==3 else h
            rgb=[int(h[i:i+2],16)/255 for i in (0,2,4)]
            hue,saturation,_=colorsys.rgb_to_hsv(*rgb)
            self.assertFalse(saturation>.25 and (60<=hue*360<=100 or 270<=hue*360<=345),token)

    def test_bundle_measurements_match_committed_evidence(self):
        bundle=json.loads(Path('website/data.js').read_text().removeprefix('window.__SNAPSHOT__ = ').removesuffix(';\n'))
        for key,file in [('heldout_v3_b','results.json'),('heldout_v3_c','reports/v3_c_results.json'),('ablation','reports/site_ablation.json')]:
            self.assertEqual(bundle['evaluation'][key],json.loads(Path(file).read_text()))
        self.assertEqual(bundle['examples'],json.loads(Path('reports/site_examples.json').read_text()))
        self.assertEqual(bundle['performance']['live_smoke'],json.loads(Path('reports/live_smoke.json').read_text()))
        self.assertEqual(bundle['performance']['benchmark_full'],json.loads(Path('reports/benchmark_full.json').read_text()))
        from src.case_notes import validate_note
        for case in bundle['examples']['examples']:
            self.assertTrue(validate_note(case['note'],case['evidence']))
        for seed in ['v3_b','v3_c']:
            for key in ['tp','fp','tn','fn']:
                self.assertEqual(bundle['evaluation']['ablation']['seeds'][seed]['checks']['all_checks'][key],bundle['evaluation']['heldout_'+seed]['factory_month'][key])

    def test_wrong_clear_bound_uses_factories_not_correlated_months(self):
        report=json.loads(Path('reports/wrong_clear_bounds.json').read_text())
        self.assertIn('independent factory outcomes',report['method'])
        for seed,value in report['seeds'].items():
            self.assertEqual(value['wrong_clear_factories'],0)
            self.assertLess(value['active_cheat_factories'],value['active_cheat_months'])
            self.assertAlmostEqual(value['approximate_upper_95'],3/value['active_cheat_factories'])
            dispositions=json.loads(Path(f'reports/{seed}_dispositions.json').read_text())
            self.assertEqual(dispositions['wrong_clears_active_cheat_months'],0)
        bundle=json.loads(Path('website/data.js').read_text().removeprefix('window.__SNAPSHOT__ = ').removesuffix(';\n'))
        self.assertEqual(bundle['evaluation']['wrong_clear_bounds'],report)

    def test_current_benchmark_is_stamped_and_count_checked(self):
        import hashlib
        report=json.loads(Path('reports/benchmark_current_reader.json').read_text())
        self.assertEqual(report['detector_sql_sha256'],hashlib.sha256(Path('sql/10_checks.sql').read_bytes()).hexdigest())
        self.assertIn('not a new full-scale run',report['scope'])
        self.assertIn('time_utc',report)
        self.assertIn('git_sha',report)
        for check in report['checks'].values():
            self.assertTrue(check['equivalent_counts_and_gaps'])
            self.assertEqual(len(check['exasol_seconds']),len(check['duckdb_seconds']))
            self.assertGreater(check['exasol_median_seconds'],0)
            self.assertGreater(check['duckdb_median_seconds'],0)
        bundle=json.loads(Path('website/data.js').read_text().removeprefix('window.__SNAPSHOT__ = ').removesuffix(';\n'))
        self.assertEqual(bundle['performance']['current_reader'],report)

    def test_canonical_metrics_are_the_only_page_data_bundle(self):
        import hashlib
        canonical=json.loads(Path('data/metrics.json').read_text())
        self.assertEqual(canonical,json.loads(Path('website/data/metrics.json').read_text()))
        self.assertEqual(canonical,json.loads(Path('website/metrics.js').read_text().removeprefix('window.__METRICS__ = ').removesuffix(';\n')))
        for seed,file in [('v3_b','results.json'),('v3_c','reports/v3_c_results.json')]:
            result=json.loads(Path(file).read_text())
            self.assertEqual(canonical['results'][seed]['factory_month'],result['factory_month'])
            self.assertEqual(canonical['results'][seed]['factory'],result['factory'])
            prevalence=canonical['results'][seed]['prevalence_sorted']
            self.assertEqual(prevalence,sorted(prevalence,key=lambda x:x['assumed_prevalence']))
        for source in canonical['sources'].values():
            self.assertEqual(source['sha256'],hashlib.sha256(Path(source['file']).read_bytes()).hexdigest())
        for slug in ['', 'problem','how-it-works','cases','results','system','data','limits']:
            page=(Path('website')/slug/'index.html').read_text()
            self.assertIn('metrics.js',page)
            self.assertNotIn('src="data.js"',page)
            self.assertIn('og:image',page)
            self.assertIn('meta name="description"',page)
