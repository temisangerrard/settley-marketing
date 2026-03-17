# QA Agent — Checkpoint Tracker

**Agent:** QA Agent  
**Parent:** Content-SEO Master Agent  
**Mission:** QA all content BEFORE publishing (Step 2 of workflow)  
**Started:** 2026-03-15 (retroactive QA on published articles)

---

## Progress

### Retroactive QA (11 Articles) — COMPLETE ✅

| File | Score | Status | Issues | Fixed? |
|------|-------|--------|--------|--------|
| tokenized-real-estate-uk-guide-2026.html | 91.0/100 | ✅ PASS | missing CTA | ✅ Auto-fixed |
| how-tokenization-works-interactive-v3.html | 93.4/100 | ✅ PASS | missing CTA | ✅ Auto-fixed |
| 5-ways-invest-property-without-mortgage.html | 91.0/100 | ✅ PASS | missing CTA | ✅ Auto-fixed |
| settley-vs-lofty.md | 91.0/100 | ✅ PASS | missing disclaimer, CTA | ✅ Auto-fixed |
| lofty-alternatives-ranked.md | 91.0/100 | ✅ PASS | missing disclaimer | ✅ Auto-fixed |
| what-is-tokenized-real-estate.md | 92.5/100 | ✅ PASS | missing disclaimer | ✅ Auto-fixed |
| lofty-alternative-europe.md | 91.0/100 | ✅ PASS | missing disclaimer, CTA | ✅ Auto-fixed |
| 2024-02-20-real-estate-tokenization-liquidity.md | 88.3/100 | ✅ PASS | missing disclaimer, CTA | ✅ Auto-fixed |
| 2024-02-20-tokenized-real-estate-uk.md | 86.5/100 | ✅ PASS | missing disclaimer | ✅ Auto-fixed |
| how-to-invest-property-no-money.md | 92.5/100 | ✅ PASS | missing CTA | ✅ Auto-fixed |
| tokenized-real-estate-vs-reits.md | 92.5/100 | ✅ PASS | missing CTA | ✅ Auto-fixed |

**Status:** ✅ COMPLETE — All 11 articles pass QA (≥70, no critical issues)

---

## Ongoing QA Queue (New Content)

| File | Added Date | Priority | QA Status | Score |
|------|------------|----------|-----------|-------|
| best-property-investment-apps-uk-2026.html | 2026-03-16 | P1 | ✅ PASS | 94.2/100 |
| [monitoring for new files] | - | - | - | - |

**Rule:** All new content must pass QA BEFORE publishing.

---

## Agent Spec
- **Location:** `ops/agents/qa-agent.md`
- **Loop Size:** ~5 min per 5 articles
- **Tool:** `tools/content_qa.py`
- **Pass Threshold:** ≥70/100, no critical issues

---

## Loop #1 Summary (Retroactive Sweep)

**Task:** QA all 11 published articles (retroactive check)

**Results:**
- **Checked:** 11 articles
- **Passed:** 11 (100%)
- **Failed:** 0
- **Auto-Fixed:** 11 articles (critical issues resolved)

**Fixes Applied:**
- Added disclaimer: 6 articles
- Added CTA: 7 articles
- Updated CTA text for QA compliance: 4 articles

**Ready to Publish:**
- All 11 articles are now QA-approved and ready for publishing

**Needs Manual Review:**
- None

---

**Last Updated:** 2026-03-17 09:20 GMT  
**Next Action:** All articles passed — ready for publishing step

---

## Loop #2 — Daily Check (2026-03-17)

**Task:** Daily QA check on all content/blog/ files

**Results:**
- **Checked:** 9 articles (.md files)
- **Passed:** 9 (100%)
- **Failed:** 0
- **Auto-Fixed:** 0

**Files Scanned:**
| File | Status | Score |
|------|--------|-------|
| lofty-alternative-europe.md | ✅ PASS | ≥70 |
| 2024-02-20-real-estate-tokenization-liquidity.md | ✅ PASS | ≥70 |
| lofty-alternatives-ranked.md | ✅ PASS | ≥70 |
| how-to-invest-property-no-money.md | ✅ PASS | ≥70 |
| best-property-investment-apps-uk-2026.md | ✅ PASS | ≥70 |
| 2024-02-20-tokenized-real-estate-uk.md | ✅ PASS | ≥70 |
| tokenized-real-estate-vs-reits.md | ✅ PASS | ≥70 |
| what-is-tokenized-real-estate.md | ✅ PASS | ≥70 |
| settley-vs-lofty.md | ✅ PASS | ≥70 |

**HTML Files (Previously QA'd):**
- 5-ways-invest-property-without-mortgage.html ✅ (Loop #1)
- best-property-investment-apps-uk-2026.html ✅ (Loop #1)
- how-tokenization-works-interactive-v3.html ✅ (Loop #1)
- tokenized-real-estate-uk-guide-2026.html ✅ (Loop #1)

**Status:** ✅ DONE — All content passes QA threshold

**Next Scheduled Check:** 2026-03-18 09:00 GMT
