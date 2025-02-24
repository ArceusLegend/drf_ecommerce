isort --diff --check .
black --diff --check --color .
flake8 .
mypy .
bandit -r -c pyproject.toml .
