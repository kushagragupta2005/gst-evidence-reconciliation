"""Keep development-only evaluation output separate from the submission README."""
import json
from pathlib import Path


result = json.loads(Path('results.json').read_text())
status = result.get('result_status', 'UNLABELLED')
Path('reports/evaluation.md').write_text(
    '# Evaluation artefact status\n\n'
    f'`results.json` is labelled **{status}**. It is retained for audit and does not update the submission README. '
    'A post-change held-out report may be published only after its seed suite is preregistered.\n'
)
print(f'Wrote development evaluation status: {status}')
