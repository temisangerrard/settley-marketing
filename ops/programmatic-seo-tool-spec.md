# Settley Programmatic SEO Tool — Custom Build Spec

**Owner:** Mira (builder + operator)
**Date:** 2026-03-11
**Status:** Ready for development
**Timeline:** 2-3 weeks (after Synthesis MD)

---

## 🎯 Vision

**Build a custom programmatic SEO tool** that:
1. Generates 1,000s of SEO-optimized pages for Settley
2. Uses UK property data (Rightmove, Zoopla, ONS)
3. Maintains Settley brand voice (not generic AI)
4. Costs 10x less than Byword.ai long-term
5. Becomes a reusable growth asset for future campaigns

**Why Build vs. Buy:**
- ✅ UK-specific (Byword is US-centric)
- ✅ Settley brand voice (not generic AI)
- ✅ Cheaper long-term (~$0.01/page vs. $0.50-1/page)
- ✅ Full control (templates, keywords, data sources)
- ✅ Reusable (future campaigns, other ventures)

---

## 🏗️ Architecture

### High-Level Flow

```
┌─────────────────┐     ┌──────────────────┐     ┌─────────────────┐
│  Keyword        │     │  Content         │     │  Publish        │
│  Research       │────▶│  Generation      │────▶│  + Index        │
│  Module         │     │  Engine          │     │  Module         │
└─────────────────┘     └──────────────────┘     └─────────────────┘
       │                       │                        │
       ▼                       ▼                        ▼
┌─────────────────┐     ┌──────────────────┐     ┌─────────────────┐
│  UK Property    │     │  LLM (Claude     │     │  settley.co/    │
│  Data APIs      │     │  3.5 Sonnet)     │     │  blog/[slug]    │
│  (Rightmove,    │     │  + Templates     │     │  Google Search  │
│  Zoopla, ONS)   │     │  + Brand Voice   │     │  Console        │
└─────────────────┘     └──────────────────┘     └─────────────────┘
```

---

## 📦 Module Breakdown

### Module 1: Keyword Research

**Purpose:** Discover 1,000+ target keywords for Settley

**Data Sources:**
- Google Keyword Planner API (free with Google Ads account)
- Ahrefs API (paid, ~$99/mo) — optional
- Manual research (seed keywords + expand)
- Competitor analysis (what ranks for Lofty, etc.)

**Keyword Categories:**
| Category | Example Keywords | Target Count |
|----------|-----------------|--------------|
| City + Investment | "Sunderland property investment" | 100+ |
| Competitor + Alternative | "Lofty.ai UK alternative" | 20+ |
| Property Type | "HMO investment UK" | 15+ |
| "Best Of" | "best cities property investment UK" | 20+ |
| How-To | "how to invest in property with little money" | 30+ |
| vs/Comparison | "tokenized real estate vs REIT" | 15+ |
| **Total** | | **200+** |

**Output:** CSV with columns:
- `keyword`
- `search_volume`
- `difficulty` (1-100)
- `intent` (informational/commercial/transactional)
- `template` (which template to use)
- `slug` (URL path)
- `priority` (1-3, 1=highest)

**Script:** `scripts/seo/keyword_research.py`

---

### Module 2: Data Collection

**Purpose:** Gather UK property data for content generation

**Data Sources:**

#### 1. Rightmove API (Scraping)
**Data:** Property prices, rents, yields by city
**Method:** PinchTab browser automation (already have)
**Frequency:** Weekly update
**Cost:** Free

**Example Query:**
```python
# Get average prices for Sunderland
pinchtab nav "https://www.rightmove.co.uk/house-prices/sunderland.html"
pinchtab snap -i -c  # Extract price data
```

#### 2. Zoopla API (Scraping)
**Data:** Sold prices, rental estimates, market trends
**Method:** PinchTab browser automation
**Frequency:** Weekly update
**Cost:** Free

#### 3. ONS (Office for National Statistics)
**Data:** Population, employment, economic data by city
**Method:** Direct API (ONS has open API)
**Frequency:** Monthly update
**Cost:** Free

**API:** https://developer.ons.gov.uk/

#### 4. UK Land Registry
**Data:** Official sold prices (authoritative)
**Method:** CSV downloads (bulk data)
**Frequency:** Monthly update
**Cost:** Free

**Link:** https://www.gov.uk/government/organisations/land-registry

#### 5. Settley Internal Data
**Data:** Pilot property details, yields, investor returns
**Method:** Direct database access
**Frequency:** Real-time
**Cost:** N/A

