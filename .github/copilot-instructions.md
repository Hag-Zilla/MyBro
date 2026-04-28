## GitHub Copilot Custom Instructions — Français / English

**Purpose**: Provide suggestions consistent with repository conventions, accelerate code
writing, and assist contributors on Python, MLOps, deployment, and observability.

**Repository Type**: This repository is dedicated to Copilot customization, instruction
quality, and prompt governance.

## Instruction Priority

1. System and platform policies
2. User request in current chat
3. Global instructions in this file
4. Path-specific instructions in `.github/instructions/`
5. Prompt templates in `.github/prompts/`

## Conflict Resolution

- Prefer the more specific rule when two rules conflict.
- If specificity is equal, prefer the most recent update with explicit rationale.
- Prefer practical and flexible guidance unless strict behavior is clearly required.

## Repository Context

- Technical Stack: Python, Docker, FastAPI, Kubernetes, Prometheus, Grafana, Loki,
  pandas, NumPy, Jupyter, SQLAlchemy, Alembic, MLflow, DVC.
- Target Audience: data scientists, ML engineers, MLOps engineers, data engineers,
  backend developers.

For agent-specific behaviour rules (permissions, governance, workflow constraints), see [AGENTS.md](../AGENTS.md).

## General Preferences

- Code Style: Follow PEP 8, explicit names, short functions (<= 50 lines), type hints
  when possible. Use an automatic formatter to ensure compliance (prefer `black` +
  `isort`).
- Docstrings: All functions and classes must include a docstring compliant with
  PEP 257; document parameters, return values, and exceptions. Prefer Google or NumPy
  style.
- Testing: Prefer `pytest`; target minimum acceptable coverage (e.g., 80% for critical
  modules).
- Logging: Use the `logging` module with appropriate levels; do not use `print` in
  production.
- Security: Never generate or propose inserting secrets (API keys, passwords). Use
  environment variables and vault solutions.

## Recommended Tools

- Automatic Formatting: `black` (configurable via `pyproject.toml`).
- Import Sorting: `isort`.
- Linting: `ruff` or `flake8` to detect PEP8 violations and common errors.
- Git Hooks: use `pre-commit` to run `black`, `isort`, and `ruff/flake8` before each
  commit.

## Docker and Containerization

- Provide lightweight and reproducible Dockerfiles (multi-stage builds if needed).
- Expose only necessary ports; set `USER` non-root when possible.
- Include instructions to build and run locally.

## Kubernetes and Deployment

- Prefer minimal Helm manifests or kustomize templates.
- Always propose requests/limits for CPU and memory.
- Suggest probes (`readiness`, `liveness`) and deployment strategies (rolling updates).

## FastAPI

- Use Pydantic for input/output model validation.
- Document routes via OpenAPI (docstrings + types).
- Propose patterns for API testing (TestClient + fixtures).

## Observability (Prometheus / Grafana / Loki)

- Propose relevant application metrics (latency, errors, counters).
- Add basic instrumentation (Prometheus client) and Grafana dashboard examples.
- Suggest structured log format (JSON) compatible with Loki.

## Data Science and Analysis

- Structure EDA notebooks with sections: Imports, Configuration, Data Loading,
  Analysis, Conclusions.
- Set random seeds early; clear notebook outputs before committing.
- Prefer `seaborn` or `plotly.express` for visualizations; always label axes.
- Use SHAP for model-agnostic feature importance.

## MLOps Best Practices

- Separate training code from service code (inference).
- Provide CI examples for training and deployment (e.g., GitHub Actions).
- Suggest model validation (unit tests + prediction integration tests).
- Use MLflow or equivalent for experiment tracking; log params, metrics, artifacts.

## Data Engineering

- Design pipelines as idempotent, incremental operations.
- Parameterize all SQL queries; never use string interpolation for values.
- Use Alembic for all schema migrations; write reversible `upgrade`/`downgrade`.
- Log row counts at each pipeline boundary; route failures to dead-letter tables.

## Authentication and Security

- Use `OAuth2PasswordBearer` + `Depends(get_current_user)` for protected routes.
- Set JWT access token expiry <= 15 min; use refresh tokens for sessions.
- Load all secrets via `pydantic-settings`; mark as `SecretStr`; never log them.

## Restrictions and Prohibitions

- Do not generate: secrets, API keys, passwords, or instructions to bypass security.
- Avoid suggestions that hardcode non-reproducible local paths.

## Operational Usage

- This file must remain at the root `.github/copilot-instructions.md` to be recognized.
- To propose a modification: open a small and explicit PR, include tests and validation
  instructions.

## Exclusions and Best Practices

- Do not directly modify CI/CD workflows or secrets; propose PRs and validation
  instructions.
- Avoid non-reproducible local paths and undeclared dependencies.
- Prefer atomic and tested changes; each PR must include tests or a justification.

## PR / Commit Conventions

- Prefer small and targeted PRs with a clear title and description of changes.
- Concise commit messages: `feat:`, `fix:`, `chore:` followed by a brief description.

## Branch Strategy

- **`main`**: production branch — full CI/CD pipelines (lint, test, security scan, build,
  deploy). Merges require passing all checks and at least one review.
- **`dev`**: development/integration branch — lighter pipelines (lint + fast tests only).
  Used for iterative work and validation before promoting to `main`.
