# Learnings - What Mira Has Learned

**Last Updated:** 2026-02-19

---

## Content Insights

### What Works
- (To be populated as content is published and measured)

### What Doesn't Work
- (To be populated as content is published and measured)

---

## Competitor Intelligence

### Lofty.ai
- US-only restriction is a major opportunity for UK/EU positioning
- Their content focuses heavily on "daily rent" messaging
- Active community on Discord
- Properties sell out quickly (demand > supply)

### RealT
- More crypto-native audience
- Ethereum ecosystem integration
- International investor access

---

## Audience Insights

### UK Market
- (Research needed)

### US Market
- (Research needed)

---

## SEO Learnings

### Keywords That Work
- (To be populated as rankings are tracked)

### Content Formats That Perform
- (To be populated as performance is measured)

---

## Process Learnings

### What Speeds Up Work
- Having company context readily available
- Clear priorities reduce decision fatigue
- Templates for common content types

### What Slows Down Work
- Unclear requirements
- Waiting for approvals
- Research without clear questions

---

## Failed Experiments

(Nothing yet - document failures to avoid repeating them)

---

## Hypotheses to Test

1. Comparison pages will capture competitor search traffic
2. UK-specific content will rank faster than US (less competition)
3. Educational content will have higher engagement than promotional
4. Property-specific content will convert better than general tokenization content

---

## Notes

This file is updated after each significant work session. It serves as institutional memory so I don't repeat mistakes or forget what works.

## 2026-03-09
- Tie every public claim to a concrete log or artifact the same day; memory entries without tool evidence create audit gaps.

## 2026-03-15
- Status dashboards must be updated immediately after agent runs complete — stale metrics create false audit findings. Auto-update or trigger dashboard refresh as part of agent completion flow.

## 2026-03-16
- Daily self-audit passed: all cron claims (QA 11/11, article drafted 3,970 words, backlinks 2/10) verified against git log + checkpoint files. Zero mismatches. System integrity confirmed.

## 2026-03-17
- **Mismatch detected:** March 17 cron runs claimed QA fixes (11 articles) and article drafting (3,970 words) as same-day execution. Git log shows commit 4279c179 ("Content pipeline: QA complete") dated March 16, 12:35 — work was done previous day. Cron jobs re-processing completed work must not claim credit as new execution. Fix: cron jobs should check git timestamps before claiming "completed today."

## 2026-03-19
- **Mismatch detected:** Self-audit cron (bd423a1d) has timed out 7 of last 10 runs (Mar 10-19). QA agent (3ff8b881) and article drafting (53194b70) also timing out. Last git commit: March 16 (45ef13d7). No daily memory files created for Mar 16-19. Claim: "system operational" vs Evidence: zero commits in 72h, no memory artifacts, repeated timeout errors. Fix: (1) reduce cron job complexity to fit timeout window, (2) add pre-flight check for git activity before claiming execution, (3) require memory file creation as completion signal.
