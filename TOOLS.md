# TOOLS.md - Mira's Setup

## Channels & Credentials

### Email
- **Address:** mirasettley@gmail.com
- **Password:** Mirasettley52% (account password)
- **App Password:** hgtjqxdmaywxnfgj (stored in .env as GMAIL_APP_PASSWORD) — use this for IMAP/SMTP
- **Status:** ✅ Working — IMAP confirmed, 17 messages in inbox
- **Access method:** IMAP (imap.gmail.com:993) + SMTP (smtp.gmail.com:587)
- **Auth:** python3 imaplib with app password

### Twitter/X + LinkedIn
- **Twitter/X:** ✅ Direct API posting via `xurl` CLI (OAuth1 configured and verified)
- **Status:** Active and ready for posting
- **Verification command:** `xurl whoami` (must return `@mirasettley` before posting)
- **Post command:** `xurl post "text"`
- **Reply command:** `xurl reply <tweet_id> "text"`
- **Read command:** `xurl read <tweet_id>` (fetch tweet details)
- **Search command:** `xurl search "query" -n 20` (search tweets)
- **Timeline command:** `xurl timeline` (home timeline)
- **Mentions command:** `xurl mentions` (your mentions)
- **Like command:** `xurl like <tweet_id>`
- **Repost command:** `xurl repost <tweet_id>`
- **Follow command:** `xurl follow @username`
- **DM command:** `xurl dm @username "text"`
- **Proof requirement:** after posting, always return the live URL `https://x.com/mirasettley/status/<tweet_id>`
- **Execution owner:** Mira executes posting actions herself in-session via `exec` tool
- **LinkedIn:** Pending setup
- **Typefully:** ✅ API key active — stored in .env as TYPEFULLY_API_KEY — Twitter connected, use for scheduling/posting tweets

**Free tool priority:** Always use `xurl` CLI first (free, direct API). Only use Typefully for scheduling if needed.

### Tally Forms API
- **Account:** mirasettley@gmail.com (Mira Settley)
- **API Key:** tly-****************************Oirp (stored in .env as TALLY_API_KEY)
- **Status:** ✅ Working — can create and submit forms programmatically
- **Use Cases:** Lead capture forms, feedback collection, automated outreach tracking

