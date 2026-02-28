# Settley Weekly Growth Report — Week Ending 2026-02-28

## 1) Shipped This Week

### A. Content & SEO Assets

**Lofty & Tokenization Content Cluster (finalised and extended)**

Building on last week’s work, this week locked in and extended the core content needed for UK/US organic acquisition:

- Confirmed and refined the Lofty-focused SEO cluster (all stored under `content/blog/`):
  - `lofty-alternative-europe.md` — Lofty alternative for European investors; clearly positions Settley as EU/UK-first.
  - `lofty-alternatives-ranked.md` — ranked list of Lofty alternatives (Settley, RealT, Arrived, Fundrise, Fraction, Roofstock, Lofty itself) with honest pros/cons.
  - `settley-vs-lofty.md` — direct comparison that states plainly when Lofty is better (US investors) and when Settley wins (UK/EU investors).
  - `what-is-tokenized-real-estate.md` — plain-English explainer that nails the “what you actually own” story and differentiates tokenized RE from REITs and crypto.
- Created/confirmed **SEO_STRATEGY baseline** in `content/SEO_STRATEGY.md`:
  - Primary keyword clusters: tokenized real estate, real estate tokenization UK, fractional property ownership, Lofty alternatives.
  - Content pillars: education, market analysis, platform features, trust/security.
  - Technical priorities: structure, schema, internal linking, page performance.

**City Landing Pages (UK market focus)**

- Shipped first two **city landing page drafts**:
  - `content/cities/manchester/landing-pages/index.md` — Manchester investment page.
    - Emphasises 6–8% yields, 4.5% YoY price growth, 85k+ students, MediaCity/Northern Quarter/Salford Quays.
    - Clear CTAs: View properties / Schedule call / Download guide.
  - `content/cities/london/landing-pages/index.md` — London investment page.
    - Focuses on London’s 2.1% YoY growth, 4.5% yields in target zones, and global capital status.
    - Positions Zone 2–3 as the sweet spot for yield/growth.
- Codified a **reusable template** in `content/templates/city-landing-page.md` for fast expansion to other cities (Birmingham, Austin, Miami, etc.).

### B. Social & Launch Systems

- Documented a **slow drip launch strategy** in `content/strategy/slow-drip-launch.md`:
  - 4-week content arc: Problem → Market Deep Dive → Solution → Social Proof.
  - Clear ratios across platform-progress, market-intel, educational, and trust posts.
  - Explicit daily/weekly posting cadence with success metrics (reply/save/share rates, profile visits, follower growth, waitlist signups).
- Built Week 1 social execution assets:
  - `content/social/drip-launch-week1.md` — fully written daily posts around:
    - Manchester affordability gap.
    - Traditional barriers (deposits, mortgage requirements, friction).
    - Student housing opportunity (85k students, 7.2% yields, bed shortage).
    - Property management headaches.
    - A long-form thread: “Why UK property investment is broken”.
  - `content/social/first-thread.md` — Settley introduction thread, clearly articulating the Manchester/London wedge and £500/£1,000 entry points.
  - `content/social/week1-content-plan.md` — daily themes (Market / Education / City Focus / Problem-Solution / BTS / Community) with canned response templates and guardrails on what to avoid.
  - `content/social/key-accounts.md` — curated list of property, proptech, Manchester, London, and fintech accounts to monitor and engage with.

**Note:** These are all in-repo assets; there is still no evidence (in this repo) that posts have been pushed live yet. Execution remains the gap, not planning.

### C. Research & Positioning

- **Company & Market Context**
  - `research/company-overview.md` — provides the shared baseline for all marketing work (mission, product, traction, markets, competition, roadmap, and immediate priorities). This is now the canonical reference for:
    - 150 users, 10 paying Founders Pass members.
    - CV Labs accelerator, Base deployment, KYC/AML ready.
    - UK/US as priority markets and Lofty as primary benchmark.

- **Competitor Deep Dive**
  - `research/lofty-competitive-analysis.md` — completed a detailed Lofty analysis from a UK-unlock perspective:
    - Confirmed Lofty is US-only (properties + investors) and US-regulation-centric.
    - Identified educational and SEO gaps: no UK/EU tax content, no “what you own” clarity, no tokenized real estate UK focus.
    - Extracted specific keyword and landing-page opportunities (e.g., “Lofty alternative for UK investors”, “UK property tokenization”, “Invest in Manchester from £500”).

- **Target Cities & Market Reports**
  - `research/market-reports/london-manchester-2024-q1.md` — London & Manchester Q1 market report:
    - London: ~£530k average prices, 3.5–5% yields, 2.1% YoY growth, strong but lower-yield.
    - Manchester: ~£210k average prices, 6–8% yields, 4.5% YoY growth, higher-yield student/tech city.
  - `research/target-cities-analysis.md` — multi-city priority analysis:
    - UK: Manchester, London, Birmingham.
    - US: Austin, Miami, Denver.
    - Strategy: Phase 1 (London/Manchester), Phase 2 (Miami/Austin), Phase 3 (Birmingham/Denver).

