# Twitter/X Automation Setup

## Status ✅

**Tools installed:**
1. **xurl** - X API CLI (OAuth1 authenticated) - Primary posting tool
2. **twitter-cli** - Twitter terminal client (installed, browser cookies needed)

**Recommended:** Use `xurl` for posting (already authenticated), `twitter-cli` for reading feeds/monitoring.

---

## Quick Start: Posting Tweets

### Using xurl (Recommended for posting)

```bash
# Simple post
xurl post "Your tweet text here"

# Or use our wrapper script
./scripts/twitter-post.sh "Your tweet text here"
```

**Test tweet posted:** 2026-03-09 13:26 GMT
- Tweet ID: `2030998905182179606`
- URL: https://x.com/mirasettley/status/2030998905182179606

### Using twitter-cli (For reading/monitoring)

```bash
# Fetch home timeline
twitter feed --max 20

# Search for keywords
twitter search "tokenized real estate" --max 10

# Monitor competitor accounts
twitter user-posts loftyai --max 5

# Post tweet (requires browser cookies)
twitter post "Hello from terminal!"
```

**Note:** twitter-cli needs browser cookies for auth. If you don't have Twitter cookies in browser, use xurl for posting.

---

## Auth Status

### xurl (Working ✅)
- **Auth method:** OAuth1 + Bearer token
- **Account:** @mirasettley
- **Status:** Verified and posting
- **Preflight check:** `./scripts/xurl_preflight.sh`

### twitter-cli (Partial ⚠️)
- **Auth method:** Browser cookies
- **Status:** Installed, needs cookie extraction
- **Best for:** Reading feeds, monitoring competitors

---

## Automation Workflows

### 1. Competitor Monitoring
```bash
# Monitor Lofty.ai Twitter
twitter user-posts loftyai --max 10 > ops/competitor-tracking/twitter-lofty-$(date +%Y%m%d).json
```

### 2. Automated Settley Updates
```bash
# Post milestone update
./scripts/twitter-post.sh "🚀 Arena Play just hit 100 users! Testing tokenized UK real estate with zero-friction onboarding. Try it → https://autobett.netlify.app/welcome"
```

### 3. Hackathon/Celo Updates
```bash
# Post about Celo hackathon submission
./scripts/twitter-post.sh "Building Arena Agent: AI-powered real estate investing on @Celo. Autonomous agent + RWA tokenization = wealth creation for emerging markets 🌍"
```

---

## Tweet Templates (Ready to Use)

### Arena Play Launch
```
🏗️ We didn't build another dashboard.

We built Arena Play:
→ Live simulation of tokenized UK real estate
→ See yields, ownership splits & liquidity in real-time
→ Zero sign-up. Zero risk. Just insight.

Try it → https://autobett.netlify.app/welcome
```

### Celo Hackathon Announcement
```
🤖 Building Arena Agent for @Celo's AI hackathon.

An autonomous AI agent that:
→ Researches tokenized properties
→ Executes micro-investments via natural language
→ Auto-rebalances portfolios

Real-world assets meet AI automation.

Follow along as we build in public 🧵
```

### Investor Traction Update
```
📊 Settley Traction Update:

• 150 users (Nigeria pilot)
• 10 paying Founder's Pass members
• 67% conversion rate
• 0→1 UK market launch next

Product works. Now scaling to UK/US with £200K pre-seed.

Building the infrastructure for tokenized real estate.
```

### Competitor Comparison
```
🔍 Lofty.ai vs Settley:

Lofty: US-focused, single-family homes, $50 min
Settley: UK-first, multi-family + commercial, £10 min

Both tokenizing real estate. Different markets, different strategies.

We're starting with Manchester + London → then US (Miami + Austin)
```

---

## Posting Cadence (Recommended)

**Weekly rhythm:**
- Monday: Product update / milestone
- Wednesday: Educational thread (tokenized real estate 101)
- Friday: Community engagement / competitor insight
- Weekend: Light engagement, retweets

**Hackathon mode (daily):**
- Daily progress updates
- Technical deep-dives
- Build-in-public threads
- Ecosystem engagement (@Celo, judges, other builders)

---

## Scripts

### twitter-post.sh
**Location:** `/Users/temisan/Downloads/settley-marketing/scripts/twitter-post.sh`

**Usage:**
```bash
# Post a tweet
./scripts/twitter-post.sh "Tweet text here"

# Show usage + last tweet
./scripts/twitter-post.sh
```

**Features:**
- Auto-checks xurl auth
- Returns live tweet URL
- Saves last tweet ID for tracking

### monitor-lofty.sh (Coming)
**Purpose:** Automated competitor Twitter monitoring
**Output:** Daily JSON files with Lofty's tweets, engagement metrics

---

## Troubleshooting

### xurl post fails with 401/403
**Fix:** Run preflight check
```bash
./scripts/xurl_preflight.sh
```

### twitter-cli says "No cookies found"
**Fix:** Log into Twitter in your browser first, then retry. Or use xurl for posting.

### Duplicate content error
**Meaning:** Tweet already posted successfully. Check the URL returned.

---

## Next Steps

1. ✅ Test posting workflow - DONE
2. ⏳ Set up competitor monitoring (Lofty, RealT, Propy)
3. ⏳ Create 2-week content calendar for Settley
4. ⏳ Build automated milestone poster (git webhook → tweet)
5. ⏳ Integrate with Arena Agent for auto-updates

---

## Resources

- xurl docs: `/opt/homebrew/lib/node_modules/openclaw/skills/xurl/SKILL.md`
- twitter-cli GitHub: https://github.com/jackwener/twitter-cli
- Twitter API limits: 2,400 tweets/day (we're well under)
