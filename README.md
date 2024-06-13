# Copier UV

[![ci](https://github.com/Obi-Wan/copier-conda/workflows/ci/badge.svg)](https://github.com/Obi-Wan/copier-conda/actions?query=workflow%3Aci)
[![documentation](https://img.shields.io/badge/docs-mkdocs%20material-blue.svg?style=flat)](https://Obi-Wan.github.io/copier-conda/)
[![gitter](https://badges.gitter.im/join%20chat.svg)](https://app.gitter.im/#/room/#copier-conda/community:gitter.im)

[Copier](https://github.com/copier-org/copier) template
for Python projects managed by [conda](https://docs.anaconda.com/free/miniconda/).

This copier template is based on:

- [copier-uv](https://github.com/pawamoy/copier-uv)

## Features

- [conda](https://docs.anaconda.com/free/miniconda/) setup, with pre-defined `pyproject.toml`
- Pre-configured tools for code formatting, quality analysis and testing:
  [ruff](https://github.com/charliermarsh/ruff),
  [mypy](https://github.com/python/mypy),
- Tests run with [pytest](https://github.com/pytest-dev/pytest) and plugins, with [coverage](https://github.com/nedbat/coveragepy) support
- Documentation built with [MkDocs](https://github.com/mkdocs/mkdocs)
  ([Material theme](https://github.com/squidfunk/mkdocs-material)
  and "autodoc" [mkdocstrings plugin](https://github.com/mkdocstrings/mkdocstrings))
- Cross-platform tasks with [duty](https://github.com/pawamoy/duty)
- Support for GitHub workflows
- Auto-generated `CHANGELOG.md` from Git (conventional) commits
- All licenses from [choosealicense.com](https://choosealicense.com/appendix/)

## Quick setup and usage

Make sure all the
[requirements](https://Obi-Wan.github.io/copier-conda/requirements)
are met, then:

```bash
copier copy --trust "https://github.com/Obi-Wan/copier-conda.git" /path/to/your/new/project
```

Or even shorter:

```bash
copier copy --trust "gh:Obi-Wan/copier-conda" /path/to/your/new/project
```

See the [documentation](https://Obi-Wan.github.io/copier-conda) for more details.