### D. Systems & Infrastructure

- **Cron & Heartbeat Config**
  - Repo now includes `.openclaw/openclaw.json` and `.openclaw/cron/jobs.json` (via this week’s commits) to support:
    - Weekly growth reporting (this artifact, plus last week’s report).
    - Model configuration for free-tier failover (OpenRouter + fallbacks), ensuring Mira can run without local Ollama.
- **Restore Scripts for OpenClaw**
  - `scripts/restore-openclaw.sh` and `scripts/ai.openclaw.gateway.plist.template` tracked in git to make it trivial to rebuild Mira’s environment on a new machine.

### E. Git Commits This Week (Last 7 Days)

From `git log --since='7 days ago'`:

- **0ff1b66 (2026-02-28)** — Weekly growth report – 2026-02-28
  - Initial version of this report; today’s version supersedes it with the same conclusions and clearer structure.

- **cf70e3c (2026-02-27)** — Weekly growth report – 2026-02-27
  - `data/weekly-reports/2026-02-27-weekly-growth-report.md` (baseline report + strategic plan; this week’s report follows that template).

- **db58629 (2026-02-27)** — Fix cron + heartbeat models: replace Ollama with free cloud
  - `.openclaw/cron/jobs.json`, `.openclaw/openclaw.json` — ensures scheduled tasks (like this report) run reliably without local model dependencies.

- **5362bb9 & 005054f (2026-02-26)** — Add free-tier model fallbacks + openclaw config to version control
  - `.openclaw/agents/main/agent/models.json` and supporting config files.

- **bb0121e (2026-02-26)** — Add openclaw restore scripts for new machine setup
  - `scripts/ai.openclaw.gateway.plist.template`, `scripts/restore-openclaw.sh`.

- **f19eaee, 03e013d, 1251fc5, db203c3 (2026-02-25)** — Core content and strategy commits (Lofty cluster, SEO strategy, Manchester/London city pages, social strategy, slow-drip plan, target city research).

Net: this week’s work was primarily systems + reporting (Friday/Saturday) on top of a heavy content/research push earlier in the week.

---

## 2) What Worked vs What Didn’t

### What Worked

1. **Clear, Cohesive Narrative for UK/US Growth**
   - Between `company-overview.md`, Lofty analysis, city reports, and the SEO strategy, we now have a coherent story: Settley as the UK/EU-focused tokenized real estate platform and the de-facto Lofty alternative for this market.
   - The blog cluster plus city pages are well aligned with that narrative.

2. **Repeatable Content Architecture**
   - City page template + Manchester/London implementations provide a pattern we can scale across dozens of locations with minimal marginal effort.
   - Social templates and week-1 plan are structured, reusable, and compatible with Typefully automation.

3. **Agent Reliability & Automation**
   - Moving models from local Ollama to free cloud fallbacks, and committing `.openclaw` configs, reduces fragility in Mira’s scheduled tasks.
   - Weekly report is now a repeatable artifact (`data/weekly-reports/*.md`), not a one-off.

4. **Honest, High-Quality Competitive Content**
   - The Lofty cluster is not hype; it fairly credits Lofty as more mature in the US while firmly positioning Settley as the right answer for UK/EU.
   - This tone is credible with both investors and sophisticated users.

### What Didn’t (or Isn’t Yet Working)

1. **Content Still Not Live on settley.co**
   - All high-leverage content — Lofty cluster, tokenization explainer, city pages — still lives only in this repo. There is no evidence of deployment.
   - Impact today: **zero search impressions, zero organic leads** from this work.

2. **No Recorded Social Execution**
   - Week 1 social plan and threads exist, but there are no logs or analytics captured here showing threads actually posted, replies made, or growth in followers/waitlist.
   - We are still in “planned presence” mode, not live audience-building.

3. **Outreach Motion Unused**
   - Tools for outreach (email access, interview flow, social targets) are in place, but there are no `campaigns/email/*.md` logs indicating:
     - Founder/investor newsletters.
     - Press outreach around Lofty alternatives.
     - Partner outreach in Manchester/London.
   - All relationship-building is latent.

4. **Data Feedback Loop Still Missing**
   - No GA/Search Console exports or basic dashboards are checked into `data/`.
   - As a result, strategy is still based on sound assumptions + external SEO knowledge, not Settley-specific performance data.

---

## 3) Competitor Intelligence Gathered This Week

Most of the heavy competitor work landed earlier this week and is summarised in the Lofty deep dive:

