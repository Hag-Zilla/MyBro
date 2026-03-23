## GitHub Copilot Custom Instructions — English

Purpose
: Provide suggestions consistent with repository conventions, accelerate code writing, and assist contributors on Python, MLOps, deployment, and observability.

Repository Type
: This repository is dedicated to Copilot customization, instruction quality, and prompt governance.

Instruction Priority
1. System and platform policies
2. User request in current chat
3. Global instructions in this file
4. Path-specific instructions in `.github/instructions/`
5. Prompt templates in `.github/prompts/`

Conflict Resolution
- Prefer the more specific rule when two rules conflict.
- If specificity is equal, prefer the most recent update with explicit rationale.
- Prefer practical and flexible guidance unless strict behavior is clearly required.

Repository Context
- Technical Stack: Python, Docker, FastAPI, Kubernetes, Prometheus, Grafana, Loki.
- Target Audience: data scientists, MLOps engineers, backend developers.

General Preferences
- Code Style: Follow PEP 8, explicit names, short functions (<= 50 lines), type hints when possible. Use an automatic formatter to ensure compliance (prefer `black` + `isort`).
- Docstrings: All functions and classes must include a docstring compliant with PEP 257; document parameters, return values, and exceptions. Prefer Google or NumPy style.
- Testing: Prefer `pytest`; target minimum acceptable coverage (e.g., 80% for critical modules).
- Logging: Use the `logging` module with appropriate levels; do not use `print` in production.
- Security: Never generate or propose inserting secrets (API keys, passwords). Use environment variables and vault solutions.

Recommended Tools
- Automatic Formatting: `black` (configurable via `pyproject.toml`).
- Import Sorting: `isort`.
- Linting: `ruff` or `flake8` to detect PEP8 violations and common errors.
- Git Hooks: use `pre-commit` to run `black`, `isort`, and `ruff/flake8` before each commit.

Example Commands (Local)
```bash
python -m pip install --user black isort ruff pre-commit
pre-commit install
black .
isort .
ruff check .
```

Docker and Containerization
- Provide lightweight and reproducible Dockerfiles (multi-stage builds if needed).
- Expose only necessary ports; set `USER` non-root when possible.
- Include instructions to build and run locally.

Kubernetes and Deployment
- Prefer minimal Helm manifests or kustomize templates.
- Always propose requests/limits for CPU and memory.
- Suggest probes (`readiness`, `liveness`) and deployment strategies (rolling updates).

FastAPI
- Use Pydantic for input/output model validation.
- Document routes via OpenAPI (docstrings + types).
- Propose patterns for API testing (TestClient + fixtures).

Observability (Prometheus / Grafana / Loki)
- Propose relevant application metrics (latency, errors, counters).
- Add basic instrumentation (Prometheus client) and Grafana dashboard examples.
- Suggest structured log format (JSON) compatible with Loki.

MLOps Best Practices
- Separate training code from service code (inference).
- Provide CI examples for training and deployment (e.g., GitHub Actions).
- Suggest model validation (unit tests + prediction integration tests).

Restrictions and Prohibitions
- Do not generate: secrets, API keys, passwords, or instructions to bypass security.
- Avoid suggestions that hardcode non-reproducible local paths.

Operational Usage
- This file must remain at the root `.github/copilot-instructions.md` to be recognized.
- To propose a modification: open a small and explicit PR, include tests and validation instructions.

---

### Path-Specific Instructions

Create `.github/instructions/NAME.instructions.md` files to add specific instructions for certain folders/modules.

Recommended section structure for path-specific files:
- Purpose
- Scope
- Guidelines
- Examples
- Validation Checklist

Example **`.github/instructions/ml-training.instructions.md`**:
```yaml
---
applyTo: "src/ml/training/**/*.py"
---

Training code: cross-validation mandatory, hyperparameters documented, drift tests.
Minimal validation split: 70/15/15 (train/val/test).
```

Example **`.github/instructions/fastapi.instructions.md`**:
```yaml
---
applyTo: "src/api/**/*.py"
---

FastAPI: Pydantic mandatory for input/output models.
Document each endpoint (docstring + types).
Add TestClient tests for response validation.
```

### Prompt Files (Reusable)

Create reusable prompt templates in `.github/prompts/` and use them via the paperclip icon in chat.

Prompt quality guidelines:
- State the objective in one clear sentence.
- Define constraints and exclusions explicitly.
- Specify expected output format.
- Keep examples realistic and concise.

First, enable in VS Code workspace settings:
```json
"chat.promptFiles": true
```

Example **`.github/prompts/code-review.prompt.md`**:
```markdown
Review this code for:
- PEP 8 compliance and style
- Type hints completeness
- Docstring coverage (all functions/classes)
- Security issues (no hardcoded secrets)
- Performance and test coverage

See standards: #file:.github/copilot-instructions.md
```

---

**How to Ask Copilot**

- Provide a clear objective: explain the goal and constraints (Python compatibility, dependencies, performance limits).
- Provide input/output examples if possible (data format, expected types).
- Indicate the desired level of detail: "code only", "code + brief explanation", or "code + tests".
- Specify the relevant files or modules, and whether the modification must be backward compatible.

**Expected Response Format**

- Provide a concise and testable implementation, with PEP 257-compliant docstrings and type annotations.
- Add a small `pytest` test when the feature is non-trivial.
- For infrastructure changes, provide the complete manifest (`Dockerfile`, `helm` chart snippet) and a brief usage note.
- For commands and instructions, use code blocks with the correct language (bash, Dockerfile, yaml).
- Never include secrets or sensitive values in plain text.

**Examples of Effective Prompts**

- "Write a function `normalize_df(df: pd.DataFrame) -> pd.DataFrame` that normalizes numeric columns. Include NumPy-style docstring and a minimal pytest test."
- "Generate a multistage `Dockerfile` for a FastAPI app (module `app:app`) with Uvicorn and expose port 8000."
- "Propose a FastAPI integration test using `TestClient` for the `/predict` endpoint."
- "Add Prometheus instrumentation to count HTTP requests and measure latency."
- "Provide a simple Helm manifest to deploy a FastAPI service with requests/limits and probes."

**Exclusions and Best Practices**

- Do not directly modify CI/CD workflows or secrets; propose PRs and validation instructions.
- Avoid non-reproducible local paths and undeclared dependencies.
- Prefer atomic and tested changes; each PR must include tests or a justification.

**PR / Commit Conventions**

- Prefer small and targeted PRs with a clear title and description of changes.
- Concise commit messages: `feat:`, `fix:`, `chore:` followed by a brief description.

### Verifying Applied Instructions

To confirm that Copilot is using the instructions:
1. Submit a request in Copilot Chat.
2. At the bottom of the Chat, check the **"References"** list.
3. If `.github/copilot-instructions.md` (or a path-specific instruction) is listed, it is active.

