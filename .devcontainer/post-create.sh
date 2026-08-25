#!/usr/bin/env bash
# Codespaces bootstrap for halal-scout-nyc.
# Mirrors .github/workflows/ci.yml: Python 3.12, uv, ruff 0.15.12.
set -euo pipefail

echo "==> Installing uv"
curl -LsSf https://astral.sh/uv/install.sh | sh
export PATH="$HOME/.local/bin:$PATH"
uv --version

echo "==> Creating virtualenv"
uv venv

echo "==> Installing project dependencies (this pulls torch; expect ~6 GB)"
uv pip install -r requirements.txt

echo "==> Installing test-only extras used by CI"
uv pip install pytest-cov pytest-timeout

echo "==> Installing pinned dev tools"
uv tool install ruff==0.15.12
uv tool install pre-commit

echo "==> Installing git hooks"
pre-commit install

if [ ! -f .env ]; then
  echo "==> Seeding .env from .env.example (fill in real keys, or use Codespaces secrets)"
  cp .env.example .env
fi

echo
echo "Ready. Useful targets:"
echo "  make test      # pytest"
echo "  make lint      # ruff check + format --check"
echo "  make api       # FastAPI on :8000"
echo "  make ui        # Streamlit on :8501"
