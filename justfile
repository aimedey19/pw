set dotenv-load := true

_default:
    @just --list --unsorted

@bootstrap:
    uv sync

@serve:
    uv run coltrane play

# Build static site
@build:
    #!/usr/bin/env bash
    export DEBUG=False
    export ALLOWED_HOSTS=oluwatobi.dev
    export COLTRANE_DESCRIPTION="Tobi DEGNON online portfolio and web developer blog, write on mostly django."
    export COLTRANE_SITE_URL="https://oluwatobi.dev"
    export COLTRANE_TITLE="Tobi Personal Website"
    coltrane record --output ../docs --force --threads 2

# Compile tailwind in watch mode
@tailwind:
    tailwindcss -i static/css/input.css -o static/css/output.css --watch


@pw *ARGS:
    uv run python site/app.py {{ ARGS }}