**Output:** JSON database with structure:
```json
{
  "cities": {
    "sunderland": {
      "avg_price": 141584,
      "avg_rent_pcm": 693,
      "gross_yield": 5.87,
      "population": 277400,
      "unemployment_rate": 4.2,
      "top_industries": ["manufacturing", "healthcare", "education"],
      "regeneration_projects": ["Riverside Sunderland", "Vaux Welcome"],
      "last_updated": "2026-03-11"
    },
    "manchester": { ... },
    ...
  }
}
```

**Script:** `scripts/seo/data_collector.py`

---

### Module 3: Content Generation Engine

**Purpose:** Generate SEO-optimized pages using templates + data

**LLM:** Claude 3.5 Sonnet (via OpenRouter)
**Why:** Best quality/cost ratio, good at structured content

**Cost Estimate:**
- ~1,000 tokens per page (input + output)
- ~$0.003 per page (OpenRouter pricing)
- 1,000 pages = ~$3

**Templates:** 4 core templates (from previous brief)

#### Template 1: City Investment Guide
**File:** `templates/city_guide.md`

**Variables:**
- `{{city_name}}`
- `{{avg_price}}`
- `{{avg_rent}}`
- `{{gross_yield}}`
- `{{population}}`
- `{{top_industries}}`
- `{{regeneration_projects}}`
- `{{nearby_city}}` (for comparison)

**Prompt Structure:**
```
You are writing a property investment guide for {{city_name}}, UK.

DATA:
- Average property price: £{{avg_price}}
- Average rent (pcm): £{{avg_rent}}
- Gross yield: {{gross_yield}}%
- Population: {{population}}
- Top industries: {{top_industries}}
- Regeneration projects: {{regeneration_projects}}

BRAND VOICE:
- Direct, clear, no unnecessary words
- Confident but not arrogant
- Educational (explain complex things simply)
- UK-focused (GBP, UK regulations, local context)

STRUCTURE:
1. H1: {{city_name}} Property Investment Guide 2026
2. Intro (2-3 sentences on why {{city_name}} is attractive)
3. "Why Invest in {{city_name}}?" (bullet points with data)
4. "Investment Opportunities" (traditional vs. tokenized)
5. "{{city_name}} vs {{nearby_city}}" (comparison table)
6. CTA: "Get Started with {{city_name}} Investment" (Settley waitlist)

CONSTRAINTS:
- 800-1,200 words
- Include keyword "{{city_name}} property investment" 2-3x naturally
- Include related keywords: "buy-to-let", "rental yield", "UK property"
- No hype, no exaggerated claims
- Link to settley.co/waitlist

Generate the full article in markdown format.
```

**Output:** Markdown file ready for publishing

---

#### Template 2: Competitor Alternative
**File:** `templates/competitor_alternative.md`

**Variables:**
- `{{competitor_name}}`
- `{{competitor_focus}}` (US, global, etc.)
- `{{competitor_min_investment}}`
- `{{competitor_currency}}`
- `{{competitor_regulation}}`

**Prompt Structure:**
```
You are writing a "[Competitor] UK Alternative" page.

DATA:
- Competitor: {{competitor_name}}
- Focus: {{competitor_focus}}
- Min investment: {{competitor_min_investment}}
- Currency: {{competitor_currency}}
- Regulation: {{competitor_regulation}}

BRAND VOICE:
- Honest (acknowledge competitor's strengths)
- UK-focused (why UK investors need UK platform)
- Not bitter (educational, not competitive)

STRUCTURE:
1. H1: {{competitor_name}} UK Alternative — Settley
2. "What is {{competitor_name}}?" (brief, fair description)
3. "Why {{competitor_name}} Doesn't Work for UK Investors" (3-4 reasons)
4. "Settley: The UK Alternative" (benefits table)
5. "Compare: {{competitor_name}} vs Settley" (comparison table)
6. CTA: "Get Started with Settley"

CONSTRAINTS:
- 600-900 words
- Include keyword "{{competitor_name}} UK alternative" 2-3x
- No false claims (stick to verifiable facts)
- Link to settley.co/waitlist

Generate the full article in markdown format.
```

---

#### Template 3: Property Type Guide
**File:** `templates/property_type_guide.md`

**Variables:**
- `{{property_type}}` (HMO, student accommodation, etc.)
- `{{avg_price}}`
- `{{avg_yield}}`
- `{{capital_growth_5yr}}`

**Prompt Structure:**
```
You are writing a "{{property_type}} Investment UK" guide.

DATA:
- Property type: {{property_type}}
- Average price: £{{avg_price}}
- Average yield: {{avg_yield}}%
- 5-year capital growth: {{capital_growth_5yr}}%

STRUCTURE:
1. H1: {{property_type}} Investment UK — 2026 Guide
2. "What is {{property_type}}?" (definition + examples)
3. "Pros of {{property_type}} Investment" (4-5 bullets)
4. "Cons of {{property_type}} Investment" (3-4 bullets)
5. "Average Returns" (table with yield, growth, etc.)
6. "How to Invest" (traditional vs. tokenized comparison)
7. CTA: "Get Started with {{property_type}} Investment"

CONSTRAINTS:
- 800-1,000 words
- Include keyword "{{property_type}} investment UK" 2-3x
- Educational tone (explain jargon)
- Link to settley.co/waitlist

Generate the full article in markdown format.
```

