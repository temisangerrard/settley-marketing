# Synthesis MD Hackathon — IMPROVED Plan (Based on Actual Codebase)

**Audit Date:** 2026-03-17 01:35 GMT  
**Repo Audited:** https://github.com/temisangerrard/autonomous-arena-scaffold  
**Status:** 🟢 **MUCH MORE ADVANCED THAN EXPECTED**

---

## 🔍 What's ALREADY Built (Codebase Audit)

### ✅ LIVE PRODUCT (5 Games)

**apps/web** — Web app + admin panel
- `/play` — Arena gameplay with player drawer
- `/admin` — Full admin panel (treasury, bots, markets)
- `/admin/chief` — Chief Ops Agent (PI-patterned)
- Auth/session system working
- Wallet integration (Coinbase + external)

**apps/server** — Multiplayer game server
- Challenge lifecycle management
- Settlement orchestration
- Market services (Polymarket feed integration)
- 5 live games:
  1. Coinflip (house game)
  2. Rock Paper Scissors (house game)
  3. Dice Duel (house game)
  4. BTC Prediction (5-minute rounds)
  5. BTC Prediction (24-hour rounds)

**apps/agent-runtime** — Bot runtime
- ✅ **Autoplay strategy wizard** (already built!)
- ✅ **Wallet readiness badge** (already built!)
- ✅ **Bot personality system** (aggressive/conservative/balanced)
- ✅ **Quick-play panel** (already built!)
- Autonomous bot play with wallet management

**apps/contracts** — Onchain escrow
- PariMutuelPool contract deployed on Base mainnet
- House treasury management
- Player win/loss settlement

---

## 🎯 What We ACTUALLY Need for Synthesis MD

### ALREADY COMPLETE (No Work Needed)

| Feature | Status | Notes |
|---------|--------|-------|
| **Autoplay Bot** | ✅ DONE | Strategy wizard, personality system built |
| **5 Live Games** | ✅ DONE | Coinflip, RPS, Dice, BTC Prediction (5min + 24hr) |
| **Admin Dashboard** | ✅ DONE | Full ops panel at `/admin` |
| **Onchain Settlement** | ✅ DONE | PariMutuelPool on Base mainnet |
| **Bot Runtime** | ✅ DONE | Agent runtime with wallet management |
| **Quick-Play Panel** | ✅ DONE | Built March 13, 2026 |

### NEEDS WORK (Synthesis-Specific)

| Feature | Status | Work Required |
|---------|--------|---------------|
| **Celo Integration** | ❌ NOT STARTED | Add Celo USDC payment path (2-4 hours) |
| **Filecoin Storage** | ❌ NOT STARTED | Store game state on Filecoin (4-6 hours) |
| **ERC-8004 Registration** | ❌ NOT STARTED | Register agents as NFTs on Base Sepolia (2-4 hours) |
| **Demo Video** | ❌ NOT STARTED | Record 2-3 min demo (1-2 hours) |
| **Submission Copy** | ❌ NOT STARTED | Write DoraHacks submission (1-2 hours) |

---

## ⚡ REALISTIC 7-Day Sprint (Based on Actual Progress)

### Day 1 (Today — March 17): REGISTER + SETUP ✅

