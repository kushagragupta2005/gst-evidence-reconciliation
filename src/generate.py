"""Seeded 12-month synthetic ledger. Truth is exported separately from detectors."""
import argparse
import csv
import json
import random
from pathlib import Path

CHEATS = ('hidden_production', 'itc_inflation', 'eway_reuse')
DECOYS = ('machinery_upgrade', 'product_mix_shift', 'longer_hours', 'seasonal_stock_build', 'new_supplier_onboarding', 'lumpy_bank_flows')
INTENSITIES = (.05, .15, .30)
TABLES = {
 # Detection inputs deliberately contain no outcome or scenario labels. Labels
 # belong only in truth.csv, which the evaluator reads outside GST_EVIDENCE.
 'factories': 'factory_id,name,address,phone,vehicle_plate',
 'suppliers': 'supplier_id,name,address,phone,linked_factory_id,owner_factory_id',
 'factory_month': 'factory_id,period_month,product,opening_stock,purchases_kg,purchases_finished,declared_output,declared_dispatch,closing_stock,power_kwh,operating_hours,raw_stock_change',
 'invoices': 'invoice_id,factory_id,period_month,quantity,invoice_value',
 'purchase_invoices': 'purchase_invoice_id,buyer_factory_id,period_month,supplier_id,quantity,invoice_value',
 'eway_bills': 'eway_id,factory_id,period_month,quantity,vehicle_plate',
 'supplier_returns': 'supplier_id,period_month,declared_sales_kg',
 'bank_entries': 'transaction_id,factory_id,period_month,amount,direction',
 'machines': 'machine_id,factory_id,installed_month,rated_units_month',
 'truth': 'factory_id,period_month,is_cheat,scenario,intensity,evasive,discrepancy_class,explanation,taxpayer_explanation',
}
SCALES = {'small': 600, 'medium': 2400, 'large': 220000}


