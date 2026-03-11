# Arena Play — Autoplay Feature + Admin Dashboard

**Hackathon:** Synthesis MD (March 13-25, 2026)
**Bounty:** Celo — $10K in bounties
**Submission:** Arena Play with Autoplay + Agent Evaluation Dashboard
**Timeline:** 12 days (March 13-25)

---

## 🎯 Hackathon Fit

### Why Arena Play Wins

**Synthesis Theme:** "Agents that pay, trust, cooperate, keep secrets"

**Arena Play Alignment:**
- ✅ **Agents that pay** — Bots wager USDC, win/lose real money
- ✅ **Agents that trust** — On-chain settlement, transparent outcomes
- ✅ **Agents that cooperate** — PVP competition, multi-agent environment
- ✅ **Agents that keep secrets** — Strategy configs, private keys, wallet security

**Celo Bounty Fit:**
- Arena Play uses crypto payments (USDC)
- Can integrate Celo blockchain for settlements
- Real-world utility (autonomous agent competition)
- Celo's agent can judge by playing against Arena bots

---

## 📋 Autoplay Feature Brief

### Problem Statement

**Current State:**
- Users must be present to play
- Manual gameplay only (approach station → place stake → select option)
- No bot persistence when user logs off
- Limited data collection for agent evaluation

**Goal:**
- Users configure bot once → bot plays autonomously
- Bot keeps playing when user logs off
- Configurable strategy (games, stakes, frequency)
- Rich data collection for agent performance analysis

---

### User Stories

#### 1. Bot Configuration

**As a player, I want to:**
- Set my bot's personality (Aggressive, Conservative, Balanced, Custom)
- Choose which games my bot plays (RPS, Dice, Heads/Tails, BTC prediction)
- Set wager amounts (fixed USDC, % of wallet, dynamic)
- Set bet frequency (games per minute, cooldown between bets)
- Set stop-loss limits (stop after losing X USDC)
- Set take-profit targets (stop after winning X USDC)
- Fund my bot's wallet (~$10 for testing)

**So that:**
- My bot can play while I'm offline
- I can test different strategies
- I can limit my risk exposure

---

#### 2. Bot Monitoring

**As a player, I want to:**
- See my bot's current status (active, paused, stopped)
- View live performance (wins, losses, profit/loss)
- Get notifications for big wins/losses
- Pause/resume my bot anytime
- Withdraw winnings anytime

**So that:**
- I can track my bot's performance
- I can intervene if needed
- I can cash out when ahead

---

#### 3. Admin Dashboard (Research/Evaluation)

**As a researcher, I want to:**
- Monitor all active bots in the arena
- Filter by game type, personality, stake size
- View aggregate statistics (win rates, profitability)
- Export data for analysis (CSV, JSON)
- Run A/B tests on bot configurations
- Compare agent performance across configs

**So that:**
- I can evaluate agent strategies
- I can publish research on agent behavior
- I can improve the Arena Play system

---

### Technical Requirements

#### Frontend (UI/UX)

**Bot Configuration Page:**
```
┌────────────────────────────────────────────────┐
│  🤖 Configure Your Bot                         │
├────────────────────────────────────────────────┤
│  Personality: [Aggressive ▼]                   │
│  ┌──────────────────────────────────────────┐  │
│  │ ○ Aggressive  (high stakes, frequent)    │  │
│  │ ○ Conservative (low stakes, selective)   │  │
│  │ ○ Balanced    (medium stakes, moderate)  │  │
│  │ ○ Custom      (tune all settings)        │  │
│  └──────────────────────────────────────────┘  │
│                                                 │
│  Games to Play:                                 │
│  ☑ Rock Paper Scissors                         │
│  ☑ Heads or Tails                              │
│  ☐ Dice                                        │
│  ☐ BTC Market (5min)                           │
│  ☐ BTC Market (24hr)                           │
│                                                 │
│  Wager Amount:                                  │
│  ○ Fixed: [____] USDC per game                 │
│  ○ Percentage: [____]% of wallet               │
│  ○ Dynamic: [Martingale ▼]                     │
│                                                 │
│  Bet Frequency:                                 │
│  Games per minute: [____]                      │
│  Cooldown between bets: [____] seconds         │
│                                                 │
│  Stop Conditions:                               │
│  Stop-loss: [____] USDC (stop after losing)    │
│  Take-profit: [____] USDC (stop after winning) │
│                                                 │
│  Wallet Balance: 10.00 USDC                    │
│  [Fund Wallet] [Start Bot] [Cancel]            │
└────────────────────────────────────────────────┘
```

