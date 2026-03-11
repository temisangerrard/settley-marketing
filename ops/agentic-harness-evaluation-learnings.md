# Agentic Harness Evaluation — Learnings from @neural_avb

**Source:** AVB (@neural_avb) — "How to design Experiments to Evaluate your Agentic Harness"
**Date:** 2026-03-10
**Tweet:** https://x.com/neural_avb/status/2031417353666441266
**Engagement:** 438 likes, 34 retweets, 922 bookmarks, 47K impressions

---

## Who is AVB?

- **Creator:** Neural Breakdown YouTube channel (@avb_fj)
- **Expertise:** Multi-Agent Reinforcement Learning (MARL), LLMs, agentic systems
- **Focus:** Experiment design for evaluating agentic harnesses

---

## Key Concepts from AVB's Work

### 1. What is an Agentic Harness?

An **agentic harness** is infrastructure that gives AI agents:
- Access to tools (APIs, browsers, code execution)
- Relevant context (memory, observations, state)
- Architectural constraints (guardrails, validation)

**Result:** Models achieve significantly better results when operating with a harness vs. raw LLM calls.

---

### 2. Why Experiment Design Matters

**The Problem:**
- Many agent builders can't tell if improvements are real or noise
- No standardized evaluation framework
- Hard to compare different approaches

**AVB's Solution:**
- Rigorous experiment design
- Clear metrics
- Controlled comparisons

---

### 3. Key Evaluation Metrics (from MARL research)

Based on related research in multi-agent evaluation:

**Performance Metrics:**
- **Win rate** — % of games/tasks completed successfully
- **Profitability** — Net gains (for betting/trading agents)
- **Task success rate** — % of tasks completed without human intervention
- **Sample efficiency** — How many trials to reach proficiency

**Behavioral Metrics:**
- **Strategic depth** — Does agent adapt to opponents?
- **Memory utilization** — Does agent learn from history?
- **Perception accuracy** — Does agent correctly interpret game state?
- **Decision latency** — How fast does agent decide?

**System Metrics:**
- **Tool usage efficiency** — Are tools used appropriately?
- **Error recovery** — Can agent recover from mistakes?
- **Generalization** — Does agent work across different games/tasks?

---

### 4. Experimental Design Principles

**From MARL diagnostics suite research:**

1. **Baseline comparisons**
   - Compare against random agent
   - Compare against un-harnessed LLM
   - Compare against previous version

2. **Ablation studies**
   - Remove one component at a time (memory, perception, tools)
   - Measure impact on performance
   - Identify which components matter most

3. **Diverse test scenarios**
   - Multiple game types (RPS, dice, market prediction)
   - Different opponent types (human, AI, mixed)
   - Varying difficulty levels

4. **Statistical significance**
   - Run enough trials (100+ games per config)
   - Report confidence intervals
   - Don't cherry-pick results

---

## Application to Arena Play

### Current Arena Play Setup

**Games:**
- RPS (Rock Paper Scissors)
- Heads or Tails
- Dice
- BTC Market Prediction (5min / 24hr)

**Agent Controls:**
- Personality configuration
- Target preference
- Cooldown settings
- Stake amounts
- Game selection

**Data Available:**
- Win/loss history
- Profit/loss tracking
- Game-by-game decisions
- Opponent types

---

### What We Can Measure (Starting Today)

#### 1. **Win Rate by Game Type**
```
Game Type       | Win Rate | Total Games | Profit/Loss
----------------|----------|-------------|-------------
RPS             |   ?%     |     ?       |    ? USDC
Heads/Tails     |   ?%     |     ?       |    ? USDC
Dice            |   ?%     |     ?       |    ? USDC
BTC 5min        |   ?%     |     ?       |    ? USDC
BTC 24hr        |   ?%     |     ?       |    ? USDC
```

#### 2. **Win Rate by Agent Personality**
```
Personality | Win Rate | Avg Stake | Profit/Game | Best Game Type
------------|----------|-----------|-------------|----------------
Aggressive  |    ?%    |    ?      |     ?       |      ?
Conservative|    ?%    |    ?      |     ?       |      ?
Balanced    |    ?%    |    ?      |     ?       |      ?
```

#### 3. **Performance Over Time**
- Learning curve (does agent improve with more games?)
- Degradation (does performance drop after X games?)
- Optimal session length

#### 4. **Opponent Analysis**
- Win rate vs. humans vs. AI agents
- Win rate by opponent skill level
- Adaptation effectiveness (does changing strategy help?)

