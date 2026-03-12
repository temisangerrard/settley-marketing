# Tool Registry

Purpose: single source of truth for discovered tools/skills, known-good commands, and gaps.

## Known Good (2026-03-08)
- xurl
  - Verify identity: `xurl whoami`
  - Post: `xurl post "<text>"`
- OpenClaw skills
  - List: `openclaw skills list`
  - Check readiness: `openclaw skills check`
- OpenClaw docs search
  - `openclaw docs "<query>"`

## Discovery Log
- 2026-03-08: Added discovery protocol. Use this file to append missing-tool incidents and resolution commands.

## Missing / Follow-up
- Add verified Typefully execution path entries after next successful run.

- 2026-03-08: Incident - `pip` command not found (per .openclaw/logs/gateway-launchd.log line 1683 on 2026-03-07T17:11Z)
  - Discovery commands: `openclaw docs "pip skill"`
  - Resolution: NOT RESOLVED. Need Homebrew/pyenv pip shim or use `python3 -m pip` fallback; document before next pip usage.
- 2026-03-08: Incident - unknown cron job id `mira-post-owner-sync` (log line 2416 on 2026-03-08T12:41Z)
  - Discovery commands: `openclaw docs "unknown cron job id"`
  - Resolution: NOT RESOLVED. Need to audit `openclaw cron list` before invoking `cron.run` to verify ID or recreate job.
- 2026-03-08: Incident - `typefully` command not found (log line 2444 on 2026-03-08T13:01Z)
  - Discovery commands: `openclaw docs "typefully skill"`
  - Resolution: Pending. Use Typefully skill script (`node .agents/skills/typefully/scripts/typefully.js ...`) per TOOLS.md; add Verified path after next run.
- 2026-03-08: Incident - `find-skills` command not found (log line 2457 on 2026-03-08T13:28Z)
  - Discovery commands: `openclaw docs "find-skills"`
  - Resolution: NOT RESOLVED. Need to confirm invocation method (likely via SKILL instructions rather than CLI); document correct usage.