**Live Bot Status Page:**
```
┌────────────────────────────────────────────────┐
│  🤖 Bot Status: ● ACTIVE                       │
├────────────────────────────────────────────────┤
│  Session Stats:                                │
│  Games Played: 47                              │
│  Wins: 28 (59.6%)                              │
│  Losses: 19                                    │
│  Profit: +3.50 USDC                            │
│                                                 │
│  Recent Games:                                 │
│  ✅ RPS vs @player123  +1.00 USDC             │
│  ❌ Heads/Tails vs @bot456  -1.00 USDC        │
│  ✅ Dice vs @player789  +2.00 USDC            │
│  ...                                           │
│                                                 │
│  [Pause Bot] [Stop Bot] [Withdraw]            │
└────────────────────────────────────────────────┘
```

**Admin Dashboard (Research View):**
```
┌────────────────────────────────────────────────┐
│  📊 Arena Analytics — All Bots                 │
├────────────────────────────────────────────────┤
│  Filters:                                      │
│  Game: [All ▼]  Personality: [All▼]  Time: [24h▼]│
├────────────────────────────────────────────────┤
│  Aggregate Stats:                              │
│  Active Bots: 127                              │
│  Total Games (24h): 1,847                      │
│  Avg Win Rate: 52.3%                           │
│  Total Volume: 18,470 USDC                     │
│                                                 │
│  By Personality:                               │
│  ┌──────────────┬──────────┬─────────────┐    │
│  │ Personality  │ Win Rate │ Profit/Game │    │
│  ├──────────────┼──────────┼─────────────┤    │
│  │ Aggressive   │ 48.2%    │ -0.12 USDC  │    │
│  │ Conservative │ 55.8%    │ +0.08 USDC  │    │
│  │ Balanced     │ 52.1%    │ +0.02 USDC  │    │
│  └──────────────┴──────────┴─────────────┘    │
│                                                 │
│  By Game Type:                                 │
│  ┌──────────────┬──────────┬─────────────┐    │
│  │ Game         │ Win Rate │ Volume      │    │
│  ├──────────────┼──────────┼─────────────┤    │
│  │ RPS          │ 51.2%    │ 8,230 USDC  │    │
│  │ Heads/Tails  │ 53.8%    │ 5,120 USDC  │    │
│  │ Dice         │ 49.1%    │ 3,890 USDC  │    │
│  │ BTC 5min     │ 54.2%    │ 1,230 USDC  │    │
│  └──────────────┴──────────┴─────────────┘    │
│                                                 │
│  [Export CSV] [Export JSON] [Run A/B Test]    │
└────────────────────────────────────────────────┘
```

---

#### Backend (Infrastructure)

**Autoplay Engine:**
- Server-side bot logic (runs even when user offline)
- Game selection algorithm (based on config)
- Wager calculation (fixed, percentage, dynamic)
- Cooldown management (rate limiting)
- Stop-loss/take-profit enforcement
- Wallet balance monitoring

**Data Collection:**
- Every game logged: type, stake, outcome, opponent, timestamp
- Bot config snapshot at session start
- Performance metrics calculated in real-time
- Export functionality (CSV, JSON)

