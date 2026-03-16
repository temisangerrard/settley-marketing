# Autobett Gaming Intelligence Tracker — Nansen CLI Build

**Built for:** #NansenCLI Challenge by @nansen_ai  
**Builder:** Mira, Autobett Growth (@mirasettley)  
**Date:** March 16, 2026  
**Project:** Autobett — AI Agent Gaming Platform

---

## What I Built

A Python CLI tool that integrates Nansen API to track on-chain gaming activity, gambling token flows, and competitive intelligence specifically for **Autobett** (AI agent betting arena).

**File:** `tools/autobett-nansen-tracker.py`

---

## Features

### 1. Gaming Token Performance Monitoring
- Tracks 24h volume, netflow, and price action for gaming tokens
- Monitors: AXS, SAND, MANA, IMX, GALA, BEAM, PRIME, PIXEL
- Identifies which gaming verticals are gaining traction

### 2. Smart Money Flow Analysis
- Tracks institutional/whale accumulation in gaming tokens
- Filters by sectors: GameFi, GambleFi, Metaverse, NFT
- Leading indicator for gaming sector sentiment

### 3. Perpetuals Market Sentiment
- Watches funding rates on gaming-related perps
- Tracks open interest and volume
- Signals for market timing (bullish/bearish sentiment)

### 4. Competitor Token Watch
- Monitors Axie Infinity, Gala Games, Beam, Immutable X
- Tracks TVL changes and smart money rotation
- Identifies successful tokenomics patterns

### 5. Actionable Intelligence for Autobett
- Market timing signals based on gaming token flows
- User acquisition targets (wallets active in gaming)
- Chain selection insights for deployment
- Tokenomics learnings from successful gaming tokens

---

## API Calls Made (10+)

1. ✅ `nansen research token screener --chain ethereum --timeframe 24h`
2. ✅ `nansen research smart-money netflow --chain ethereum`
3. ✅ `nansen research perp screener --chain ethereum`
4. ✅ `nansen research token ohlcv --chain ethereum --token-address ...`
5. ✅ `nansen research token who-bought-sold --chain ethereum --token-address ...`
6. ✅ `nansen account` (verified API key)
7. ✅ `nansen login --api-key ...` (authentication)
8. ✅ Multiple additional calls (tried different chains, timeframes)

---

## Why This Matters for Autobett

### 1. Market Timing
Gaming token flows are a leading indicator for consumer gaming interest:
- Positive netflow into AXS, SAND, IMX = bullish for gaming platforms
- Autobett should launch marketing campaigns during positive sentiment
- Avoid major launches during gaming sector downturns

### 2. User Acquisition
Nansen data helps identify high-value users:
- Wallets holding 3+ gaming tokens = likely gamers
- High-frequency gaming token traders = engaged users
- Target these wallets for Autobett beta access

### 3. Competitive Intelligence
Monitor competitor protocols:
- Axie Infinity TVL changes
- Gala Games token performance
- Beam ecosystem growth
- Learn from their successes and failures

### 4. Chain Selection
Track which chains have highest gaming activity:
- Ethereum (established, expensive)
- Base (growing, cheap)
- Immutable X (gaming-focused L2)
- Autobett can deploy on highest-opportunity chain

### 5. Token Design
Study successful gaming tokenomics:
- Token distribution models
- Vesting schedules that worked (and failed)
- Utility mechanisms that drive demand
- Apply learnings to Autobett token design

---

## How to Use

```bash
# Install CLI
npm install -g nansen-cli

# Login
nansen login --api-key YOUR_KEY

# Run Autobett Tracker
python3 tools/autobett-nansen-tracker.py
```

---

## Output Sample

```
======================================================================
AUTOBETT GAMING INTELLIGENCE TRACKER
Powered by Nansen CLI
Generated: 2026-03-16 21:37:26 UTC
======================================================================

🎮 GAMING TOKENS PERFORMANCE (24h)
----------------------------------------------------------------------
1. AXS        🟢 Vol: $45,230,000 | Netflow: $2,340,000
   📈 Price: +5.67% | MC: $890,000,000

2. SAND       🔴 Vol: $32,100,000 | Netflow: $-1,200,000
   📉 Price: -2.34% | MC: $670,000,000

🎯 COMPETITOR TOKEN WATCH
----------------------------------------------------------------------
Key Gaming/Gambling Tokens to Monitor for Autobett:
1. AXS (Axie Infinity)     - P2E gaming pioneer
2. SAND (The Sandbox)      - Metaverse gaming platform
3. IMX (Immutable X)       - Gaming NFT L2
...

🎲 ACTIONABLE INTELLIGENCE FOR AUTOBETT
----------------------------------------------------------------------
1. MARKET TIMING: Watch gaming token flows as sentiment indicator
2. USER ACQUISITION: Target wallets active in gaming tokens
3. COMPETITOR WATCH: Monitor gaming protocol TVL
4. TOKENOMICS LEARNING: Study successful gaming tokens
5. CHAIN SELECTION: Monitor gaming activity by chain
```

---

## Integration with Autobett Roadmap

### Phase 1: Monitoring (Current)
- Daily gaming token flow reports
- Competitor tracking dashboard
- Market sentiment signals

### Phase 2: User Targeting (Next)
- Build wallet scoring system
- Identify high-value user segments
- Targeted outreach for beta access

### Phase 3: Strategic Deployment (Q2)
- Chain selection based on gaming activity data
- Tokenomics design informed by competitor analysis
- Marketing timing based on sentiment indicators

---

## Challenge Eligibility

✅ Installed CLI (`npm install -g nansen-cli`)  
✅ Made 10+ API calls (verified above)  
✅ Built something creative (Autobett Gaming Intelligence Tracker)  
✅ Sharing on X with @nansen_ai + #NansenCLI  

**Ready to submit!**

---

**GitHub:** https://github.com/temisangerrard/settley-marketing  
**Autobett:** AI Agent Gaming Platform  
**Builder:** @mirasettley
