"""Seed-A-only threshold trade-off table and figure for the V2 detector."""
import json
from pathlib import Path

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

from src.evaluate import GRID, clustered_metrics, prepare

truth, matrix, _ = prepare('data/v2_train')
frame = truth.reset_index()
rows = []
for threshold in GRID:
    item = frame.copy()
    item['signals'] = (matrix.to_numpy() > threshold).sum(axis=1)
    item['flagged'] = item.signals >= 2
    monthly = clustered_metrics(item)
    evasive = clustered_metrics(item[(item.is_cheat == 1) & (item.evasive == 1)])
    factory_queue = item.groupby('factory_id').agg(is_cheat=('is_cheat','max'), flagged=('flagged','sum')).reset_index()
    factory_queue['flagged'] = factory_queue.flagged >= 2
    rows.append({
        'threshold': threshold,
        'monthly': monthly,
        'evasive': evasive,
        'prioritised_factory_months': int(item.flagged.sum()),
        'factory_queue_size_k2': int(factory_queue.flagged.sum()),
    })
artifact = {
    'dataset': 'V2-A / seed 31001 / calibration only',
    'selection_rule': 'minimum factory-month balanced error; larger threshold on ties',
    'selected_threshold': 0.05,
    'rows': rows,
}
Path('reports/v2_threshold_tradeoff.json').write_text(json.dumps(artifact, indent=2, allow_nan=False) + '\n')

fig, axes = plt.subplots(1, 2, figsize=(10, 4))
x = [row['threshold'] * 100 for row in rows]
axes[0].plot(x, [row['monthly']['recall'] * 100 for row in rows], marker='o', label='Recall')
axes[0].plot(x, [row['evasive']['recall'] * 100 for row in rows], marker='o', label='Evasive recall')
axes[0].plot(x, [row['monthly']['fpr'] * 100 for row in rows], marker='o', label='FPR')
axes[0].axvline(5, color='#bd4b30', linestyle='--', label='Selected 5%')
axes[0].set(xlabel='Ratio threshold (%)', ylabel='Rate (%)', title='Calibration trade-off on V2-A')
axes[0].legend(); axes[0].grid(alpha=.2)
axes[1].plot(x, [row['prioritised_factory_months'] for row in rows], marker='o', label='Priority factory-months')
axes[1].plot(x, [row['factory_queue_size_k2'] for row in rows], marker='o', label='Factory queue, K=2')
axes[1].axvline(5, color='#bd4b30', linestyle='--')
axes[1].set(xlabel='Ratio threshold (%)', ylabel='Cases', title='Review workload on V2-A')
axes[1].legend(); axes[1].grid(alpha=.2)
fig.tight_layout(); fig.savefig('reports/v2_threshold_tradeoff.png', dpi=160); plt.close(fig)
