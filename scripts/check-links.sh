#!/usr/bin/env bash

set -euo pipefail

if command -v lychee >/dev/null 2>&1; then
    LYCHEE_BIN="$(command -v lychee)"
elif [ -x /snap/bin/lychee ]; then
    LYCHEE_BIN=/snap/bin/lychee
else
    echo "lychee is required for the link-check hook but was not found in PATH or at /snap/bin/lychee." >&2
    echo "Install it with 'snap install lychee' and ensure /snap/bin is available in your PATH." >&2
    exit 1
fi

exec "$LYCHEE_BIN" --no-progress --verbose --max-concurrency 8 ./**/*.md
