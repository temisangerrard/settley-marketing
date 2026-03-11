# Arena Play — Product Upgrades Roadmap

**Date:** 2026-03-11
**Status:** Draft for review
**Owner:** Temisan + @senatorT__

---

## Current State (As of 2026-03-11)

✅ **Live:**
- Email signup → instant bot + wallet
- Dashboard with wallet address
- USDC + ETH funding
- 3 games: RPS, Heads/Tails, Dice
- PVP (player vs player)
- Station-based gameplay

❌ **Missing/Broken:**
- Autoplay (OFF, being rebuilt)
- Gas abstraction (users pay own gas)
- Game discovery (manual approach required)

---

## Product Upgrades — Prioritized

### 🥇 Priority 1: Restore Autoplay (Core Feature)

**Problem:** Users can't set bot to play automatically. Must be present to play.

**Solution:**
- Autoplay configuration panel
- Strategy settings:
  - Which games to play (RPS, dice, heads/tails)
  - Bet size (fixed, % of wallet, martingale, etc.)
  - Stop-loss limit
  - Take-profit target
  - Cooldown between games
- Bot plays while user offline
- Push notifications for big wins/losses (optional)

**User Story:**
> "As a user, I want to set my bot's strategy and let it play while I'm at work, so I can earn even when I'm not actively playing."

**Technical Requirements:**
- Autoplay engine (server-side)
- Strategy configuration UI
- Wallet signing (auto-sign for approved bets)
- Safety limits (max loss per session)

**Effort Estimate:** 2-3 weeks

**Impact:** ⭐⭐⭐⭐⭐ (Core differentiator)

---

### 🥈 Priority 2: Gas Abstraction (UX Critical)

**Problem:** Users need ETH for gas. Friction for non-crypto natives.

**Solution:**
**Option A: Privy.io**
- Embedded wallets
- Gasless transactions (platform subsidizes)
- Email/social login (no seed phrases)

**Option B: Base (Coinbase L2)**
- Low gas fees
- Potential sponsorship (Base ecosystem grants)
- USDC native on Base

**Option C: Hybrid**
- Platform pays gas initially
- Deduct from winnings
- Or: include gas in bet amount

**User Story:**
> "As a new user, I want to just fund with USDC and play, without worrying about ETH or gas fees."

**Technical Requirements:**
- Privy.io integration OR Base deployment
- Gas estimation + subsidy logic
- Wallet abstraction layer

**Effort Estimate:** 1-2 weeks (Privy), 2-3 weeks (Base migration)

**Impact:** ⭐⭐⭐⭐⭐ (Removes major onboarding friction)

---

### 🥉 Priority 3: Game Lobby / Discovery

**Problem:** Users must manually approach stations/players. Hard to find games.

**Solution:**
- Lobby view (list of active games)
- Filter by:
  - Game type (RPS, dice, heads/tails)
  - Stake size (low, mid, high)
  - Player skill/ranking
- "Quick join" button (auto-match)
- Spectate mode (watch before playing)

**User Story:**
> "As a user, I want to see all available games and join with one click, instead of walking around looking for stations."

**Technical Requirements:**
- Lobby backend (game state tracking)
- Matchmaking logic
- UI for lobby + filters

**Effort Estimate:** 2-3 weeks

**Impact:** ⭐⭐⭐⭐ (Major UX improvement)

---

### Priority 4: Leaderboards + Rankings

**Problem:** No competition beyond individual games. No progression.

**Solution:**
- Global leaderboards (by winnings, win rate, games played)
- Weekly/monthly seasons
- Tiers/leagues (Bronze, Silver, Gold, Diamond)
- Rewards for top players (USDC prizes, badges)

**User Story:**
> "As a competitive player, I want to see how I rank against others and compete for prizes."

**Technical Requirements:**
- Ranking system (ELO or similar)
- Leaderboard backend
- Seasonal reset logic
- Prize distribution

**Effort Estimate:** 1-2 weeks

**Impact:** ⭐⭐⭐⭐ (Drives retention + competition)

---

### Priority 5: More Games

**Problem:** Only 3 games. Gets repetitive.

**Solution:**
**Near-term (easy):**
- Coin flip variants (best of 3, 5, 7)
- Dice variants (over/under, exact number)

**Mid-term (medium):**
- Card games (War, simple poker variants)
- Wheel of fortune

**Long-term (complex):**
- Multi-player games (3+ players)
- Team games

**User Story:**
> "As a user, I want variety in games so I don't get bored playing the same 3 games."

**Technical Requirements:**
- Game logic (smart contracts or server-side)
- UI for each game
- Balance testing (house edge, fairness)

**Effort Estimate:** 1 week per game (simple), 2-3 weeks (complex)

**Impact:** ⭐⭐⭐ (Retention, but not core)

---

### Priority 6: Social Features

**Problem:** No way to interact with other players beyond betting.