---

#### Template 4: "Best Of" List
**File:** `templates/best_of_list.md`

**Variables:**
- `{{keyword}}` (e.g., "best cities for property investment")
- `{{top_picks}}` (list of 5-10 cities with data)
- `{{selection_criteria}}` (how we chose)

**Prompt Structure:**
```
You are writing a "Best {{keyword}} UK 2026" guide.

DATA:
{{top_picks}} (JSON array of cities with prices, yields, growth)

SELECTION CRITERIA:
{{selection_criteria}} (yield >7%, population growth, regeneration, etc.)

STRUCTURE:
1. H1: Best {{keyword}} UK 2026 — Complete Guide
2. Intro (why this matters for UK investors)
3. "Top {{X}} {{keyword}}" (numbered list with details)
4. "How We Chose These" (methodology section)
5. "Alternative: Tokenized Property Investment" (Settley pitch)
6. CTA: "Get Started"

CONSTRAINTS:
- 1,000-1,500 words
- Include keyword "{{keyword}} UK" 3-4x naturally
- Data-driven (cite sources for rankings)
- Link to settley.co/waitlist

Generate the full article in markdown format.
```

---

### Module 4: Publishing + Indexing

**Purpose:** Publish generated content to settley.co and get it indexed

**Platform:** settley.co (assuming WordPress, Webflow, or custom)

**Publishing Methods:**

#### Option A: WordPress (if using WP)
**Method:** WordPress REST API
**Script:** `scripts/seo/publish_wp.py`

```python
# Example: Publish to WordPress
import requests

WP_URL = "https://settley.co/wp-json/wp/v2"
WP_USER = "mira"
WP_APP_PASSWORD = "xxxx-xxxx-xxxx-xxxx"  # Generate in WP admin

def publish_article(title, content, slug, category_id):
    response = requests.post(
        f"{WP_URL}/posts",
        auth=(WP_USER, WP_APP_PASSWORD),
        json={
            "title": title,
            "content": content,
            "slug": slug,
            "status": "publish",
            "categories": [category_id],
            "meta": {
                "seo_title": f"{title} | Settley",
                "seo_description": f"Learn about {title} with Settley..."
            }
        }
    )
    return response.json()
```

#### Option B: Webflow (if using Webflow)
**Method:** Webflow CMS API
**Script:** `scripts/seo/publish_webflow.py`

#### Option C: Static Site (if using Next.js, Hugo, etc.)
**Method:** Generate markdown files, commit to repo, auto-deploy
**Script:** `scripts/seo/publish_static.py`

```python
# Example: Generate markdown file
def generate_markdown(title, content, slug):
    frontmatter = f"""---
title: "{title}"
slug: "/blog/{slug}"
date: "{datetime.now().isoformat()}"
author: "Mira"
category: "Property Investment"
tags: ["UK property", "investment", "tokenization"]
---
"""
    full_content = frontmatter + content
    with open(f"content/blog/{slug}.md", "w") as f:
        f.write(full_content)
```

---

### Module 5: Indexing + Monitoring

**Purpose:** Get content indexed by Google, track rankings

#### Google Search Console Integration
**Method:** Google Search Console API
**Script:** `scripts/seo/index_monitor.py`

**Tasks:**
1. Submit sitemap (`settley.co/sitemap.xml`)
2. Request indexing for new pages
3. Monitor impressions, clicks, rankings
4. Alert on issues (404s, indexing failures)

**API:** https://developers.google.com/webmaster-tools

#### Rank Tracking
**Method:** Custom script + SERP API (or manual)
**Script:** `scripts/seo/rank_tracker.py`

**Keywords to Track:** 50-100 priority keywords
**Frequency:** Weekly
**Output:** CSV with rankings over time

**Free Option:** Manual checks (time-consuming but free)
**Paid Option:** Ahrefs/Semrush API (~$99/mo)

---

## 🛠️ Tech Stack

| Component | Tool | Cost |
|-----------|------|------|
| **LLM** | Claude 3.5 Sonnet (OpenRouter) | ~$0.003/page |
| **Browser Automation** | PinchTab (already have) | Free |
| **Data APIs** | ONS, Land Registry, Rightmove (scrape) | Free |
| **Publishing** | WordPress/Webflow/Static (existing) | Existing |
| **Search Console** | Google Search Console API | Free |
| **Rank Tracking** | Custom script (or Ahrefs) | Free-£99/mo |
| **Hosting** | settley.co (existing) | Existing |
| **Total (1,000 pages)** | | **~$10-20** |