**Mira (Execution):**
- [x] Audit codebase (done — this doc)
- [ ] **REGISTER on Synthesis MD** (https://synthesis.md/)
- [ ] Create DoraHacks project page
- [ ] Tweet: "Arena Play already LIVE with 5 games + autoplay bots. Adding Celo + Filecoin for @synthesis_md"
- [ ] Set up progress tracking

**Temisan (Technical):**
- [ ] Review Celo integration docs
- [ ] Review Filecoin Pin API docs
- [ ] Review ERC-8004 standard

**End of Day Deliverable:**
- ✅ Registration complete
- ✅ Project page live
- ✅ Integration docs reviewed

---

### Day 2 (March 18): CELO INTEGRATION

**Temisan (Build — 4 hours):**
- [ ] Add Celo USDC payment option (alongside Base)
- [ ] Update treasury ops to support Celo
- [ ] Test Celo deposits/withdrawals

**Mira (Support — 2 hours):**
- [ ] Document progress (tweet thread #1)
- [ ] Write Celo integration section of submission copy

**End of Day Deliverable:**
- ✅ Celo USDC working
- ✅ Tweet thread posted

---

### Day 3 (March 19): FILECOIN INTEGRATION

**Temisan (Build — 6 hours):**
- [ ] Capture game state snapshots (existing data → Filecoin)
- [ ] Store using Filecoin Pin API
- [ ] Retrieve/verify stored game state (demo flow)

**Mira (Support — 2 hours):**
- [ ] Document progress (tweet thread #2)
- [ ] Prepare Filecoin demo script

**End of Day Deliverable:**
- ✅ Filecoin storage working
- ✅ Retrieval demo ready

---

### Day 4 (March 20): ERC-8004 AGENT REGISTRATION

**Temisan (Build — 4 hours):**
- [ ] Register Arena Play agents as ERC-8004 NFTs (Base Sepolia)
- [ ] Link agents to Filecoin-stored game state
- [ ] Test agent discoverability

**Mira (Support — 2 hours):**
- [ ] Document progress (tweet thread #3)
- [ ] Record demo video (rough cut)

**End of Day Deliverable:**
- ✅ ERC-8004 registration working
- ✅ Demo video recorded

---

### Day 5 (March 21): POLISH + TEST

**Temisan (Build — 4 hours):**
- [ ] Fix bugs from testing
- [ ] Ensure all 3 integrations work together
- [ ] Prepare repo for public viewing

**Mira (Support — 4 hours):**
- [ ] Finalize submission copy
- [ ] Edit demo video (final cut)
- [ ] Prepare DoraHacks submission files

**End of Day Deliverable:**
- ✅ All features tested
- ✅ Demo video ready
- ✅ Submission copy ready

---

### Day 6 (March 22): SUBMIT 🎯

**Mira (Execution — 3 hours):**
- [ ] Submit to Synthesis MD (Open Track)
- [ ] Submit to Celo bounty track
- [ ] Submit to Filecoin track (if exists)
- [ ] Post submission tweet (thread #4)
- [ ] Share in Discord, Twitter, Reddit

**Temisan (Support — 1 hour):**
- [ ] Final code review
- [ ] Ensure repo is public + documented
- [ ] Be available for judge questions

**End of Day Deliverable:**
- ✅ Submission complete (all 3 tracks)
- ✅ Public announcement

---

### Day 7-8 (March 23-25): PROMOTE + WAIT

**Mira (Marketing — 1 hour/day):**
- [ ] Daily progress tweets
- [ ] Share demo video widely
- [ ] Engage with other Synthesis projects
- [ ] Monitor judge feedback

**Temisan (Technical — On-call):**
- [ ] Monitor for bugs/issues
- [ ] Respond to judge questions
- [ ] Prepare for potential win

---

## 📊 REALISTIC Success Metrics

| Metric | Target | Current | Confidence |
|--------|--------|---------|------------|
| Registration | Complete | ⏳ Today | ✅ 100% |
| Autoplay feature | **Already working** | ✅ DONE | ✅ 100% |
| Admin dashboard | **Already working** | ✅ DONE | ✅ 100% |
| Celo integration | Working | ❌ Not started | ✅ 90% (2-4 hours) |
| Filecoin integration | Working | ❌ Not started | ✅ 80% (4-6 hours) |
| ERC-8004 registration | Working | ❌ Not started | ✅ 90% (2-4 hours) |
| Demo video | 2-3 min | ❌ Not recorded | ✅ 100% |
| Submission | 3 tracks | ❌ Not submitted | ✅ 100% |

**Overall Confidence:** 90%+ (because 70% is ALREADY BUILT)

---

## 🏆 Prize Tracks (Realistic)

| Track | Prize | Fit | Confidence | Submit? |
|-------|-------|-----|------------|---------|
| **Open Track** | Shared pool | ✅ Arena Play (agents that pay) | ✅ 95% | ✅ YES |
| **Celo** | $10K+ | ✅ USDC on Celo | ✅ 90% | ✅ YES |
| **Filecoin** | TBD (bounty) | ✅ Game state storage | ✅ 80% | ✅ YES |
| **ERC-8004** | TBD | ✅ Agent registration | ✅ 90% | Maybe |

**Total Potential:** $10K+ + Filecoin bounty

**Realistic Expected Win:** $5K-15K (conservative)

---

## 🎯 Key Advantage (vs. Other Hackathon Teams)

**Most teams:** Starting from scratch, building MVP in 7 days  
**Us:** ALREADY HAVE LIVE PRODUCT with:
- 5 games working
- Autoplay bots deployed
- Admin dashboard live
- Onchain settlement on Base mainnet
- Bot runtime with personality system

**We're not building — we're INTEGRATING.**

**Time required:** 12-16 hours total (not 40-60 hours like other teams)

**Risk:** Very low (core product already works)

---

## 📁 Files to Reference

**Existing Codebase:**
- `/Users/temisan/Downloads/autobett-repo/README.md` — Product overview
- `/Users/temisan/Downloads/autobett-repo/progress.md` — Full build history
- `/Users/temisan/Downloads/autobett-repo/apps/` — All app code
- `/Users/temisan/Downloads/autobett-repo/docs/plans/` — Previous plans

**New Plan:**
- `ops/hackathons/synthesis-md-improved-plan.md` — This document

---

## 🚀 Immediate Next Steps (Next 2 Hours)

**Mira:**
1. ⏳ Register on Synthesis MD (https://synthesis.md/)
2. ⏳ Create DoraHacks project page
3. ⏳ Tweet announcement (mention LIVE product + integrations)
4. ⏳ Set up Day 1-6 tracking doc

**Temisan:**
1. ⏳ Review Celo docs (https://docs.celo.org/)
2. ⏳ Review Filecoin Pin API (https://docs.filecoin.io/)
3. ⏳ Review ERC-8004 standard (https://eips.ethereum.org/EIPS/eip-8004)

**End of Day 1:** Registration complete, docs reviewed, ready to build Day 2.

---

**Plan Created:** 2026-03-17 01:35 GMT  
**Based On:** Actual codebase audit (autonomous-arena-scaffold repo)  
**Confidence:** 90%+ (70% already built)  
**Owners:** Temisan (technical integrations), Mira (execution + submission)

**We've got this. Product is LIVE. Just adding 3 integrations.**
