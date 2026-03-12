# ACP Agent Spec: SEO Content Writer

**Purpose:** Delegate SEO article research and writing to Claude Code or Codex via ACP harness.

**Orchestrator:** Mira (main session)
**Executor:** Claude Code or Codex (ACP session)

---

## When to Use

- Weekly SEO articles (Tuesday cron)
- Landing page copy
- Competitor comparison pages
- Technical documentation
- Long-form educational content (1500+ words)

---

## Spawn Command (Claude Code)

```bash
./scripts/claude_harness.sh "Write 2000-word SEO article on 'tokenized real estate UK'. 

Task breakdown:
1. Research: Search for top 10 ranking pages for 'tokenized real estate UK', 'fractional property investment UK'
2. Analyze: What keywords, structure, and angles do competitors use?
3. Differentiate: What gaps can Settley fill? (UK-focused, compliance-first, £500 entry)
4. Write: 1500-2500 words, educational tone, specific data points
5. Save: content/blog/tokenized-real-estate-uk-guide.md
6. Commit: git add + commit with descriptive message
7. Report: Keyword targeted, search intent, why chosen, file path, commit SHA

Guardrails:
- Never claim completion without verification
- If blocked: state exact dependency needed
- Educational > promotional (80/20 rule)
- UK audience focus (GBP, UK regulations, UK cities)
- Include Settley mention only where natural"
```

---

## Spawn Command (Codex)

```bash
codex --sandbox --output-format markdown "Write 2000-word SEO article on 'tokenized real estate UK'.

Task breakdown:
1. Research: Search for top 10 ranking pages for 'tokenized real estate UK', 'fractional property investment UK'
2. Analyze: What keywords, structure, and angles do competitors use?
3. Differentiate: What gaps can Settley fill? (UK-focused, compliance-first, £500 entry)
4. Write: 1500-2500 words, educational tone, specific data points
5. Save: content/blog/tokenized-real-estate-uk-guide.md
6. Commit: git add + commit with descriptive message
7. Report: Keyword targeted, search intent, why chosen, file path, commit SHA

Guardrails:
- Never claim completion without verification
- If blocked: state exact dependency needed
- Educational > promotional (80/20 rule)
- UK audience focus (GBP, UK regulations, UK cities)
- Include Settley mention only where natural"
```

---

## Via OpenClaw sessions_spawn (Recommended)

```javascript
sessions_spawn({
  runtime: "acp",
  agentId: "claude-code",  // or "codex"
  mode: "run",             // one-shot
  thread: false,           // no Discord thread needed
  task: `Write 2000-word SEO article on 'tokenized real estate UK'.

Task breakdown:
1. Research: Search for top 10 ranking pages for 'tokenized real estate UK', 'fractional property investment UK'
2. Analyze: What keywords, structure, and angles do competitors use?
3. Differentiate: What gaps can Settley fill? (UK-focused, compliance-first, £500 entry)
4. Write: 1500-2500 words, educational tone, specific data points
5. Save: content/blog/tokenized-real-estate-uk-guide.md
6. Commit: git add + commit with descriptive message
7. Report: Keyword targeted, search intent, why chosen, file path, commit SHA

Guardrails:
- Never claim completion without verification
- If blocked: state exact dependency needed
- Educational > promotional (80/20 rule)
- UK audience focus (GBP, UK regulations, UK cities)
- Include Settley mention only where natural`,
  runTimeoutSeconds: 600,  // 10 min max
  streamTo: "parent"       // stream output to Mira's session
})
```

---

## Output Contract

**On completion, ACP agent must report:**
1. **File path:** `content/blog/<slug>.md`
2. **Git commit SHA:** `abc1234...`
3. **Keyword targeted:** Exact phrase
4. **Search intent:** Informational / Commercial / Transactional
5. **Word count:** Actual count
6. **Status:** `DONE`, `BLOCKED:<reason>`, or `UNVERIFIED`

**Mira verifies:**
- File exists at path
- Git commit exists
- Content quality check (educational, UK-focused, no hype)

---

## Orchestrator Workflow (Mira)

1. **Intake:** Receive SEO topic from content calendar or keyword research
2. **Spawn:** Call `sessions_spawn` with ACP runtime + full task spec
3. **Monitor:** Check progress via `subagents(action="list")` if long-running
4. **Verify:** On completion, verify file + commit exist
5. **Deliver:** Report to Temisan with file path, commit SHA, keyword, and preview

---

## Error Handling

| Error | Action |
|-------|--------|
| `BLOCKED:missing_api_key` | Mira: Add key to .env, retry |
| `BLOCKED:network_failure` | Mira: Retry with backoff, or switch to other agent |
| `timeout` | Mira: Check if partial work done, spawn with longer timeout |
| `context_overflow` | Mira: Split task into research + writing phases |

---

## Reusable Templates

### Template: Competitor Analysis
```
Analyze [competitor_name] for SEO strategy:
1. Crawl: homepage, features, pricing, blog, top 5 articles
2. Extract: target keywords, content structure, CTAs
3. Identify: content gaps we can exploit
4. Report: 10-bullet summary + 3 action recommendations for Settley
Save to: research/competitors/[competitor]-analysis-[date].md
```

### Template: Landing Page Copy
```
Write landing page copy for [page_name]:
1. Audience: [UK/US property investors, age X-Y, income Z]
2. Value prop: [specific benefit]
3. Tone: Educational, direct, no hype
4. Sections: Hero, Problem, Solution, How It Works, Social Proof, CTA
5. SEO: Target keyword [keyword], include in H1, meta description
Save to: content/pages/[slug].md
```

### Template: Blog Post
```
Write [word_count]-word blog post on [topic]:
1. Keyword: [primary keyword]
2. Secondary keywords: [list 3-5]
3. Audience: [UK/US investors]
4. Structure: Introduction, Problem, Solution, Data/Proof, CTA
5. Include: Specific stats, Settley mention (natural), internal links
Save to: content/blog/[slug].md
```

---

**Last Updated:** 2026-03-12
**Owner:** Mira, Founder Operating Partner
