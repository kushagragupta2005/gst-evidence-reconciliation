import gzip
import hashlib
import json
import sqlite3
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
from src.api import FrozenProtocolMismatch, verify_frozen_protocol
from scripts import restore_audit_evidence

class AuditIntegrityTests(unittest.TestCase):
    def test_live_protocol_mismatch_is_rejected(self):
        with patch('src.api.query',return_value=[{'mismatched_months':1}]):
            with self.assertRaises(FrozenProtocolMismatch):verify_frozen_protocol()
        with patch('src.api.query',return_value=[{'mismatched_months':0}]):
            self.assertTrue(verify_frozen_protocol()['view_decisions_match_frozen_protocol'])

    def test_schema_default_matches_published_threshold(self):
        connection=sqlite3.connect(':memory:')
        connection.execute("ATTACH DATABASE ':memory:' AS GST_EVIDENCE")
        schema=Path('sql/00_schema.sql').read_text().replace('CREATE SCHEMA IF NOT EXISTS GST_EVIDENCE;','').replace('CREATE OR REPLACE','CREATE')
        connection.executescript(schema)
        self.assertEqual(connection.execute('SELECT THRESHOLD FROM GST_EVIDENCE.SETTINGS').fetchone()[0],json.loads(Path('results.json').read_text())['protocol']['threshold'])
        connection.close()

    def test_corrupted_audit_archive_is_rejected_before_restore(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);p=root/'data/audit/v3_b/features.csv.gz';p.parent.mkdir(parents=True)
            raw=b'A,B\n1,2\n';packed=gzip.compress(raw,mtime=0);p.write_bytes(packed+b'corruption')
            manifest={'files':[{'source':'data/v3_b/features.csv','archive':'data/audit/v3_b/features.csv.gz','sha256':hashlib.sha256(raw).hexdigest(),'archive_sha256':hashlib.sha256(packed).hexdigest()}]}
            (root/'data/audit/manifest.json').write_text(json.dumps(manifest))
            with patch.object(restore_audit_evidence,'ROOT',root):
                with self.assertRaisesRegex(ValueError,'Archive hash mismatch'):restore_audit_evidence.restore()
            self.assertFalse((root/'data/v3_b/features.csv').exists())
