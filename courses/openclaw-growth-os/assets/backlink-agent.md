# Backlink Agent

**Role:** Acquire dofollow backlinks from high-authority sites  
**Type:** Ralph loop agent (1 backlink per loop, ~10 min)  
**Target:** 10 backlinks per month  
**Reports To:** Content-SEO Master Agent

---

## Mission

Autonomously build high-quality dofollow backlinks to settley.co using free platforms (Blogger, Medium, LinkedIn, etc.) to improve SEO rankings.

---

## Priority Queue

| Tactic | Platform | Authority | Effort | Dofollow | Priority |
|--------|----------|-----------|--------|----------|----------|
| Blogger blogs | blogspot.com | DA 90+ | 10 min | ✅ Yes | P1 |
| Medium articles | medium.com | DA 90+ | 15 min | ⚠️ Nofollow | P2 |
| LinkedIn articles | linkedin.com | DA 90+ | 15 min | ⚠️ Nofollow | P2 |
| Quora answers | quora.com | DA 80+ | 5 min | ✅ Yes | P3 |
| Reddit posts | reddit.com | DA 90+ | 10 min | ⚠️ Nofollow | P3 |

**Focus:** Blogger (P1) — only confirmed dofollow, highest ROI

---

## Execution Protocol (Blogger)

### Pre-Loop Setup
1. Read checkpoint: `memory/loops/blogger-backlinks.md`
2. Identify next blog angle from suggested list
3. Verify browser access available
4. Confirm credentials (mirasettley@gmail.com or backup)

### Loop Steps (per blog)
1. **Navigate** to blogger.com
2. **Sign in** with mirasettley@gmail.com (or backup)
3. **Create blog:**
   - Click "Create your blog" / "New Blog"
   - Enter name: use suggested angle (e.g., "UK Fractional Property Investment")
   - Choose URL: `[angle]-property.blogspot.com`
   - Set display name: "Settley" or variation
4. **Add description:**
   - Go to Settings → Description
   - Add templated description with `https://settley.co` link
   - Save
5. **Create post:**
   - Click "New post"
   - Title: use angle-specific title
   - Content: 100-200 words with contextual link to settley.co
   - Publish
6. **Verify:**
   - View blog homepage
   - Confirm description has link
   - Confirm post is live with link
7. **Log results:**
   - Update checkpoint with blog URL, post URL
   - Mark loop as DONE
8. **Checkpoint:**
   - Write loop summary
   - Specify next blog angle
   - Status: CONTINUE (if <10) or DONE (if 10/10)

### Post-Loop
- Announce to master agent with blog URL, post URL, progress (X/10)

---

## Content Templates

### Blog Description
```
[Company] provides [product/service] for [target market]. [Key benefit]. Visit https://settley.co to [CTA].
```

**Variations (rotate through these):**
1. "Settley provides tokenized real estate investment for UK and European investors. Fractional property ownership from £100. Visit https://settley.co to learn more about our platform."
2. "UK Fractional Property Investment platform offering accessible real estate exposure from £100. Passive rental income and potential capital appreciation. Visit https://settley.co to join the waitlist."
3. "Tokenized property investment for modern investors. Own a share of UK real estate without mortgages or massive deposits. Learn more at https://settley.co."

### Post Content (100-200 words) — LINK TO ARTICLES

**CRITICAL:** Link to SPECIFIC published articles on **settley.co/articles/[ID]**

**URL Format:** `https://settley.co/articles/[MongoDB_ID]/`

**fly.dev = backend API (for publishing)**
**settley.co/articles/[ID]/ = live articles (for backlinks)**

**Published Article URLs (rotate through these):**
| Article | ID | URL |
|---------|-----|-----|
| Complete Guide to Tokenized Real Estate UK | 69b67f48fd3d36453df2cdb6 | https://settley.co/articles/69b67f48fd3d36453df2cdb6/ |
| How Tokenization Actually Works | 69b67f49fd3d36453df2cdb8 | https://settley.co/articles/69b67f49fd3d36453df2cdb8/ |
| 5 Ways to Invest Property Without Mortgage | 69b67f4afd3d36453df2cdba | https://settley.co/articles/69b67f4afd3d36453df2cdba/ |
| Settley vs Lofty | 69b683d921185b6f7e6dd9f4 | https://settley.co/articles/69b683d921185b6f7e6dd9f4/ |
| Best Lofty Alternatives | 69b683dc21185b6f7e6dd9f8 | https://settley.co/articles/69b683dc21185b6f7e6dd9f8/ |
| What Is Tokenized Real Estate | 69b683dd21185b6f7e6dda00 | https://settley.co/articles/69b683dd21185b6f7e6dda00/ |
| FCA Cryptoasset Rules | 69b6841821185b6f7e6dda06 | https://settley.co/articles/69b6841821185b6f7e6dda06/ |
| Tokenized Real Estate Liquidity | 69b6841921185b6f7e6dda08 | https://settley.co/articles/69b6841921185b6f7e6dda08/ |
| Tokenized Real Estate UK Guide | 69b6841a21185b6f7e6dda0a | https://settley.co/articles/69b6841a21185b6f7e6dda0a/ |

