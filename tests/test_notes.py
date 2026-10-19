import unittest
from src.case_notes import build_case_note,validate_note

class NotesTest(unittest.TestCase):
    def setUp(self):
        self.rows=[{'factory_id':'F000006','month':'2026-04','check_family':'dispatch_invoice','expected':'120.25','observed':'100.00','gap':'20.25'}]
        self.note=build_case_note('F000006',self.rows)
    def test_valid_note(self):self.assertTrue(validate_note(self.note,self.rows))
    def test_tampered_note(self):self.assertFalse(validate_note(self.note+' Amount 987654321.123.',self.rows))
    def test_swapped_fields(self):self.assertFalse(validate_note(self.note.replace('expected 120.25, observed 100.00','expected 100.00, observed 120.25'),self.rows))
    def test_written_numbers(self):self.assertFalse(validate_note(self.note+' Five invoices missing.',self.rows))
    def test_unsupported_percentage(self):self.assertFalse(validate_note(self.note+' 20.25% hidden.',self.rows))
