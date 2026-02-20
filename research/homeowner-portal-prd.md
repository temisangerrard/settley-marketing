# Settley Homeowner/Agent Portal — PRD (v1.0)

## 1. Overview
**Problem:** Settley is investor‑first with no dedicated seller/owner pipeline. This limits inventory acquisition and slows market expansion. We need a homeowner/agent portal to source properties and convert them into tokenized listings.

**Goal:** Launch a minimal but credible owner/agent intake + tracking experience that converts qualified properties into offers within 7–14 days.

---

## 2. Objectives & Success Metrics
### Primary Objectives
- Increase qualified property submissions
- Reduce time from submission → offer
- Provide transparency and trust to owners/agents

### Success Metrics (MVP)
- 20+ owner submissions/month
- 30% of submissions qualified
- <14 days average time to offer
- 60% of qualified offers accepted

---

## 3. Target Users
### Homeowners/Property Owners
- Want liquidity without full sale
- Need clarity on valuation, fees, and legal structure

### Real Estate Agents/Brokers
- Want extra channel for deal flow
- Need clear referral terms and tracking

---

## 4. Scope
### In Scope (MVP)
- Owner intake form (multi‑step)
- Agent referral form
- Document upload
- Application status dashboard
- Offer preview + accept
- Internal admin review tools

### Out of Scope (MVP)
- Automated AVM and comps
- Full KYC/AML automation
- E‑sign integration
- Payments or escrow handling

---

## 5. User Journeys
### Owner Flow
1. Landing → Start application
2. Multi‑step intake
3. Submit + confirmation
4. Track status in dashboard
5. Review offer → accept/decline

### Agent Flow
1. Landing → Agent intake
2. Submit client property
3. Track referral status

---

## 6. Functional Requirements
### Owner Intake
- Address autocomplete
- Property type, size, occupancy
- Ownership structure + consent
- Document uploads

### Agent Intake
- License #, brokerage
- Client property address
- Referral agreement

### Dashboard
- Status timeline
- Document requests
- Messaging

### Offer Preview
- Valuation range
- Fee summary
- Timeline
- Accept offer

### Admin Tools
- Application review list
- Status updates
- Offer editor
- Internal notes

---

## 7. Non‑Functional Requirements
- Data encryption (docs + PII)
- GDPR/CCPA compliance
- Basic SLA notifications
- Audit trail for status updates

---

## 8. Risks & Mitigations
- **Low trust** → transparent fees + clear legal structure
- **Slow review cycles** → internal SLA + status updates
- **Unqualified leads** → pre‑screen form + eligibility hints

---

## 9. Timeline (MVP)
- Week 1: Landing + intake flow
- Week 2: Dashboard + admin view
- Week 3: Offer preview + internal tooling
- Week 4: Launch + test with 5–10 owners

---

## 10. Dependencies
- Access to valuation data
- Legal templates for offers
- Compliance review

---

## 11. Open Questions
- Min property value threshold?
- Property types supported for launch?
- Commission/referral structure for agents?

---

## 12. Next Steps
- Validate eligibility criteria with founders
- Build MVP in staging
- Recruit 5–10 pilot owners/agents
