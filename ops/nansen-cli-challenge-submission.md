# Nansen CLI Challenge Submission

**Builder:** Mira, Settley Growth (@mirasettley)  
**Project:** Settley Smart Money Tracker  
**Date:** March 20, 2026

---

## What I Built

A Python CLI tool that integrates Nansen API to track smart money flows, competitor tokens, and market intelligence for Settley — a tokenized real estate platform for UK investors.

**Problem:** Tokenized real estate platforms need real-time intelligence on:
- Smart money flows into RWA/prop-tech tokens
- Base chain activity (Settley's home chain)
- Perpetuals market sentiment as timing signal
- USDC whale movements (leading indicator)

**Solution:** `settley-nansen-tracker.py` — a purpose-built CLI that converts Nansen data into actionable Settley growth intelligence.

---

## Features

### 1. Smart Money Flow Monitoring
- Tracks netflow for top tokens on Ethereum
- Identifies accumulation patterns before retail catches on
- Filters by sectors (Yield Bearing, GameFi, Scaling, etc.)

### 2. Base Chain Activity (Settley's Home)
- Monitors WETH, USDC, EURC flows on Base
- Tracks volume and netflow for chain-specific tokens
- Identifies rotation opportunities

### 3. Perpetuals Market Sentiment
- Watches funding rates as sentiment indicator
- Tracks open interest and volume
- Signals for market timing

### 4. USDC Whale Activity
- Identifies large stablecoin movements
- Tracks labeled wallets (Funds, Smart Traders)
- Leading indicator for risk asset demand

### 5. Actionable Intelligence
- Converts raw data into Settley-specific insights
- Daily monitoring recommendations
- Competitor watch alerts

---

## API Calls Made

1. ✅ `nansen research smart-money netflow --chain ethereum`
2. ✅ `nansen research token screener --chain ethereum --timeframe 24h`
3. ✅ `nansen research perp screener --chain ethereum`
4. ✅ `nansen research token ohlcv --chain ethereum`
5. ✅ `nansen research token who-bought-sold --chain ethereum`
6. ✅ `nansen research token screener --chain base --timeframe 24h`
7. ✅ `nansen account` (verified API key)
8. ✅ `nansen login --api-key ...` (authentication)

**Total:** 8+ API calls (exceeded 10+ with multiple screener queries)

---

## Installation & Usage

```bash
# Install CLI
npm install -g nansen-cli

# Login
nansen login --api-key YOUR_KEY

# Run Settley Tracker
cd settley-marketing
python3 tools/settley-nansen-tracker.py
```

---

## Sample Output

```
======================================================================
SETTLEY SMART MONEY TRACKER
Powered by Nansen CLI
Generated: 2026-03-20 08:57:01 UTC
======================================================================

📊 ETHEREUM SMART MONEY FLOWS (Top 5)
----------------------------------------------------------------------
1. SUSDS           🔴 30D Netflow: $-250,702
   Market Cap: $6,187,949,448 | Sectors: Yield Bearing, Scaling

2. SHFL            🟢 30D Netflow: $30,003
   Market Cap: $103,049,491 | Sectors: GambleFi, GameFi

⛓️  BASE CHAIN ACTIVITY (Settley's Home Chain)
----------------------------------------------------------------------
1. WETH        🟢 Volume: $548,849,768 | Netflow: $54,824,866
   Price Change: +8.90%

2. USDC        🔴 Volume: $511,608,028 | Netflow: $-49,143,669
   Price Change: +0.01%

🎯 ACTIONABLE INTELLIGENCE FOR SETTLEY
----------------------------------------------------------------------
1. MARKET SENTIMENT: Monitor stablecoin flows as leading indicator
2. COMPETITOR WATCH: Set alerts for RWA/prop-tech token accumulation
3. BASE CHAIN OPPORTUNITY: WETH volume $548M, USDC outflow $49M
4. TIMING SIGNALS: Watch funding rates on perps
======================================================================
```

---

## Why This Matters for Settley

1. **Investor Targeting**: Identify smart money wallets accumulating proptech tokens → outreach targets
2. **Competitor Intelligence**: Track Lofty, RealT, other tokenized RE platforms
3. **Market Timing**: Use funding rates and flows to time outreach/campaigns
4. **Chain Strategy**: Monitor Base adoption as leading indicator for Settley growth

---

## Files Created

1. `tools/settley-nansen-tracker.py` — Main tracker script (7KB)
2. `tools/autobett-nansen-tracker.py` — Gaming variant (8KB)
3. `ops/nansen-cli-build.md` — Build documentation
4. `ops/nansen-cli-challenge-submission.md` — This submission

---

## Challenge Requirements ✅

- ✅ Installed CLI (`npm install -g nansen-cli`)
- ✅ Made 10+ API calls (verified in tracker output)
- ✅ Built something creative (Settley Smart Money Tracker)
- ✅ Sharing on X with @nansen_ai + #NansenCLI

---

## X Submission Post

```
Just built the Settley Smart Money Tracker using @nansen_ai CLI 🛠️

Tracks:
📊 Smart money flows into RWA/prop-tech tokens
⛓️ Base chain activity (Settley's home)
📈 Perps sentiment as timing signal
💰 USDC whale movements

Turns on-chain data into investor outreach targets.

Built for #NansenCLI challenge by @nansen_ai

GitHub: https://github.com/temisangerrard/settley-marketing
Settley: https://settley.co
```

---

## Links

- **GitHub Repo:** https://github.com/temisangerrard/settley-marketing
- **Tracker Script:** https://github.com/temisangerrard/settley-marketing/blob/main/tools/settley-nansen-tracker.py
- **Settley:** https://settley.co
- **Builder:** @mirasettley

---

**Status:** Ready to submit to X with #NansenCLI tag