def generate(scale, out_dir, seed, count=None, noise_multiplier=1.0,
             missing_documents_rate=0.0, fake_explanations=False):
    rng = random.Random(seed)
    count = count or SCALES[scale]
    out_dir = Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    handles = {n: (out_dir / (n + '.csv')).open('w', newline='') for n in TABLES}
    writers = {n: csv.writer(h, lineterminator='\n') for n, h in handles.items()}
    counts = dict.fromkeys(TABLES, 0)
    for n, fields in TABLES.items():
        writers[n].writerow(fields.split(','))
    def emit(n, *values):
        writers[n].writerow([round(v, 4) if isinstance(v, float) else v for v in values])
        counts[n] += 1
    scenarios = [CHEATS[i % 3] if i % 10 < 3 else DECOYS[i % 6] if i % 10 < 7 else 'honest' for i in range(count)]
    rng.shuffle(scenarios)
    # Real three-party cycles, represented by purchase edges; never used as truth by SQL.
    loop_ids = [i + 1 for i, s in enumerate(scenarios) if s == 'itc_inflation']
    links = {}
    for j in range(0, len(loop_ids) - 2, 3):
        a, b, c = loop_ids[j:j+3]
        links.update({a:b, b:c, c:a})
    for i, scenario in enumerate(scenarios, 1):
        fid, sid = f'F{i:06}', f'S{i:06}'
        truth = 'cheat' if scenario in CHEATS else 'decoy' if scenario in DECOYS else 'honest'
        intensity = rng.choice(INTENSITIES) if truth == 'cheat' else 0
        evasive = int(truth == 'cheat' and rng.random() < .25)
        active = set(rng.sample(range(3, 12), rng.randint(3, 8))) if truth == 'cheat' else set()
        address, phone, plate = f'{i} Industrial Estate Sector {i%12}', f'+91-98{i:08}', f'KA{i%99:02}AB{i%10000:04}'
        emit('factories', fid, f'Synthetic Works {i:06}', address, phone, plate)
        emit('suppliers', sid, f'Synthetic Supplier {i:06}', f'{i+count} Trade Estate', phone, f'F{links[i]:06}' if i in links else '', fid)
        emit('machines', f'M{i:06}', fid, '2025-01', 1800)
        if scenario == 'machinery_upgrade':
            emit('machines', f'M{i:06}B', fid, '2026-04', 2200)
        opening, size = 1500., rng.uniform(700, 1700)
        for m in range(12):
            month = f'2026-{m+1:02}'
            live = m in active
            output = size * rng.uniform(.82, 1.18)
            purchases = output / .8
            dispatch = output * rng.uniform(.78, .97)
            declared = output * (1-intensity if live and scenario == 'hidden_production' else 1)
            declared_dispatch = dispatch * (1-intensity if live and scenario == 'eway_reuse' else 1)
            invoice = dispatch * (1-intensity if live and scenario in ('hidden_production', 'eway_reuse') and not evasive else 1)
            if live and scenario == 'hidden_production' and evasive:
                invoice = dispatch
            purchase_claim = purchases / (1-intensity) if live and scenario == 'itc_inflation' else purchases
            power, hours, raw_change = output * 4, 160, 0
            incoming, outgoing = dispatch * 120, purchases * 90
            if live and evasive and scenario == 'itc_inflation':
                outgoing = purchase_claim * 90
            if live and evasive and scenario == 'eway_reuse':
                incoming = invoice * 120
            # Ordinary measurement/timing noise independent of labels, plus occasional large errors.
            def measure(v):
                return max(0, v * (1+rng.gauss(0,.015*noise_multiplier)+
                                   (rng.uniform(-.18,.18)*noise_multiplier if rng.random()<.025 else 0)))
            purchases, power, incoming, outgoing = map(measure, (purchases, power, incoming, outgoing))
            # Stock is an independent physical record. V2 deliberately breaks
            # its identity for each active fraud type without using labels in
            # detector SQL: concealed output remains in stock, ITC cases report
            # a falsified closing balance, and re-used e-way cases physically
            # dispatch more than the declared dispatch.
            closing = opening + declared - declared_dispatch
            if live and scenario == 'hidden_production':
                closing = opening + output - dispatch
            elif live and scenario == 'itc_inflation':
                closing -= purchases * intensity
            elif live and scenario == 'eway_reuse':
                closing = opening + declared - dispatch
            expected_class = 'clean'
            explanation = 'ordinary measurement and booking noise'
            if live:
                expected_class = {'hidden_production':'contradicting evidence','itc_inflation':'supplier issue','eway_reuse':'mismatch'}[scenario]
                explanation = 'only one independent source family exposed' if evasive else 'concealment may remain below the calibrated threshold'
                # Missing invoice documentation is a separate ground-truth discrepancy.
                if scenario == 'eway_reuse' and not evasive and rng.random() < .1:
                    invoice = 0
                    expected_class = 'missing documents'
            elif truth == 'decoy' and m >= 3:
                expected_class = 'needs human review'
                explanation = scenario.replace('_', ' ') + ': legitimate timing or operating change; not proof of wrongdoing'
                if scenario in ('machinery_upgrade','longer_hours'):
                    power *= 1.35
                    hours = 220 if scenario == 'longer_hours' else 160
                elif scenario == 'product_mix_shift':
                    purchases *= 1.3
                elif scenario == 'seasonal_stock_build':
                    raw_change = purchases * .35
                    purchases += raw_change
                elif scenario == 'lumpy_bank_flows':
                    incoming *= 1.45 if m%2 else .55
            product = 'sheet' if scenario == 'product_mix_shift' and m>=3 else 'steel_rod'
            emit('factory_month', fid, month, product, opening, purchases, 0, declared, declared_dispatch, closing, power, hours, raw_change)
            # Robustness variants remove one ordinary document at a declared rate.  The
            # truth label remains independent from whether the document is available.
            missing_document = rng.random() < missing_documents_rate
            if invoice and missing_document is not True:
                emit('invoices', f'I{i:06}-{m:02}', fid, month, invoice, invoice*120)
            emit('purchase_invoices', f'P{i:06}-{m:02}', fid, month, sid, purchase_claim, purchase_claim*90)
            # Two independent shipment records, same document ID only for planted reuse.
            for shipment in range(2):
                doc = 0 if live and scenario == 'eway_reuse' else shipment
                emit('eway_bills', f'E{i:06}-{m:02}-{doc}', fid, month, dispatch/2, plate)
            if not (scenario == 'new_supplier_onboarding' and m>=3) and not missing_document:
                emit('supplier_returns', sid, month, measure(output/.8))
            else:
                expected_class = 'missing documents'
            emit('bank_entries', f'B{i:06}-{m:02}I', fid, month, incoming, 'in')
            emit('bank_entries', f'B{i:06}-{m:02}O', fid, month, outgoing, 'out')
            taxpayer_explanation = ''
            if truth == 'decoy' and m >= 3:
                taxpayer_explanation = 'documented ' + scenario.replace('_', ' ')
            elif live and fake_explanations:
                taxpayer_explanation = rng.choice((
                    'documented machinery change', 'documented product mix shift',
                    'documented longer operating hours', 'documented seasonal stock build'))
            emit('truth', fid, month, int(live), scenario, intensity, evasive,
                 expected_class, explanation, taxpayer_explanation)
            opening = closing
    for h in handles.values():
        h.close()
    manifest = {'seed':seed, 'factories':count, 'months':12, 'rows':counts,
                'raw_evidence_rows':sum(v for k,v in counts.items() if k not in ('truth','factories','suppliers','machines')),
                'noise_multiplier':noise_multiplier,
                'missing_documents_rate':missing_documents_rate,
                'fake_explanations':fake_explanations}
    (out_dir/'manifest.json').write_text(json.dumps(manifest, indent=2)+'\n')
    print(json.dumps(manifest))
    return manifest

if __name__ == '__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--scale', choices=SCALES, default='small')
    p.add_argument('--out', default='data/generated')
    p.add_argument('--seed', type=int, default=20261020)
    p.add_argument('--factories', type=int)
    p.add_argument('--noise-multiplier', type=float, default=1.0)
    p.add_argument('--missing-documents-rate', type=float, default=0.0)
    p.add_argument('--fake-explanations', action='store_true')
    a=p.parse_args()
    generate(a.scale, a.out, a.seed, a.factories, a.noise_multiplier,
             a.missing_documents_rate, a.fake_explanations)
