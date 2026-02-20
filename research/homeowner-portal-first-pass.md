# Settley Homeowner/Agent Portal — First‑Pass Spec (v0.1)

> Goal: add a homeowner/agent-facing experience (seller/owner intake + asset management) that complements the investor portal. This is a **first‑pass MVP**: high-signal workflow, minimal surface area.

## Why this exists (problem framing)
Settley is currently investor‑only. To onboard real inventory (UK/US), we need a simple seller/agent path:
- Capture property leads + docs
- Evaluate eligibility fast
- Provide a transparent pipeline (status, next steps)
- Offer a path to tokenize or list (or decline with reasoning)

## Primary personas
1. **Homeowner / Property Owner**
   - Wants liquidity or partial sale without full exit
   - Needs clarity on valuation, fees, timeline, legal structure
2. **Real Estate Agent / Broker**
   - Wants additional channel to close deals
   - Needs referral tracking and commission clarity

## First‑Pass MVP Scope
### Core flows (MVP)
1. **Apply to List / Tokenize (Owner)**
   - Address → Property details → Ownership/Title → Upload docs → Submit
2. **Agent Referral / Partner Intake**
   - Agent profile → Client/property submission → Referral tracking
3. **Application Status Tracking**
   - Status: Submitted → Under Review → Approved → Offer Sent → In Due Diligence → Listed → Tokenized → Closed
4. **Docs & Communication**
   - Upload docs; message panel for requests
5. **Offer Summary (if approved)**
   - Estimated valuation range, fees, projected timeline

### Nice‑to‑have (post‑MVP)
- On‑platform e‑sign (Docusign)
- Automated AVM estimate + comps
- KYC/AML pipeline
- Automated rent/lease verification

---

## UX: Key Screens (first pass)
1. **Landing: “List your property with Settley”**
   - Value prop: fractional liquidity, transparent fees
   - CTA: “Start application” (email or phone)

2. **Owner Intake Form (multi‑step)**
   - Address (autocomplete)
   - Property type (SFH, condo, multi‑family)
   - Occupancy status (occupied, vacant)
   - Annual rent / mortgage balance (optional)
   - Ownership details (sole/joint, entity?)
   - Upload docs (deed, mortgage statement, lease, ID)
   - Consent + submit

3. **Agent Intake**
   - Agent info (license #, brokerage)
   - Client/property info
   - Agreement to referral terms

4. **Dashboard**
   - Status timeline
   - Requested documents checklist
   - Messages
   - Estimated timeline

5. **Offer Preview**
   - Valuation range
   - Fees (tokenization, management)
   - Timeline + next steps
   - “Accept offer” → triggers due diligence

---

## Data Model (minimal)
### Entities
- **User** (role: owner|agent)
- **Property** (address, type, occupancy, size)
- **Application** (status, timestamps, assigned analyst)
- **Document** (type, url, status)
- **Offer** (valuation_low, valuation_high, fees, terms)
- **Message** (threaded comms)
- **Referral** (agent_id, property_id, commission terms)

---

## API Endpoints (first pass)
### Auth
- POST /auth/register
- POST /auth/login
- POST /auth/verify-email

### Owner Flow
- POST /applications
- GET /applications/{id}
- PUT /applications/{id}
- POST /applications/{id}/documents

### Agent Flow
- POST /agents
- POST /agents/{id}/referrals

### Offers
- GET /applications/{id}/offer
- POST /applications/{id}/offer/accept

### Messages
- GET /applications/{id}/messages
- POST /applications/{id}/messages

---

## Operational Process (internal)
1. **Intake Review** → validate docs & eligibility
2. **Underwriting** → valuation + legal structure
3. **Offer** → present terms
4. **Due Diligence** → finalize data for listing
5. **Listing / Tokenization**

---

## Requirements & Assumptions
- **Audience:** UK/US homeowners/agents
- **Compliance:** must include legal disclaimers
- **Data Security:** encrypted storage for docs

---

## What we learned from Lofty
Direct Lofty homeowner pages are not publicly accessible with basic fetch in this environment (no search API key, dynamic pages). We still align to Lofty’s known model:
- Offer liquidity without full sale
- Transparent fees and timeline
- Documentation‑heavy intake

---

## Next Steps (if approved)
1. Build landing + intake flow in frontend
2. Implement minimal API + DB schema
3. Internal admin view for applications
4. Publish MVP and test 5–10 homeowners/agents
