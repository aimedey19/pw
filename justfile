_default:
    @just --list --unsorted

@serve:
    uv run coltrane play

# Build static site
@build:
    coltrane record --output docs --force --threads 2

# Compile tailwind in watch mode
@tailwind:
    tailwindcss -i static/css/input.css -o static/css/output.css --watch