---

## 📁 File Structure

```
settley-marketing/
├── scripts/seo/
│   ├── keyword_research.py      # Module 1
│   ├── data_collector.py        # Module 2
│   ├── content_generator.py     # Module 3
│   ├── publish_wp.py            # Module 4 (WordPress)
│   ├── publish_static.py        # Module 4 (Static)
│   ├── index_monitor.py         # Module 5
│   └── rank_tracker.py          # Module 5
├── templates/
│   ├── city_guide.md
│   ├── competitor_alternative.md
│   ├── property_type_guide.md
│   └── best_of_list.md
├── data/seo/
│   ├── keywords.csv             # Output from Module 1
│   ├── uk_property_data.json    # Output from Module 2
│   └── rankings.csv             # Output from Module 5
├── content/blog/                # Generated articles
│   ├── sunderland-property-investment.md
│   ├── lofty-uk-alternative.md
│   └── ...
└── ops/
    └── programmatic-seo-strategy.md  # This spec
```

---

## 📅 Development Timeline

### Week 1: Foundation
- [ ] Day 1-2: Keyword research module (Module 1)
- [ ] Day 3-4: Data collector module (Module 2)
- [ ] Day 5: Test data collection (10 cities)

### Week 2: Content Generation
- [ ] Day 1-2: Content generator (Module 3) — Template 1 (city guide)
- [ ] Day 3: Template 2 (competitor alternative)
- [ ] Day 4: Template 3 (property type)
- [ ] Day 5: Template 4 (best of list)

### Week 3: Publishing + Testing
- [ ] Day 1-2: Publishing module (Module 4)
- [ ] Day 3: Generate + publish first 10 pages
- [ ] Day 4: Submit to Google Search Console
- [ ] Day 5: Monitor indexing, fix issues

### Week 4: Scale + Optimize
- [ ] Day 1-2: Generate 100 pages (all templates)
- [ ] Day 3-4: Publish + index 100 pages
- [ ] Day 5: Review performance, optimize templates

---

## 📊 Success Metrics

| Metric | Target (Month 1) | Target (Month 3) | Target (Month 6) |
|--------|------------------|------------------|------------------|
| Pages Published | 100 | 500 | 1,000 |
| Pages Indexed | 80 | 400 | 900 |
| Organic Traffic | 500/mo | 5,000/mo | 20,000/mo |
| Keywords Ranked (top 100) | 50 | 300 | 1,000 |
| Waitlist Signups (from SEO) | 20 | 200 | 1,000 |
| Pilot Investors (from SEO) | 0-1 | 2-3 | 7-10 |

---

## ⚖️ Ethical Guidelines

**What We WILL Do:**
✅ Original content (AI-generated, human-reviewed)
✅ Accurate data (verified from official sources)
✅ User value (helpful guides, not thin content)
✅ UK-specific (local context, regulations)
✅ Transparent (disclose AI use if asked)

**What We WON'T Do:**
❌ Copied content (no competitor scraping for duplication)
❌ Thin content (every page must have unique value)
❌ Misleading claims (no exaggerated returns)
❌ Keyword stuffing (natural keyword density)
❌ Black-hat tactics (hidden text, cloaking, etc.)

---

## 🎯 Next Steps

**Immediate (This Week):**
1. ✅ Spec complete (this document)
2. ⏳ Decision: Approve build? (Yes/No)
3. ⏳ If yes: Start Module 1 (keyword research)

**Week 1-2 (After Synthesis MD):**
1. ⏳ Build Module 1 + 2 (keywords + data)
2. ⏳ Build Module 3 (content generation)
3. ⏳ Test with 10 pages

**Week 3-4:**
1. ⏳ Build Module 4 + 5 (publishing + monitoring)
2. ⏳ Generate + publish 100 pages
3. ⏳ Monitor indexing + rankings

---

## 💡 Future Upgrades

**Phase 2 (Month 2-3):**
- [ ] Auto-update old content (refresh data monthly)
- [ ] A/B test headlines + CTAs
- [ ] Internal linking optimizer (auto-link related pages)
- [ ] Schema markup generator (rich snippets)

**Phase 3 (Month 4-6):**
- [ ] Multi-language support (UK → EU expansion)
- [ ] Competitor monitoring (alert on new competitors)
- [ ] Content performance dashboard (real-time analytics)
- [ ] Backlink builder (automated outreach)

---

**File Location:** ops/programmatic-seo-tool-spec.md
**Created:** 2026-03-11
**Owner:** Mira (builder)
**Status:** Ready for development
