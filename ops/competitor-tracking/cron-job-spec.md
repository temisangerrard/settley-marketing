# Cron Job Specification - Daily Competitive Intelligence

**Job Name:** Daily: Competitive Intelligence Check  
**Schedule:** 8:00 AM Europe/London (daily)  
**Owner:** Mira  
**Priority:** High (growth-critical)

---

## Job Configuration

```json
{
  "name": "Daily: Competitive Intelligence Check",
  "schedule": {
    "kind": "cron",
    "expr": "0 8 * * *",
    "tz": "Europe/London"
  },
  "payload": {
    "kind": "agentTurn",
    "message": "Run daily competitive intelligence check:\n1. Check Google Alerts inbox (mirasettley@gmail.com) for new alerts\n2. Run SERP check for 5 priority keywords\n3. Check competitor homepages for changes\n4. Scan Twitter/X for competitor mentions\n5. Generate daily report in ops/competitor-tracking/daily-reports/\n6. Flag any RED or YELLOW alerts for immediate attention\n7. Update memory/YYYY-MM-DD.md with findings",
    "timeoutSeconds": 300
  },
  "sessionTarget": "isolated",
  "enabled": true,
  "delivery": {
    "mode": "announce",
    "channel": "telegram",
    "to": "795232660"
  }
}
```

---

## Daily Task Checklist

The cron job should execute these steps:

### 1. Email Check (mirasettley@gmail.com)
- [ ] Scan for Google Alerts notifications
- [ ] Scan for competitor press releases
- [ ] Flag urgent alerts (funding announcements, major launches)

### 2. SERP Check (5 Priority Keywords)
- [ ] "tokenized real estate" - UK
- [ ] "lofty.ai alternative" - UK
- [ ] "fractional real estate investing" - UK
- [ ] "settley" - UK
- [ ] "invest in real estate with $100" - UK

Record:
- Settley position (if ranking)
- Lofty.ai position
- New domains in top 10
- AI Overview presence

### 3. Competitor Website Check
- [ ] Lofty.ai homepage (visual change detection)
- [ ] Fundrise homepage (visual change detection)
- [ ] Check for new blog posts/announcements

### 4. Social Media Scan
- [ ] Twitter/X: "lofty.ai" mentions (last 24h)
- [ ] Twitter/X: "tokenized real estate" (last 24h)
- [ ] LinkedIn: Competitor posts

### 5. Report Generation
- [ ] Create/update daily report markdown file
- [ ] Update SERP tracking spreadsheet
- [ ] Log any alerts in alert log

### 6. Alert Classification
**RED ALERT** (Message Temisan immediately):
- New well-funded competitor
- Major price drop (>20%)
- Settley brand keyword drops below #5
- Major platform enters space

**YELLOW ALERT** (Include in report, review within 24h):
- New competitor in top 10
- Competitor feature launch
- Negative sentiment spike

**GREEN** (Log only):
- Minor SERP changes (±2 positions)
- Routine blog posts

### 7. Memory Update
- [ ] Update `memory/YYYY-MM-DD.md` with key findings
- [ ] Add any action items to tomorrow's priorities

---

## Alert Delivery

**Default:** Announce to Telegram channel (Temisan's chat)

**RED ALERT:** Immediate message with:
```
🚨 COMPETITIVE INTELLIGENCE ALERT

Type: [Competitor Launch / Price Drop / SERP Drop / Platform Entry]
Severity: HIGH
Action Required: [Specific action]

Details:
[2-3 sentence summary]

Full Report: [link to daily report]
```

**Weekly Summary:** Friday 3:00 PM
- Week's key findings
- Trends identified
- Recommended actions for next week

---

## Failure Handling

**If job times out (>5 min):**
- Log timeout in alert log
- Send message: "⚠️ CI check timed out - manual check required"
- Retry once after 1 hour

**If email access fails:**
- Skip email check
- Continue with other checks
- Log: "Email check skipped - access issue"

**If SERP check fails:**
- Use cached data from previous day
- Log: "SERP check failed - using cached data"
- Flag for manual review

---

## Success Metrics

| Metric | Target | Measurement |
|--------|--------|-------------|
| Job completion rate | >95% | Cron run logs |
| Alert detection time | <24 hours | Alert timestamp vs. event |
| Report generation | Daily by 9 AM | Report file timestamps |
| False positive rate | <10% | Alert accuracy review |

---

## Manual Override

**To run manually:**
```bash
# Run the SERP checker script
python3 ops/competitor-tracking/scripts/serp_checker.py

# Or trigger via cron
openclaw cron run <job-id>
```

**To pause job:**
```bash
openclaw cron update <job-id> --enabled=false
```

**To review past runs:**
```bash
openclaw cron runs <job-id>
```

---

## Integration with Other Systems

### Memory System
- Daily findings → `memory/YYYY-MM-DD.md`
- Weekly summary → `memory/learnings.md`
- Major alerts → `MEMORY.md` (if strategically significant)

### Content Pipeline
- Competitor content gaps → Content agent topics
- Competitor announcements → Response content (blog, social)

### Investor Outreach
- Competitor funding news → Update investor narrative
- Market trends → Include in investor updates

### Product Development
- Feature gaps → Product backlog items
- Competitive threats → Priority features

---

## Phase 2 Upgrades (Week 3-4)

1. **SERP API Integration**
   - Add DataForSEO or SerpAPI key
   - Automate full keyword tracking (17 keywords)
   - Store historical data for trend analysis

2. **Visual Change Detection**
   - Integrate Visualping API
   - Automated screenshot comparison
   - Alert on >10% visual change

3. **Social Listening**
   - Twitter API integration
   - Sentiment analysis
   - Influencer mention tracking

4. **Dashboard**
   - Google Data Studio or custom dashboard
   - Real-time SERP positions
   - Competitor traffic trends

---

**Created:** 2026-03-20  
**First Run:** 2026-03-21 8:00 AM  
**Review Date:** 2026-03-27 (after 7 days of data)
