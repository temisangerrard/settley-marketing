# Heartbeat checklist

**Output contract (strict):**
- If no verified changes since last check, reply exactly `HEARTBEAT_OK`.
- Only report items backed by concrete evidence (file path + timestamp, commit SHA, or URL).
- Do not claim outreach/posting/publishing happened unless verifiable proof exists in this run.
- If something cannot be verified, mark it `UNVERIFIED`.
- If access/tooling is missing, mark it `BLOCKED` and state the exact dependency needed.

---

## 📧 Daily Non-Negotiables

- [ ] **Check mirasettley@gmail.com** for investor replies, partnership requests, press inquiries — if urgent, message Temisan now with sender, subject, 2-bullet summary, recommended action
- [ ] **Update investor outreach progress** in ops/prospecting/progress-YYYY-MM-DD.md with sent count, responses, next actions
- [ ] **Git commit with SHA** as proof of daily work (even if just memory file update)

---

## 🎯 Active Projects & Challenges (Track Daily)

### Nansen CLI Challenge (#NansenCLI)
- [ ] **Status:** Submitted (X post published, commit SHA proof)
- [ ] **Files:** tools/settley-nansen-tracker.py, ops/nansen-cli-challenge-submission.md
- [ ] **X Post:** https://x.com/mirasettley/status/2034917529001288100
- [ ] **Monitor:** Check for Nansen engagement/response, retweets, challenge results
- [ ] **Next:** If credits refresh, run tracker daily at 9 AM UTC for actual intelligence

### Competitive Intelligence System
- [ ] **Status:** System launched, baseline initiated (3/20 keywords analyzed)
- [ ] **Files:** ops/competitor-tracking/competitive-intelligence-system.md, serp-baseline-2026-03-20.csv
- [ ] **Remaining:** Complete baseline for 17 more keywords (tokenized real estate, real estate tokens, etc.)
- [ ] **Daily:** Check for new competitor movements, SERP changes, clone detection

### A16z Speedrun Accelerator
- [ ] **Status:** Opportunity identified, applications open April 2026
- [ ] **Precedent:** Smart Bricks (proptech) raised $5M pre-seed led by a16z Speedrun
- [ ] **Next:** Draft application strategy doc, research 3-5 more accelerators with proptech/fintech precedents
- [ ] **Deadline:** Applications open April 2026

---

## 📊 Growth Pipeline (Update Daily)

### Investor Outreach
- [ ] **Total sent:** 40 emails (23 initial + 17 follow-ups as of Mar 20)
- [ ] **Responses:** 0 (awaiting — normal 10-15% response rate = 4-6 expected)
- [ ] **Next follow-up wave:** March 21+ (any non-responders from March 6-7 batch, 15+ days elapsed)
- [ ] **File:** ops/prospecting/investor-outreach.csv, ops/prospecting/progress-2026-03-20.md

### Content Pipeline
- [ ] **Published today:** Check content/blog/ for new articles
- [ ] **Target:** 5 articles/week
- [ ] **Drafts:** Check content/drafts/ and content/blog/ for ready-to-publish pieces

### Social/Distribution
- [ ] **X posts:** Check @mirasettley for published posts
- [ ] **Scheduled:** Check Typefully for scheduled posts
- [ ] **Engagement:** Monitor X notifications for replies, retweets, new followers

---

## 🚨 Blockers & Risks

- [ ] **Email responses:** Track response rate (expecting 10-15% = 4-6 of 40)
- [ ] **Cron system:** 9 of 12 jobs disabled — manual execution active
- [ ] **Content velocity:** Track articles published vs. 5/week target

---

## 🔗 Link Intake (Temisan's Shares)

For each link Temisan shares:
- [ ] Open and extract: what it is, deadline/eligibility, leverage potential, effort required
- [ ] Log action recommendation in memory/YYYY-MM-DD.md or dedicated ops/ file
- [ ] Execute on approval (application draft, task plan, agent spec, outreach, implementation)

---

## ⏰ Timing Rules

- **If quiet for 8+ hours during daytime (08:00-23:00):** Send brief status update
- **If investor response received:** Message Temisan immediately with summary
- **If growth opportunity blocked:** Message Temisan with exact dependency needed
- **End of day (20:00 GMT):** Daily metrics report (if not already sent)

---

## 📝 Memory & Continuity

- [ ] **Daily memory file:** memory/YYYY-MM-DD.md with what actually happened (commits, emails, articles)
- [ ] **Ralph loop checkpoints:** For long tasks, resume from memory/loops/<task-slug>.md, execute one chunk, write new checkpoint
- [ ] **Weekly review:** Friday 15:00 GMT — full growth report (automated cron still active)

---

**Last Updated:** 2026-03-20 (added Nansen CLI challenge, competitive intelligence, Speedrun accelerator tracking)
