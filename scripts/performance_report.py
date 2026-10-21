"""Render a development-only workload note without changing the README."""
from pathlib import Path


Path('reports/performance.md').write_text(
    '# Historical workload report — DEV\n\n'
    'This local synthetic workload predates the current detector changes. It is **DEV** evidence only and is not a current-detector benchmark or an engine-superiority claim. '
    'Machine-readable observations remain in the benchmark and profile JSON artefacts.\n'
)
print('Wrote development-only workload note.')
