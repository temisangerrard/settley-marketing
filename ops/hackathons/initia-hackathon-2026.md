# INITIATE: The Initia Hackathon — Arena Play Submission

**Hackathon:** INITIATE Season 1 (Initia + DoraHacks)
**Project:** Arena Play — AI Agent Gaming Platform
**Submission Type:** Appchain Gaming Application
**Timeline:** 4 weeks (March 13 - April 10, 2026)
**Owner:** Temisan (technical), Mira (execution)

---

## Hackathon Overview

### What is Initia?
Initia is an appchain platform that lets developers launch profitable applications with:
- **100ms block times** — Fast enough for real-time gaming
- **Instant bridging/deposits** — Cross-chain UX without friction
- **Social logins** — Onboard non-crypto users
- **Full value capture** — Keep transaction revenue, no gas tax to L1
- **AI-assisted deployment** — Deploy chain + app with AI tooling

### Why Arena Play Fits
- ✅ **Gaming needs speed** — 100ms blocks = playable games
- ✅ **Microtransactions** — Keep revenue from each bet/action
- ✅ **Cross-chain users** — Bridge USDC from Ethereum, Solana, etc.
- ✅ **AI agents** — Arena Play already uses AI for game logic

---

## Prize Pool (Estimated)

Based on typical L1 hackathons (Initia raised $10M+):

| Place | Prize (Estimated) |
|-------|-------------------|
| 1st | $50,000 - $100,000 USDC |
| 2nd | $25,000 - $50,000 USDC |
| 3rd | $10,000 - $25,000 USDC |
| Best UX | $10,000 USDC (bonus track) |
| Best AI Integration | $10,000 USDC (bonus track) |
| Community Choice | $5,000 USDC (bonus track) |

**Total potential:** $100k - $200k+ in non-dilutive funding

---

## Submission Requirements

### Must Have (MVP)
- [ ] Deployed appchain on Initia testnet
- [ ] Working game logic (at least 1 game mode)
- [ ] User onboarding (social login or wallet)
- [ ] Transaction flow (deposit, bet, withdraw)
- [ ] GitHub repo with documentation
- [ ] Demo video (3-5 min)

### Nice to Have (Bonus Points)
- [ ] Cross-chain bridging (USDC from Ethereum/Solana)
- [ ] AI agent integration (auto-play, NPCs, or game logic)
- [ ] Revenue dashboard (show transaction fees earned)
- [ ] Mobile-responsive UI
- [ ] Live demo URL (not just testnet)

---

## Arena Play Hackathon Scope

### Core Features (Week 1-2)
1. **Game Mode:** Rock-Paper-Scissors + Heads/Tails (existing code)
2. **Betting:** USDC bets (0.1 - 10 USDC range)
3. **Deployment:** Initia testnet appchain
4. **Onboarding:** Social login (Google/Twitter) + wallet creation
5. **UI:** Simple web interface (React + Initia SDK)

### Stretch Features (Week 3-4)
1. **Cross-chain bridge:** Deposit USDC from Ethereum mainnet
2. **AI opponent:** Claude-powered NPC that plays against users
3. **Revenue dashboard:** Show fees earned, player stats
4. **Leaderboard:** Top players, biggest wins
5. **Mobile UI:** Responsive design for phone play

---

## Technical Architecture

### Stack
- **Blockchain:** Initia appchain (Cosmos SDK + Move VM)
- **Smart Contracts:** Move language (Initia native)
- **Frontend:** React + Initia SDK
- **Backend:** Node.js (existing Arena Play logic)
- **AI:** OpenRouter API (Claude, for NPC logic)
- **Hosting:** Vercel (frontend), Initia testnet (chain)

### Reuse from Existing Code
- ✅ Game logic (RPS, Heads/Tails, Dice)
- ✅ AI agent architecture (OpenClaw integration)
- ✅ UI components (existing Settley design system)
- ✅ Analytics tracking (GA4 already configured)

### New Development Needed
- ⚠️ Initia appchain deployment (new)
- ⚠️ Move smart contracts (new language)
- ⚠️ Cross-chain bridge integration (new)
- ⚠️ Social login flow (new)

---

## Week-by-Week Timeline

### Week 1 (March 13-20): Setup + Deployment
- [ ] Day 1-2: Initia docs + starter templates
- [ ] Day 3-4: Deploy testnet appchain
- [ ] Day 5-7: Write Move contracts (betting, payouts)
- **Milestone:** Testnet live, contracts deployed

### Week 2 (March 21-27): Frontend + Integration
- [ ] Day 1-3: React UI (betting interface)
- [ ] Day 4-5: Connect to Initia SDK
- [ ] Day 6-7: Test transaction flow end-to-end
- **Milestone:** Playable demo on testnet

