## GitHub Copilot Custom Instructions — Français / English

**Purpose**: Provide suggestions consistent with repository conventions, accelerate code
writing, and assist contributors on Python, MLOps, deployment, and observability.

**Repository Type**: This repository is dedicated to Copilot customization, instruction
quality, and prompt governance.

## Language Configuration

- **Interaction language**: English — all Copilot responses and comments directed at the
  user must be in English, unless the user explicitly switches to another language.
- **Development language**: Python — all source code, docstrings, and inline comments
  must be written in English (standard convention for code).

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

## Agent Behaviour

### General

- Treat this file as the authoritative style reference for agent behaviour.
- Prefer minimal, targeted changes over broad refactors.
- Each change must be independently testable or documented if a test is not applicable.

### Custom Rules (User Preferences)

- Never perform a `git commit`, `git push`, or any version control write operation on
  behalf of the user. Propose the command instead.
- Be direct and honest. Do not flatter or soften incorrect assumptions.
- Always ask clarifying questions before proceeding when a request is ambiguous,
  incomplete, or could be interpreted in multiple ways.
- When any file in the repository is created, moved, renamed, or deleted, update
  `README.md` to reflect the change before considering the task complete.
- When proposing solutions, reference industry best practices and state-of-the-art
  approaches; explain trade-offs and justify recommendations.

### Instruction and Prompt Files

- When creating a new `.instructions.md` file, use
  `.github/instructions/TEMPLATE.instructions.md` as the base.
- `applyTo` glob patterns must be specific enough to avoid unintended matches.
- Prompt files (`.prompt.md`) must include a `#file:` reference to
  `.github/copilot-instructions.md`.

### Expected Response Format

- **Be minimal**: default to 1-3 sentences. Expand only when the user explicitly asks
  (e.g., "explain", "elaborate", "detail", "give an example").
- Provide a concise and testable implementation, with PEP 257-compliant docstrings and
  type annotations.
- Add a small `pytest` test when the feature is non-trivial.
- For infrastructure changes, provide the complete manifest (`Dockerfile`, `helm` chart
  snippet) and a brief usage note.
- For commands and instructions, use code blocks with the correct language (bash,
  Dockerfile, yaml).
- Never include secrets or sensitive values in plain text.

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
