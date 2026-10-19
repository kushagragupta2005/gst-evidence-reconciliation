#!/usr/bin/env python3
"""Load generated CSV evidence into Exasol Personal, run checks, and score."""

import argparse
import os
import ssl
import time
from pathlib import Path

import pyexasol


TABLES = {
    "factories.csv": ("FACTORIES", "factory_id,name,address,phone,vehicle_plate,ground_truth,scenario"),
    "suppliers.csv": ("SUPPLIERS", "supplier_id,name,address,phone,linked_factory_id"),
    "factory_month.csv": ("FACTORY_MONTH", "factory_id,period_month,product,opening_stock,purchases_kg,purchases_finished,declared_output,declared_dispatch,closing_stock,power_kwh,operating_hours"),
    "invoices.csv": ("INVOICES", "invoice_id,factory_id,period_month,quantity,invoice_value"),
    "purchase_invoices.csv": ("PURCHASE_INVOICES", "purchase_invoice_id,buyer_factory_id,period_month,supplier_id,quantity,invoice_value"),
    "eway_bills.csv": ("EWAY_BILLS", "eway_id,factory_id,period_month,quantity,vehicle_plate"),
    "supplier_returns.csv": ("SUPPLIER_RETURNS", "supplier_id,period_month,declared_sales_kg"),
    "bank_entries.csv": ("BANK_ENTRIES", "transaction_id,factory_id,period_month,amount"),
    "machines.csv": ("MACHINES", "machine_id,factory_id,installed_month,rated_units_month"),
}


