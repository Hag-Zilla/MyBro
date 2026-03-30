# AGENTS.md — Copilot Agent Instructions

This file provides behaviour guidance for AI agents (Copilot coding agent, Copilot code review) operating in this repository.

## Repository Purpose

This repository is dedicated to GitHub Copilot customization: instruction files, prompt templates, and prompt governance.

## Agent Behaviour

### General
- Treat `.github/copilot-instructions.md` as the authoritative style reference.
- Prefer minimal, targeted changes over broad refactors.
- Each change must be independently testable or documented if a test is not applicable.

### Code Changes
- Follow PEP 8 and include type hints on all function signatures.
- All functions and classes must have a PEP 257-compliant docstring.
- Do not introduce new dependencies without updating `pyproject.toml` or `requirements.txt`.

### Security
- Never generate secrets, passwords, or API keys in any file.
- Do not add `print` statements to production code paths.
- Do not relax CORS, auth, or rate-limiting configurations without explicit justification.

### Pull Requests
- Scope PRs to a single concern (one feature, one fix, one refactor).
- Commit messages must follow the `feat:`, `fix:`, `chore:`, `docs:` prefix convention.
- Include a brief description of the change and how to verify it.

### Instruction and Prompt Files
- When creating a new `.instructions.md` file, use `.github/instructions/TEMPLATE.instructions.md` as the base.
- `applyTo` glob patterns must be specific enough to avoid unintended matches.
- Prompt files (`.prompt.md`) must include a `#file:` reference to `.github/copilot-instructions.md`.
