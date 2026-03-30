# MyBro

Repository dedicated to GitHub Copilot customization and instruction governance.

## What This Repository Contains

- Global Copilot instructions: [.github/copilot-instructions.md](.github/copilot-instructions.md)
- Path-specific instructions: [.github/instructions/](.github/instructions)
- Reusable prompt templates: [.github/prompts/](.github/prompts)
- Golden prompt scenarios: [.github/golden-prompts/](.github/golden-prompts)
- Contribution rules for instruction changes: [CONTRIBUTING.md](CONTRIBUTING.md)
- CI checks for instruction quality and consistency: [.github/workflows/docs-quality.yml](.github/workflows/docs-quality.yml)

## Governance Model

Instruction priority is intentionally simple and explicit:

1. System and platform policies
2. User request in current chat
3. Global repository instructions
4. Path-specific instructions
5. Prompt files

When two repository rules conflict, the more specific rule should win.
When specificity is equal, prefer the most recent and clearly justified update.

## Repository Goals

- Keep instructions clear, testable, and easy to maintain
- Favor practical guidance over rigid rules in early stages
- Avoid contradictory directives across files
- Keep all instruction content in English

## File Conventions

### Global Instructions

- Location: [.github/copilot-instructions.md](.github/copilot-instructions.md)
- Scope: repository-wide behavior and standards

### Path-Specific Instructions

- Location: [.github/instructions/](.github/instructions)
- Required frontmatter:

```yaml
---
applyTo: "glob/pattern/**/*.py"
---
```

- Recommended section order:
  - Purpose
  - Guidelines
  - Examples

### Prompt Templates

- Location: [.github/prompts/](.github/prompts)
- Keep prompts focused, reusable, and concise
- Include expected output style and constraints

### Golden Prompt Scenarios

- Location: [.github/golden-prompts/](.github/golden-prompts)
- Purpose: behavior regression checks for instruction quality
- Usage: run scenario prompts in Copilot Chat and compare against expected behavior
- Scoring rubric: [.github/golden-prompts/SCORECARD.md](.github/golden-prompts/SCORECARD.md)
- Reporting template: [.github/golden-prompts/report-template.md](.github/golden-prompts/report-template.md)

## Local Validation

Recommended quick validation before opening a PR:

1. **Install pre-commit hooks** (one-time setup):

   ```bash
   pip install pre-commit
   pre-commit install
   ```

2. **Hooks run automatically on commit**, checking:

   - Markdown structure and style
   - Spelling for instruction files
   - JSON and YAML syntax
   - Custom instruction validation

3. **Or run manually**:

   ```bash
   pre-commit run --all-files
   ```

CI runs these checks automatically on every push and pull request.

## Typical Workflow

1. Propose a small, focused change
2. Update affected instruction or prompt files
3. Ensure no rule contradictions are introduced
4. Open a PR with clear rationale and impact

## Using These Instructions in Another Repository

Run this from the **root of any new local git repo** to fetch the Copilot
configuration directly from MyBro on GitHub:

```bash
curl -sSL https://raw.githubusercontent.com/Hag-Zilla/MyBro/main/scripts/bootstrap-copilot.sh | bash
```

The script fetches and places:

- `.github/copilot-instructions.md` — global rules
- `AGENTS.md` — agent governance rules
- `.github/instructions/` — all path-specific instruction files
- `.github/prompts/` — all reusable prompt templates

Validation infrastructure (workflows, pre-commit config, linting configs) is
intentionally **not** copied — it stays in MyBro only.

Re-run the command at any time to pull updates from MyBro.

## Roadmap

- Add change log for instruction evolution and compatibility notes