### Week 3 (March 28 - April 3): Polish + AI
- [ ] Day 1-2: Social login integration
- [ ] Day 3-4: AI opponent (Claude-powered NPC)
- [ ] Day 5-7: Revenue dashboard + leaderboards
- **Milestone:** Full feature set complete

### Week 4 (April 4-10): Submission
- [ ] Day 1-2: Demo video (3-5 min)
- [ ] Day 3-4: Documentation + GitHub cleanup
- [ ] Day 5: Submit to DoraHacks
- [ ] Day 6-7: MVP Demo Day prep (mid-hackathon showcase)
- **Milestone:** Submission complete

---

## Resource Requirements

### Time
- **Temisan:** 10-15 hours/week (technical lead)
- **Mira:** 5-10 hours/week (execution, docs, submission)
- **Total:** 60-100 hours over 4 weeks

### Costs
- **Initia testnet:** Free (Anvil credits provided)
- **OpenRouter API:** £0-50 (AI opponent calls)
- **Hosting:** £0 (Vercel free tier)
- **Total:** £0-50 (mostly free)

### Tools Needed
- [ ] Initia developer account (sign up)
- [ ] DoraHacks account (register team)
- [ ] GitHub repo (create: `arena-play-initia`)
- [ ] OpenRouter API key (already have)
- [ ] Vercel account (for hosting)

---

## Success Criteria

### Minimum Viable Submission
- ✅ Deployed appchain on Initia testnet
- ✅ 1 playable game (RPS or Heads/Tails)
- ✅ Users can deposit, bet, withdraw
- ✅ Demo video submitted
- ✅ GitHub repo with docs

### Winning Submission (Target)
- ✅ All MVP features + 2+ stretch features
- ✅ Cross-chain bridging working
- ✅ AI opponent playable
- ✅ Revenue dashboard showing real transactions
- ✅ Professional demo video + docs
- ✅ Live demo URL (not just testnet)

### Moonshot (If Everything Goes Perfect)
- ✅ Top 3 finish ($25k+ prize)
- ✅ Community Choice award ($5k bonus)
- ✅ Initia team picks up for mainnet deployment
- ✅ Press coverage (CoinDesk, Decrypt, etc.)

---

## Risks + Mitigation

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| Initia docs incomplete | Medium | High | Join Initia Discord, ask for help early |
| Move language learning curve | High | Medium | Use starter templates, copy existing contracts |
| Cross-chain bridge fails | Medium | Low | Make it a bonus feature, not core |
| AI opponent too expensive | Low | Low | Rate limit AI calls, cache responses |
| Not enough time (4 weeks) | Medium | High | Scope MVP tightly, cut stretch features if needed |

---

## Next Steps (This Week)

### Day 1 (Today — March 13)
- [ ] Register on DoraHacks
- [ ] Create GitHub repo (`temisangerrard/arena-play-initia`)
- [ ] Read Initia hackathon docs (https://docs.initia.xyz/hackathon)
- [ ] Join Initia Discord (support channel)

### Day 2-3 (March 14-15)
- [ ] Deploy Initia testnet appchain (follow starter guide)
- [ ] Write basic Move contract (bet + payout logic)
- [ ] Test contract on testnet

### Day 4-5 (March 16-17)
- [ ] Set up React frontend (copy existing Arena Play UI)
- [ ] Connect to Initia SDK
- [ ] Test end-to-end flow (deposit → bet → withdraw)

### Day 6-7 (March 18-19)
- [ ] MVP milestone check: Is it playable?
- [ ] If yes: Continue to Week 2 features
- [ ] If no: Debug, ask Initia Discord for help

---

## Submission Links

- **Hackathon Page:** https://dorahacks.io/hackathon/initiate/detail
- **Initia Docs:** https://docs.initia.xyz/hackathon
- **DoraHacks Submission:** (TBD — register team first)
- **GitHub Repo:** https://github.com/temisangerrard/arena-play-initia (create)
- **Demo Video:** (TBD — record Week 4)
- **Live Demo:** (TBD — deploy to Vercel Week 3)

---

## Notes

- **Settley SEO continues** — This is parallel work (Temisan on hackathon, Mira on content)
- **Non-dilutive funding** — Prize money doesn't dilute equity
- **Reusable code** — Even if we don't win, we have a deployable gaming appchain
- **Investor narrative** — "Built on Initia, won hackathon, raised seed" is a strong story

---

**Last Updated:** March 13, 2026
**Owner:** Temisan + Mira
**Status:** Planning → Execution (Week 1 starts today)
