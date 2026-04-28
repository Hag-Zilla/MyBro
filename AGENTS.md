# AGENTS.md — Copilot Agent Instructions

This file provides behaviour guidance for AI agents (Copilot coding agent, Copilot code review) operating in this repository.

## Repository Purpose

This repository is dedicated to GitHub Copilot customization: instruction files, prompt templates, and prompt governance.

## Agent Behaviour

### Language Configuration

- **Interaction language**: English — all Copilot responses and comments directed at the
  user must be in English, unless the user explicitly switches to another language.
- **Development language**: Python — all source code, docstrings, and inline comments
  must be written in English (standard convention for code).

### General

- Treat `.github/copilot-instructions.md` as the authoritative style reference.
- Prefer minimal, targeted changes over broad refactors.
- Each change must be independently testable or documented if a test is not applicable.

### Custom Rules (User Preferences)

- Never perform a `git commit`, `git push`, or any version control write operation on
  behalf of the user. Propose the command instead.
- Be direct and honest. Do not flatter or soften incorrect assumptions — if the user is
  wrong, say so clearly and explain why.
- Always ask clarifying questions before proceeding when a request is ambiguous,
  incomplete, or could be interpreted in multiple ways.
- When any file in the repository is created, moved, renamed, or deleted, update
  `README.md` to reflect the change before considering the task complete.
- When proposing solutions, reference industry best practices and state-of-the-art
  approaches; explain trade-offs and justify recommendations.

### Security

- Do not add `print` statements to production code paths.
- Do not relax CORS, auth, or rate-limiting configurations without explicit justification.

### Instruction and Prompt Files

- When creating a new `.instructions.md` file, use `.github/instructions/TEMPLATE.instructions.md`
  as the base.
- `applyTo` glob patterns must be specific enough to avoid unintended matches.
- Prompt files (`.prompt.md`) must include a `#file:` reference to `.github/copilot-instructions.md`.

### Expected Response Format

- **Be minimal**: default to 1-3 sentences. Expand only when the user explicitly asks
  (e.g., "explain", "elaborate", "detail", "give an example"). Avoid restating the
  question, filler sentences, or summaries of what was done. This saves tokens and
  keeps interactions efficient.
- Provide a concise and testable implementation, with PEP 257-compliant docstrings and
  type annotations.
- Add a small `pytest` test when the feature is non-trivial.
- For infrastructure changes, provide the complete manifest (`Dockerfile`, `helm` chart
  snippet) and a brief usage note.
- For commands and instructions, use code blocks with the correct language (bash,
  Dockerfile, yaml).
- Never include secrets or sensitive values in plain text.

For code style, PR conventions, commit format, and branch strategy, defer to
[`.github/copilot-instructions.md`](.github/copilot-instructions.md).