def execute_file(connection, path):
    sql = path.read_text(encoding="utf-8")
    for statement in sql.split(";"):
        if statement.strip():
            connection.execute(statement)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--data", default="data/generated")
    parser.add_argument("--dsn", default=os.environ.get("EXASOL_DSN", "localhost:8563"))
    parser.add_argument("--user", default=os.environ.get("EXASOL_USER", "sys"))
    parser.add_argument("--password", default=os.environ.get("EXASOL_PASSWORD", "exasol"))
    args = parser.parse_args()
    data = Path(args.data)

    connect_options = {
        "dsn": args.dsn,
        "user": args.user,
        "password": args.password,
        "compression": True,
        "autocommit": True,
    }
    # Exasol Personal's local endpoint uses a self-signed certificate. Keep
    # normal certificate validation enabled for any non-local DSN.
    if args.dsn.split(":", 1)[0].lower() in {"localhost", "127.0.0.1", "::1"}:
        connect_options["websocket_sslopt"] = {"cert_reqs": ssl.CERT_NONE}
    conn = pyexasol.connect(**connect_options)
    try:
        execute_file(conn, Path("sql/00_schema.sql"))
        for filename, (table, _) in TABLES.items():
            header = TABLES[filename][1].split(",")
            # Explicit column lists keep file and database order aligned.
            conn.execute("TRUNCATE TABLE GST_EVIDENCE.%s" % table)
            conn.import_from_file(str(data / filename), ("GST_EVIDENCE", table),
                                  import_params={"columns": [c.upper() for c in header], "skip": 1})
            count = conn.execute("SELECT COUNT(*) FROM GST_EVIDENCE.%s" % table).fetchone()[0]
            print("Loaded %-18s %s rows" % (table, count))
        execute_file(conn, Path("sql/20_entities.sql"))
        execute_file(conn, Path("sql/10_checks.sql"))

        for view in ("V_MATERIAL_OUTPUT", "V_DISPATCH_INVOICE", "V_STOCK_ROLLFORWARD",
                     "V_SUPPLIER_LOOP", "V_RANKED_CASES"):
            start = time.perf_counter()
            count_rows = conn.execute("SELECT COUNT(*) FROM GST_EVIDENCE.%s" % view).fetchone()[0]
            elapsed = time.perf_counter() - start
            print("Query time %-22s %.3f seconds (%s rows)" % (view, elapsed, count_rows))

        start = time.perf_counter()
        result = conn.execute("SELECT FACTORY_ID, STATUS FROM GST_EVIDENCE.V_RANKED_CASES WHERE STATUS='prioritise'").fetchall()
        elapsed = time.perf_counter() - start
        flagged = {row[0] for row in result}
        labels = conn.execute("SELECT FACTORY_ID, GROUND_TRUTH FROM GST_EVIDENCE.FACTORIES").fetchall()
        cheats = {fid for fid, label in labels if label == "cheat"}
        decoys = {fid for fid, label in labels if label == "decoy"}
        tp = len(cheats & flagged)
        fp_decoys = len(decoys & flagged)
        print("Cheat catch rate: %d/%d = %.1f%%" % (tp, len(cheats), 100.0 * tp / max(1, len(cheats))))
        print("Honest-decoy false-positive rate: %d/%d = %.1f%%" %
              (fp_decoys, len(decoys), 100.0 * fp_decoys / max(1, len(decoys))))
        print("Prioritised query time: %.3f seconds (%d factory-month cases)" % (elapsed, len(result)))
        decoy_example = conn.execute("""
            SELECT r.FACTORY_ID, r.PERIOD_MONTH
            FROM GST_EVIDENCE.V_RANKED_CASES r
            JOIN GST_EVIDENCE.FACTORIES f ON f.FACTORY_ID=r.FACTORY_ID
            WHERE r.STATUS='clear' AND f.GROUND_TRUTH='decoy'
            ORDER BY r.FACTORY_ID, r.PERIOD_MONTH LIMIT 1
        """).fetchone()
        print("Cleared honest-decoy demo example: %s %s" % (decoy_example or ("none", "")))
        # Sanity counts are deliberately separate from scoring labels.
        for table, _ in TABLES.values():
            print("Row count %-18s %s" % (table, conn.execute(
                "SELECT COUNT(*) FROM GST_EVIDENCE.%s" % table).fetchone()[0]))
        print("Row count %-18s %s" % ("ENTITY_KEYS", conn.execute(
            "SELECT COUNT(*) FROM GST_EVIDENCE.ENTITY_KEYS").fetchone()[0]))
        key_checks = {
            "orphan factory-month rows": "SELECT COUNT(*) FROM GST_EVIDENCE.FACTORY_MONTH m LEFT JOIN GST_EVIDENCE.FACTORIES f ON f.FACTORY_ID=m.FACTORY_ID WHERE f.FACTORY_ID IS NULL",
            "orphan invoice factories": "SELECT COUNT(*) FROM GST_EVIDENCE.INVOICES i LEFT JOIN GST_EVIDENCE.FACTORIES f ON f.FACTORY_ID=i.FACTORY_ID WHERE f.FACTORY_ID IS NULL",
            "orphan purchase invoice factories": "SELECT COUNT(*) FROM GST_EVIDENCE.PURCHASE_INVOICES i LEFT JOIN GST_EVIDENCE.FACTORIES f ON f.FACTORY_ID=i.BUYER_FACTORY_ID WHERE f.FACTORY_ID IS NULL",
            "orphan purchase invoice suppliers": "SELECT COUNT(*) FROM GST_EVIDENCE.PURCHASE_INVOICES i LEFT JOIN GST_EVIDENCE.SUPPLIERS s ON s.SUPPLIER_ID=i.SUPPLIER_ID WHERE s.SUPPLIER_ID IS NULL",
            "orphan e-way bill factories": "SELECT COUNT(*) FROM GST_EVIDENCE.EWAY_BILLS e LEFT JOIN GST_EVIDENCE.FACTORIES f ON f.FACTORY_ID=e.FACTORY_ID WHERE f.FACTORY_ID IS NULL",
            "orphan bank factories": "SELECT COUNT(*) FROM GST_EVIDENCE.BANK_ENTRIES b LEFT JOIN GST_EVIDENCE.FACTORIES f ON f.FACTORY_ID=b.FACTORY_ID WHERE f.FACTORY_ID IS NULL",
            "orphan supplier returns": "SELECT COUNT(*) FROM GST_EVIDENCE.SUPPLIER_RETURNS r LEFT JOIN GST_EVIDENCE.SUPPLIERS s ON s.SUPPLIER_ID=r.SUPPLIER_ID WHERE s.SUPPLIER_ID IS NULL",
            "orphan machines": "SELECT COUNT(*) FROM GST_EVIDENCE.MACHINES m LEFT JOIN GST_EVIDENCE.FACTORIES f ON f.FACTORY_ID=m.FACTORY_ID WHERE f.FACTORY_ID IS NULL",
            "duplicate factory-month keys": "SELECT COUNT(*) FROM (SELECT FACTORY_ID, PERIOD_MONTH FROM GST_EVIDENCE.FACTORY_MONTH GROUP BY FACTORY_ID, PERIOD_MONTH HAVING COUNT(*) > 1)",
        }
        for name, query in key_checks.items():
            print("Join sanity %-25s %s" % (name, conn.execute(query).fetchone()[0]))
    finally:
        conn.close()


if __name__ == "__main__":
    main()
