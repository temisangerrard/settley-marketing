#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
ENV_FILE="${ROOT_DIR}/.env"

if ! command -v xurl >/dev/null 2>&1; then
  echo "BLOCKED:xurl_missing"
  exit 10
fi

if [[ ! -f "${ENV_FILE}" ]]; then
  echo "BLOCKED:env_missing"
  exit 11
fi

username_from_whoami() {
  xurl whoami 2>/dev/null | perl -ne 'print "$1\n" if /"username"\s*:\s*"([^"]+)"/'
}

extract_env() {
  local key="$1"
  perl -ne "print \$1 if /^${key}=(.*)\$/" "${ENV_FILE}" | tail -n 1
}

is_target_user() {
  local got="${1:-}"
  [[ "${got}" == "mirasettley" ]]
}

current_user="$(username_from_whoami || true)"
if is_target_user "${current_user}"; then
  echo "OK:xurl_auth_valid username=${current_user}"
  exit 0
fi

X_API_ID="$(extract_env X_API_ID)"
X_API_SECRET="$(extract_env X_API_SECRET)"
X_ACCESS_TOKEN="$(extract_env X_ACCESS_TOKEN)"
X_ACCESS_SECRET="$(extract_env X_ACCESS_SECRET)"
X_BEARER_TOKEN="$(extract_env X_BEARER_TOKEN)"

if [[ -z "${X_API_ID}" || -z "${X_API_SECRET}" || -z "${X_ACCESS_TOKEN}" || -z "${X_ACCESS_SECRET}" || -z "${X_BEARER_TOKEN}" ]]; then
  echo "BLOCKED:x_env_vars_missing"
  exit 12
fi

xurl auth oauth1 \
  --consumer-key "${X_API_ID}" \
  --consumer-secret "${X_API_SECRET}" \
  --access-token "${X_ACCESS_TOKEN}" \
  --token-secret "${X_ACCESS_SECRET}" >/dev/null

xurl auth app --bearer-token "${X_BEARER_TOKEN}" >/dev/null

rechecked_user="$(username_from_whoami || true)"
if is_target_user "${rechecked_user}"; then
  echo "OK:xurl_auth_repaired username=${rechecked_user}"
  exit 0
fi

echo "BLOCKED:x_auth_invalid_or_revoked"
exit 13
