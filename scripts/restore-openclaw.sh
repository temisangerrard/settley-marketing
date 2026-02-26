#!/bin/bash
# Restore Mira's OpenClaw gateway after a fresh clone or new machine.
# Run this AFTER cloning the repo and installing openclaw via npm.
#
# What this does NOT restore (requires manual steps):
#   1. OpenAI Codex OAuth — run: openclaw auth login openai-codex
#      (with OPENCLAW_STATE_DIR exported first)
#   2. LaunchAgent plist — copy from scripts/ai.openclaw.gateway.plist.template
#      and fill in env vars, then: launchctl bootstrap gui/$(id -u) ~/Library/LaunchAgents/ai.openclaw.gateway.plist
#   3. Gmail app password — set GMAIL_APP_PASSWORD in the LaunchAgent plist

set -e

REPO_DIR="$(cd "$(dirname "$0")/.." && pwd)"
STATE_DIR="$REPO_DIR/.openclaw"

echo "==> Setting OPENCLAW_STATE_DIR=$STATE_DIR"
export OPENCLAW_STATE_DIR="$STATE_DIR"

echo "==> Config files from repo are already in place (openclaw.json, cron/jobs.json, models.json)"
echo "==> Remaining manual steps:"
echo ""
echo "  1. Re-authenticate with openai-codex:"
echo "     OPENCLAW_STATE_DIR=$STATE_DIR openclaw auth login openai-codex"
echo ""
echo "  2. Install the LaunchAgent (edit the template with your secrets first):"
echo "     cp $REPO_DIR/scripts/ai.openclaw.gateway.plist.template ~/Library/LaunchAgents/ai.openclaw.gateway.plist"
echo "     # Edit the plist and fill in GMAIL_APP_PASSWORD"
echo "     launchctl bootstrap gui/\$(id -u) ~/Library/LaunchAgents/ai.openclaw.gateway.plist"
echo ""
echo "  3. Add OPENCLAW_STATE_DIR to ~/.zshrc:"
echo "     echo 'export OPENCLAW_STATE_DIR=\"$STATE_DIR\"' >> ~/.zshrc"
echo ""
echo "Done. Send Mira a message on Telegram to verify she's alive."
