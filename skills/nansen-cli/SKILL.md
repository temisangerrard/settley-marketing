---
name: nansen-cli
description: Use the Nansen CLI to access on-chain intelligence data. Use when you need smart money flows, token analytics, whale tracking, or market sentiment data for crypto/DeFi research.
---

# Nansen CLI Skill

Access Nansen's on-chain analytics platform via CLI. Provides smart money tracking, token analytics, whale movements, and market intelligence.

## Before Using

Gather this context:

### 1. Authentication
- API key required: `nansen login --api-key <key>`
- Get key at: https://app.nansen.ai/api
- Alternative: x402 micropayments via `nansen wallet create`

### 2. Data Requirements
- What chain? (ethereum, solana, base, arbitrum, polygon, etc.)
- What timeframe? (24h, 7d, 30d, etc.)
- What data type? (smart money, token, perp, wallet, etc.)

### 3. Output Format
- `--pretty` for human-readable JSON
- `--table` for tabular output
- `--format csv` for spreadsheet import

---

## Available Commands

### Smart Money Tracking
```bash
nansen research smart-money netflow --chain ethereum --limit 10
nansen research smart-money dex-trades --chain ethereum --limit 5
```

### Token Analytics
```bash
nansen research token screener --chain ethereum --timeframe 24h --limit 10
nansen research token ohlcv --chain ethereum --token-address 0x... --timeframe 1h
nansen research token who-bought-sold --chain ethereum --token-address 0x... --timeframe 24h
```

### Perpetuals Data
```bash
nansen research perp screener --chain ethereum --limit 10
nansen research perp leaderboard --chain ethereum --limit 5
```

### Wallet Analysis
```bash
nansen wallet create
nansen wallet list
nansen account
```

---

## Usage Examples

### Track Smart Money Flows
```bash
nansen research smart-money netflow --chain ethereum --limit 5 --pretty
```

**Use when:** You want to see which tokens smart money is accumulating

### Token Performance
```bash
nansen research token screener --chain base --timeframe 24h --limit 10 --pretty
```

**Use when:** Researching token performance on specific chain

### Whale Activity
```bash
nansen research token who-bought-sold --chain ethereum --token-address 0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48 --timeframe 24h --limit 5 --pretty
```

**Use when:** Tracking large holder movements for specific token

---

## Common Issues

### "Insufficient credits"
- Free tier has limited API calls
- Solution: Wait for credit reset or upgrade plan

### "API key required"
- Run: `nansen login --api-key <your-key>`
- Or set env var: `export NANSEN_API_KEY=<your-key>`

### "Unknown subcommand"
- Check available commands: `nansen research --help`
- Some commands require specific chains or parameters

---

## Output Interpretation

### Smart Money Netflow
- Positive netflow = accumulation (bullish)
- Negative netflow = distribution (bearish)
- Track 30d trends for conviction

### Token Screener
- Volume: Trading activity level
- Netflow: Buy vs sell pressure
- Market cap: Token valuation
- Price change: 24h performance

### Perpetuals
- Funding rate: Long/short sentiment
- Open interest: Total positions
- Volume: Trading activity

---

## Related Skills

- **trading-analysis**: For deeper trading strategy analysis
- **defi-research**: For DeFi protocol research
- **on-chain-alerts**: For setting up automated alerts

---

## Best Practices

1. **Start with broad queries** (screener) then narrow down (specific tokens)
2. **Use pretty format** for initial exploration
3. **Check credit balance** before running large queries: `nansen account`
4. **Cache results** for repeated analysis (data doesn't change frequently)
5. **Combine with other data sources** for complete picture
