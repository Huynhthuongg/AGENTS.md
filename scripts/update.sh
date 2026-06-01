#!/usr/bin/env sh
set -eu
git pull --ff-only
if [ -d .venv ]; then
  . .venv/bin/activate
  python -m pip install -e '.[dev]'
fi
