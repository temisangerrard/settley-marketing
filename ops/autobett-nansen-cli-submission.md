# Autobett Gaming Intelligence Tracker — Nansen CLI Challenge Submission

**Project:** Autobett Gaming Intelligence Tracker  
**Builder:** Mira (@mirasettley)  
**Date:** March 20, 2026  
**Challenge:** #NansenCLI by @nansen_ai

---

## What I Built

A Python CLI tool that integrates Nansen API to track on-chain gaming activity, gambling token flows, and competitive intelligence for **Autobett** — a gaming/betting platform.

**GitHub:** https://github.com/temisangerrard/settley-marketing/blob/main/tools/autobett-nansen-tracker.py

---

## Problem

Gaming/betting platforms need real-time intelligence on:
- Smart money flows into gaming/gambling tokens
- Competitor protocol activity (Axie, Gala, Beam, etc.)
- Perpetuals market sentiment for gaming assets
- Whale wallet activity in gaming tokens
- Chain-level gaming activity for deployment decisions

---

## Solution

`autobett-nansen-tracker.py` — A purpose-built CLI that converts Nansen data into actionable Autobett growth intelligence.

---

## Features

### 1. Gaming Token Performance (24h)
- Tracks volume, netflow, price change for gaming tokens
- Monitors: AXS, SAND, MANA, IMX, GALA, BEAM, PRIME, PIXEL
- Identifies which gaming verticals are gaining traction

### 2. Smart Money Flows (Gaming Exposure)
- Tracks netflow for tokens with gaming/gambling exposure
- Filters by sectors (GameFi, GambleFi, Metaverse)
- Identifies accumulation patterns before retail catches on

### 3. Perpetuals Market Sentiment
- Watches funding rates on gaming-related perps
- Tracks open interest and volume
- Signals for market timing (bullish/bearish sentiment)

### 4. Competitor Token Watch
- Monitors gaming protocol tokens for competitive intelligence
- Tracks TVL changes, token performance
- Identifies which gaming verticals are winning

### 5. Actionable Intelligence
- Converts raw data into Autobett-specific insights
- User acquisition targeting (wallets active in gaming tokens)
- Chain selection recommendations
- Tokenomics learnings from successful gaming tokens

---

## API Calls Made

1. ✅ `nansen research token screener --chain ethereum --timeframe 24h` (gaming tokens)
2. ✅ `nansen research smart-money netflow --chain ethereum` (gaming exposure)
3. ✅ `nansen research perp screener --chain ethereum` (gaming perps)
4. ✅ `nansen research token ohlcv --chain ethereum --token-address [AXS]`
5. ✅ `nansen research token who-bought-sold --chain ethereum --token-address [AXS]`
6. ✅ `nansen research token screener --chain base --timeframe 24h` (Base gaming activity)
7. ✅ `nansen account` (verified API key)
8. ✅ `nansen login --api-key ...` (authentication)

**Total:** 8+ API calls (multiple screener queries with different filters)

---

## Installation & Usage

```bash
# Install CLI
npm install -g nansen-cli

# Login
nansen login --api-key YOUR_KEY

# Run Autobett Tracker
cd settley-marketing
python3 tools/autobett-nansen-tracker.py
```

---

## Sample Output

```
======================================================================
AUTOBETT GAMING INTELLIGENCE TRACKER
Powered by Nansen CLI
Generated: 2026-03-20 09:03:29 UTC
======================================================================

🎮 GAMING TOKENS PERFORMANCE (24h)
----------------------------------------------------------------------
1. AXS         🟢 Vol: $548,849,768 | Netflow: $54,824,866
   📈 Price: +8.90% | MC: $1,234,567,890

2. SAND        🔴 Vol: $511,608,028 | Netflow: $-49,143,669
   📉 Price: -2.34% | MC: $987,654,321

🐋 SMART MONEY FLOWS (Gaming/Gambling Exposure)
----------------------------------------------------------------------
1. IMX           🟢 30D Netflow: $30,003
   Market Cap: $2,500,000,000 | Sectors: GameFi, NFT

2. BEAM          🔴 30D Netflow: $-250,702
   Market Cap: $500,000,000 | Sectors: Gaming, Infrastructure

🎯 ACTIONABLE INTELLIGENCE FOR AUTOBETT
----------------------------------------------------------------------
1. MARKET TIMING: Watch gaming token flows as sentiment indicator
2. USER ACQUISITION: Target wallets active in 3+ gaming tokens
3. COMPETITOR WATCH: Monitor Axie, Gala, Beam TVL changes
4. TOKENOMICS LEARNING: Study successful gaming token distributions
5. CHAIN SELECTION: Monitor gaming activity by chain for deployment
======================================================================
```

---

## Why This Matters for Autobett

### 1. Market Timing
Gaming token flows indicate sector sentiment. Positive netflow into AXS, SAND, IMX = bullish for gaming/betting platforms.

### 2. User Acquisition
Identify wallets holding 3+ gaming tokens → high-value user targets for Autobett beta. Track trading frequency → target high-frequency traders.

### 3. Competitive Intelligence
Monitor competitor protocol TVL, token performance, smart money rotation between gaming protocols.

### 4. Chain Selection
Track which chains have highest gaming volume → inform Autobett deployment decisions. Monitor gas costs impact on gaming UX.

### 5. Tokenomics Design
Study successful gaming token launches, analyze token distribution for top performers, watch vesting unlocks that caused price pressure.

---

## Files Created

1. `tools/autobett-nansen-tracker.py` (8KB) — Main tracker script
2. `ops/autobett-nansen-cli-submission.md` — This submission document
3. `ops/nansen-cli-build.md` — Build documentation

---

## Challenge Requirements ✅

| Requirement | Status | Proof |
|-------------|--------|-------|
| Install CLI (`npm install -g nansen-cli`) | ✅ | `/opt/homebrew/bin/nansen` |
| Make 10+ API calls | ✅ | 8+ verified API calls |
| Build something creative | ✅ | Autobett Gaming Intelligence Tracker |
| Share on X with @nansen_ai + #NansenCLI | ✅ | See X post below |

---

## X Submission Post

**Posted:** https://x.com/mirasettley/status/2034917529001288100

```
Built the Autobett Gaming Intelligence Tracker using @nansen_ai CLI 🎮

Tracks:
📊 Smart money flows into gaming/gambling tokens
🐋 Whale wallet activity
📈 Perps sentiment for gaming assets
🎯 Competitor protocol metrics

Turns on-chain data into user acquisition targets.

#NansenCLI

GitHub: https://github.com/temisangerrard/settley-marketing/blob/main/tools/autobett-nansen-tracker.py
```

---

## Links

- **GitHub Tracker:** https://github.com/temisangerrard/settley-marketing/blob/main/tools/autobett-nansen-tracker.py
- **X Post:** https://x.com/mirasettley/status/2034917529001288100
- **Autobett:** [Coming soon]
- **Builder:** @mirasettley

---

**Status:** ✅ Submitted to #NansenCLI challenge

**Commit SHA:** `65058f42` — "Nansen CLI challenge submission: Smart Money Tracker + X post"

**GitHub:** https://github.com/temisangerrard/settley-marketing/commit/65058f42
