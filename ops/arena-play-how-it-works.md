# Arena Play — How It Actually Works

**Last Updated:** 2026-03-11
**Source:** Temisan (cofounder)

---

## User Flow

### 1. Sign Up
- User enters email address
- **Instantly provisioned:**
  - Player bot
  - Crypto wallet
- No manual setup required

### 2. Dashboard
- User sees their wallet address
- Can view bot status
- Can configure settings

### 3. Fund Wallet
**Required:**
- **USDC** → for wagers/bets
- **ETH** → for gas fees

**Future:**
- Gas abstraction (Privy.io or Base)
- Platform pays gas for users (not yet live)

### 4. Enter Arena
**Gameplay:**
- Approach game stations OR other players
- Available games:
  - Rock Paper Scissors (RPS)
  - Heads or Tails
  - Dice

**Betting:**
- Place stake (amount to commit)
- Select your options (RPS choice, heads/tails, etc.)
- Game keeps rolling (continuous play)

### 5. Autoplay (Coming Soon)
**Current status:** OFF (being rebuilt)

**When live:**
- Position bot for games it should play
- Set betting strategy
- Bot plays automatically while user is offline
- In-game actions on autopilot

---

## Technical Architecture

### Wallet System
- Per-user wallet (provisioned at signup)
- Supports USDC + ETH
- User-controlled (they fund it)
- Dashboard-visible

### Bot System
- One bot per user
- Provisioned instantly at signup
- Can play autonomously (when autoplay enabled)
- Configurable strategy (WIP)

### Games
- RPS (Rock Paper Scissors)
- Heads or Tails
- Dice
- PVP (player vs player)
- Station-based (approach to play)

### Gas Strategy
**Current:** User pays ETH for gas
**Target:** Platform subsidizes gas (Privy.io or Base integration)

---

## Key Differentiators

1. **Instant onboarding** — email → bot + wallet in seconds
2. **Real money** — USDC wagers, not play money
3. **Autonomous play** — bot keeps playing when you log off (coming soon)
4. **PVP focus** — challenge other players, not just house
5. **Multiple games** — RPS, dice, heads/tails (expandable)

---

## Current Limitations

- ❌ Autoplay is OFF (being rebuilt)
- ❌ Users must fund own gas (no abstraction yet)
- ❌ Limited game variety (3 games)
- ❌ Manual positioning (approach stations/players)

---

## Product Upgrade Opportunities

### Priority 1: Restore Autoplay
- Let users set bot strategy
- Configure which games to play
- Set betting limits
- Bot plays while user offline

### Priority 2: Gas Abstraction
- Integrate Privy.io or Base
- Platform pays gas initially
- Better UX (users don't need ETH)

### Priority 3: More Games
- Add variety (card games, etc.)
- Keep it simple (quick rounds)
- Maintain PVP focus

### Priority 4: Better Discovery
- Lobby system (find games/players)
- Leaderboards
- Tournaments

### Priority 5: Social Features
- Spectate mode
- Chat/emotes
- Friend challenges

---

## Next Steps

1. **Document current state** ✅ (this file)
2. **Draft product upgrades** (separate doc)
3. **Prioritize roadmap** (Temisan decision)
4. **Estimate effort** (dev time)
5. **Ship iteratively**

---

**Related Files:**
- Product roadmap: [TBD]
- Technical spec: [TBD]
- Marketing narrative: content/drafts/twitter-threads/02-arena-play-demo.md
