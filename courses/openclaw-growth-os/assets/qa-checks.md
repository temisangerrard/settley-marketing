# QA Agent — Checkpoint Tracker

**Agent:** QA Agent  
**Parent:** Content-SEO Master Agent  
**Mission:** QA all content BEFORE publishing (Step 2 of workflow)  
**Started:** 2026-03-15 (retroactive QA on published articles)

---

## Progress

### Retroactive QA (9 Published Articles)

| File | Score | Status | Issues | Fixed? |
|------|-------|--------|--------|--------|
| tokenized-real-estate-uk-guide-2026.html | ⏳ PENDING | - | - | - |
| how-tokenization-works-interactive-v3.html | ⏳ PENDING | - | - | - |
| 5-ways-invest-property-without-mortgage.html | ⏳ PENDING | - | - | - |
| settley-vs-lofty.md | ⏳ PENDING | - | - | - |
| lofty-alternatives-ranked.md | ⏳ PENDING | - | - | - |
| what-is-tokenized-real-estate.md | ⏳ PENDING | - | - | - |
| lofty-alternative-europe.md | ⏳ PENDING | - | - | - |
| 2024-02-20-real-estate-tokenization-liquidity.md | ⏳ PENDING | - | - | - |
| 2024-02-20-tokenized-real-estate-uk.md | ⏳ PENDING | - | - | - |

**Status:** ⏳ NOT STARTED — awaiting first QA loop

---

## Ongoing QA Queue (New Content)

| File | Added Date | Priority | QA Status |
|------|------------|----------|-----------|
| [monitoring for new files] | - | - | - |

**Rule:** All new content must pass QA BEFORE publishing.

---

## Agent Spec
- **Location:** `ops/agents/qa-agent.md`
- **Loop Size:** ~5 min per 5 articles
- **Tool:** `tools/content_qa.py`
- **Pass Threshold:** ≥70/100, no critical issues

---

## Loop #1 Plan (Retroactive Sweep)

**Task:** QA all 9 published articles (retroactive check)

**Steps:**
1. Run `python3 content_qa.py scan ../content/blog/`
2. Parse scores and issues
3. Auto-fix critical issues (disclaimer, CTA, image paths)
4. Flag articles needing manual review
5. Report results to master agent

**Expected Output:**
- X articles pass (no action needed)
- Y articles need auto-fixes
- Z articles need manual review

---

**Last Updated:** 2026-03-15 11:40 GMT  
**Next Action:** Spawn QA Agent for Loop #1 (retroactive sweep)
