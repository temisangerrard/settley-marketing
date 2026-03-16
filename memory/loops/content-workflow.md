# Content Publishing Workflow — Master Reference

**Created:** 2026-03-15 (updated from 2026-03-14 directives)  
**Source:** Founder directive + memory/2026-03-14.md

---

## Workflow Order (STRICT)

```
┌─────────────────────────────────────────────────────────────┐
│  Step 1: CONTENT WRITTEN                                    │
│  Agent: Content Writer Agent                                │
│  Location: content/blog/ (output)                           │
│  Format: .md with frontmatter                               │
│  Target: 5 articles/week, 20/month                          │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│  Step 2: QA CHECK ⚠️ REQUIRED BEFORE PUBLISHING             │
│  Agent: QA Agent                                            │
│  Tool: tools/content_qa.py                                  │
│  Checks:                                                    │
│  - Legal disclaimer present                                 │
│  - CTA present                                              │
│  - Images use public URLs (not local paths)                 │
│  - Word count ≥800                                          │
│  - No template/QA language leaked                           │
│  - Overall score ≥70/100                                    │
│  Output: Pass → Proceed | Fail → Fix issues first           │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│  Step 3: PUBLISH TO API                                     │
│  Agent: Publishing Agent                                    │
│  Endpoint: POST https://settley.fly.dev/articles/create     │
│  Fields: title, content (HTML), status: published           │
│  Output: Article ID + URL                                   │
│  Checkpoint: memory/loops/article-publishing.md             │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│  Step 4: BACKLINK CREATION                                  │
│  Agent: Backlink Agent                                      │
│  Tactics: Blogger, Medium, LinkedIn, Quora                  │
│  Links TO: Published article URLs from Step 3               │
│  Output: Backlink URLs                                      │
│  Checkpoint: memory/loops/blogger-backlinks.md              │
└─────────────────────────────────────────────────────────────┘
```

---

## Agent Responsibilities

| Agent | Step | Tool | Checkpoint File | Status |
|-------|------|------|-----------------|--------|
| QA Agent | 2 | `tools/content_qa.py` | `memory/loops/qa-checks.md` | ⏸️ Not spawned |
| Publishing Agent | 3 | API POST + scripts | `memory/loops/article-publishing.md` | ✅ 9/9 done |
| Backlink Agent | 4 | Browser automation | `memory/loops/blogger-backlinks.md` | ⏳ 1/10 — Loop #2 ready |

---

## Key Rules (From 2026-03-14 Directive)

1. **Read blueprint first:** `content/templates/mira-article-blueprint.md`
2. **Use body-only template:** `content/templates/settley-article-body-only.html`
3. **Images:** Check `/assets/images` first before external stock
4. **Never leak template language:** No "template", "canonical", "QA", "Mira" in reader-facing copy
5. **QA before publish:** Do not publish articles that fail QA checks

---

## Current State (2026-03-15 11:30)

**Step 1 (Content):** ✅ 9 articles created in `content/blog/`  
**Step 2 (QA):** ⚠️ Not formally run — articles published without QA pass  
**Step 3 (Publish):** ✅ 9/9 articles published to API  
**Step 4 (Backlinks):** ⏳ 1/10 Blogger blogs created

**Gap:** QA should happen BEFORE publishing. For future articles, enforce Step 2 → Step 3 order.

---

## Agent Specs

- **Content-SEO Master:** `ops/agents/content-seo-master.md`
- **Publishing Agent:** `ops/agents/publishing-agent.md`
- **Backlink Agent:** `ops/agents/backlink-agent.md`
- **QA Agent:** [TO BE CREATED]

---

**Last Updated:** 2026-03-15 11:35 GMT  
**Next Review:** After QA Agent spec created