### Telegram (Command Interface)
- **Bot Token:** in .env as TELEGRAM_BOT_TOKEN
- **Chat ID:** 795232660 (Temisan's)
- **Status:** ✅ Configured via openclaw
- **Runtime:** openclaw agent (node_modules/openclaw)

## LLM / AI
- **Primary:** OpenRouter → anthropic/claude-3.5-sonnet
- **Fallbacks:** openrouter/deepseek/deepseek-chat-v3-0324, ollama/qwen3-coder:30b
- **Heartbeat model:** ollama/qwen3-coder:30b (local, free)
- **OpenRouter Key:** in .env as OPENROUTER_API_KEY

### Claude Code Harness
- **Purpose:** Use Claude Code for deep reasoning / code-planning tasks when standard replies are drifting or shallow.
- **Command:** `./scripts/claude_harness.sh "<task>"`
- **Timeout:** default 180s (`CLAUDE_HARNESS_TIMEOUT_SECONDS` override)
- **Output contract:** if harness fails, return exact `BLOCKED:*` code from script; do not speculate.
- **When to use:** multi-step technical planning, debugging playbooks, and high-stakes execution checklists.

## Browser Automation

### PinchTab ✅
- **Status:** Installed 2026-03-09, running on port 9867
- **Purpose:** Token-efficient browser control for AI agents (12MB Go binary)
- **Key benefit:** 800 tokens/page vs 10K+ for screenshots (92% savings)
- **Commands:**
  - Start: `pinchtab` (background server)
  - Navigate: `pinchtab nav https://example.com`
  - Snapshot: `pinchtab snap -i -c` (interactive elements)
  - Extract text: `pinchtab text` (token-efficient)
  - Click: `pinchtab click e5`
  - Fill: `pinchtab fill e3 "text"`
- **Health check:** `curl http://localhost:9867/health`
- **Scripts:** `scripts/monitor-lofty.sh` (automated competitor tracking)
- **Docs:** `/ops/tools/pinchtab-setup.md`
- **Use cases:** Competitor monitoring, investor research, Arena Agent data collection

## Workspace
- **Repo:** https://github.com/temisangerrard/settley-marketing
- **Local path:** /Users/temisan/Downloads/settley-marketing
- **Obsidian vault:** /Users/temisan/Downloads/settley-marketing/vault

## Pending Setup
- [x] Gmail App Password ✅
- [x] Typefully API key ✅
- [x] Tally API key ✅
- [ ] LinkedIn OAuth token (direct posting)

## Error Recovery Playbook (Mira)

When a tool call fails, use this exact sequence and report `DONE` or `BLOCKED:<reason>`.

### 1) X posting failures

- Symptom: `Tool xurl not found`
  - Fix: never call a `xurl` tool directly; call shell via `exec`:
    - `xurl whoami`
    - `xurl post "<tweet text>"`
  - Before every post, run:
    - `./scripts/xurl_preflight.sh`
    - If output starts with `BLOCKED:`, stop and return that exact blocker.

- Symptom: `403 Forbidden` on `xurl post`
  - Fix sequence:
    1. `xurl auth status`
    2. If oauth1/bearer missing, load from `.env` and re-auth:
       - `xurl auth oauth1 --consumer-key "$X_API_ID" --consumer-secret "$X_API_SECRET" --access-token "$X_ACCESS_TOKEN" --token-secret "$X_ACCESS_SECRET"`
       - `xurl auth app --bearer-token "$X_BEARER_TOKEN"`
    2b. Do NOT use `xurl auth login --env` (invalid command in this setup).
    3. Verify: `xurl whoami` must return `@mirasettley`
    4. Retry post.
  - If still forbidden: `BLOCKED:x_api_scope_or_account_permissions`

- Symptom: `401 Unauthorized` on `xurl whoami` or `xurl post`
  - Fix sequence:
    1. Re-apply OAuth1 + bearer from environment values (do not print secrets).
    2. Verify with `xurl whoami` and require `username: "mirasettley"`.
    3. Retry `xurl post`.
  - If still unauthorized: `BLOCKED:x_auth_invalid_or_revoked`

X identity and scope sanity checks:
- Canonical account must be `@mirasettley` (from `xurl whoami`).
- If any response says another handle (e.g., `@miraforsettley`), treat as hallucination and re-run `xurl whoami`.
- `xurl whoami` does not print scopes; do not infer scope names from it.
- Scope/credential discussion must be grounded in raw `xurl auth status` output only.
- Never use `read .env` in chat flow and never echo API keys in replies/tool output.

- Output contract after successful post:
  - raw `xurl post` JSON
  - final URL `https://x.com/mirasettley/status/<id>`

Safe helper:
- Use `./scripts/xurl_preflight.sh` to verify/repair auth without exposing keys.

### 2) Typefully failures

- Symptom: `command not found: typefully`
  - Fix: use the script already wired in this machine:
    - `node .agents/skills/typefully/scripts/typefully.js ...`
  - If script missing: `BLOCKED:typefully_script_missing`

### 3) Browser failures

- Symptom: `browser failed: HTTP 404`
  - Fix:
    1. verify relay: `openclaw status --all`
    2. verify ports: gateway `18790`, browser relay `18792`
    3. verify extension token matches `gateway.auth.token`
  - If mismatch persists: `BLOCKED:browser_relay_misconfigured`

### 4) Cron job failures

- Symptom: `unknown cron job id`
  - Fix: `openclaw cron list --json`, then use the real `id` from output.

### 5) Non-negotiable execution rule

- Never claim action complete without tool proof from this run.
- If no proof, return `NOT EXECUTED` or `BLOCKED:<exact_reason>`.

## Skill Discovery Protocol

Use this protocol when a task needs a capability that appears missing.

1. Identify failure trigger:
- `command not found`
- `Tool <name> not found`
- unknown command/flag behavior

2. Discover available capabilities:
- `openclaw skills list`
- `openclaw skills check`
- `openclaw docs "<task> skill"`
- `openclaw docs "<tool>"`
- Treat `<available_skills>` text in prompt as a hint, not ground truth; runtime truth is `openclaw skills list`.

3. Resolve:
- If a skill/tool exists, use it in the same run.
- If missing, append incident + required capability to `memory/tool-registry.md`.
- Return `BLOCKED:missing_skill_or_tool` with exact requirement.
