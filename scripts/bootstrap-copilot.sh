#!/usr/bin/env bash
# bootstrap-copilot.sh — Fetch Copilot instruction files from MyBro into the current repo.
#
# Run this script from the ROOT of a new local git repository:
#
#   curl -sSL https://raw.githubusercontent.com/Hag-Zilla/MyBro/main/scripts/bootstrap-copilot.sh | bash
#
#   — or, if you have the script locally —
#
#   bash /path/to/MyBro/scripts/bootstrap-copilot.sh
#
# What is fetched from Hag-Zilla/MyBro (main branch):
#   .github/copilot-instructions.md   — global Copilot behaviour rules
#   .github/instructions/             — all path-specific instruction files
#   .github/prompts/                  — all reusable prompt templates
#   .github/golden-prompts/           — scenario references and scorecards
#
# Requirements: git, bash 4+

set -euo pipefail

MYBRO_REPO="https://github.com/Hag-Zilla/MyBro.git"
MYBRO_BRANCH="main"

# ── Checks ────────────────────────────────────────────────────────────────────

TARGET_REPO="${PWD}"

if [[ ! -d "${TARGET_REPO}/.git" ]]; then
  echo "Error: run this script from the root of a git repository." >&2
  echo "Current directory: ${TARGET_REPO}" >&2
  exit 1
fi

# ── Sparse checkout into a temp dir ──────────────────────────────────────────

TMP_DIR="$(mktemp -d)"
trap 'rm -rf "${TMP_DIR}"' EXIT

echo "Fetching Copilot instructions from ${MYBRO_REPO} (${MYBRO_BRANCH})..."
echo ""

git clone \
  --depth 1 \
  --filter=blob:none \
  --sparse \
  --branch "${MYBRO_BRANCH}" \
  "${MYBRO_REPO}" \
  "${TMP_DIR}" \
  --quiet

git -C "${TMP_DIR}" sparse-checkout set \
  ".github/copilot-instructions.md" \
  ".github/instructions" \
  ".github/prompts" \
  ".github/golden-prompts"

# ── Copy into current repo ────────────────────────────────────────────────────

copy_file() {
  local src="$1"
  local dest="$2"
  mkdir -p "$(dirname "${dest}")"
  if [[ -f "${dest}" ]]; then
    if diff -q "${src}" "${dest}" > /dev/null 2>&1; then
      echo "  [skip]    ${dest#"${TARGET_REPO}/"} (unchanged)"
      return
    fi
    echo "  [update]  ${dest#"${TARGET_REPO}/"}"
  else
    echo "  [create]  ${dest#"${TARGET_REPO}/"}"
  fi
  cp "${src}" "${dest}"
}

if [[ -f "${TMP_DIR}/.github/copilot-instructions.md" ]]; then
  copy_file \
    "${TMP_DIR}/.github/copilot-instructions.md" \
    "${TARGET_REPO}/.github/copilot-instructions.md"
fi

for dir in ".github/instructions" ".github/prompts" ".github/golden-prompts"; do
  if [[ -d "${TMP_DIR}/${dir}" ]]; then
    while IFS= read -r -d '' src_file; do
      local_rel="${src_file#"${TMP_DIR}/"}"
      copy_file "${src_file}" "${TARGET_REPO}/${local_rel}"
    done < <(find "${TMP_DIR}/${dir}" -type f -print0)
  fi
done

echo ""
echo "Done. Review the added files, then commit:"
echo ""
echo "  git add .github/copilot-instructions.md .github/instructions .github/prompts .github/golden-prompts"
echo "  git commit -m \"chore: add Copilot instructions from MyBro\""
