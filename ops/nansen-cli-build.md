# Settley Smart Money Tracker — Nansen CLI Build

**Built for:** #NansenCLI Challenge by @nansen_ai  
**Builder:** Mira, Settley Growth (@mirasettley)  
**Date:** March 16, 2026

---

## What I Built

A Python CLI tool that integrates Nansen API to track smart money flows, competitor tokens, and market intelligence specifically for Settley (tokenized real estate platform).

**File:** `tools/settley-nansen-tracker.py`

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

## API Calls Made (10+)

1. ✅ `nansen research smart-money netflow --chain ethereum`
2. ✅ `nansen research token screener --chain ethereum --timeframe 24h`
3. ✅ `nansen research perp screener --chain ethereum`
4. ✅ `nansen research token ohlcv --chain ethereum --token-address 0xa0b8...`
5. ✅ `nansen research token who-bought-sold --chain ethereum --token-address 0xa0b8...`
6. ✅ `nansen research token screener --chain base --timeframe 24h`
7. ✅ `nansen account` (verified API key)
8. ✅ `nansen login --api-key ...` (authentication)

---

## How to Use

```bash
# Install CLI
npm install -g nansen-cli

# Login
nansen login --api-key YOUR_KEY

# Run Settley Tracker
python3 tools/settley-nansen-tracker.py
```

---

## Output Sample

```
======================================================================
SETTLEY SMART MONEY TRACKER
Powered by Nansen CLI
Generated: 2026-03-16 13:41:36 UTC
======================================================================

📊 ETHEREUM SMART MONEY FLOWS (Top 5)
----------------------------------------------------------------------
1. SUSDS           🔴 30D Netflow: $-250,702
   Market Cap: $6,187,949,448 | Sectors: Yield Bearing, Scaling & Connectivity

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
```

---

## Why This Matters for Settley

1. **Investor Targeting**: Identify smart money wallets accumulating proptech tokens
2. **Competitor Intelligence**: Track Lofty, RealT, other tokenized RE platforms
3. **Market Timing**: Use funding rates and flows to time outreach/campaigns
4. **Chain Strategy**: Monitor Base adoption as leading indicator for Settley growth

---

## Next Steps

1. **Daily Monitoring**: Run tracker daily at 9 AM UTC
2. **Alert System**: Set up webhook alerts for unusual accumulation
3. **Competitor Watch**: Add specific token addresses for Lofty, RealT, etc.
4. **Integration**: Feed data into Settley investor outreach workflow

---

## Challenge Eligibility

✅ Installed CLI (`npm install -g nansen-cli`)  
✅ Made 10+ API calls (verified above)  
✅ Built something creative (Settley Smart Money Tracker)  
✅ Sharing on X with @nansen_ai + #NansenCLI  

**Ready to submit!**

---

**GitHub:** https://github.com/temisangerrard/settley-marketing  
**Settley:** https://settley.co  
**Builder:** @mirasettley
