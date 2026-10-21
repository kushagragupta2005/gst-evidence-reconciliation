#!/bin/sh
set -eu

.venv/bin/pip-licenses --format=markdown --with-urls --with-description > THIRD_PARTY.md
