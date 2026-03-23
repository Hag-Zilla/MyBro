# Contributing

This repository manages GitHub Copilot customization files.

## Contribution Principles

- Keep changes small and focused
- Keep all instruction content in English
- Prefer clear and testable guidance
- Start with flexible guidance before strict enforcement
- Avoid contradictions across files

## Change Scope

Use one PR for one intent:

- Add or improve one instruction domain
- Refine one prompt family
- Update governance and validation rules

## Required Checks

Before merge, ensure:

1. Markdown quality checks pass
2. Spelling checks pass
3. Link checks pass
4. Instruction frontmatter and section checks pass

## Authoring Rules

For files under [.github/instructions/](.github/instructions):

- Include YAML frontmatter with applyTo
- Use recommended sections from the template
- Prefer practical examples over abstract rules

For files under [.github/prompts/](.github/prompts):

- State objective clearly
- Add constraints and expected format
- Keep prompts reusable and concise

## Pull Request Checklist

- Explain why this change is needed
- Describe expected impact on Copilot behavior
- Mention any potential conflict risk with existing instructions
- Confirm CI checks are green

## Commit Message Convention

Use concise messages:

- feat: add new instruction guidance
- fix: resolve instruction conflict
- chore: improve repo governance docs