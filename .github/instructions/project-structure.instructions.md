---
applyTo: "**"
---

## Purpose

Enforce a consistent project layout across all repositories so Copilot generates files,
imports, and references that match the expected directory structure.

## Expected Directory Layout

```text
project-root/
├── src/<package>/              # Main source package (snake_case name)
│   ├── __init__.py
│   ├── api/                    # FastAPI routers and schemas
│   ├── core/                   # Business logic, domain models
│   ├── db/                     # Database models, migrations (Alembic)
│   ├── ml/
│   │   ├── training/           # Training scripts and pipelines
│   │   └── inference/          # Serving, prediction endpoints
│   └── utils/                  # Shared helpers
├── tests/
│   ├── unit/                   # Pure unit tests (no I/O)
│   └── integration/            # Tests requiring external services
├── notebooks/                  # EDA and experimentation only
├── docs/                       # Additional documentation
├── scripts/                    # Utility and bootstrap scripts
├── assets/                     # Static files (images, logos)
├── .github/
│   ├── copilot-instructions.md
│   ├── instructions/           # Domain-specific instruction files
│   ├── prompts/                # Reusable prompt templates
│   └── workflows/              # GitHub Actions CI/CD
│       ├── docs-quality.yml    # Full pipeline (main branch)
│       └── dev-quality.yml     # Lightweight pipeline (dev branch)
├── README.md
├── CONTRIBUTING.md
├── pyproject.toml
├── .pre-commit-config.yaml
└── .gitignore
```

## Guidelines

- All source code lives under `src/<package>/`; never place modules at the repo root.
- Test files mirror the `src/` structure: `tests/unit/test_<module>.py`.
- `notebooks/` is for exploration only; no production logic belongs there.
- `scripts/` contains executable utilities; each script must be self-contained.
- Use snake_case for all Python file and directory names.
- Each Python package directory must contain an `__init__.py`.
- New top-level directories require a justification comment in `README.md`.

## Examples

```text
# Correct: module inside src/<package>/
src/myapp/core/preprocessing.py

# Correct: matching test
tests/unit/test_preprocessing.py

# Wrong: module at repo root
myapp_utils.py
```
