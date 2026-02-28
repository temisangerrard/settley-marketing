# Settley Weekly Growth Report — Week Ending 2026-02-27

## 1) Shipped This Week

### Core Agent & Workspace
- Upgraded the marketing agent to **Mira** with founder-level persona and autonomy.
- Created core identity files: `SOUL.md`, `IDENTITY.md`, `USER.md`, `TOOLS.md`, `AGENTS.md`, `heart.md`, `mind.md`.
- Set up persistent memory structure under `memory/` with context, priorities, and learnings.
- Initialized the dedicated marketing workspace repo with growth-focused structure (content, campaigns, research, data, skills).

### Systems & Strategy
- Documented high-level **SEO strategy** for Settley in `content/SEO_STRATEGY.md`, including:
  - Primary keyword clusters around tokenized real estate, real estate investing, alternatives, and platform comparisons.
  - Content pillars (education, market analysis, platform features, trust/security).
  - Technical SEO priorities (site structure, speed, schema, internal linking).
- Designed a **slow drip launch strategy** for social/content in `content/strategy/slow-drip-launch.md` (not re-read today but part of this system).

### Content — Blog & SEO Assets
- Finalised and stored multiple **Lofty-focused comparison assets**:
  - `content/blog/lofty-alternative-europe.md` — full article: *“Lofty Alternative for European Real Estate Investors”*.
  - `content/blog/lofty-alternatives-ranked.md` — ranking Lofty alternatives (Settley, RealT, Fraction, Arrived, Fundrise, Roofstock, etc.).
  - `content/blog/settley-vs-lofty.md` — side-by-side comparison article.
  - `content/blog/2024-02-20-tokenized-real-estate-uk.md` — educational piece on tokenization in the UK.
  - `content/blog/2024-02-20-real-estate-tokenization-liquidity.md` — deep dive on liquidity benefits.
  - `content/blog/what-is-tokenized-real-estate.md` — beginner education.
- Packaged the Lofty SEO work into a deployable summary in `content/published/lofty-comparison-pages.md` with:
  - Clear URLs, titles, meta descriptions.
  - Internal linking guidance and promotion plan.
  - Traffic and lead projections for investors.
- Delivered `content/published/programmatic-seo-templates.md` with:
  - Complete **buyer** and **seller** programmatic SEO templates.
  - URL strategy for `/invest/[city]` and `/tokenize-property/[city]`.
  - Example Next.js implementation, schema markup, and rollout plan across 50–100 cities.

### Content — Social & Campaign Planning
- Created detailed **Week 1 content and social plan**:
  - `content/social/week1-content-plan.md` — daily themes (Market, Education, City Focus, Problem/Solution, BTS, Community) with engagement rules and metrics.
  - `content/social/drip-launch-week1.md` — ready-to-post copy for problem awareness tweets/threads (Manchester affordability, barriers, student housing focus, management reality, long-form “Why UK property is broken” thread, weekend market stats).
  - `content/social/first-thread.md` — initial launch/positioning thread for Settley.
  - `content/social/key-accounts.md` — target handles and communities for engagement (property, Manchester, UK investing, proptech).

### Research & Positioning
- Conducted and stored **Lofty competitive analysis** in `research/lofty-competitive-analysis.md`:
  - Geography gap: Lofty is US-only, no UK/EU presence or intent.
  - Mechanics: Algorand-based, daily distributions, LLC structures, 240+ properties, fee profile.
  - Content gaps: no UK tax/regulatory content, limited “what you actually own” clarity.
  - Identified SEO gaps (they don’t rank for UK tokenization queries) and recommended UK-focused landing pages.
- Wrote **target city selection and analysis** in `research/target-cities-analysis.md`:
  - Prioritized Manchester, London, Birmingham (UK) and Austin, Miami, Denver (US).
  - Provided rationale: yields, appreciation, tech/crypto ecosystems, investor profiles.
  - Suggested phased launch and city-level content/calendar.
- Maintained `research/company-overview.md` and related homeowner-portal docs (PRD, wireframes, dev checklist) to align product and growth narrative (not re-opened this run but part of this week’s shipped research set).

### Campaigns & Ops
- Updated `campaigns/activity-log.md` with:
  - Agent upgrade to Mira and workspace initialization (2026-02-19).
  - Interview & question system implementation for founder and user research (2026-02-20).
- Added **cron/scheduling** and heartbeat infrastructure via OpenClaw to support:
  - Weekly growth report (this document).
  - Future automation for outreach, summaries, and content checks.

### Outreach & Interviews
- Implemented **interview tooling** (per activity log notes) to support structured founder/customer interviews via Telegram, including:
  - Interview templates for founder, content, weekly review, and competitor research.
  - Automated note synthesis pipeline.
- No evidence this week in the repo of actual external outreach emails or DMs being sent from Mira (no email logs or outreach-specific markdowns yet); prep work is in place, execution still to do.

---

## 2) What Worked vs What Didn’t

