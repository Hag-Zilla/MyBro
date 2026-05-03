#!/usr/bin/env python3
"""Validate instruction and prompt governance contracts.

This script enforces repository conventions for:
- `.github/instructions/*.instructions.md` files
- `.github/prompts/*.prompt.md` files

It is intended to run in both pre-commit and CI.
"""

from __future__ import annotations

from pathlib import Path
import re
import sys


REPO_ROOT = Path(__file__).resolve().parents[1]
INSTRUCTIONS_DIR = REPO_ROOT / ".github" / "instructions"
PROMPTS_DIR = REPO_ROOT / ".github" / "prompts"

REQUIRED_INSTRUCTION_HEADERS = (
    "## Purpose",
    "## Guidelines",
    "## Examples",
)


def _extract_frontmatter(content: str) -> tuple[str | None, str]:
    """Return frontmatter and body if a frontmatter block exists."""
    if not content.startswith("---\n"):
        return None, content

    end = content.find("\n---\n", 4)
    if end == -1:
        return None, content

    frontmatter = content[4:end]
    body = content[end + 5 :]
    return frontmatter, body


def _validate_instruction_file(path: Path) -> list[str]:
    """Validate a single `.instructions.md` file."""
    issues: list[str] = []
    rel_path = path.relative_to(REPO_ROOT)
    content = path.read_text(encoding="utf-8")
    frontmatter, body = _extract_frontmatter(content)

    if frontmatter is None:
        issues.append(f"{rel_path}: missing valid YAML frontmatter block")
        return issues

    if re.search(r"^applyTo:\s*\".+\"\s*$", frontmatter, flags=re.MULTILINE) is None:
        issues.append(f"{rel_path}: frontmatter must define non-empty applyTo")

    for header in REQUIRED_INSTRUCTION_HEADERS:
        if header not in body:
            issues.append(f"{rel_path}: missing required section '{header}'")

    return issues


def _validate_prompt_file(path: Path) -> list[str]:
    """Validate a single `.prompt.md` file."""
    issues: list[str] = []
    rel_path = path.relative_to(REPO_ROOT)
    content = path.read_text(encoding="utf-8")

    required_reference = "#file:.github/copilot-instructions.md"
    if required_reference not in content:
        issues.append(f"{rel_path}: missing required reference '{required_reference}'")

    return issues


def main() -> int:
    """Run all instruction and prompt contract checks."""
    issues: list[str] = []

    instruction_files = sorted(INSTRUCTIONS_DIR.glob("*.instructions.md"))
    prompt_files = sorted(PROMPTS_DIR.glob("*.prompt.md"))

    if not instruction_files:
        issues.append(f"{INSTRUCTIONS_DIR}: no .instructions.md files found")
    if not prompt_files:
        issues.append(f"{PROMPTS_DIR}: no .prompt.md files found")

    for file_path in instruction_files:
        issues.extend(_validate_instruction_file(file_path))

    for file_path in prompt_files:
        issues.extend(_validate_prompt_file(file_path))

    if issues:
        print("Instruction contract validation failed:\n")
        for issue in issues:
            print(f"- {issue}")
        return 1

    print(
        "Instruction contract validation passed "
        f"({len(instruction_files)} instruction files, {len(prompt_files)} prompt files)."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
