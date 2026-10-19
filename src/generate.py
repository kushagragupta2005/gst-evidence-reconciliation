#!/usr/bin/env python3
"""Create deterministic synthetic GST evidence for the reconciliation demo."""

import argparse
import csv
import random
from pathlib import Path


PRODUCTS = ("steel_rod", "wire", "sheet")
CHEATS = ("hidden_output", "dispatch_without_invoice", "stock_gap", "supplier_loop")
DECOYS = ("machinery_change", "product_mix_shift", "longer_hours")
TABLES = {
    "factories.csv": ["factory_id", "name", "address", "phone", "vehicle_plate", "ground_truth", "scenario"],
    "suppliers.csv": ["supplier_id", "name", "address", "phone", "linked_factory_id"],
    "factory_month.csv": ["factory_id", "month", "product", "opening_stock", "purchases_kg", "purchases_finished", "declared_output", "declared_dispatch", "closing_stock", "power_kwh", "operating_hours"],
    "invoices.csv": ["invoice_id", "factory_id", "month", "quantity", "value"],
    "purchase_invoices.csv": ["purchase_invoice_id", "buyer_factory_id", "month", "supplier_id", "quantity", "value"],
    "eway_bills.csv": ["eway_id", "factory_id", "month", "quantity", "vehicle_plate"],
    "supplier_returns.csv": ["supplier_id", "month", "declared_sales_kg"],
    "bank_entries.csv": ["transaction_id", "factory_id", "month", "amount"],
    "machines.csv": ["machine_id", "factory_id", "installed_month", "rated_units_month"],
}