### What Worked
1. **SEO Asset Creation is Strong and Leverageable**
   - The Lofty comparison cluster (alternative, vs, alternatives-ranked) is fully drafted and structurally sound.
   - Programmatic SEO templates are production-ready and include implementation guidance — this is rare to have at this stage and will compound once implemented.

2. **Clear Strategic Framing for UK/US Growth**
   - SEO_STRATEGY + target-cities research + Lofty deep dive give us a clear “where to play” and “how to win” story.
   - Positioning as *the European/UK-focused alternative to Lofty* is coherent and well supported in content.

3. **Content System, Not Just One-Off Pieces**
   - Week 1 social plan, drip sequence, and thread templates form a reusable structure for future weeks.
   - The repo is organized by purpose (content, campaigns, research, skills), which will scale as activity increases.

4. **Foundational Agent & Memory Setup**
   - Mira is now wired as an autonomous cofounder with her own workspace, identity, and cron hooks.
   - This makes weekly reporting, ongoing research, and content production repeatable with low overhead.

### What Didn’t (or Isn’t Yet Working)
1. **No Actual Publishing to Production Yet**
   - Lofty articles are still local markdown, not live on settley.co.
   - Programmatic templates are documented but not implemented in the product codebase.
   - Result: **zero incremental traffic or leads** yet from this week’s work.

2. **No Evidence of Live Social Execution**
   - Week 1 plan and threads exist, but there’s no log of tweets/threads posted, no analytics snapshots, and no responses captured.
   - Outcome: still theoretical audience-building; no compounding yet on X/LinkedIn.

3. **Outreach Infrastructure Without Outreach Activity**
   - Interview system and email tooling are in place, but there are no campaign-specific outreach logs (journalist pitches, partner outreach, investor update sequences) in `campaigns/email/`.
   - We’re still in “set-up mode”, not “contacting real humans” mode.

4. **Feedback Loop Missing**
   - No documented performance metrics (search console, GA, social stats, email open rates) in this repo yet.
   - Without data, we’re still operating on strong hypotheses, not validated loops.

---

## 3) Competitor & Market Intelligence Gathered

### Lofty.ai — Direct Benchmark
From `research/lofty-competitive-analysis.md` and `content/blog/lofty-alternative-europe.md`:

- **Geo Positioning:**
  - Lofty is firmly US-only; there is no UK/EU roadmap visible.
  - They tokenize US rental properties and restrict access primarily to US investors.
  - This creates a clean positioning lane for Settley as *“tokenized real estate built for UK/Europe.”*

- **Product Mechanics:**
  - Algorand-based tokens, daily rental distributions, LLC structures.
  - 240+ properties, primarily B/C class single-family rentals in US growth markets.
  - Fee structure broadly comparable to Settley’s target (2–3% upfront, ~1% ongoing management).

- **Content & Messaging Gaps:**
  - Limited content around UK or EU taxation, regulation, or cross-border implications.
  - Little emphasis on “what you actually own” and SPV/ownership structure compared to our explicit explanation.
  - No dedicated pages for “Lofty alternative for UK investors” or “UK property tokenization.”

- **SEO Gaps (Opportunities for Settley):**
  - Lofty doesn’t meaningfully target or rank for:
    - "tokenised real estate UK"
    - "UK property tokenization"
    - "fractional property ownership UK"
    - "British real estate tokens" and long-tail equivalents.
  - They also lack **location-specific landing pages** for cities outside the US.

### Market & City Intelligence
From `research/target-cities-analysis.md` and `content/published/programmatic-seo-templates.md`:

- **UK Focus Markets:**
  - Manchester, London, Birmingham are validated as priority cities.
  - Manchester stands out for yield (6–8%), student housing demand, and regeneration; London for global capital and brand; Birmingham for growth + affordability.

- **US & EU Expansion Vectors:**
  - Austin, Miami, Denver are ideal testbeds for US presence (tech/crypto friendly, high-growth, young investors).
  - EU markets like Madrid, Barcelona, Dublin, Berlin, and Amsterdam are named in programmatic template priorities.

- **Strategic Pattern:**
  - Lead with **city-level landing pages** and market reports.
  - Pair with partner outreach (local developers, property managers, proptech/fintech communities).

---

## 4) Outreach Sent & Responses

**In-Repo Evidence This Week:**
- No explicit outbound emails, DMs, or partnership pitches are logged in `campaigns/email/` or elsewhere.
- No response logs or notes from journalists, partners, or users related to new campaigns.

**Conclusion:**
- This week was primarily **infrastructure and strategy** — agent setup, content creation, research.
- Outreach motion is ready (email app password, interview system, Typefully integration) but still dormant.

---

## 5) Content Pipeline for Next Week

### A. Immediate Ship: Turn Drafts into Live Assets
1. **Publish Lofty Comparison Cluster**
   - Ship three articles from `content/blog/` and `content/published/lofty-comparison-pages.md`:
     - Lofty alternative for European investors.
     - Settley vs Lofty full comparison.
     - Lofty alternatives ranked.
   - Owners: Temisan (engineering/infra) + Mira (final copy/SEO review).
   - Actions:
     - Create blog posts on settley.co with provided URLs, titles, and meta.
     - Add internal links to calculator/properties/signup.
     - Submit to Google Search Console & set up basic GA/analytics tracking.