#### 5. **Betting Strategy Effectiveness**
- Fixed stake vs. percentage stake vs. martingale
- Optimal stake size for each game type
- Risk-adjusted returns (Sharpe ratio equivalent)

---

### What We Should Build (Evaluation Dashboard)

**Phase 1: Basic Analytics (1-2 weeks)**
- [ ] Win/loss tracking per game type
- [ ] Profit/loss tracking
- [ ] Agent configuration logging
- [ ] Export to CSV for analysis

**Phase 2: Advanced Metrics (2-3 weeks)**
- [ ] Win rate by personality config
- [ ] Win rate by stake size
- [ ] Performance over time charts
- [ ] Opponent type breakdown

**Phase 3: Experiment Framework (3-4 weeks)**
- [ ] A/B testing for agent configs
- [ ] Statistical significance calculator
- [ ] Automated experiment runner
- [ ] Results dashboard

---

### Experiment Ideas for Arena Play

#### Experiment 1: Personality Impact
**Hypothesis:** Aggressive agents win more but have higher variance

**Setup:**
- 3 agent configs: Aggressive, Conservative, Balanced
- 100 games each (same game type)
- Measure: Win rate, profit/game, max drawdown

**Expected Outcome:** Quantify trade-off between aggression and consistency

---

#### Experiment 2: Game Type Proficiency
**Hypothesis:** Some agents are better at certain games

**Setup:**
- 1 agent config
- 50 games each: RPS, Dice, Heads/Tails, BTC prediction
- Measure: Win rate, profit/game

**Expected Outcome:** Identify which games favor AI agents

---

#### Experiment 3: Memory/History Impact
**Hypothesis:** Agents with history tracking outperform stateless agents

**Setup:**
- Agent A: Full history (last 10 games)
- Agent B: No history (stateless)
- 100 games each (same conditions)
- Measure: Win rate, adaptation speed

**Expected Outcome:** Quantify value of memory for agent performance

---

#### Experiment 4: Stake Strategy
**Hypothesis:** Percentage-based staking outperforms fixed staking

**Setup:**
- Strategy A: Fixed 10 USDC per game
- Strategy B: 5% of wallet per game
- Strategy C: Martingale (double after loss)
- 100 games each
- Measure: Final wallet balance, max drawdown, ruin probability

**Expected Outcome:** Optimal betting strategy for autonomous agents

---

## Collaboration Opportunity with AVB

**Why AVB might care:**
- Arena Play is a **real-world multi-agent environment**
- Live PVP data (not simulation)
- Diverse game types (not just one task)
- Real economic incentives (not toy rewards)

**What we could offer:**
- Access to Arena Play as evaluation testbed
- Real agent performance data
- Collaboration on experiment design
- Co-authored research/paper on agentic evaluation

**Approach (after implementing basic metrics):**
> "Hey AVB, we built Arena Play — autonomous agent betting arena with RPS, dice, BTC prediction.
> 
> Your article on experiment design for agentic harnesses is exactly what we need. We're tracking win rates, profitability, personality configs across 1000+ games.
> 
> Would love your take on our evaluation framework. Arena Play could be a real-world testbed for MARL research.
> 
> Interested in collaborating?"

---

## Immediate Next Steps

1. **Implement basic tracking** (this week)
   - Log every game: type, stake, outcome, agent config, opponent type
   - Export to CSV for analysis

2. **Run first experiment** (next week)
   - Personality impact (Aggressive vs. Conservative vs. Balanced)
   - 100 games per config
   - Publish results (blog post + tag AVB)

3. **Build evaluation dashboard** (2-3 weeks)
   - Win rates, profit tracking, performance charts
   - Public leaderboard (optional)

4. **Reach out to AVB** (after first results)
   - Share findings
   - Propose collaboration
   - Offer Arena Play as research testbed

---

## Related Research

**Papers to Read:**
1. "General Modular Harness for LLM Agents in Multi-Turn Gaming Environments" (arXiv 2507.11633)
2. "Evaluation and Benchmarking of LLM Agents: A Survey" (arXiv 2507.21504)
3. "HarnessLLM: Automatic Testing Harness Generation via Reinforcement Learning" (arXiv 2511.01104)
4. "Toward Evolutionary Intelligence: LLM-based Agentic Systems with MARL" (SSRN 5819182)

**GitHub Repos:**
- EleutherAI/lm-evaluation-harness
- tmgthb/Autonomous-Agents (MARL diagnostics suite)
- luo-junyu/Awesome-Agent-Papers

---

**File Location:** ops/agentic-harness-evaluation-learnings.md
**Last Updated:** 2026-03-11
**Owner:** Mira (for Arena Play evaluation framework)
