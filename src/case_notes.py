"""Evidence-grounded case note helpers, with a numeric consistency check."""

import json
import os
import re
from decimal import Decimal, InvalidOperation


NUMBER = re.compile(r"(?<![A-Za-z0-9])[-+]?(?:\d{1,3}(?:,\d{3})+|\d+)(?:\.\d+)?")


def build_case_note(factory_id, evidence_rows):
    """Build a concise note strictly from SQL evidence values."""
    parts = []
    for row in evidence_rows:
        parts.append("%s: expected %s, observed %s, gap %s (%s)" % (
            row["check_family"], row["expected"], row["observed"], row["gap"], row["evidence"]))
    note = "Factory %s requires review. " % factory_id + ". ".join(parts) + "."
    return note


def numbers_match_evidence(note, evidence_rows):
    """Return whether each number in a note occurs in the supplied evidence."""
    evidence_numbers = set()
    for row in evidence_rows:
        for field in ("month", "expected", "observed", "gap", "evidence"):
            for token in NUMBER.findall(str(row.get(field, ""))):
                try:
                    evidence_numbers.add(Decimal(token.replace(",", "")).normalize())
                except InvalidOperation:
                    continue
    for token in NUMBER.findall(note):
        try:
            if Decimal(token.replace(",", "")).normalize() not in evidence_numbers:
                return False
        except InvalidOperation:
            return False
    return True


def generate_llm_note(evidence_rows):
    """Ask the Responses API to write a note from SQL evidence rows only."""
    from openai import OpenAI

    client = OpenAI()
    response = client.responses.create(
        model=os.environ.get("OPENAI_MODEL", "gpt-6-astra"),
        store=False,
        instructions=("Write a concise case note using only the supplied SQL evidence rows. "
                      "Describe observed discrepancies neutrally and recommend human review. "
                      "Do not decide whether fraud occurred. Do not introduce facts or numbers."),
        input=json.dumps(evidence_rows, default=str),
    )
    return response.output_text
