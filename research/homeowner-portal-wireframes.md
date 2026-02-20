# Settley Homeowner/Agent Portal — UI Wireframes (Text)

> Low‑fi wireframe notes for first‑pass MVP. Layouts described in sections for quick dev translation.

---

## 1) Landing: “List your property with Settley”
**Goal:** Convert homeowners/agents into application start.

**Header**
- Logo (left)
- Nav: How it works | Fees | FAQs | For agents | Sign in
- CTA: Start application

**Hero**
- H1: “Unlock liquidity from your property — without selling the whole home.”
- Sub: “Settle lets owners sell a portion of equity or list properties for tokenized investing. Transparent fees, clear timelines.”
- Primary CTA: Start application
- Secondary CTA: Talk to an analyst

**Social Proof / Trust**
- “As seen in …”
- Compliance note: “Not an offer; subject to eligibility.”

**How it works (3 steps)**
1) Submit property
2) Receive offer
3) Get funded / listed

**Eligibility Snapshot**
- Property types
- Min value range
- Occupancy conditions

**FAQs**
- Fees, timeline, legal structure, what happens if declined

---

## 2) Owner Intake — Multi‑step Wizard
**Global**
- Progress bar at top (Step 1/5)
- Save & resume (email magic link)

**Step 1: Property Basics**
- Address (autocomplete)
- Property type (SFH, condo, multi‑family)
- Year built, beds/baths, sqft
- Occupancy status (occupied/vacant)

**Step 2: Financials**
- Estimated value (optional)
- Current mortgage balance
- Monthly rent (if occupied)
- HOA fees

**Step 3: Ownership**
- Owner name(s)
- Ownership structure (sole/joint/entity)
- Any liens?
- “Confirm you are authorized to list” checkbox

**Step 4: Documents**
- Upload: deed, mortgage statement, lease, ID
- Drag/drop area + progress
- “Can’t upload now? We’ll request later”

**Step 5: Contact + Consent**
- Phone, email
- Preferred contact method
- Consent & legal disclaimers
- Submit

---

## 3) Agent Intake
**Form**
- Agent name, brokerage, license #
- Website/LinkedIn (optional)
- Client property address
- Agreement to referral terms
- Submit

---

## 4) Application Dashboard (Owner)
**Header**
- “Your application” + status badge

**Left: Status Timeline**
- Submitted → Under Review → Offer Sent → Due Diligence → Listed → Closed

**Right: Action Panel**
- “Requested documents” checklist
- “Message analyst” button

**Bottom: Offer Preview (if available)**
- Valuation range
- Estimated timeline
- Fee summary
- Button: Accept offer

---

## 5) Offer Detail
- Summary card (valuation range, fees, timeline)
- Legal structure explainer (SPV / trust)
- Accept offer + next steps

---

## 6) Admin View (Internal)
**List view**
- Applications table: status, address, owner, value estimate, SLA
- Filters: status, region, price band

**Detail view**
- Applicant details + docs
- Notes + internal messages
- Offer editor
- Status change

---

## 7) Error / Decline State
- Clear reason (e.g., property type not supported)
- Suggest alternatives / reapply later
- Contact link
