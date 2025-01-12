set dotenv-load := true

export SECRET_KEY := "django-insecure-+-+8z1sdaddasdsadsadasd"
export ALLOWED_HOSTS := "oluwatobi.dev,localhost"
export COLTRANE_DESCRIPTION := "Tobi DEGNON online portfolio and web developer blog, write on mostly django."
export COLTRANE_SITE_URL := "https://oluwatobi.dev"
export COLTRANE_TITLE := "Tobi Personal Website"

_default:
    @just --list --unsorted

@bootstrap:
    uv sync

@serve:
    uvx honcho start

@play:
    uv run coltrane play

# Compile tailwind in watch mode
@tailwind:
    uv run tailwindcss -i site/static/css/input.css -o site/static/css/output.css --watch

# Build static site
build:
    #!/usr/bin/env bash
    export DEBUG=False
    uv run coltrane record --output ../static_site --force --threads 2

@pw *ARGS:
    uv run python site/app.py {{ ARGS }}

@fmt:
    just --fmt --unstable
    uvx ruff format
