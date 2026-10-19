"""Evidence-only notes with numeric membership and field-binding validation."""
import json
import os
import re
from decimal import Decimal,InvalidOperation

NUMBER=re.compile(r'(?<![A-Za-z0-9])[-+]?(?:\d{1,3}(?:,\d{3})+|\d+)(?:\.\d+)?(?:[eE][-+]?\d+)?')
WORDS=re.compile(r'\b(zero|one|two|three|four|five|six|seven|eight|nine|ten|hundred|thousand|million|billion)\b',re.I)

def decimal(value):return Decimal(str(value).replace(',','')).normalize()

def numbers_match_evidence(note,evidence_rows):
    # Written-out numbers and percentages are withheld; evidence quantities have explicit units/fields.
    if WORDS.search(note) or '%' in note:return False
    source=json.dumps(evidence_rows,default=str)
    try:return all(decimal(token) in {decimal(t) for t in NUMBER.findall(source)} for token in NUMBER.findall(note))
    except InvalidOperation:return False

def sentence(row):
    return f"{row['check_family']}: expected {row['expected']}, observed {row['observed']}, gap {row['gap']}."

def build_case_note(factory_id,evidence_rows):
    return 'Evidence summary for factory '+factory_id+'. '+ ' '.join(sentence(row) for row in evidence_rows)+' Human review is required; these discrepancies do not establish fraud.'

def validate_note(note,rows):
    if not numbers_match_evidence(note,rows):return False
    # Every factual numeric claim is tied to a named row; prevents swapping existing expected/observed values.
    claims=re.findall(r'([a-z_]+): expected ([^,]+), observed ([^,]+), gap ([^.]+(?:\.\d+)?)[.]',note)
    if len(claims)!=len(rows):return False
    remaining=list(rows)
    for name,expected,observed,gap in claims:
        try:
            matching=next((r for r in remaining if r['check_family']==name and all(decimal(r[k])==decimal(v) for k,v in [('expected',expected),('observed',observed),('gap',gap)])),None)
        except InvalidOperation:return False
        if matching is None:return False
        remaining.remove(matching)
    # Numeric prose outside the row-bound claims is not accepted.
    stripped=re.sub(r'[a-z_]+: expected [^,]+, observed [^,]+, gap [-+\d.eE]+[.]','',note)
    stripped=re.sub(r'F\d{6}','',stripped)
    return not NUMBER.search(stripped)

def generate_llm_note(rows):
    from openai import OpenAI
    base=build_case_note(str(rows[0]['factory_id']),rows)
    response=OpenAI().responses.create(model=os.getenv('OPENAI_MODEL','gpt-6-astra'),store=False,
        instructions='Write a short neutral case note using only evidence. Preserve each supplied expected/observed/gap sentence exactly. Outside these sentences use no numbers, written-out numerals, dates, percentages or additional facts. Do not decide guilt or flagging; request human review. Return only the note.',
        input=json.dumps({'evidence':rows,'required_numeric_sentences':[sentence(r) for r in rows]},default=str))
    note=response.output_text
    if not validate_note(note,rows):raise ValueError('LLM note rejected: numeric or field-binding validation failed.')
    return note