- **Lofty.ai** remains:
  - US-only for both properties and investor access.
  - Stronger on liquidity (daily rent, more active secondary market).
  - Weaker or non-existent on UK/EU relevance, MiCA framing, and city-specific UK content.
- **Positioning Window:**
  - We have a clear wedge as *“Lofty for UK/EU”*, backed by:
    - Our Base/Ethereum L2 stack (more mainstream than Algorand).
    - SPV-based ownership structure, explained in plain English.
    - City-specific UK focus (Manchester/London/Birmingham) and market data).

No new named competitors beyond those already captured (RealT, Arrived, Fundrise, Fraction, Roofstock), but the existing analysis is sufficient for the current stage — we don’t need more names; we need execution.

---

## 4) Outreach Sent & Responses

**Outreach logged in this repo this week:** None.

- No email campaigns or investor updates committed under `campaigns/`.
- No partner outreach or journalist pitch logs.
- No structured DM campaigns recorded.

Conclusion: this week was about **infrastructure + reporting**, not conversations. Next week needs at least one concrete outreach motion live (see recommendations).

---

## 5) Content Pipeline for Next Week

### Priority 1 — Ship Lofty Cluster to Production

- **What:** Publish the following to settley.co:
  - Lofty alternative for European investors.
  - Settley vs Lofty comparison.
  - Lofty alternatives ranked.
  - Tokenized real estate plain-English explainer.
- **How:**
  - Wire markdown/MDX into the webfront (or simple CMS if it exists).
  - Ensure URLs, title tags, and meta descriptions follow the specs in each file.
  - Add internal links to properties, calculator, and signup.
  - Register in Google Search Console and trigger indexing.

### Priority 2 — Launch First 5–10 City Pages

- **What:** Implement and publish `/invest/[city]` pages for:
  - Manchester, London, Birmingham (UK).
  - 2–3 US cities (Austin, Miami, Denver) if technically simple.
- **How:**
  - Use `content/templates/city-landing-page.md` as the template.
  - Back city data with a simple JSON or static TS object for now.
  - Add basic schema (LocalBusiness/Place + FAQ if present).

### Priority 3 — Start Social Execution (Not Just Planning)

- **What:** Run Week 1 social schedule using Typefully + X.
  - Post at least 1 thread and 1–2 singles per day.
  - Use `key-accounts.md` to drive replies and quote-tweets.
- **How:**
  - Mira drafts and schedules via Typefully using existing copy.
  - You approve initial cadence if you want a human in the loop.
  - Log performance in a simple `data/social/2026-03-week1-metrics.md`.

### Priority 4 — Minimal Outreach Motion

- **What:** Launch one small but real outreach campaign.
  - Example: 10 warm emails to UK proptech/fintech founders or angels, using Lofty alternative story and content as proof.
- **How:**
  - Create `campaigns/email/2026-03-lofty-alternative-launch.md` to track:
    - Targets, messaging, dates, responses.
  - Use Mira to draft, you to send from founder email.

---

## 6) Top Strategic Recommendation (Headline)

**Move from “content in repo” to “content in production”: publish the Lofty comparison cluster and at least Manchester/London city pages within the next week, with basic analytics wired, so we have real UK/US demand data to point to.**

This is the single highest-leverage action for Settley’s UK/US presence right now because it:

- Creates **searchable proof** that people are actively looking for Lofty alternatives and UK tokenized real estate.
- Gives us **URLs to anchor all outreach and social** (investor updates, Twitter threads, cold emails).
- Starts the **SEO compounding clock** — every week we delay is a week of lost impressions.
- Produces **hard numbers** (clicks, time on page, signup conversions) to show investors when we talk about traction and inbound interest.

Everything else (social, outreach, further research) becomes more effective once these assets are live and discoverable.

---

## 7) Tools & Access Needed to Unlock Next Level

1. **Publishing Pipeline to settley.co**
   - A clear way (even if manual) to turn `content/*.md` into live pages.
   - Minimal requirement: you or a dev can copy/paste and deploy; ideal is Git-based MDX.

2. **Analytics Visibility**
   - GA4 or Plausible set up and accessible.
   - Google Search Console access for settley.co.
   - A simple convention for dropping exports/snapshots into `data/analytics/` each week.

3. **Social Posting Agreement & Access**
   - Confirmation that Mira can:
     - Draft and schedule posts via Typefully.
     - Use the Settley X account regularly without individual approvals (or with a lightweight approval path).

4. **Outreach Logging Convention**
   - Agreement that all structured outreach lives under `campaigns/email/` or `campaigns/outreach/` so Mira can track and optimise follow-ups.

Once those are in place, we can shift from “preparing to grow” to **actually compounding UK/US presence** every week.