**Solution:**
- Friend system (add friends, see online status)
- Challenge friends directly
- Chat/emotes (limited, to prevent spam)
- Share results (Twitter, Discord)

**User Story:**
> "As a user, I want to challenge my friends and share my big wins."

**Technical Requirements:**
- Friend graph (database)
- Chat system (websocket or polling)
- Social sharing integration

**Effort Estimate:** 2-3 weeks

**Impact:** ⭐⭐⭐ (Viral growth, but not core)

---

### Priority 7: Tournaments

**Problem:** No structured competition.

**Solution:**
- Scheduled tournaments (daily, weekly)
- Entry fee (USDC)
- Prize pool (winner takes all, or top 3 split)
- Bracket system (single/double elimination)

**User Story:**
> "As a competitive player, I want to enter tournaments and compete for bigger prizes."

**Technical Requirements:**
- Tournament backend (brackets, scheduling)
- Registration system
- Prize distribution
- Anti-cheat (prevent collusion)

**Effort Estimate:** 3-4 weeks

**Impact:** ⭐⭐⭐⭐ (High engagement, marketing hook)

---

### Priority 8: Analytics Dashboard

**Problem:** Users can't track their performance over time.

**Solution:**
- Personal stats:
  - Total games played
  - Win rate
  - Total profit/loss
  - Best game type
  - Biggest win/loss
- Charts/graphs (performance over time)
- Export data (CSV)

**User Story:**
> "As a user, I want to see my performance history and understand my strategy effectiveness."

**Technical Requirements:**
- Analytics backend (event tracking)
- Dashboard UI
- Data aggregation

**Effort Estimate:** 1-2 weeks

**Impact:** ⭐⭐ (Nice-to-have, not critical)

---

### Priority 9: Mobile Optimization

**Problem:** Arena may not work well on mobile.

**Solution:**
- Responsive design
- Touch-friendly controls
- Mobile-first UI
- PWA (progressive web app)

**User Story:**
> "As a mobile user, I want to play on my phone without issues."

**Technical Requirements:**
- Responsive CSS
- Touch event handling
- PWA manifest + service worker

**Effort Estimate:** 2-3 weeks

**Impact:** ⭐⭐⭐⭐ (Mobile is where users are)

---

### Priority 10: Referral System

**Problem:** No built-in growth mechanism.

**Solution:**
- Referral links (unique per user)
- Reward: both referrer + referee get bonus (e.g., 5 USDC)
- Track referrals in dashboard
- Leaderboard for top referrers

**User Story:**
> "As a user, I want to invite friends and earn rewards when they play."

**Technical Requirements:**
- Referral tracking (codes, links)
- Reward distribution
- Fraud prevention (prevent self-referrals)

**Effort Estimate:** 1-2 weeks

**Impact:** ⭐⭐⭐⭐ (Viral growth)

---

## Recommended Roadmap

### Phase 1: Core Experience (4-6 weeks)
1. **Restore Autoplay** (2-3 weeks) — CRITICAL
2. **Gas Abstraction** (1-2 weeks) — CRITICAL
3. **Game Lobby** (2-3 weeks) — HIGH

### Phase 2: Engagement (4-6 weeks)
4. **Leaderboards** (1-2 weeks)
5. **More Games** (1-2 weeks)
6. **Mobile Optimization** (2-3 weeks)

### Phase 3: Growth (4-6 weeks)
7. **Tournaments** (3-4 weeks)
8. **Referral System** (1-2 weeks)
9. **Social Features** (2-3 weeks)

### Phase 4: Polish (ongoing)
10. **Analytics Dashboard** (1-2 weeks)
11. Additional games
12. Performance optimization

---

## Success Metrics

| Metric | Current | Target (3 months) |
|--------|---------|-------------------|
| Daily Active Users | TBD | 100+ |
| Weekly Active Users | TBD | 500+ |
| Avg. Session Duration | TBD | 10+ minutes |
| Autoplay Adoption | 0% | 60%+ of users |
| Gasless Tx % | 0% | 100% |
| User Retention (D7) | TBD | 40%+ |
| Referral Rate | 0% | 20%+ of new users |

---

## Open Questions

1. **Gas subsidy budget:** How much USDC/month to subsidize gas?
2. **Autoplay safety:** What are the max loss limits?
3. **Game fairness:** Provably fair? Audit required?
4. **Prize funding:** Where do tournament prizes come from? (house edge, sponsorships?)
5. **Compliance:** Any gaming/gambling regulations to consider?

---

## Next Steps

1. **Review this doc** (Temisan + @senatorT__)
2. **Prioritize** (what's most important for next 4 weeks?)
3. **Estimate effort** (confirm/reject my estimates)
4. **Start Phase 1** (Autoplay + Gas + Lobby)

---

**Related Files:**
- How it works: ops/arena-play-how-it-works.md
- Twitter thread: content/drafts/twitter-threads/02-arena-play-demo.md
