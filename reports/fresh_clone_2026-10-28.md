# Offline fresh-clone verification — 28 October 2026

PASS for source commit `91b53c51b0ff0344f8c51204f9b6a7c87323a4c3`.

Command: `PYTHON=<project-python> PIP_NO_INDEX=1 PIP_FIND_LINKS=<local-compatible-wheelhouse> sh scripts/verify_clean_setup.sh --offline`.

- Created a real local Git clone with independent objects; preserved the public origin URL for artifact links.
- Created a new isolated virtualenv and installed every pinned application dependency from cached compatible wheels.
- Ran all offline tests, restored and hash-verified the six A/B/C synthetic scoring CSVs, reproduced A-only threshold/K selection and held-out metrics, replayed B/C ablation, built canonical metrics and all pages, and compiled Python sources.
- Measured elapsed time: 22 seconds. No step failed in this run. PyPI downloads had timed out during preparation, so cached original pip wheel bodies were recovered and validated by pip against the pinned requirements for offline installation. No upstream checksum verification or fresh online package availability is claimed.
- Excluded: new Exasol installation, schema recreation, a second machine, current full-scale load, and user video/portal submission. Live source parity and guards were tested separately through the restricted account after the approved settings-only repair.

See reports/clean_setup.json for the actual run timestamp and exact scope. The later commits only publish reports, documentation, manifest and snapshot provenance; this record does not silently claim they were independently re-cloned. The existing submit-candidate-1 tag is not moved.
