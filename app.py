"""Minimal evidence-first case list and factory timeline."""

import os
import ssl

import pyexasol
import streamlit as st

from src.case_notes import build_case_note, generate_llm_note, numbers_match_evidence


st.set_page_config(page_title="GST Evidence Reconciliation", layout="wide")
st.title("GST Evidence Reconciliation")
st.caption("A SQL-ranked review queue from independent evidence. Flags require at least two check families.")


@st.cache_resource
def connect():
    dsn = os.environ.get("EXASOL_DSN", "localhost:8563")
    options = {
        "dsn": dsn,
        "user": os.environ.get("EXASOL_USER", "sys"),
        "password": os.environ.get("EXASOL_PASSWORD", "exasol"),
        "compression": True,
    }
    # Only relax certificate checking for Exasol Personal's local self-signed
    # endpoint. Remote DSNs keep PyExasol's default certificate validation.
    if dsn.split(":", 1)[0].lower() in {"localhost", "127.0.0.1", "::1"}:
        options["websocket_sslopt"] = {"cert_reqs": ssl.CERT_NONE}
    return pyexasol.connect(**options)


try:
    conn = connect()
    cases = conn.export_to_list("""
        SELECT r.FACTORY_ID, f.NAME, r.PERIOD_MONTH, r.SIGNAL_COUNT, r.EVIDENCE_COUNT,
               r.TOTAL_ABSOLUTE_GAP, r.STATUS
        FROM GST_EVIDENCE.V_RANKED_CASES r
        JOIN GST_EVIDENCE.FACTORIES f ON f.FACTORY_ID=r.FACTORY_ID
        WHERE r.STATUS='prioritise'
        ORDER BY r.TOTAL_ABSOLUTE_GAP DESC, r.FACTORY_ID, r.PERIOD_MONTH
    """)
    review_cases = conn.export_to_list("""
        SELECT r.FACTORY_ID, f.NAME, r.PERIOD_MONTH, r.SIGNAL_COUNT, r.EVIDENCE_COUNT,
               r.TOTAL_ABSOLUTE_GAP, r.STATUS
        FROM GST_EVIDENCE.V_RANKED_CASES r
        JOIN GST_EVIDENCE.FACTORIES f ON f.FACTORY_ID=r.FACTORY_ID
        WHERE r.STATUS='review only'
        ORDER BY r.FACTORY_ID, r.PERIOD_MONTH LIMIT 50
    """)
    clear_cases = conn.export_to_list("""
        SELECT r.FACTORY_ID, f.NAME, r.PERIOD_MONTH, r.SIGNAL_COUNT, r.EVIDENCE_COUNT,
               r.TOTAL_ABSOLUTE_GAP, r.STATUS
        FROM GST_EVIDENCE.V_RANKED_CASES r
        JOIN GST_EVIDENCE.FACTORIES f ON f.FACTORY_ID=r.FACTORY_ID
        WHERE r.STATUS='clear'
        ORDER BY r.FACTORY_ID, r.PERIOD_MONTH LIMIT 100
    """)
except Exception as error:
    st.error("Could not connect to Exasol. Start Exasol Personal and load the demo data first.")
    st.exception(error)
    st.stop()

st.subheader("Prioritised factory-months")
case_dicts = [dict(zip(("factory_id", "name", "month", "signal_count", "evidence_count", "total_absolute_gap", "status"), row))
              for row in cases]
if case_dicts:
    st.dataframe(case_dicts, use_container_width=True, hide_index=True,
                 column_config={"total_absolute_gap": st.column_config.NumberColumn(format="%.2f")})
else:
    st.info("No factory-month has two independent discrepancy signals.")
all_cases = cases + review_cases + clear_cases
if not all_cases:
    st.stop()
labels = {"%s · %s · %s · %s" % (row[6].upper(), row[0], row[1], row[2]): row for row in all_cases}
selection = st.selectbox("Inspect a prioritised case, single-signal review, or cleared factory", list(labels))
case = labels[selection]
factory_id = case[0]
evidence = conn.export_to_list("""
    SELECT FACTORY_ID, PERIOD_MONTH, CHECK_FAMILY, EXPECTED, OBSERVED, GAP, EVIDENCE, DISCREPANCY_CLASS
    FROM GST_EVIDENCE.V_ALL_EVIDENCE
    WHERE FACTORY_ID='%s' AND PERIOD_MONTH='%s'
    ORDER BY PERIOD_MONTH, CHECK_FAMILY
""" % (factory_id, case[2]))
keys = ("factory_id", "month", "check_family", "expected", "observed", "gap", "evidence", "discrepancy_class")
evidence = [dict(zip(keys, row)) for row in evidence]

st.subheader("Evidence timeline · %s" % factory_id)
st.dataframe(evidence, use_container_width=True, hide_index=True)
if evidence:
    note = build_case_note(factory_id, evidence)
    if os.environ.get("OPENAI_API_KEY") and st.button("Write case note with the configured LLM"):
        with st.spinner("Writing from the displayed SQL evidence…"):
            note = generate_llm_note(evidence)
    if numbers_match_evidence(note, evidence):
        st.subheader("Evidence-based case note")
        st.write(note)
    else:
        st.error("Case note withheld because a number did not match the evidence rows.")
    st.caption("The note is advisory and does not change the SQL ranked queue.")
elif case[6] == "clear":
    st.success("No check view raised a discrepancy for this factory and period.")
