# MyBro — GitHub Copilot Customization & Instruction Governance

<div align="center">
  <img src="assets/logo.png" alt="MyBro Logo" width="200">

  **Govern GitHub Copilot with explicit instructions, reusable prompts, and repository-level standards.**

  **Built for Python, data, ML, MLOps, and API teams that need consistent AI-assisted development.**
</div>

[![CI](https://github.com/Hag-Zilla/MyBro/actions/workflows/quality.yml/badge.svg?branch=main)](https://github.com/Hag-Zilla/MyBro/actions/workflows/quality.yml) [![GitHub release](https://img.shields.io/github/v/release/Hag-Zilla/MyBro)](https://github.com/Hag-Zilla/MyBro/releases) [![License](https://img.shields.io/badge/License-CC%20BY--NC%204.0-lightgrey.svg)](LICENSE) [![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen.svg)](.pre-commit-config.yaml)
[![GitHub Copilot](https://img.shields.io/badge/GitHub%20Copilot-customized-black.svg)](.github/copilot-instructions.md)

MyBro provides a structured governance layer for GitHub Copilot: global instructions,
path-specific rules, reusable prompts, and golden scenarios. The goal is to make
Copilot behavior more predictable, auditable, and aligned with real engineering
standards across repositories.

## Table of Contents

1. [About](#about)
2. [Key Features](#key-features)
3. [Quick Start](#quick-start)
4. [Architecture and File Structure](#architecture-and-file-structure)
5. [Configuration and Customization](#configuration-and-customization)
6. [Contributing](#contributing)
7. [License](#license)

## About

MyBro is a governance framework for GitHub Copilot customization. It provides a
structured way to define global instructions, domain-specific instruction files, reusable
prompts, and evaluation scenarios so teams can keep Copilot outputs consistent,
secure, and aligned with engineering standards.

It is designed for teams working on Python, data, ML, MLOps, and API projects that want
repeatable AI-assisted development behavior across repositories.

## Key Features

- Global Copilot guidance in `.github/copilot-instructions.md`.
- Domain-specific instruction packs in `.github/instructions/`.
- Reusable operational prompts in `.github/prompts/`.
- Golden scenarios and scorecards in `.github/golden-prompts/`.
- Repository bootstrap automation via `scripts/bootstrap-copilot.sh`.
- Quality gates with pre-commit and GitHub Actions (lint, spell, link checks).
- Explicit support for target-repository standards through `./docs/STANDARDS.md`.

## Quick Start

1. Clone the repository:

    ```bash
    git clone https://github.com/Hag-Zilla/MyBro.git
    cd MyBro
    ```

1. Set up the development environment:

    ```bash
    uv sync --group dev
    uv run pre-commit install
    uv run pre-commit install-hooks
    ```

1. Validate everything locally:

    ```bash
    uv pre-commit run --all-files
    ```

1. Use the bootstrap script in a target repository:

    ```bash
    curl -sSL https://raw.githubusercontent.com/Hag-Zilla/MyBro/main/scripts/bootstrap-copilot.sh | bash
    ```

This installs:

- `.github/copilot-instructions.md`
- `.github/instructions/`
- `.github/prompts/`
- `.github/golden-prompts/`

In target repositories, place standards in `./docs/STANDARDS.md` so Copilot can apply
local engineering conventions in addition to MyBro rules.

## Architecture and File Structure

MyBro uses a layered instruction model:

1. System and platform policies
2. User request in current chat
3. Global instructions (`.github/copilot-instructions.md`)
4. Repository standards (`./docs/STANDARDS.md`, when present)
5. Path-specific instructions (`.github/instructions/*.instructions.md`)
6. Prompt templates (`.github/prompts/*.prompt.md`)

Tracked repository structure:

  MyBro/
  ├── .github/
  │   ├── copilot-instructions.md
  │   ├── .markdownlint.json
  │   ├── .cspell.json
  │   ├── instructions/
  │   │   ├── TEMPLATE.instructions.md
  │   │   ├── project-structure.instructions.md
  │   │   ├── readme-structure.instructions.md
  │   │   ├── ml-training.instructions.md
  │   │   ├── ml-inference.instructions.md
  │   │   ├── eda.instructions.md
  │   │   ├── notebooks.instructions.md
  │   │   ├── experiment-tracking.instructions.md
  │   │   ├── data-validation.instructions.md
  │   │   ├── data-engineering.instructions.md
  │   │   ├── mlops-pipelines.instructions.md
  │   │   ├── fastapi-api.instructions.md
  │   │   ├── auth-security.instructions.md
  │   │   ├── observability.instructions.md
  │   │   └── environments.instructions.md
  │   ├── prompts/
  │   │   ├── add-auth.prompt.md
  │   │   ├── add-prometheus-metrics.prompt.md
  │   │   ├── code-review.prompt.md
  │   │   ├── data-pipeline.prompt.md
  │   │   ├── docker-k8s.prompt.md
  │   │   ├── eda-analysis.prompt.md
  │   │   ├── ml-pipeline-ci.prompt.md
  │   │   └── write-tests.prompt.md
  │   ├── golden-prompts/
  │   │   ├── README.md
  │   │   ├── SCORECARD.md
  │   │   ├── report-template.md
  │   │   ├── code-review-request.scenario.md
  │   │   ├── fastapi-endpoint.scenario.md
  │   │   ├── ml-training-function.scenario.md
  │   │   └── security-sensitive-request.scenario.md
  │   └── workflows/
  │       └── quality.yml
  ├── scripts/
  │   └── bootstrap-copilot.sh
  ├── assets/
  │   └── logo.png
  ├── README.md
  ├── CONTRIBUTING.md
  ├── LICENSE
  ├── .pre-commit-config.yaml
  ├── pyproject.toml
  ├── uv.lock
  └── .gitignore

Current inventory:

- `15` instruction files (`*.instructions.md`, including template and repo-wide rules)
- `8` prompt templates (`*.prompt.md`)
- `4` golden scenarios (`*.scenario.md`)

## Configuration and Customization

### Language Configuration

Language behavior is defined in `.github/copilot-instructions.md`.

| Setting | Default | Purpose |
|---|---|---|
| Interaction language | English | Language for user-facing assistant responses |
| Development language | Python | Language convention for generated code and comments |

### Branch Strategy and Quality Workflow

| Branch | Workflow Trigger | Validation Scope |
|---|---|---|
| `main` | push + PR | markdownlint + cspell + lychee |
| `develop` | push + PR | markdownlint + cspell + lychee |

Implementation details:

- Workflow file: `.github/workflows/quality.yml`
- Link check runs only on `main` (or PRs targeting `main`)
- Local quality uses `.pre-commit-config.yaml` with aligned tools

### Domain Coverage

MyBro covers these domains through `.instructions.md` files:

- ML training and inference
- EDA and notebooks
- Experiment tracking
- Data validation and data engineering
- MLOps orchestration
- FastAPI APIs
- Auth and security
- Observability
- Environment and settings management
- Repository-wide structure and README governance

### Authoring and Extension

To add a new domain instruction:

1. Copy `.github/instructions/TEMPLATE.instructions.md`
2. Set a precise `applyTo` pattern
3. Add actionable guidelines and one realistic example
4. Reference `.github/copilot-instructions.md` from related prompt files

For prompt templates in `.github/prompts/`, prefer:

- clear objective
- explicit constraints
- measurable expected outputs
- references using `#file:` tags

## Contributing

Contributions are welcome. Keep changes focused and testable.

Use this workflow:

1. Create a focused branch from `develop`.
1. Update instructions/prompts/scenarios with clear intent.
1. Run local validation:

    ```bash
    uv run pre-commit run --all-files
    ```

1. Open a PR with:

- rationale and expected behavior change
- conflict risk notes (if any)
- validation evidence (checks passing)

For full contribution details, see [CONTRIBUTING.md](CONTRIBUTING.md).

## License

This project is licensed under the Creative Commons Attribution-NonCommercial 4.0
International License (CC BY-NC 4.0).

See [LICENSE](LICENSE) for the full text.

For commercial use or alternative licensing, contact the maintainers.

---

<div align="center">
  <p>
    <strong>Made with 💪 for teams that love clean code and smart automation.</strong>
  </p>
  <p>
    ⭐ If MyBro helped you, consider starring the repo!
  </p>
</div>
