# MyBro — GitHub Copilot Customization & Instruction Governance

<div align="center">
  <img src="assets/logo.png" alt="MyBro Logo" width="200">

  **Professional-grade GitHub Copilot customization framework with domain-specific instructions, reusable prompts, and automated quality governance.**

  **Built with:** Markdown · Python · GitHub Actions · pre-commit
</div>

![CI](https://github.com/Hag-Zilla/MyBro/actions/workflows/docs-quality.yml/badge.svg) ![GitHub release (latest by date)](https://img.shields.io/github/v/release/Hag-Zilla/MyBro) ![License: CC BY-NC 4.0](https://img.shields.io/badge/License-CC%20BY--NC%204.0-lightgrey.svg) ![GitHub Copilot](https://img.shields.io/badge/GitHub%20Copilot-customized-black.svg) ![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen.svg) ![markdownlint](https://img.shields.io/badge/markdownlint-passing-brightgreen.svg)

---

## 📋 Table of Contents

1. [About](#about)
2. [Key Features](#key-features)
3. [Quick Start](#quick-start)
4. [Architecture & File Structure](#architecture--file-structure)
5. [Domain Coverage](#domain-coverage)
6. [Configuration & Customization](#configuration--customization)
   - [Language Configuration](#language-configuration)
   - [Branch Strategy](#branch-strategy)
7. [Governance Model](#governance-model)
8. [File Conventions & Standards](#file-conventions--standards)
9. [Code Quality & Development Standards](#code-quality--development-standards)
10. [Extra Documentation](#extra-documentation)
11. [Resources & References](#resources--references)
12. [Contributing](#contributing)
13. [Troubleshooting](#troubleshooting)
14. [Support](#support)
15. [License](#license)

---

## About

**MyBro** is a comprehensive framework for managing GitHub Copilot's behavior at scale. Instead of relying on default AI suggestions, MyBro enables teams to enforce consistent coding standards, adopt domain-specific best practices, and ensure all Copilot interactions align with organizational requirements.

The repository solves three fundamental challenges:

- **Consistency**: Maintain uniform coding, security, and documentation standards across projects
- **Domain Expertise**: Inject specialized knowledge for ML, MLOps, data engineering, APIs, and more
- **Governance**: Validate instruction quality and prevent conflicting guidance through automated CI checks

MyBro is ideal for **Python teams working on data, ML, and API projects** who use GitHub Copilot and want to enforce consistent practices at scale.

**Target audience:** ML engineers · Data engineers · MLOps engineers · Backend Python developers · Tech leads on data/AI projects

---

## Key Features

**Global Custom Instructions**
Centralized guidance file (`copilot-instructions.md`) applied across all Copilot interactions, covering code style, security, testing, and design patterns.

**Domain-Specific Instructions**
Specialized `*.instructions.md` files covering 12 domain areas (ML training, data engineering, FastAPI, authentication, observability, and more), plus repository-wide structure rules, that activate automatically based on file path patterns.

**Reusable Prompt Templates**
Pre-crafted `*.prompt.md` files for common workflows (data pipelines, Prometheus metrics, authentication flows)—copy, customize, and submit to Copilot.

**Golden Prompt Scenarios**
High-quality example prompts and expected outputs for reference and learning.

**Automated Quality Checks**
GitHub Actions CI workflows validate instruction structure, formatting, spelling, and broken links—catch documentation and instruction issues before merge.

**Clear Instruction Priority**
Documented priority and conflict-resolution rules ensure specific instructions override general ones; most recent, well-reasoned updates take precedence when specificity is equal.

**Pre-commit Integration**
Local hooks run markdown linting, spellcheck, and link checks before each commit—fail fast, fix locally.

**Consolidated Agent Rules**
Agent behavior guidance (Copilot, code review bots) is consolidated in `.github/copilot-instructions.md` to keep a single source of truth.

---

## Quick Start

### 1) Clone and Explore the Repository

```bash
git clone https://github.com/Hag-Zilla/MyBro.git
cd MyBro
```

### 2) Activate the Custom Instructions in Your VS Code Workspace

Once cloned, the `.github/copilot-instructions.md` file is automatically recognized by VS Code (if you have the Copilot Chat extension installed). To verify activation:

1. Open VS Code in the MyBro workspace: `code .`
2. Open VS Code Settings: `Ctrl+,` (Windows/Linux) or `Cmd+,` (macOS)
3. Search for **"Copilot"** and verify that custom instructions are enabled
4. Check the Copilot Chat panel—it should reference instructions from this repo

### 3) Install Pre-commit Hooks (Recommended)

Set up automated quality checks to run before each commit:

```bash
pip install pre-commit
pre-commit install
```

Verify the installation:

```bash
pre-commit run --all-files
```

Expected output: ✓ All checks pass (markdownlint, cspell, link check).

### 4) Essential Configuration Files

| File/Directory | Purpose | Example |
|---|---|---|
| `.github/copilot-instructions.md` | Global Copilot behavior (code style, security, logging) | [Read it](./.github/copilot-instructions.md) |
| `.github/instructions/` | Domain-specific rules (path-based activation) | [Browse domains](#domain-coverage) |
| `.github/prompts/` | Ready-to-use prompt templates | [EDA template](.github/prompts/eda-analysis.prompt.md) |
| `.github/golden-prompts/` | Reference examples and expected outputs | [View examples](.github/golden-prompts/) |
| `CONTRIBUTING.md` | Contribution workflow and PR requirements | [Read it](./CONTRIBUTING.md) |

### 5) Verify Installation

Test that the setup works by opening Copilot Chat and running a simple prompt:

```text
Create a simple Python function with PEP 8 style, type hints, and a docstring.
```

**Expected behavior**: Copilot should generate code with:

- Explicit variable names
- Type annotations
- Google-style docstring
- Proper formatting (black/isort compatible)

If output doesn't follow these conventions, instructions may not be loaded. Check:

```bash
pre-commit run --all-files
```

### 6) Advanced: Clone into Other Projects

To use MyBro's instructions in another project:

```bash
# Option A: Add as a git submodule
git submodule add https://github.com/Hag-Zilla/MyBro.git .copilot-governance

# Option B: Copy the .github directory
cp -r MyBro/.github ./your-project/.github
```

Then, customize paths in `.github/instructions/*.instructions.md` to match your codebase structure.

---

## Architecture & File Structure

### High-Level Architecture

MyBro operates on a **layered instruction model**:

```text
┌─────────────────────────────────────────────┐
│  User Request in Copilot Chat               │
└────────────────┬────────────────────────────┘
                 │
           ┌─────▼─────────────────────────────────┐
           │  Instruction Priority Resolver        │
           │  (Specificity → Recency)              │
           └─────┬─────────────────────────────────┘
                 │
       ┌─────────┴─────────────┬──────────────┐
       │                       │              │
    ┌──▼───┐            ┌──────▼──────┐  ┌────▼────┐
    │Global│            │Path-Specific│  │Prompts  │
    │Instr.│            │Instructions │  │Templates│
    └──────┘            └─────────────┘  └─────────┘
       │                      │              │
       └──────────┬───────────┴──────────────┘
                  │
          ┌───────▼────────────┐
          │ More Accurate      │
          │ Copilot Behavior   │
          └────────────────────┘
```

### Complete Project Structure

```text
MyBro/
│
├── README.md                              # This file
├── LICENSE                                # CC BY-NC 4.0 license
├── CONTRIBUTING.md                        # Contribution workflow & PR checklist
├── followup.txt                           # Follow-up tasks & roadmap
│
├── .github/
│   │
│   ├── copilot-instructions.md           # Global instructions (code style, security, testing)
│   │   └─ Covers: PEP 8, type hints, docstrings, logging, security, Docker, K8s, FastAPI
│   │
│   ├── instructions/                     # Domain-specific instruction files
│   │   ├── TEMPLATE.instructions.md      # Template for new domain instructions
│   │   ├── project-structure.instructions.md  # Expected project layout (all repos)
│   │   ├── readme-structure.instructions.md   # Required README sections and format
│   │   ├── ml-training.instructions.md   # ML model training best practices
│   │   ├── ml-inference.instructions.md  # ML model serving & inference
│   │   ├── eda.instructions.md           # Exploratory data analysis (EDA)
│   │   ├── notebooks.instructions.md     # Jupyter notebook standards
│   │   ├── experiment-tracking.instructions.md  # MLflow & experiment management
│   │   ├── data-validation.instructions.md      # Data quality & schema validation
│   │   ├── data-engineering.instructions.md     # ETL pipelines & SQL standards
│   │   ├── mlops-pipelines.instructions.md      # Workflow orchestration (DAGs)
│   │   ├── fastapi-api.instructions.md   # FastAPI & REST API design
│   │   ├── auth-security.instructions.md # OAuth2, JWT, security best practices
│   │   ├── observability.instructions.md # Prometheus, Grafana, Loki
│   │   └── environments.instructions.md  # Config management & environment variables
│   │
│   ├── prompts/                          # Reusable prompt templates
│   │   ├── eda-analysis.prompt.md        # Template: EDA workflow
│   │   ├── data-pipeline.prompt.md       # Template: ETL pipeline
│   │   ├── ml-pipeline-ci.prompt.md      # Template: ML pipeline CI/CD
│   │   ├── add-auth.prompt.md            # Template: Add authentication
│   │   ├── add-prometheus-metrics.prompt.md  # Template: Instrument metrics
│   │   ├── docker-k8s.prompt.md          # Template: Docker & Kubernetes
│   │   └── code-review.prompt.md         # Template: Code review checklist
│   │
│   ├── golden-prompts/                   # High-quality example scenarios
│   │   └── ... (reference outputs & expected behavior)
│   │
│   ├── scripts/                          # Automation & CI/CD helpers
│   │   └── bootstrap-copilot.sh          # Setup script for new projects
│   │
│   └── workflows/                        # GitHub Actions CI
│       ├── docs-quality.yml              # Full pipeline (main): lint, spell, links, validate
│       └── dev-quality.yml               # Lightweight pipeline (dev): lint + spell only
│
├── .pre-commit-config.yaml                # Pre-commit hook definitions
├── .github/.markdownlint.json             # Markdown linting rules
├── .github/.cspell.json                   # Spell-check dictionary
│
├── scripts/                               # Repository-level utilities
│   └── bootstrap-copilot.sh               # Initialize MyBro in new projects
│
├── assets/
│   └── logo.png                           # MyBro logo
│
└── .git/                                  # Git version control
```

---

## Domain Coverage

MyBro provides specialized instruction files covering 12 domain areas, plus repository-wide structure and README standards. Each file activates automatically when you edit files matching its `applyTo` glob pattern:

| Domain | Instruction File | Prompt Template | Focus Area |
|---|---|---|---|
| **ML Training** | [ml-training.instructions.md](.github/instructions/ml-training.instructions.md) | — | Model development, hyperparameter tuning, reproducibility |
| **ML Inference** | [ml-inference.instructions.md](.github/instructions/ml-inference.instructions.md) | — | Model serving, latency optimization, versioning |
| **EDA & Analysis** | [eda.instructions.md](.github/instructions/eda.instructions.md) | [eda-analysis.prompt.md](.github/prompts/eda-analysis.prompt.md) | Data exploration, visualization, statistical testing |
| **Jupyter Notebooks** | [notebooks.instructions.md](.github/instructions/notebooks.instructions.md) | — | Notebook structure, reproducibility, output management |
| **Experiment Tracking** | [experiment-tracking.instructions.md](.github/instructions/experiment-tracking.instructions.md) | — | MLflow, hyperparameter logging, artifact management |
| **Data Validation** | [data-validation.instructions.md](.github/instructions/data-validation.instructions.md) | — | Schema validation, quality checks, error handling |
| **Data Engineering / ETL** | [data-engineering.instructions.md](.github/instructions/data-engineering.instructions.md) | [data-pipeline.prompt.md](.github/prompts/data-pipeline.prompt.md) | SQL standards, idempotency, incremental processing |
| **MLOps Pipelines** | [mlops-pipelines.instructions.md](.github/instructions/mlops-pipelines.instructions.md) | [ml-pipeline-ci.prompt.md](.github/prompts/ml-pipeline-ci.prompt.md) | DAGs, Airflow, workflow orchestration, CI/CD |
| **FastAPI** | [fastapi-api.instructions.md](.github/instructions/fastapi-api.instructions.md) | — | Pydantic validation, OpenAPI docs, testing patterns |
| **Authentication & Security** | [auth-security.instructions.md](.github/instructions/auth-security.instructions.md) | [add-auth.prompt.md](.github/prompts/add-auth.prompt.md) | OAuth2, JWT, SECRET management, CORS |
| **Observability** | [observability.instructions.md](.github/instructions/observability.instructions.md) | [add-prometheus-metrics.prompt.md](.github/prompts/add-prometheus-metrics.prompt.md) | Prometheus metrics, Grafana, structured logging (Loki) |
| **Environment Config** | [environments.instructions.md](.github/instructions/environments.instructions.md) | — | Config management, secrets, environment variables |
| **Docker & Kubernetes** | — | [docker-k8s.prompt.md](.github/prompts/docker-k8s.prompt.md) | Multi-stage builds, resource limits, health checks |
| **Code Review** | — | [code-review.prompt.md](.github/prompts/code-review.prompt.md) | Review checklists, best practices, standards |

---

## Configuration & Customization

### Using Custom Instructions in Your Own Project

The easiest way to adopt MyBro's instructions in a new project:

```bash
# From your project root:
curl -sSL https://raw.githubusercontent.com/Hag-Zilla/MyBro/main/scripts/bootstrap-copilot.sh | bash
```

This downloads:

- `.github/copilot-instructions.md` (global + agent behavior rules)
- All `.github/instructions/*.instructions.md` files
- All `.github/prompts/*.prompt.md` templates
- `.github/golden-prompts/` reference scenarios

### Language Configuration

Two language settings are declared at the top of `copilot-instructions.md`:

| Setting | Key | Default |
|---|---|---|
| Interaction language | `Interaction language` | English |
| Development language | `Development language` | Python |

- **Interaction language** controls the language Copilot uses in responses to the user.
- **Development language** sets the expected programming language for source code, docstrings, and inline comments.

To change either, edit the `## Language Configuration` section in
`.github/copilot-instructions.md`.

### Branch Strategy

| Branch | CI/CD scope |
|---|---|
| `main` | Full pipeline: lint, test, security scan, build, deploy — requires review |
| `dev` | Lightweight: lint + fast tests only — for iterative work |

### Customize Instructions for Your Team

Each `.instructions.md` file has YAML frontmatter defining `applyTo` patterns:

```yaml
---
applyTo: "src/ml/training/**/*.py"
---
# Instructions apply to ML training code only
```

**To adapt for your codebase:**

1. Modify the `applyTo` glob pattern to match your directory structure
2. Update specific guidance to reflect your conventions
3. Commit changes to your project

### Create a New Domain-Specific Instruction

1. Copy [TEMPLATE.instructions.md](.github/instructions/TEMPLATE.instructions.md)
2. Fill in YAML frontmatter with your `applyTo` pattern
3. Add sections covering:
   - Purpose (why this domain matters)
   - Guidelines (do's and don'ts)
   - Examples (code snippets)
   - References (links to tools/docs)
4. Submit a PR to MyBro or use locally in your project

---

## Governance Model

### Instruction Priority

Copilot resolves conflicting instructions using **strict priority**:

1. **System & platform policies** (GitHub, VS Code)
2. **User request in current chat** (explicit override)
3. **Global instructions** (`copilot-instructions.md`)
4. **Path-specific instructions** (`.github/instructions/*.md`)
5. **Prompt templates** (`.github/prompts/*.md`)

### Conflict Resolution Rules

- **More specific rules override general rules**: A path-specific rule for `src/ml/**/*.py` beats a global Python rule
- **Recent, justified rules win**: When specificity is equal, the most recent update with explicit rationale takes precedence
- **Flexible guidance is preferred**: Start with guidance; only enforce strict rules when clearly required

### CI/CD Validation

Every commit triggers automated checks:

- ✅ Markdown structure and syntax (markdownlint)
- ✅ Spelling and dictionary correctness (cspell)
- ✅ Link validation (no broken references)
- ✅ JSON/YAML syntax correctness

Failures block merges. Fixes are required before PR acceptance.

---

## File Conventions & Standards

### `.instructions.md` Files

**Location:** `.github/instructions/`

**Required Frontmatter:**

```yaml
---
applyTo: "glob/pattern/**/*.py"
description: "Brief description of scope"
---
```

**Recommended Sections:**

- **Purpose** — Why this domain/pattern matters
- **Guidelines** — Do's and don'ts (practical advice)
- **Examples** — Code snippets showing correct behavior
- **Tools/References** — Links to relevant tools, docs, standards
- **Common Mistakes** — Anti-patterns to avoid

### `.prompt.md` Files

**Location:** `.github/prompts/`

**Structure:**

```markdown
# Prompt Title

## Objective
Clear statement of what this prompt achieves.

## Prerequisites
Tools, setup, files needed before running.

## Constraints
Output format, length limits, style requirements.

## Workflow Steps
Numbered steps or sections.

## Expected Output
Example result or quality criteria.

## Resources
Links to related docs or templates.
```

### Golden Prompts

**Location:** `.github/golden-prompts/`

**Purpose:** High-quality scenario examples and expected outputs—used for regression testing and prompt/instruction quality review.

**Format:**

- Prompt scenario (what you submit to Copilot)
- Ideal/expected output
- Quality rubric (what makes it good)
- Common issues (what to watch for)

---

## Code Quality & Development Standards

### Tools & Automation

| Tool | Purpose | Config File | Setup |
|---|---|---|---|
| **markdownlint** | Markdown style validation | `.github/.markdownlint.json` | `pre-commit install` |
| **cspell** | Spell-checking for instructions | `.github/.cspell.json` | `pre-commit install` |
| **pre-commit** | Run hooks before each commit | `.pre-commit-config.yaml` | `pip install pre-commit && pre-commit install` |
| **GitHub Actions** | CI/CD validation on push/PR | `.github/workflows/docs-quality.yml` (main), `.github/workflows/dev-quality.yml` (dev) | Auto-runs on push/PR |

### Local Setup for Contributors

```bash
# 1. Clone repo and enter directory
git clone https://github.com/Hag-Zilla/MyBro.git
cd MyBro

# 2. Install pre-commit hooks (one-time)
pip install pre-commit
pre-commit install

# 3. Make changes and commit
# Hooks automatically validate before commit

# 4. Or manually run all checks
pre-commit run --all-files
```

---

## Extra Documentation

Detailed documentation for specialized topics:

| Document | Focus | Audience |
|---|---|---|
| [CONTRIBUTING.md](CONTRIBUTING.md) | Contribution workflow, PR checklist, commit conventions | Contributors, maintainers |
| [.github/copilot-instructions.md](.github/copilot-instructions.md) | Global coding standards (PEP 8, security, testing) | All developers |
| [.github/instructions/](.github/instructions/) | Domain-specific guidance (MLOps, FastAPI, auth, etc.) | Domain specialists |
| [.github/prompts/](.github/prompts/) | Ready-to-use prompt templates | Copilot Chat users |
| [.github/golden-prompts/](.github/golden-prompts/) | High-quality scenario examples | Instruction authors |

---

## Resources & References

### External References

- **Copilot Documentation**
  - [GitHub Copilot Official Docs](https://docs.github.com/en/copilot)
  - [Custom Instructions Guide](https://docs.github.com/en/copilot/customizing-copilot)

- **Industry Standards**
  - [PEP 8 — Python Style Guide](https://pep8.org/)
  - [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html)
  - [FastAPI Best Practices](https://fastapi.tiangolo.com/)

- **Tools & Frameworks**
  - [pre-commit hooks](https://pre-commit.com/)
  - [markdownlint](https://github.com/DavidAnson/markdownlint)
  - [cspell](https://cspell.org/)
  - [shields.io](https://shields.io/) — Badge generator

### Related Projects

- **MyBro on GitHub**: [Hag-Zilla/MyBro](https://github.com/Hag-Zilla/MyBro)
- **cspell Dictionary**: [MyBro .github/.cspell.json](.github/.cspell.json)
- **markdownlint Config**: [MyBro .github/.markdownlint.json](.github/.markdownlint.json)

---

## Contributing

We welcome contributions! MyBro is designed to grow and improve with community input.

**All contribution guidelines, PR requirements, and code standards are documented in [CONTRIBUTING.md](CONTRIBUTING.md).**

---

## Troubleshooting

| Symptom | Likely Cause | Fix |
|---|---|---|
| Instructions seem inactive in Copilot Chat | File not found or workspace not opened from root | Ensure `.github/copilot-instructions.md` exists and open VS Code from the repo root |
| `pre-commit run` fails on markdownlint | Formatting or structure violation | Check the rule in `.github/.markdownlint.json`; fix indentation, blank lines, or heading levels |
| `pre-commit run` fails on cspell | Unknown word in an instruction file | Add the word to the `words` array in `.github/.cspell.json` |
| Not sure which instruction applies to a file | Glob pattern mismatch | Check the `applyTo` frontmatter in each `.instructions.md` against your file path |
| Two instructions seem contradictory | Overlapping glob patterns | The more specific glob wins — see [Governance Model](#governance-model) |
| CI passes locally but fails on GitHub | Environment or hook version mismatch | Pin hook versions in `.pre-commit-config.yaml` and ensure they match CI config |

---

## Support

### Getting Help

- **Questions about Copilot?** Check the [GitHub Copilot documentation](https://docs.github.com/copilot)
- **Issues with MyBro instructions?** Open an [issue on GitHub](https://github.com/Hag-Zilla/MyBro/issues)
- **Want to discuss improvements?** Start a [discussion on GitHub](https://github.com/Hag-Zilla/MyBro/discussions)

### Maintainer

**MyBro** is maintained by [Hag-Zilla](https://github.com/Hag-Zilla).

For inquiries or contributions, please:

- Open an issue with detailed context
- Submit a PR with your improvements
- Start a discussion for feature ideas

### Reporting Issues

If you find bugs or conflicts in instructions:

1. Open a GitHub issue with:
   - Clear description of the problem
   - Steps to reproduce
   - Expected vs. actual behavior
   - Copilot instructions file involved

2. Include context:
   - Your OS and VS Code version
   - Copilot Chat extension version
   - Relevant code snippets

---

## License

MyBro is licensed under the **Creative Commons Attribution-NonCommercial 4.0 International License** (CC BY-NC 4.0).

**Full license text:** [LICENSE](LICENSE)

For commercial use or alternative licensing, contact the maintainers.

---

<div align="center">
  <p>
    <strong>Made with 💪 for teams that love clean code and smart automation.</strong>
  </p>
  <p>
    ⭐ If MyBro helped you, consider starring the repo!
  </p>
  <p>
    <a href="https://github.com/Hag-Zilla/MyBro">View on GitHub</a> ·
    <a href="https://github.com/Hag-Zilla/MyBro/issues">Report Issue</a> ·
    <a href="https://github.com/Hag-Zilla/MyBro/discussions">Start Discussion</a>
  </p>
</div>