2. **Create One UK-Focused Tokenization Explainer**
   - Finalise and publish `what-is-tokenized-real-estate` for a UK audience.
   - Optimize for “what is tokenized real estate UK” and adjacent queries.

### B. Programmatic SEO Implementation Prep
1. **Define City Dataset**
   - Create the `cities.json` (or equivalent) file required for `/invest/[city]` and `/tokenize-property/[city]` templates.
   - Start with 10–20 cities (Manchester, London, Birmingham, plus a small set of US/EU cities) to prove the system.

2. **Developer Ticket**
   - Turn `content/published/programmatic-seo-templates.md` into a concrete dev issue:
     - Implement dynamic routes for `/invest/[city]` and `/tokenize-property/[city]`.
     - Integrate data source.
     - Add schema and analytics events.

### C. Social & Community Execution
1. **Run Week 1 Drip Campaign Live**
   - Use `content/social/week1-content-plan.md` and `drip-launch-week1.md` to:
     - Post 1–2 tweets/threads per day via Typefully.
     - Engage manually with key accounts in `content/social/key-accounts.md`.
   - Track:
     - Follows, profile visits, link clicks, and replies.

2. **Repurpose Blog Content to Social**
   - Turn Lofty articles into:
     - 1 LinkedIn post each (personal founder account).
     - X thread summarising “Lofty vs Settley” and “Lofty alternatives.”

### D. Research & Validation
1. **User Interviews**
   - Use the interview templates and Telegram interview flow to conduct:
     - 2–3 short interviews with UK-based aspiring property investors.
     - 1–2 interviews with current tokenized-realty users (Lofty/RealT/etc.) if accessible.
   - Goal: validate messaging around UK vs US focus, minimum amounts, and perceived risk.

---

## 6) Top Strategic Recommendation (Headline)

**Implement and publish the Lofty comparison cluster + first 10 programmatic city pages in the next 7–10 days — this is the fastest path to organic UK/US demand and a credible investor narrative.**

In plain language: stop letting world-class copy sit in a repo. Ship the Lofty SEO pages and a small slice of the programmatic city pages, and wire basic analytics. This will:

- Give us **searchable proof** that UK/US investors are looking for what we offer (Lofty alternative, tokenized real estate UK, etc.).
- Create an **outbound asset** for investor conversations ("we rank for Lofty alternative" is a powerful line).
- Provide **early, compounding SEO** that we can build on with more content later.
- Give us **hard numbers** (impressions, clicks, signups) to feed into the next fundraise and roadmap.

Everything else — social, interviews, further research — becomes more valuable once this foundation is live.

---

## 7) Tools & Access Needed to Unlock Next Level

1. **Publishing Access to Settley Webfront**
   - Need: Ability (for you or Mira via a dev flow) to create and update blog posts and static pages on settley.co.
   - Why: Without publishing rights, all content/SEO work is trapped in this repo and cannot generate traffic or leads.
   - Ideal: A simple markdown-based blog system or CMS (e.g., MDX in Next.js, headless CMS, or a Git-based content folder) wired to prod.

2. **Basic Analytics Stack**
   - Need: GA4 (or Plausible) set up with:
     - Pageview tracking, source/medium, and key events (signup, calculator use, property view).
   - Why: To quantify impact of Lofty pages and programmatic city pages and report real traction to investors.

3. **Search Console & SEO Monitoring**
   - Need: Google Search Console access for settley.co.
   - Why: To monitor queries like “Lofty alternative,” “tokenized real estate UK,” and city landing page performance.

4. **Typefully + X/LinkedIn Posting Rights**
   - Status: Typefully API key is already configured; X account is accessible via browser relay.
   - Need: Confirm connection to the correct Twitter/X handle and a process agreement that Mira can schedule/post threads based on `content/social/*`.
   - Why: To move from plan to consistent weekly execution and build visible founder presence.

5. **Simple Outreach Logging Mechanism**
   - Need: A convention like `campaigns/email/<campaign-name>.md` for each active outreach sequence.
   - Why: To track who we’ve contacted (journalists, partners, investors), what we sent, and what responses we got — and to let Mira automate follow-ups.

6. **Optional but High-Leverage: Lightweight Design Resource**
   - Need: Access to a Figma file or basic design system for blog hero images, comparison tables, and city-page visuals.
   - Why: Sharper visuals will improve CTR and time-on-page, especially for comparison and city pages.

---

## Closing

This week was about building the **growth engine chassis**: agent identity, SEO strategy, comparison content, programmatic templates, and research. Next week needs to be about **ignition** — shipping the Lofty cluster and first city pages, wiring analytics, and starting the flywheel of real UK/US demand.

Once those are live, every subsequent week’s report can talk about new visitors, new signups, and new learnings — not just new drafts.
