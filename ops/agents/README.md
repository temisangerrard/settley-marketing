# Content & SEO Agent System

**Created:** 2026-03-15  
**Architect:** Mira (Settley Growth)  
**Status:** ACTIVE — ready to deploy

---

## Overview

Autonomous agent system for content publication and SEO backlink acquisition. Agents execute in Ralph loops, checkpoint progress, and report to Mira daily.

**Philosophy:** Mira orchestrates, agents execute. Scale output without linear time investment.

---

## Agent Hierarchy

```
┌─────────────────────────────────────┐
│         Mira (Human Overseer)       │
│  - Sets strategy                    │
│  - Reviews daily reports            │
│  - Unblocks issues                  │
└─────────────────┬───────────────────┘
                  │
                  ▼
┌─────────────────────────────────────┐
│    Content-SEO Master Agent         │
│  - Coordinates sub-agents           │
│  - Daily reports to Mira            │
│  - Priority queue management        │
└─────────┬─────────────────┬─────────┘
          │                 │
          ▼                 ▼
┌──────────────────┐  ┌──────────────────┐
│ Publishing Agent │  │  Backlink Agent  │
│ - Publish to API │  │ - Blogger blogs  │
│ - 1 article/loop │  │ - 1 blog/loop    │
│ - ~2 min/loop    │  │ - ~10 min/loop   │
└──────────────────┘  └──────────────────┘
```

---

## Agents

### 1. Content-SEO Master Agent
**Spec:** `ops/agents/content-seo-master.md`  
**Role:** Orchestrator and reporter  
**Responsibilities:**
- Coordinate sub-agents
- Daily reports to Mira (20:00 GMT)
- Priority queue management
- Escalate blockers

### 2. Publishing Agent
**Spec:** `ops/agents/publishing-agent.md`  
**Role:** Article publication  
**Target:** All files in `content/blog/` published to API  
**Loop:** 1 article per loop (~2 min)  
**Checkpoint:** `memory/loops/article-publishing.md`  
**Status:** ✅ DONE (9/9 articles published)

### 3. Backlink Agent
**Spec:** `ops/agents/backlink-agent.md`  
**Role:** SEO backlink acquisition  
**Target:** 10 Blogger blogs in 30 days  
**Loop:** 1 blog per loop (~10 min)  
**Checkpoint:** `memory/loops/blogger-backlinks.md`  
**Status:** ⏳ 1/10 complete — ready for Loop #2

---

## How to Deploy

### Spawn Master Agent
```
sessions_spawn with:
  task: "You are the Content-SEO Master Agent. Read ops/agents/content-seo-master.md and begin coordinating sub-agents. Start with Backlink Agent Loop #2 (Blogger blogs). Report daily at 20:00 GMT."
  mode: "session"
  runtime: "subagent"
  label: "content-seo-master"
```

### Spawn Individual Agent
```
sessions_spawn with:
  task: "You are the Backlink Agent. Read ops/agents/backlink-agent.md. Execute Loop #2 now (create Blogger blog #2). Use Ralph loop protocol. Checkpoint in memory/loops/blogger-backlinks.md"
  mode: "session"
  runtime: "subagent"
  label: "backlink-agent"
```

---

## Ralph Loop Protocol

**All agents follow this protocol:**

1. **Read checkpoint** before starting
2. **Execute one atomic task** (1 article, 1 backlink, etc.)
3. **Log evidence** (URLs, IDs, counts)
4. **Write checkpoint** with:
   - What was completed
   - Next task
   - Status (CONTINUE / DONE / BLOCKED)
5. **Report** to master agent or Mira

**Loop Size Guidelines:**
- Publishing: ~2 min per article
- Backlinks: ~10 min per blog
- QA: ~5 min per 5 articles
- Monitoring: ~3 min per day

---

## Reporting

### Daily Report (Master → Mira)
**Time:** 20:00 GMT  
**Channel:** Telegram (sessions_send)  
**Format:**
```markdown
## Content/SEO Daily Report — [DATE]

### Publishing
- Published: X articles
- Pending: Y articles
- Blocked: Z articles

### Backlinks
- Created: X backlinks
- Target: Y/week
- Progress: X/Y (Z%)

### QA
- Checked: X articles
- Passed: Y
- Failed: Z

### Blockers
- [none / list]

### Next 24h
- [planned actions]
```

### Blocker Alerts (Immediate)
**Trigger:** Any P1 blocker  
**Format:**
```
🚨 BLOCKER: [description]

**Impact:** [what's blocked]
**Need:** [what's required]
**Context:** [details]
```

---

## Checkpoint Files

All agents write to `memory/loops/`:

| File | Agent | Purpose |
|------|-------|---------|
| `article-publishing.md` | Publishing Agent | Track published articles |
| `blogger-backlinks.md` | Backlink Agent | Track backlink creation |
| `qa-checks.md` | QA Agent | Track QA scores |
| `seo-monitoring.md` | Monitoring Agent | Track performance metrics |

**Checkpoint Format:**
```markdown
## [Agent] Loop #X

**Task:** [what was attempted]

**Result:**
- [outcomes with evidence]

**Next Loop:**
- [specific next task]

**Status:** CONTINUE / DONE / BLOCKED:[reason]
```

---

## Pipeline Documentation

Supporting docs in `ops/seo/`:

| File | Purpose |
|------|---------|
| `blogger-backlink-pipeline.md` | Full SOP for Blogger backlinks |
| `[future]` | Medium pipeline, guest posting, etc. |

---

## Kill Switches

**Mira can halt operations by:**
1. Send "PAUSE" — all agents stop
2. Send "STOP [agent]" — specific agent halted
3. Send "RESET" — clear checkpoints, fresh start

**Agents auto-halt if:**
- 3 consecutive loop failures
- API auth errors (401/403)
- Browser automation fails 3x
- No response to blocker for 24h

---

## Current Status (2026-03-15 11:30)

| Agent | Status | Progress | Next Action |
|-------|--------|----------|-------------|
| Publishing | ✅ DONE | 9/9 articles | Monitor for new content |
| Backlink | ⏳ ACTIVE | 1/10 blogs | Loop #2 (Blogger blog #2) |
| QA | ⏸️ IDLE | 0 checks | Await spawn |
| Monitoring | ⏸️ IDLE | 0 checks | Await spawn |

**Ready to spawn:** Master Agent or Backlink Agent for Loop #2

---

## Scaling Plan

**Phase 1 (Week 1-2):**
- ✅ Publishing Agent (9 articles done)
- 🔄 Backlink Agent (1/10, continue to 10)
- ⏳ QA Agent (audit published articles)

**Phase 2 (Week 3-4):**
- Monitoring Agent (track rankings/traffic)
- Medium pipeline (if Blogger effective)
- Content refresh loop (update old articles)

**Phase 3 (Month 2+):**
- Guest posting pipeline
- Competitor monitoring
- Keyword research agent

---

**Owner:** Mira (Settley Growth)  
**Last Updated:** 2026-03-15 11:30 GMT  
**Next Review:** 2026-03-22 (weekly)