**Admin Dashboard API:**
- Aggregate statistics endpoint
- Filter by game type, personality, time range
- Bot listing with status
- A/B test runner (compare configs)

---

### Gamification Elements

**Visual Design:**
- Robot/avatar representing user's bot
- Animated status indicators (thinking, playing, won, lost)
- Progress bars (toward stop-loss/take-profit)
- Achievement badges (100 games, 50% win rate, profitable session)
- Leaderboards (top bots by profit, win rate, games played)

**Feedback:**
- Sound effects (win/loss, game start/end)
- Push notifications (big wins, stop conditions hit)
- Session summaries (email/SMS after bot stops)

---

## 📊 Research/Evaluation Framework

### What We Can Measure

#### 1. **Strategy Effectiveness**

| Personality | Win Rate | Profit/Game | Best Game | Worst Game |
|------------|----------|-------------|-----------|------------|
| Aggressive | ?% | ? USDC | ? | ? |
| Conservative | ?% | ? USDC | ? | ? |
| Balanced | ?% | ? USDC | ? | ? |

**Hypothesis:** Conservative bots have higher win rates but lower absolute profits.

---

#### 2. **Game Type Analysis**

| Game | Avg Win Rate | Avg Stake | Volume (24h) |
|------|--------------|-----------|--------------|
| RPS | ?% | ? USDC | ? USDC |
| Heads/Tails | ?% | ? USDC | ? USDC |
| Dice | ?% | ? USDC | ? USDC |
| BTC 5min | ?% | ? USDC | ? USDC |
| BTC 24hr | ?% | ? USDC | ? USDC |

**Hypothesis:** BTC prediction has highest variance, RPS most skill-dependent.

---

#### 3. **Wager Strategy Impact**

| Strategy | Ruin Rate | Avg Profit | Max Drawdown |
|----------|-----------|------------|--------------|
| Fixed 1 USDC | ?% | ? USDC | ? USDC |
| 5% of wallet | ?% | ? USDC | ? USDC |
| Martingale | ?% | ? USDC | ? USDC |

**Hypothesis:** Martingale has highest ruin rate, fixed stakes most sustainable.

---

#### 4. **Frequency Optimization**

| Games/Min | Win Rate | Profit/Hour | Burnout Rate |
|-----------|----------|-------------|--------------|
| 1 | ?% | ? USDC | ?% |
| 5 | ?% | ? USDC | ?% |
| 10 | ?% | ? USDC | ?% |
| 20 | ?% | ? USDC | ?% |

**Hypothesis:** Moderate frequency (5-10 games/min) optimal for profit vs. risk.

---

### Experiment Designs

#### Experiment 1: Personality Showdown
**Duration:** 7 days
**Setup:** 3 bot configs (Aggressive, Conservative, Balanced), 100 USDC each
**Measure:** Final balance, win rate, max drawdown
**Outcome:** Which personality is most profitable?

---

#### Experiment 2: Game Type Specialization
**Duration:** 7 days
**Setup:** 5 bots, each plays only one game type
**Measure:** Win rate, profit/game, volume
**Outcome:** Which game favors autonomous agents?

---

#### Experiment 3: Wager Strategy Stress Test
**Duration:** 7 days
**Setup:** 3 bots with different wager strategies, 100 USDC each
**Measure:** Ruin rate, final balance, volatility
**Outcome:** Which strategy is most sustainable?

---

## 🏆 Hackathon Submission Plan

### Deliverables

**1. Working Autoplay Feature**
- Bot configuration UI
- Server-side autoplay engine
- Live status monitoring
- Stop-loss/take-profit enforcement

**2. Admin Dashboard**
- Aggregate analytics
- Filter by game/personality/time
- Export functionality
- A/B test runner

**3. Research Paper (Blog Post)**
- "Autonomous Agent Competition: Lessons from 10,000 Games"
- Methodology (experiment design)
- Results (win rates, profitability, optimal configs)
- Code + data open-sourced

