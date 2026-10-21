"""Attach precomputed robustness summaries without reselecting operating choices."""
import json
from pathlib import Path

base = json.loads(Path('results.json').read_text())
variants = {}
for label, path in {
    'noise_1_5x':'reports/robustness_noise_1_5x.json',
    'noise_2x':'reports/robustness_noise_2x.json',
    'missing_documents_10pct':'reports/robustness_missing_documents_10pct.json',
}.items():
    item = json.loads(Path(path).read_text())
    variants[label] = {
        'dataset':item['dataset'],
        'factory_month':item['factory_month'],
        'factory':item['factory'],
        'factory_queue':{'k':item['factory_queue']['k'], 'queue_size':item['factory_queue']['queue_size'],
                         'metrics':item['factory_queue']['seed_c']},
    }
base['robustness'] = {
    'protocol':'Each variant uses the frozen seed-A threshold and K. No robustness result changes calibration.',
    'variants':variants,
}
Path('results.json').write_text(json.dumps(base, indent=2)+'\n')
