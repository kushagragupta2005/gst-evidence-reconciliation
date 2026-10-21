#!/bin/sh
set -eu
make test
exec make dashboard
