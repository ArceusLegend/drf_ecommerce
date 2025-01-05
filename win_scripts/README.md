# Windows scripts

This directory contains .bat scripts that perform the same functionality as those in the Makefile command.

The idea is to provide the same utilities for Windows, without the need to download extra software.

These have to be run from the root of this project directory, so they can access the entire project tree, as well as their config files.

## Available scripts

### - check.bat

Runs all the linters on the existing code. Also runs automatically on every push to the remote Github repo.

These linters are:
- Mypy, for type checking Python code
- Flake8, checks Python code against coding style (PEP 8), programming errors, and complex constructs
- isort, for sorting imports alphabetically, and separating them into sections and types
- Black, for maintaining code formatting that is compliant with PEP 8
- Bandit, for security checks

You can find the configurations for mypy (and its plugins), flake8, and isort in `setup.cfg`
The configurations for bandit and black can be found in `pyproject.toml`

NOTE: If you're planning to use Django's built-in template language for building a front-end out off of this project, you should also include a linter like `djlint` for your templates

### - format.bat

Automatically formats the code with black and isort, where needed.

isort configurations can be found in `setup.cfg`, while black configurations can be found in `pyproject.toml`.

NOTE: If you're planning to use Django's built-in template language for building a front-end out off of this project, you should also include a linter like `djlint` for your templates
