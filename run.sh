#!/bin/bash
# Mira - OpenClaw-powered Marketing Cofounder
# All data stays in this folder

# Get script directory (Mira's workspace)
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Keep ALL OpenClaw data local to this folder
export OPENCLAW_CONFIG_PATH="$SCRIPT_DIR/.openclaw/openclaw.json"
export OPENCLAW_STATE_DIR="$SCRIPT_DIR/.openclaw"
export OPENCLAW_DATA_DIR="$SCRIPT_DIR/.openclaw"
export OPENCLAW_PLUGINS_DIR="$SCRIPT_DIR/.openclaw/plugins"
export OPENCLAW_CREDENTIALS_DIR="$SCRIPT_DIR/.openclaw/credentials"
# Do not hardcode a gateway token here.
# OpenClaw will use the token from .openclaw/openclaw.json.
unset OPENCLAW_GATEWAY_TOKEN

# Create necessary directories
mkdir -p "$SCRIPT_DIR/.openclaw/agents/main/sessions"
mkdir -p "$SCRIPT_DIR/.openclaw/credentials"
mkdir -p "$SCRIPT_DIR/.openclaw/plugins"

# Secure the config
chmod 600 "$SCRIPT_DIR/.openclaw/openclaw.json" 2>/dev/null

# Load local .env if exists
if [ -f "$SCRIPT_DIR/.env" ]; then
    set -a
    source "$SCRIPT_DIR/.env"
    set +a
fi

# Run openclaw from local node_modules
exec "$SCRIPT_DIR/node_modules/.bin/openclaw" "$@"
