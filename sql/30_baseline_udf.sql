CREATE OR REPLACE PYTHON3 SET SCRIPT GST_EVIDENCE.ROBUST_POWER_BASELINE(factory_id VARCHAR(20), period_month VARCHAR(7), kwh_per_unit DOUBLE)
EMITS (factory_id VARCHAR(20), period_month VARCHAR(7), baseline DOUBLE, robust_z DOUBLE) AS
import statistics

def run(ctx):
    rows = []
    while True:
        rows.append((ctx.factory_id, ctx.period_month, ctx.kwh_per_unit))
        if not ctx.next():
            break
    rows.sort(key=lambda row: row[1])
    history = []
    for fid, month, value in rows:
        if value is None:
            continue
        if len(history) >= 3:
            median = statistics.median(history)
            mad = statistics.median(abs(x - median) for x in history)
            z = (value-median) / max(1.4826*mad, 0.05)
            ctx.emit(fid, month, median, z)
        history.append(value)
/