def generate(scale, out_dir, seed):
    rng = random.Random(seed)
    count = {"small": 60, "medium": 1000, "large": 120000}[scale]
    months = ("2026-01", "2026-02", "2026-03")
    out_dir.mkdir(parents=True, exist_ok=True)
    handles = {name: (out_dir / name).open("w", newline="", encoding="utf-8") for name in TABLES}
    writers = {name: csv.DictWriter(handles[name], fieldnames=header, lineterminator="\n")
               for name, header in TABLES.items()}
    for name, writer in writers.items():
        writer.writeheader()

    # Balanced synthetic labels make the demo metrics interpretable at small scale.
    cheat_n = max(1, count // 5)
    decoy_n = max(1, count // 5)
    supplier_loop_n = max(3, (cheat_n // len(CHEATS) // 3) * 3)
    cheat_counts = [cheat_n // len(CHEATS)] * len(CHEATS)
    cheat_counts[CHEATS.index("supplier_loop")] = supplier_loop_n
    remaining_cheats = cheat_n - sum(cheat_counts)
    for index in range(remaining_cheats):
        cheat_counts[index % (len(CHEATS) - 1)] += 1
    scenarios = [scenario for scenario, n in zip(CHEATS, cheat_counts) for _ in range(n)]
    scenarios += [DECOYS[i % len(DECOYS)] for i in range(decoy_n)]
    scenarios += ["honest"] * (count - len(scenarios))
    rng.shuffle(scenarios)
    loop_members = [index + 1 for index, value in enumerate(scenarios) if value == "supplier_loop"]
    loop_next = {}
    for start in range(0, len(loop_members), 3):
        group = loop_members[start:start + 3]
        for pos, member in enumerate(group):
            loop_next[member] = group[(pos + 1) % len(group)]

    for i, scenario in enumerate(scenarios, 1):
        fid = "F%06d" % i
        truth = "cheat" if scenario in CHEATS else ("decoy" if scenario in DECOYS else "honest")
        address = "%d Industrial Estate, Sector %d" % (100 + i, 1 + i % 12)
        phone = "+91-98%08d" % i
        plate = "KA%02dAB%04d" % (1 + i % 99, i % 10000)
        writers["factories.csv"].writerow(dict(factory_id=fid, name="Synthetic Works %06d" % i,
            address=address, phone=phone, vehicle_plate=plate, ground_truth=truth, scenario=scenario))

        linked_factory = "F%06d" % loop_next[i] if scenario == "supplier_loop" else ""
        supplier_id = "S%06d" % i
        writers["suppliers.csv"].writerow(dict(supplier_id=supplier_id, name="Synthetic Supplier %06d" % i,
            address=address, phone=phone, linked_factory_id=linked_factory))
        writers["machines.csv"].writerow(dict(machine_id="M%06d-1" % i, factory_id=fid,
            installed_month="2024-01", rated_units_month=1200))
        if scenario == "machinery_change":
            writers["machines.csv"].writerow(dict(machine_id="M%06d-2" % i, factory_id=fid,
                installed_month="2026-02", rated_units_month=500))

        opening = 1000.0
        for month_index, month in enumerate(months):
            product = PRODUCTS[(i + month_index) % len(PRODUCTS)]
            purchases_kg = 1000.0 + rng.randint(-50, 50)
            expected_output = int(purchases_kg * 0.8)
            declared_output = expected_output
            dispatch = int(expected_output * 0.72)
            invoice_qty = dispatch
            power = int(expected_output * 4)
            operating_hours = 160
            bank = int(invoice_qty * 120)
            closing = opening + purchases_kg * 0.8 - dispatch

            if scenario == "hidden_output":
                # Power and material consumption imply output above the declared return.
                declared_output = int(expected_output * 0.72)
                power = int(expected_output * 6)
                dispatch = int(expected_output * 0.82)
                invoice_qty = int(expected_output * 0.65)
                closing = opening + declared_output - dispatch
            elif scenario == "dispatch_without_invoice":
                # Pair the missing invoice with a material/output contradiction so
                # the two-signal rule can prioritize this planted case.
                declared_output = int(expected_output * 0.72)
                dispatch = int(expected_output * 0.93)
                invoice_qty = int(expected_output * 0.60)
                bank = int(invoice_qty * 120)
                power = int(expected_output * 6)
                closing = opening + purchases_kg * 0.8 - dispatch
            elif scenario == "stock_gap":
                # Keep a distinct material/output mismatch alongside the stock
                # roll-forward gap; power is supporting evidence in the same family.
                declared_output = int(expected_output * 0.72)
                closing -= 350
                power = int(expected_output * 6)
            elif scenario == "supplier_loop":
                # A circular related-party chain is synthetic and explicitly represented.
                invoice_qty = int(dispatch * 0.65)
            elif scenario == "machinery_change":
                power = int(expected_output * (5.0 if month_index == 1 else 4.0))
            elif scenario == "product_mix_shift":
                if month_index == 1:
                    product = "sheet"
            elif scenario == "longer_hours":
                power = int(expected_output * 5.0)
                operating_hours = 220

            writers["factory_month.csv"].writerow(dict(factory_id=fid, month=month, product=product,
                opening_stock=round(opening, 2), purchases_kg=round(purchases_kg, 2),
                purchases_finished=0, declared_output=declared_output, declared_dispatch=dispatch,
                closing_stock=round(closing, 2), power_kwh=power, operating_hours=operating_hours))
            inv_id = "%s-%s" % (fid, month.replace("-", ""))
            if scenario != "dispatch_without_invoice":
                writers["invoices.csv"].writerow(dict(invoice_id=inv_id, factory_id=fid, month=month,
                    quantity=invoice_qty, value=invoice_qty * 120))
            writers["purchase_invoices.csv"].writerow(dict(purchase_invoice_id="P" + inv_id,
                buyer_factory_id=fid, month=month, supplier_id=supplier_id,
                quantity=round(purchases_kg, 2), value=round(purchases_kg * 90, 2)))
            writers["eway_bills.csv"].writerow(dict(eway_id="E" + inv_id, factory_id=fid, month=month,
                quantity=dispatch, vehicle_plate=plate))
            supplier_sales = purchases_kg * (0.65 if scenario == "supplier_loop" else 1.0)
            writers["supplier_returns.csv"].writerow(dict(supplier_id=supplier_id, month=month,
                declared_sales_kg=round(supplier_sales, 2)))
            writers["bank_entries.csv"].writerow(dict(transaction_id="B" + inv_id, factory_id=fid,
                month=month, amount=bank))
            opening = closing

    for handle in handles.values():
        handle.close()
    print("Wrote %s factories and %s monthly evidence rows to %s (seed=%s)" %
          (count, count * len(months), out_dir, seed))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--scale", choices=("small", "medium", "large"), default="small")
    parser.add_argument("--out", default="data/generated")
    parser.add_argument("--seed", type=int, default=20261019)
    args = parser.parse_args()
    generate(args.scale, Path(args.out), args.seed)


if __name__ == "__main__":
    main()
