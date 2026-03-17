# My Complete Tool Inventory — No Excuses

**Audit Date:** 2026-03-17 01:10 GMT  
**Purpose:** Every tool I have access to. No researching new tools. EXECUTE with these.

---

## ✅ READY TO USE (Configured & Working)

### Communication / Outreach

| Tool | What It Does | Status | Use For |
|------|--------------|--------|---------|
| **xurl** | Twitter/X API CLI | ✅ OAuth1 configured | Post tweets, reply, DM, search, timeline |
| **himalaya** | Email CLI (IMAP/SMTP) | ✅ Gmail configured | Read/send emails, investor outreach |
| **message** | Telegram bot | ✅ Configured | Send messages to Temisan |
| **Tally API** | Form builder | ✅ API key in .env | UK waitlist landing page |

**Commands I Use Daily:**
```bash
# Twitter
xurl whoami  # Verify account
xurl post "tweet text"  # Post tweet
xurl dm @username "message"  # Send DM
xurl search "query" -n 20  # Search tweets

# Email
himalaya envelope list --page-size 20  # List emails
himalaya message read <id>  # Read email
# Send via python3 smtplib (app password in .env)

# Tally
curl -X POST https://api.tally.so/forms/<id>/responses \
  -H "Authorization: Bearer <TALLY_API_KEY>" \
  -H "Content-Type: application/json" \
  -d '{"data": {...}}'
```

---

### Content Creation

| Tool | What It Does | Status | Use For |
|------|--------------|--------|---------|
| **visualise** | Inline SVG/HTML diagrams | ✅ Installed | Article visuals, interactive content |
| **OpenRouter API** | LLM access (Claude, etc.) | ✅ API key in .env | Content drafting, research |
| **Claude Code Harness** | Deep reasoning via Claude | ✅ Script exists | Technical planning, complex tasks |

**Commands:**
```bash
# Claude Code for complex tasks
./scripts/claude_harness.sh "<task>"

# Visualise skill (automatic via OpenClaw)
# Just ask for diagrams/visuals in prompts
```

---

### Browser Automation

| Tool | What It Does | Status | Use For |
|------|--------------|--------|---------|
| **PinchTab** | Browser control (token-efficient) | ✅ Running on port 9867 | Competitor monitoring, web research |
| **browser** | OpenClaw browser tool | ✅ Configured | Web automation, snapshots |

**Commands:**
```bash
# PinchTab
pinchtab nav https://example.com
pinchtab snap -i -c  # Snapshot interactive elements
pinchtab text  # Extract text

# Health check
curl http://localhost:9867/health
```

---

### Content Pipeline (My Own Agents)

| Agent | What It Does | Status | Use For |
|-------|--------------|--------|---------|
| **Content Writer Agent** | Drafts SEO articles | ✅ Cron at 11:00 GMT | 5 articles/week |
| **QA Agent** | Quality-checks content | ✅ Cron at 09:00 GMT | Pre-publish QA |
| **Publishing Agent** | Publishes to API | ✅ On-demand | API publishing |
| **Backlink Agent** | Creates Blogger backlinks | ✅ Cron at 14:00 GMT | 1 backlink/day |
| **Content-SEO Master** | Orchestrates all agents | ✅ Cron at 20:00 GMT | Daily reports |

**Checkpoint Files:**
- `memory/loops/content-writing.md`
- `memory/loops/qa-checks.md`
- `memory/loops/article-publishing.md`
- `memory/loops/blogger-backlinks.md`

---

### Developer Tools

| Tool | What It Does | Status | Use For |
|------|--------------|--------|---------|
| **npm/npx** | Node.js package manager | ✅ Installed | Installing tools |
| **python3** | Python runtime | ✅ Installed | Scripts, automation |
| **git** | Version control | ✅ Configured | Commits, pushes |
| **curl** | HTTP requests | ✅ Installed | API calls |
| **jq** | JSON parser | ✅ Installed | Parsing API responses |

---

### OpenClaw Native Tools

| Tool | What It Does | Status | Use For |
|------|--------------|--------|---------|
| **sessions_spawn** | Spawn sub-agents | ✅ Available | Delegate tasks to specialized agents |
| **subagents** | Manage spawned agents | ✅ Available | List, steer, kill sub-agents |
| **cron** | Manage cron jobs | ✅ Available | Schedule automated tasks |
| **memory_search** | Search memory files | ✅ Available | Recall prior work |
| **web_search** | Brave Search API | ✅ Available | Web research |
| **web_fetch** | Fetch URL content | ✅ Available | Extract article text |
| **exec** | Run shell commands | ✅ Available | Any CLI tool |
| **process** | Manage background processes | ✅ Available | Long-running commands |
| **read/write/edit** | File operations | ✅ Available | Read/write files |

---

### Skills Available (59/88 Ready)

**Ready Skills (✓):**
- 🔐 1password
- 📦 clawhub
- 🧩 coding-agent
- ♊️ gemini
- 📦 gh-issues
- 🐙 github
- 📧 gog (Google Workspace)
- 🏥 healthcheck
- 📧 himalaya
- 📱 imsg (iMessage)
- 🔧 mcporter (MCP servers)
- 📊 model-usage
- 📄 nano-pdf
- 📓 obsidian
- 📝 session-logs
- 🎯 skill-creator
- 📝 summarize
- 📋 things-mac
- 🎥 video-frames
- 🌤️ weather
- 🐦 xurl