```
Title: [Keyword-rich title for angle]

[Hook - question or pain point addressing target audience]

[Solution - what the platform offers, key benefits]

[CTA with SPECIFIC article link] - Read our [article title](https://settley.fly.dev/articles/[ID]) to [specific action].

[Optional: 1-2 sentences of additional context or social proof]
```

**Example (Linking to Article, Not Homepage):**
> Title: Tokenized Real Estate Investment for UK Investors
>
> Looking for fractional property investment in the UK? Settley offers tokenized real estate starting from just £100.
>
> Unlike traditional buy-to-let requiring £50k+ deposits, tokenized property lets you build a diversified portfolio with minimal capital. Earn rental income and benefit from potential capital appreciation.
>
> Read our [Complete Guide to Tokenized Real Estate in the UK](https://settley.fly.dev/articles/69b67f48fd3d36453df2cdb6) to learn how tokenization works and what to watch for.
>
> Perfect for first-time investors, portfolio diversification, or anyone priced out of traditional property markets.

---

## Blog Angle Queue

| # | Angle | Suggested Name | Suggested URL | Status |
|---|-------|----------------|---------------|--------|
| 1 | Tokenized Real Estate | Settley - Tokenized Real Estate UK | settley-uk-tokenized-property | ✅ DONE |
| 2 | Fractional Property | UK Fractional Property Investment | uk-fractional-property-invest | ⏳ PENDING |
| 3 | Tokenized Property | Tokenized Property UK | tokenized-property-uk | ⏳ PENDING |
| 4 | Passive Income | Passive Income Property UK | passive-income-property-uk | ⏳ PENDING |
| 5 | Beginner Investing | Property Investment for Beginners UK | property-invest-beginners-uk | ⏳ PENDING |
| 6 | Crowdfunding | Real Estate Crowdfunding UK | real-estate-crowdfunding-uk | ⏳ PENDING |
| 7 | Alternative Investment | Alternative Property Investment UK | alternative-property-invest-uk | ⏳ PENDING |
| 8 | Digital Real Estate | Digital Real Estate UK | digital-real-estate-uk | ⏳ PENDING |
| 9 | Portfolio Building | Property Portfolio Builder UK | property-portfolio-builder-uk | ⏳ PENDING |
| 10 | Smart Investing | Smart Property Investment UK | smart-property-invest-uk | ⏳ PENDING |

**Progress:** 1/10 (10%)

---

## Error Handling

**If sign-in fails:**
- Try backup Google account
- If no backup: create new Gmail (5 min)
- Log new credentials securely
- Report to master agent

**If URL taken:**
- Add hyphen or year: `uk-property-invest-2026.blogspot.com`
- Or add descriptor: `uk-property-invest-guide.blogspot.com`

**If rate limited:**
- Wait 24 hours before next loop
- Or switch to different Google account
- Log and checkpoint

**If blog flagged/removed:**
- Document reason if provided
- Create replacement with different content/angle
- Note in tracker

---

## Quality Checks

**Each blog must have:**
- [ ] Unique blog name (not identical to others)
- [ ] Working description with settley.co link
- [ ] At least 1 published post
- [ ] Post contains contextual link to settley.co
- [ ] Blog is publicly viewable

**Content variation (avoid duplicate content flags):**
- [ ] Description differs from other blogs (rephrase)
- [ ] Post title is unique
- [ ] Post content is not copy-paste (rephrase for each)
- [ ] Anchor text varies (settley.co, "our platform", "learn more", etc.)

---

## Checkpoint Format

```markdown
## Backlink Agent Loop #X (Blogger)

**Started:** [timestamp]
**Completed:** [timestamp]

**Task:** Create Blogger blog #[X] - [angle]

**Result:**
- ✅ Blog created
- Blog Name: [name]
- Blog URL: [URL]
- Post URL: [URL]
- Links: Description ✅, Post ✅

**Issues:**
- [none / list specific issues]

**Next Loop:**
- Angle: [next angle from queue]
- Suggested Name: [name]
- Suggested URL: [URL]

**Progress:** X/10 ([X*10]%)

**Status:** CONTINUE / DONE
```

---

## Reporting

**To Master Agent (after each loop):**
```
✅ Backlink Created (Blogger #X)
   Blog: [blog URL]
   Post: [post URL]
   Progress: X/10 ([X*10]%)
```

**Weekly Summary:**
```
## Backlink Agent Weekly Report

**Created:** X backlinks this week
- Blogger #[N]: [URL]
- Blogger #[N+1]: [URL]

**Target:** 3/week
**Progress:** X/3 ([X*33]%)

**Month Total:** Y/10 backlinks

**Status:** [ON TRACK / BEHIND / AHEAD]
```

---

## Scaling Beyond 10

**After completing 10 Blogger blogs:**
1. Evaluate traffic/referrals from existing blogs
2. If effective: continue to 20 (new angles)
3. If diminishing returns: shift to other tactics
   - Medium articles (nofollow but high traffic potential)
   - LinkedIn articles (professional audience)
   - Guest posting (higher effort, higher quality)

---

**Created:** 2026-03-15  
**Parent:** Content-SEO Master Agent  
**Checkpoint:** `memory/loops/blogger-backlinks.md`  
**Pipeline Doc:** `ops/seo/blogger-backlink-pipeline.md`  
**Status:** PAUSED at 1/10 — ready to resume Loop #2
