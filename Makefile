# NOTE: These run natively only on Linux systems.
# To run on windows, you will need to install WSL, or a similar package for GNU commands
# To run any of these commands, go to the command line and type `make <command>`
# Example: `make check`, `make format`

check:
	isort --diff --check .			# isort configuration in `setup.cfg`
	black --diff --check --color .	# black configuration in `pyproject.toml`
	flake8 .						# flake8 configuration in `setup.cfg`
	mypy .							# mypy configuration in `setup.cfg`
	bandit -r -c pyproject.toml .	# mypy configuration in `pyproject.toml`

format:
	isort .
	black .

start_dev:
	python manage.py runserver
