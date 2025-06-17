These instructions apply to all files in this repository.

## Setup
- Python 3.12 is required.
- Use Poetry ≥1.8 for dependency management.
- Install dependencies with: `make install           # or: poetry install --no-root --sync --quiet`
* Optionally start a shell using poetry shell.

## Testing
* Validate the project with poetry check.
* Run the full test suite using: `pytest -q`

## Directory layout
```
.
├─ mds3loader/       *# source package (CLI, loader code, utilities)*
│  ├─ cli.py
│  ├─ config.py
│  ├─ loader/
│  ├─ metadata/
│  └─ utils/
├─ tests/            *# PyTest tests*
├─ docs/             *# project documentation*
├─ .github/workflows/ci.yml  *# CI job*
├─ Makefile
├─ pyproject.toml
├─ poetry.lock
└─ README.md
```
## Style
* Use standard Black formatting (4‑space indentation).
* Keep functions small and focused.
* Write docstrings for all public functions and classes.
* Use the [Google Python styleguide](https://google.github.io/styleguide/pyguide.html)

## Commit messages
* First line ≤50 characters in imperative mood.
* Separate body with a blank line; wrap lines at 72 characters.
* Explain why a change is made if it isn’t obvious.

## Pull requests
* Include a concise summary of the change and any testing performed.
