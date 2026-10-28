# Synthetic audit evidence

These compressed CSVs are the exact saved V3-B/V3-C feature rows and evaluator predictions used by the published metrics. Every record is synthetic. Prediction labels are for offline scoring only; they are never loaded into the restricted API.

`manifest.json` records compressed and uncompressed SHA-256 hashes, byte counts and row counts. Run `make restore-audit` to verify and restore the local CSV paths. Then `make audit` recomputes the published confidence intervals and ablation baseline from those inputs.

The full multi-million-row generated datasets are intentionally regenerated from code rather than copied into Git. No database image, credentials, local virtualenv or private environment file belongs in this folder.
