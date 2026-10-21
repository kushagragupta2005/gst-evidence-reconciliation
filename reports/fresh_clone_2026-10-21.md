# Fresh-clone reproduction log — 21 October 2026

Command sequence, from a newly cloned local checkout at `/private/tmp/gst-fresh-clone-20261021`:

1. `git clone --no-local . /private/tmp/gst-fresh-clone-20261021` — **passed**.
2. `sh scripts/bootstrap.sh` — **blocked** while creating the new virtual environment: pip retried the pinned `altair` download from PyPI and hit an HTTPS read timeout.
3. `make provision-dashboard`, `make test`, and `make reproduce` — **not run**, because step 2 did not complete.

This is a dependency-network failure in the fresh environment, not a successful reproduction. The existing `reports/clean_setup.json` records the earlier fresh-source offline smoke separately. `submit-candidate-1` remains untagged until the full sequence completes.
