# Settley Weekly Growth Report — Week Ending 2026-03-01

_Generated automatically by Mira on 2026-03-01 (weekly cron)._ 

## 1) Shipped This Week

### A. Content, Research & Systems (Net View for the Week)

This week’s work was heavily front‑loaded (earlier in the week) and focused on three areas:

1. **Core UK/EU SEO content cluster around Lofty & tokenization**  
   (all under `content/blog/`)
   - `lofty-alternative-europe.md` — positions Settley as the **Lofty alternative for UK/EU investors**, with a clear explanation of why Lofty is US‑only and how Settley fills that gap.
   - `lofty-alternatives-ranked.md` — ranked list of Lofty alternatives (Settley, RealT, Arrived, Fundrise, Fraction, Roofstock, Lofty itself) with honest pros/cons and a comparison table.
   - `settley-vs-lofty.md` — direct A/B comparison; explicitly says when Lofty is better (US investors, more inventory, more liquidity) vs when Settley is the right choice (UK/EU investors, local markets, Ethereum ecosystem).
   - `what-is-tokenized-real-estate.md` — plain‑English explainer that nails the “what you actually own” story (SPV → property) and differentiates tokenized RE from both REITs and crypto.

2. **City pages, templates & market research assets**  
   - `content/SEO_STRATEGY.md` — baseline SEO strategy for UK/US growth (keyword clusters, content pillars, and technical priorities).
   - `content/cities/london/landing-pages/index.md` — London investment page draft (Zone 2–3 focus, 4.5% yields, 2.1% YoY growth, clear CTAs to view properties / schedule call / download guide).
   - `content/cities/manchester/landing-pages/index.md` — Manchester investment page draft (6–8% yields, 4.5% YoY growth, 85k students, MediaCity/Salford/Northern Quarter story).
   - `content/templates/city-landing-page.md` — reusable template that lets us scale to Birmingham, Austin, Miami, etc. quickly.
   - `research/market-reports/london-manchester-2024-q1.md` — London/Manchester market report (prices, yields, growth, opportunity areas).
   - `research/target-cities-analysis.md` — initial multi‑city rollout plan (Phase 1: London/Manchester, Phase 2: Miami/Austin, Phase 3: Birmingham/Denver).

3. **Social / launch strategy & OpenClaw infrastructure**  
   - `content/strategy/slow-drip-launch.md` — 30‑day slow‑drip launch system (Problem → Market Deep Dive → Solution → Social Proof) plus daily/weekly cadence and KPIs.
   - `content/social/first-thread.md` — “Introducing Settley” Twitter thread, built around Manchester/London and the £500/£1,000 entry point wedge.
   - `content/social/week1-content-plan.md` — Week 1 daily themes, canned response templates, and guardrails on what not to say.
   - `content/social/drip-launch-week1.md` — fully written Week 1 posts (housing reality, traditional barriers, student housing opportunity, management headaches, and a “UK property is broken” thread).
   - `content/social/key-accounts.md` — list of UK property / proptech / Manchester / London / fintech accounts to engage with.
   - `.openclaw/openclaw.json`, `.openclaw/cron/jobs.json`, `.openclaw/agents/main/agent/models.json` — committed config so Mira’s cron jobs (including this report) can run on free‑tier cloud models without depending on local Ollama.
   - `scripts/restore-openclaw.sh` and `scripts/ai.openclaw.gateway.plist.template` — restore scripts so this entire setup can be brought back on a new machine quickly.

**New work since the last report (2026-02-28):** operationally, the only net new artifact is **this weekly report**; there were no additional code/content commits between 2026‑02‑28 and the timestamp of this run. The week overall, however, did include the heavy content and infrastructure work listed above.

### B. Git Commits (Last 7 Days)

From `git log --since='7 days ago'`:

- `fdf2366`, `be965b7`, `0ff1b66`, `cf70e3c` — creation and refinement of the 2026‑02‑27 and 2026‑02‑28 weekly reports under `data/weekly-reports/`.
- `db58629`, `5362bb9`, `005054f` — committed OpenClaw cron/model configuration and shifted to free cloud model fallbacks.
- `bb0121e` — added OpenClaw restore scripts (`scripts/restore-openclaw.sh`, launchd plist template).
- `f19eaee`, `03e013d`, `1251fc5`, `db203c3` — core content & research push (Lofty cluster, SEO strategy, social plan, Manchester/London pages, Lofty competitive analysis, target cities, market report).

Net: **the week delivered a strong foundation of content and systems**, but there has been no additional publishing or outreach activity since the previous report.

---

## 2) What Worked & What Didn’t

### What Worked

1. **Strategic clarity for UK/EU positioning**  
   - Content and research are now tightly aligned around the simplest story: _Settley is the Lofty‑style tokenized real estate platform built for UK/EU investors_.
   - The Lofty comparison cluster + Manchester/London pages + market reports all reinforce this narrative.

2. **Reusable content architecture**  
   - City template + first two city pages give us a blueprint to roll out dozens of `/invest/[city]` pages at low marginal cost.
   - Social launch docs (first thread, week1 plan, slow‑drip strategy) are structured in a way that plugs straight into Typefully.

3. **Agent reliability & portability**  
   - Committing `.openclaw` configs and adding restore scripts means Mira is now a reproducible, cron‑driven growth system rather than a fragile local setup.

### What Didn’t / Gaps Exposed

1. **No production deployment yet**  
   - All high‑leverage content (Lofty cluster, tokenization explainer, city pages) still lives only in this repo. There is no evidence of it being shipped to `settley.co`.
   - Impact: **zero impressions, zero organic clicks, zero signups** from this work so far.

