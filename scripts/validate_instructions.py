"""Validate instruction markdown files for frontmatter and required sections."""

from __future__ import annotations

from pathlib import Path
import re
import sys


REPO_ROOT = Path(__file__).resolve().parents[1]
INSTRUCTIONS_DIR = REPO_ROOT / ".github" / "instructions"

REQUIRED_HEADINGS = [
    "## Purpose",
    "## Scope",
    "## Guidelines",
    "## Examples",
    "## Validation Checklist",
]


def parse_frontmatter(text: str) -> tuple[str | None, str]:
    """Extract frontmatter block and remaining body.

    Returns a tuple with frontmatter string (or None if absent) and markdown body.
    """
    if not text.startswith("---\n"):
        return None, text

    marker = "\n---\n"
    end_index = text.find(marker, 4)
    if end_index == -1:
        return None, text

    frontmatter = text[4:end_index]
    body = text[end_index + len(marker) :]
    return frontmatter, body


def validate_instruction_file(path: Path) -> list[str]:
    """Validate one instruction file and return error messages."""
    errors: list[str] = []
    text = path.read_text(encoding="utf-8")

    frontmatter, body = parse_frontmatter(text)
    if frontmatter is None:
        errors.append("Missing valid YAML frontmatter delimiters.")
    else:
        if not re.search(r"(?m)^applyTo:\s*\".+\"\s*$", frontmatter):
            errors.append("Frontmatter must contain applyTo with a quoted value.")

    for heading in REQUIRED_HEADINGS:
        if heading not in body:
            errors.append(f"Missing required heading: {heading}")

    if re.search(r"[\u00C0-\u017F]", text):
        # Heuristic to catch accented words commonly indicating non-English text.
        errors.append("Non-ASCII accented characters detected; keep instruction files English-only.")

    return errors


def main() -> int:
    """Run validation for all instruction files and print a CI-friendly report."""
    if not INSTRUCTIONS_DIR.exists():
        print("No .github/instructions directory found; nothing to validate.")
        return 0

    files = sorted(INSTRUCTIONS_DIR.glob("*.instructions.md"))
    if not files:
        print("No instruction files found; nothing to validate.")
        return 0

    has_errors = False
    for file_path in files:
        errors = validate_instruction_file(file_path)
        if not errors:
            print(f"OK: {file_path.relative_to(REPO_ROOT)}")
            continue

        has_errors = True
        print(f"ERROR: {file_path.relative_to(REPO_ROOT)}")
        for err in errors:
            print(f"  - {err}")

    return 1 if has_errors else 0


if __name__ == "__main__":
    raise SystemExit(main())