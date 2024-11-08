# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

```markdown
## [Unreleased] - YYYY-MM-DD
### Added
### Changed
### Deprecated
### Fixed
### Security
```

## [Unreleased] - YYYY-MM-DD
### Added
- Created CLI sub-commands for run and list.
- The Nox virtual environment directory can now be set using the environment variable
  `NOX_ENVDIR`.
- Added py.typed marker file for mypy.
### Changed
- Renamed project to `labtest`.
### Deprecated
### Fixed
- The nox session `cli` no longer runs by default and generates an error due to lack
  of command line arguments.
- The nox session `clean` no longer requires the creation of a virtual environment.
- Changed the GitHub workflow badge from the `python-sample` repo to the correct
  `python-labtest` repo.
### Security
