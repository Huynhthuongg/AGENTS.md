#!/usr/bin/env sh
set -eu
STAMP="$(date +%Y%m%d-%H%M%S)"
DEST="backup-$STAMP.tar.gz"
tar --exclude='.git' --exclude='.venv' --exclude='backup-*.tar.gz' -czf "$DEST" .
echo "Created $DEST"
