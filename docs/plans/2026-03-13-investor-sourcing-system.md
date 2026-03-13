# Investor Sourcing System Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Create a reusable investor sourcing rubric and a fresh thesis-fit target list for Mira’s outreach work.

**Architecture:** The system uses one judgment file and one execution file. The rubric defines fit, exclusions, and scoring. The target list applies those rules to current named investors sourced from official fund and team pages.

**Tech Stack:** Markdown docs, repo memory files, official fund websites

---

### Task 1: Create the rubric

**Files:**
- Create: `ops/prospecting/investor-sourcing-rubric.md`

**Step 1: Define fit buckets**

Write the exact investor types Mira should prioritize:
- proptech specialists
- fintech investors with investing / real-world asset overlap
- pre-seed funds with UK/US marketplace or infrastructure appetite
- investors comfortable with regulated or asset-heavy software categories

**Step 2: Define disqualifiers**

List the exact anti-targets:
- generic inbox-first outreach
- late-stage funds without pre-seed behavior
- investors with no proptech, fintech, asset access, or marketplace logic
- broad “innovation” groups without an accountable investor contact

**Step 3: Define scorecard**

Create a 25-point score:
- thesis fit
- stage fit
- geography fit
- contact quality
- angle quality

**Step 4: Define workflow**

Spell out the sequence:
1. identify fit
2. find named investor
3. verify on official site
4. assign score
5. only then source contact path

### Task 2: Create the fresh target list

**Files:**
- Create: `ops/prospecting/investor-targets-v2-2026-03-13.md`

**Step 1: Build a short list from official sites**

Use current fund/team pages to collect named targets with clear fit.

**Step 2: Apply the rubric**

For each target, include:
- fund
- named person
- why they fit Settley
- recommended angle
- score
- official source
- next research action

**Step 3: Tier the list**

Split into:
- Tier A: highest priority now
- Tier B: strong but secondary
- Tier C: keep warm / optional

### Task 3: Wire the queue and memory

**Files:**
- Modify: `ops/current-needs-2026-03-13.md`
- Modify: `memory/2026-03-13.md`

**Step 1: Point the needs queue at the new files**

Update the investor-targeting item so Mira starts from the rubric and target list.

**Step 2: Log the system in memory**

Add a note that investor outreach quality now depends on the new rubric + target list rather than loose ad hoc sourcing.
