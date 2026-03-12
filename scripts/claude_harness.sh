#!/usr/bin/env bash
set -euo pipefail

TIMEOUT_SECONDS="${CLAUDE_HARNESS_TIMEOUT_SECONDS:-600}"

if ! command -v claude >/dev/null 2>&1; then
  echo "BLOCKED:claude_cli_missing"
  echo "Fix: npm i -g @anthropic-ai/claude-code"
  exit 20
fi

if [[ "${1:-}" == "" ]]; then
  echo "BLOCKED:missing_prompt"
  echo "Usage: ./scripts/claude_harness.sh \"<task prompt>\""
  exit 21
fi

PROMPT="$1"
TMP_OUT="$(mktemp)"
trap 'rm -f "$TMP_OUT"' EXIT

# Run Claude Code with a hard timeout so Mira cannot hang the lane forever.
set +e
perl -e 'my $t=shift @ARGV; alarm($t); exec @ARGV;' "${TIMEOUT_SECONDS}" claude -p "${PROMPT}" >"${TMP_OUT}" 2>&1
STATUS=$?
set -e

if [[ ${STATUS} -eq 0 ]]; then
  cat "${TMP_OUT}"
  exit 0
fi

if grep -qiE "login|auth|unauthorized|not authenticated" "${TMP_OUT}"; then
  echo "BLOCKED:claude_auth_required"
  echo "Fix: run 'claude login' in terminal, then retry."
  exit 22
fi

if [[ ${STATUS} -eq 142 || ${STATUS} -eq 124 ]]; then
  echo "BLOCKED:claude_timeout"
  echo "Fix: retry with smaller task or set CLAUDE_HARNESS_TIMEOUT_SECONDS."
  exit 23
fi

echo "BLOCKED:claude_harness_error"
sed -n '1,60p' "${TMP_OUT}"
exit 24
