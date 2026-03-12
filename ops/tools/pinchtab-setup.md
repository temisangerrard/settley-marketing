# PinchTab - Browser Automation for AI Agents

## Setup Complete ✅

**Installed:** 2026-03-09
**Version:** pinchtab 0.7.8
**Status:** Running on port 9867

## What It Does

PinchTab is a 12MB Go binary that provides HTTP API control over Chrome browsers. Built specifically for AI agent workflows.

## Key Benefits

| Feature | Benefit |
|---------|---------|
| **Token-efficient** | 800 tokens/page vs 10K+ for screenshots (12x savings) |
| **Multi-instance** | Parallel browser sessions with isolated profiles |
| **Self-contained** | No dependencies, works on Raspberry Pi |
| **Accessibility-first** | Stable element refs (not fragile coordinates) |
| **HTTP API** | Control via curl, CLI, or any HTTP client |

## Installation

```bash
curl -fsSL https://pinchtab.com/install.sh | bash
```

## Usage

### Start Server
```bash
pinchtab
# Runs on http://localhost:9867
```

### Basic Commands
```bash
# Navigate
pinchtab nav https://example.com

# Get interactive elements
pinchtab snap -i -c

# Click element
pinchtab click e5

# Fill input
pinchtab fill e3 "text"

# Extract text (token-efficient)
pinchtab text

# Full page screenshot
pinchtab screenshot
```

### HTTP API Example
```bash
# Navigate
curl -X POST http://localhost:9867/actions/nav \
  -H "Content-Type: application/json" \
  -d '{"url":"https://example.com"}'

# Get snapshot
curl http://localhost:9867/snapshot?filter=interactive
```

## Use Cases for Settley

### 1. Competitor Monitoring ✅
**Script:** `scripts/monitor-lofty.sh`
- Tracks Lofty.ai property listings
- Monitors yield changes, new properties
- Output: `ops/competitor-tracking/lofty/`

### 2. Investor Research
- Scrape investor databases (Crunchbase, AngelList)
- Extract contact info, investment thesis
- Build prospecting lists automatically

### 3. Arena Agent Data Collection
- Pull HM Land Registry data
- Scrape Rightmove, Zoopla for property comps
- Real-time yield calculations

### 4. Content Distribution
- Multi-profile posting to different platforms
- Isolated sessions for different brands
- Automated cross-posting workflows

## Token Efficiency Test

**Lofty.ai Homepage:**
- Screenshot method: ~10,000 tokens
- PinchTab text extraction: 4,973 characters (~800 tokens)
- **Savings: 92% reduction**

## Running Scripts

### Manual Competitor Scan
```bash
cd /Users/temisan/Downloads/settley-marketing
./scripts/monitor-lofty.sh
```

### Automated (Cron)
```bash
# Add to crontab: run daily at 9 AM
0 9 * * * cd /Users/temisan/Downloads/settley-marketing && ./scripts/monitor-lofty.sh
```

## Troubleshooting

### Error: "profile already has active instance"
**Fix:** Wait 2-3 seconds for server to initialize, or restart:
```bash
pkill pinchtab
pinchtab
```

### Error: "auto-launch failed"
**Fix:** Check if Chrome is running, kill conflicting processes:
```bash
pkill -f "Chrome"
pinchtab
```

### Health Check
```bash
curl http://localhost:9867/health
# Should return: {"mode":"dashboard","status":"ok"}
```

## Next Steps

1. ✅ Test basic navigation/snapshot - DONE
2. ✅ Create competitor monitoring script - DONE
3. ⏳ Set up automated daily scans (cron)
4. ⏳ Build investor research scraper
5. ⏳ Integrate with Arena Agent data collection

## Resources

- Docs: https://pinchtab.com/docs
- GitHub: https://github.com/pinchtab/pinchtab
- SMCP Plugin: Available for AI agent integration (15 tools)
