# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [unreleased]

### Added

- python-dotenv 1.0.1 as a requirement

### Changed

- Database settings to load dynamically based on the system's envvars
- Debug mode to load from .env. It is now a toggle for dev/prod modes
- Network settings to load dynamically from envvars. Will be overriden if dev mode is toggled on

## [0.0.3] - 26/12/2024

### Added

- This changelog!

## [0.0.2] - 24/12/2024

### Added

- A CI/CD pipeline that checks that the committed code is linted. Will be expanded for tests later as well.

## [0.0.1] - 21/12/2024

### Added

- Initial repo commit
- .gitignore file with some common directories and files that should be excluded from version control
- Compartmentalized requirements files for python libs
- Settings files (`pyproject.toml`, `setup.cfg`) for linting tools
- A `.env.template` file that will later be expanded for easily setting up envvars

### Changed

- Every file that wasn't properly linted, using `black` and `isort`

### Removed

- The Django hardcoded secret key, replaced with an envvar

[unreleased]: https://github.com/ArceusLegend/drf_ecommerce/compare/0.0.3...HEAD
[0.0.3]: https://github.com/ArceusLegend/drf_ecommerce/compare/0.0.2...0.0.3
[0.0.2]: https://github.com/ArceusLegend/drf_ecommerce/compare/0.0.1...0.0.2
[0.0.1]: https://github.com/ArceusLegend/drf_ecommerce/releases/tag/0.0.1