**4. Demo Video (3 min)**
- Show bot configuration
- Show live gameplay (bot playing autonomously)
- Show admin dashboard
- Show research findings

---

### Timeline

| Date | Milestone |
|------|-----------|
| **Mar 13** | Hackathon starts, begin autoplay development |
| **Mar 15** | Bot configuration UI complete |
| **Mar 17** | Autoplay engine working (server-side) |
| **Mar 19** | Admin dashboard (basic analytics) |
| **Mar 21** | First experiment running (100+ games) |
| **Mar 22** | Building closes, final polish |
| **Mar 23** | Research paper drafted |
| **Mar 24** | Demo video recorded |
| **Mar 25** | Submission complete |

---

### Judging Criteria (Synthesis MD)

**Agent Autonomy:** ✅ Bots play without human intervention
**Real-World Utility:** ✅ Real money, real competition
**Trust/Transparency:** ✅ On-chain settlement, open data
**Celo Integration:** ⚠️ Can integrate Celo for USDC payments
**Research Value:** ✅ First large-scale agent competition dataset

---

## 🔧 Technical Stack

**Frontend:**
- React (existing Arena Play codebase)
- Tailwind CSS (gamified UI)
- Recharts (analytics charts)

**Backend:**
- Node.js (existing Arena Play server)
- WebSocket (live bot status updates)
- PostgreSQL (game logs, bot configs)

**Blockchain:**
- Current: ETH + USDC (ERC-20)
- Hackathon: Integrate Celo (cUSD or CELO)

**Analytics:**
- Custom aggregation queries
- CSV/JSON export
- A/B test framework (custom)

---

## 💰 Budget

**Development:** 0 USDC (sweat equity)
**Test Capital:** 50 USDC (5 bots × 10 USDC each)
**Hackathon Entry:** Free
**Total:** 50 USDC

---

## 🎯 Success Metrics

**Hackathon:**
- ✅ Top 3 finish (win bounty share)
- ✅ Celo agent judges Arena Play bots
- ✅ Press coverage (Synthesis MD partners)

**Product:**
- ✅ 50+ users enable autoplay in first week
- ✅ 1,000+ autonomous games played in first month
- ✅ Research paper published (Medium, Mirror, arXiv)

**Research:**
- ✅ 10,000+ games logged
- ✅ Statistically significant findings
- ✅ Open dataset for ML/RL researchers

---

## ⚠️ Risks & Mitigations

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| Autoplay bugs (bot loses money unexpectedly) | Medium | High | Stop-loss limits, testing with small stakes |
| Celo integration too complex | Medium | Medium | Fallback to ETH/USDC, note Celo compatibility |
| Not enough data for research | Low | Medium | Extend experiment duration, incentivize users |
| Hackathon submission incomplete | Low | High | Prioritize core features (autoplay + dashboard) |

---

## 📝 Next Steps

**Immediate (Today):**
1. ✅ Brief approved by Temisan
2. ⏳ Set up Celo wallet + get cUSD for testing
3. ⏳ Create hackathon registration (Arena Play submission)

**This Week (Mar 11-13):**
1. ⏳ Bot configuration UI design (Figma/mockup)
2. ⏳ Autoplay engine architecture (server-side logic)
3. ⏳ Admin dashboard wireframe

**Hackathon Week 1 (Mar 13-19):**
1. ⏳ Implement bot configuration page
2. ⏳ Implement autoplay engine
3. ⏳ Start first experiment (personality showdown)

**Hackathon Week 2 (Mar 20-25):**
1. ⏳ Admin dashboard (analytics + export)
2. ⏳ Research paper draft
3. ⏳ Demo video
4. ⏳ Submit to Synthesis MD

---

**File Location:** ops/arena-autoplay-brief.md
**Created:** 2026-03-11
**Owner:** Temisan (dev lead) + Mira (research + submission)
**Status:** Ready for development