**Missing Skills (✗) — NOT USING:**
- apple-notes, apple-reminders, bear-notes, blogwatcher, blucli, bluebubbles, camsnap, discord, eightctl, gifgrep, openhue, oracle, sag, sherpa-onnx-tts, slack, songsee, sonoscli, spotify-player, tmux, trello, voice-call, wacli

**Rule:** If it's ✗ missing, I DON'T research or install it. Use what's ✓ ready.

---

## 🎯 Tools for My 3 Tracks (March 17-30)

### Track 1: Autobett Marketing

| Tool | How I Use It | Daily Target |
|------|--------------|--------------|
| **xurl** | Post 3-5 tweets, send 10 DMs | 15 actions/day |
| **Discord** (manual) | Engage in 5 gaming servers | 5 engagements/day |
| **Reddit** (manual) | Post/comment in 3 subs | 3 posts/day |
| **web_search** | Research gaming communities | 10 min/day |

**No new tools needed.**

---

### Track 2: Gumroad Course Launch

| Tool | How I Use It | Daily Target |
|------|--------------|--------------|
| **Loom/OBS** (install if needed) | Record course videos | 2 hours/day |
| **Gumroad** (web) | Upload videos, configure page | 4 hours (Day 6-7) |
| **xurl** | Promote course on Twitter | 3 tweets/day |
| **himalaya** | Email interested leads | 10 emails/day |
| **message** | Send progress updates | Daily at 20:00 |

**No new tools needed.**

---

### Track 3: Settley Growth

| Tool | How I Use It | Daily Target |
|------|--------------|--------------|
| **Tally** | UK waitlist landing page | Launch Day 1-2 |
| **Canva** (web) | PDF lead magnet design | 2 hours (Day 1) |
| **himalaya** | Investor outreach emails | 5 emails/day |
| **xurl** | Share content on Twitter | 3 tweets/day |
| **web_search** | Find investor contacts | 20 min/day |
| **message** | Customer interview scheduling | 1 interview/day |

**No new tools needed.**

---

## 🚫 Tools I Will NOT Research (Rule #6)

| Tool | Why I'm Skipping |
|------|------------------|
| **Context Hub (chub)** | Not needed for current tracks |
| **SkillGrade** | Tool research = procrastination |
| **Hermes Agent** | Distraction from execution |
| **DeepAgents** | Already have OpenClaw |
| **Cofounder 2** | Not relevant to current priorities |
| **Any new tool** | If it's not in this list, I'm NOT using it |

**Rule:** Use existing tools for 14 days. Re-evaluate April 1.

---

## 📋 Daily Tool Usage Checklist

**Every morning (09:00):**
```
□ xurl whoami (verify Twitter access)
□ himalaya envelope list (check emails)
□ Review yesterday's progress in memory/loops/
```

**Every day (execution):**
```
□ xurl post (3-5 Autobett tweets)
□ xurl dm (10 gaming/AI accounts)
□ himalaya (5 investor emails)
□ Tally (UK waitlist promotion)
□ sessions_spawn or subagents (if delegating)
□ exec (any CLI commands needed)
```

**Every evening (20:00):**
```
□ message (send progress report to Temisan)
□ Update memory/loops/ with checkpoints
□ Commit to git if files changed
```

---

## 🔧 Tool Troubleshooting (No Excuses)

### If xurl fails:
```bash
# Check auth
xurl auth status
xurl whoami

# Re-auth if needed
xurl auth oauth1 --consumer-key "$X_API_KEY" --consumer-secret "$X_API_SECRET" --access-token "$X_ACCESS_TOKEN" --token-secret "$X_ACCESS_SECRET"

# Use preflight script
./scripts/xurl_preflight.sh
```

### If himalaya fails:
```bash
# Check config
himalaya account list

# Test inbox
himalaya envelope list --page-size 5
```

### If cron jobs fail:
```bash
# List all cron jobs
openclaw cron list --json

# Check specific job
openclaw cron runs --jobId <id>
```

### If browser fails:
```bash
# Check PinchTab
curl http://localhost:9867/health

# Check OpenClaw browser
openclaw status --all
```

**No "I can't" excuses. Fix or work around.**

---

## 📊 Tool ROI Tracking

**Every Friday, I'll report:**

| Tool | Times Used | Outcome | Keep Using? |
|------|------------|---------|-------------|
| xurl | X times | Y followers, Z DMs | Yes/No |
| himalaya | X times | Y emails, Z replies | Yes/No |
| Tally | X times | Y signups | Yes/No |
| ... | ... | ... | ... |

**If a tool isn't driving outcomes, I stop using it.**

---

## Commitment

**I commit to:**
- Using ONLY tools in this inventory for 14 days (March 17-30)
- Zero tool research (no Context Hub, SkillGrade, Hermes, DeepAgents)
- Fixing tool issues within 1 hour (not using as excuse)
- Reporting tool usage in daily progress updates

**If I need a tool that's not listed:**
1. Check if it's in ✗ missing skills (don't install)
2. Check if existing tool can do it (usually yes)
3. If truly blocked, document in daily report (not as excuse, as data)

---

**Inventory Created:** 2026-03-17 01:10 GMT  
**Valid Through:** March 30, 2026 (14 days)  
**Owner:** Mira, Founder Operating Partner

**No more "I can't because I don't have X tool." I have everything I need.**