2. **No live social execution**  
   - Week 1 social plan and assets exist, but there’s no trace of actual posting, replies, or metrics. We’re still planning the feed, not running it.

3. **No recorded outreach activity**  
   - `campaigns/` contains historical setup notes only; there are no new email/DM/partner/investor outreach logs for this week.

4. **No feedback loop from analytics**  
   - No GA4/Search Console/Plausible snapshots in `data/`; strategy is still driven by general SEO knowledge + market intuition, not Settley-specific performance data.

---

## 3) Competitor Intelligence Gathered

This week did not add new competitor names, but the **Lofty deep dive** and content derived from it clarified our wedge:

- **Lofty.ai**
  - US properties only; US investors only; Delaware LLC structure; Algorand blockchain; daily rent; active secondary market.
  - No serious UK/EU presence, no UK/EU tax or regulatory content, and no focus on European cities.
- **Opportunity for Settley**
  - Own the "Lofty alternative for UK/EU" narrative: SPV structure, Base (Ethereum L2), UK/EU cities (Manchester/London/Birmingham), UK/EU‑oriented education.

The Lofty cluster content already embeds this intelligence (and does so in a way that’s credible to investors and users).

---

## 4) Outreach Sent & Responses

**Outreach logged in this repo for the week:** _none_.

- No new email campaigns or founder updates under `campaigns/email/`.
- No logged partner, journalist, or angel outreach.
- No structured DM campaigns captured.

Conclusion: the week was focused on **strategy, content creation, and infrastructure**. Outreach and relationship‑building remain dormant.

---

## 5) Content & Execution Pipeline for Next Week

1. **Publish the Lofty comparison cluster to production**  
   - Ship these pages to `settley.co` (or the current marketing site):
     - Lofty alternative for European investors.
     - Settley vs Lofty.
     - Lofty alternatives ranked.
     - What is tokenized real estate? (plain‑English explainer).
   - Ensure URLs, title tags, and meta descriptions match the specs in each file.
   - Wire internal links from these pages to signup, property listings, and any calculator/guide pages.

2. **Ship at least Manchester + London city pages**  
   - Implement `/invest/manchester` and `/invest/london` using the content in `content/cities/.../index.md`.
   - Add minimal schema (LocalBusiness/Place + FAQ where relevant).
   - Include clear CTAs (view properties, join waitlist, book a call).

3. **Start Week 1 social schedule (for real)**  
   - Use Typefully + X to post:
     - The “First Twitter Thread: Introducing Settley”.
     - 1–2 single posts per weekday as defined in `drip-launch-week1.md`.
   - Aim for minimum execution: **5 posts + 1 thread** in the next 7 days.
   - Log basic metrics in a new file: `data/social/2026-03-week1-metrics.md`.

4. **Launch a small, focused outreach experiment**  
   - Pick one of:
     - 10 warm intros to UK proptech/fintech founders or angels using the Lofty‑alternative narrative.
     - 10 journalist/creator pitches around “Lofty alternative for UK/EU investors”.
   - Track it in `campaigns/email/2026-03-lofty-alternative-launch.md` (targets, copy, send dates, responses).

5. **Set up analytics plumbing**  
   - Confirm GA4 or Plausible is live on `settley.co`.
   - Confirm Google Search Console is connected.
   - Decide a simple weekly export format in `data/analytics/` (e.g., `2026-03-traffic-summary.md`).

---

## 6) Top Strategic Recommendation — Highest-Leverage Next Move

**Ship the Lofty comparison cluster and the Manchester/London city pages to production this week, with basic analytics wired, so we start collecting real UK/EU demand data and have live URLs to anchor social + outreach.**

Why this is the single highest‑leverage move right now:

- It turns the work we’ve already done from **potential energy into compounding traffic**.
- It gives us **credible proof points** for investors: impressions, clicks, time on page, and early signups around the Lofty‑alternative narrative.
- It gives every social post, cold DM, and investor email a **concrete destination** instead of vague “coming soon” messaging.
- It starts differentiating Settley in exactly the niche where Lofty is weakest (UK/EU), using content we already have.

Everything else (social consistency, outreach, more content) becomes more effective once these live assets exist.

---

## 7) Tools & Access Needed to Unlock the Next Level

1. **Reliable publishing path to settley.co**  
   - A clear, documented way to get `content/*.md` → live pages (even if manual for now):
     - Who owns implementing these pages (you vs another dev)?
     - Where to place the markdown/MDX in the web repo.
     - How to trigger deploys.

2. **Analytics access & routine**  
   - GA4 or Plausible credentials and confirmation they’re installed.
   - Google Search Console access for `settley.co`.
   - Agreement that once a week, we drop a short traffic/SEO snapshot into `data/analytics/` so Mira can make decisions based on real data.

3. **Social posting workflow**  
   - Confirmation that Mira can use Typefully with the Settley X account:
     - Either full autonomy within agreed guardrails, or a lightweight approval step for the first few weeks.
   - A simple convention for logging what was posted + key metrics so we can iterate the content mix.

4. **Outreach logging convention**  
   - Agreement that structured outreach (investors, partners, media) is logged under `campaigns/email/` or `campaigns/outreach/`.
   - This lets Mira handle follow‑ups, summarize response rates, and refine messaging over time.

With those pieces in place, we can move from “planning and drafting” to a weekly rhythm where **content ships, gets discovered, and feeds a data‑driven growth loop for Settley’s UK/US presence.**
