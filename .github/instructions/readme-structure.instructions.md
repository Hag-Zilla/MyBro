---
applyTo: "**"
---

## Purpose

Enforce a consistent README structure so every project exposes the same navigation
pattern and minimum required information.

## Required Sections (in order)

1. **Title + Badges** — Project name as H1; shields.io badges for CI, release, license,
   and any relevant tool (Copilot, pre-commit, etc.).
2. **Table of Contents** — Linked list matching the actual headings below.
3. **About** — One paragraph: what the project does, the problem it solves, and the
   target audience.
4. **Key Features** — Bulleted list of the main capabilities (5–8 items max).
5. **Quick Start** — Numbered steps: clone → environment setup → run.
   Include the minimum commands to get a working state.
6. **Architecture & File Structure** — High-level diagram or tree view of the project
   layout (reference `project-structure.instructions.md`).
7. **Configuration & Customization** — How to adapt the project (env vars, config
   files, instruction files). Include language and branch strategy tables.
8. **Contributing** — Link to `CONTRIBUTING.md`; one-sentence summary of the workflow.
9. **License** — License name and link to `LICENSE`.

## Guidelines

- Do not add sections that are empty or contain only "Coming soon."
- Keep the **About** section under 5 sentences.
- **Quick Start** must be self-contained: a reader with a clean environment should reach
  a working state following only those steps.
- Use ATX headings only (`##`, `###`), never setext (underline-style).
- Fenced code blocks must specify a language (` ```bash `, ` ```python `, ` ```text `).
- Lists must be surrounded by blank lines (markdownlint MD032).
- Line length limit: follow the value set in `.github/.markdownlint.json`.
- The interaction language of the README must match the `Interaction language` setting
  in `.github/copilot-instructions.md`.

## Badges (standard set)

```markdown
![CI](https://github.com/<org>/<repo>/actions/workflows/docs-quality.yml/badge.svg)
![GitHub release](https://img.shields.io/github/v/release/<org>/<repo>)
![License](https://img.shields.io/badge/License-<SPDX>-lightgrey.svg)
![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen.svg)
```

Replace `<org>`, `<repo>`, and `<SPDX>` with actual values.

## Examples

```markdown
# MyProject — Short tagline

![CI](https://github.com/org/myproject/actions/workflows/docs-quality.yml/badge.svg)
![License](https://img.shields.io/badge/License-MIT-lightgrey.svg)

## About

MyProject does X to solve Y for Z audience.

## Quick Start

```bash
git clone https://github.com/org/myproject.git
cd myproject
pip install -e ".[dev]"
pre-commit install
```
```
