# Investor Sourcing System Design

## Goal

Give Mira a reusable way to identify better-fit investors and a fresh outreach list built from that logic, so future investor sourcing does not drift back to generic inboxes and weak-fit funds.

## Problem

Investor outreach is not failing because email delivery is broken. It is failing because target selection is too loose. Generic team inboxes, broad sector-agnostic funds, and low-thesis-fit contacts waste cycles and make response rates look worse than they should.

## Design

Use a two-file system:

1. A reusable sourcing rubric that defines:
- who counts as a strong fit
- who to avoid
- how to score each prospect
- what outreach order to follow
- what evidence is required before a prospect is added

2. A fresh target list that applies the rubric to current named investors and funds using official fund/team pages.

## Scope

Included:
- thesis-fit criteria
- disqualifiers
- scoring model
- outreach priority tiers
- named investor targets with rationale and source links

Excluded:
- writing outreach emails
- validating email addresses
- sending outreach
- CRM automation

## Key Rules

- Named partner or principal first. Generic inbox only as fallback.
- Official fund pages and team pages are the default source of truth.
- Sector fit must be explicit, not inferred from vague “we invest in software” language.
- Settley should be framed as a fit for one of these buckets: fintech infrastructure, proptech, real-world assets, marketplaces for access, or regulated asset access.
- Any target added to the list should have a concrete angle, not just “UK pre-seed fund.”

## Deliverables

- `ops/prospecting/investor-sourcing-rubric.md`
- `ops/prospecting/investor-targets-v2-2026-03-13.md`
- update `ops/current-needs-2026-03-13.md`
- update `memory/2026-03-13.md`
