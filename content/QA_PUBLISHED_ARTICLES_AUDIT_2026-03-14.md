# Published Articles QA Audit Report

**Date:** 2026-03-14  
**Auditor:** Mira (Content QA Tool v1.0 with Design Checks)  
**Scope:** All 15 published articles on settley.fly.dev  
**API Endpoint:** `https://settley.fly.dev/articles`

---

## Executive Summary

**Total Articles Reviewed:** 15  
**✅ Passed:** 6 (40.0%)  
**❌ Failed:** 9 (60.0%)

### Average Scores

| Category | Score | Status |
|----------|-------|--------|
| **SEO** | 96.7/100 | ✅ Excellent |
| **Brand** | 88.1/100 | ✅ Good |
| **Quality** | 80.7/100 | ⚠️ Needs work |
| **Design** | 73.6/100 | ⚠️ Needs work |
| **Overall** | 84.8/100 | ⚠️ Good |

---

## Key Findings

### ✅ What's Working Well

1. **SEO Excellence (96.7/100)** - All articles have proper word counts, titles, and structure
2. **Brand Voice (88.1/100)** - Consistent tone, no hype words, educational focus
3. **Recent Articles Pass** - 6 canonical articles meet all requirements

### ⚠️ Critical Issues

1. **Older Article (ID: 6984bc29a65d4c23c2b804b8)** - Missing ALL design components:
   - No breadcrumb navigation
   - No risk warning callout
   - No disclaimer section
   - No CTA strip
   - Only 367 words (below 800 minimum)
   - **Score: 58.2/100 - Needs complete rebuild**

2. **Duplicate/Versions** - Multiple versions of same articles exist:
   - "How Tokenization Actually Works" has 4 versions (original, FIXED, V2, V3 Canonical)
   - "FCA Cryptoasset Rules" has 2 versions
   - "Fractional Property Investment UK" has 2 versions
   - "How to Invest with £500" has 2 versions
   - "Tokenized Real Estate vs REITs" has 2 versions

3. **Design Compliance (73.6/100)** - "Fixed" versions still missing components:
   - Some missing breadcrumbs
   - Some missing key takeaways boxes
   - Some missing proper typography

---

## Article-by-Article Breakdown

### ✅ PASSED ARTICLES (6)

#### 1. Complete Guide to Tokenized Real Estate in the UK (2026)
- **ID:** 69b324239b0dd5e8aac560f4
- **Score:** 95.2/100 ✅
- **Word Count:** 2,122
- **Status:** Fully compliant, production-ready
- **Issues:** 8 minor (sentence length only)

#### 2. FCA Cryptoasset Rules 2026
- **ID:** 69b3cee4d79383944b72f316
- **Score:** 94.5/100 ✅
- **Word Count:** 2,557
- **Status:** Fully compliant
- **Issues:** 9 minor (sentence length)

#### 3. How to Invest in Property with £500 in the UK (2026)
- **ID:** 69b3d3f73129ce2d3d138291
- **Score:** 93.8/100 ✅
- **Word Count:** 3,173
- **Status:** Fully compliant
- **Issues:** 15 minor (sentence/paragraph length)

#### 4. Tokenized Real Estate vs REITs: An Honest Comparison (2026)
- **ID:** 69b3f912f37d8ada2c68f005
- **Score:** 93.8/100 ✅
- **Word Count:** 2,513
- **Status:** Fully compliant

#### 5. Fractional Property Investment UK: Complete Guide (2026)
- **ID:** 69b3fc8999e82c9d864609fb
- **Score:** 93.8/100 ✅
- **Word Count:** 3,317
- **Status:** Fully compliant

#### 6. How Tokenization Actually Works: An Interactive Guide (2026)
- **ID:** 69b438cec1713c1335795eba
- **Score:** 96.8/100 ✅ **HIGHEST SCORE**
- **Word Count:** 2,629
- **Status:** Fully compliant, best-in-class
- **Issues:** 6 minor only

---

### ❌ FAILED ARTICLES (9)

#### 7. How Fractional Property Ownership Works (OLDEST)
- **ID:** 6984bc29a65d4c23c2b804b8
- **Score:** 58.2/100 ❌ **LOWEST SCORE**
- **Word Count:** 367 (way too short)
- **Critical Issues:**
  - ❌ Missing breadcrumb navigation
  - ❌ Missing risk warning callout
  - ❌ Missing disclaimer section
  - ❌ Missing legal disclaimer
- **Action:** **DELETE or completely rebuild**

#### 8. How Tokenization Actually Works — FIXED
- **ID:** 69b43ef1d2d694302bb345e9
- **Score:** 88.2/100 ❌
- **Issue:** Duplicate of canonical version
- **Action:** DELETE (keep V3 Canonical instead)

#### 9. How Tokenization Actually Works — V2
- **ID:** 69b441d71ce046130686b312
- **Score:** 69.0/100 ❌
- **Design Score:** 20/100 (missing most components)
- **Action:** DELETE (keep V3 Canonical)

#### 10. How Tokenization Actually Works — V3 Canonical
- **ID:** 69b443781ce046130686b32c
- **Score:** 82.0/100 ❌
- **Design Score:** 65/100
- **Issues:** Missing some design components
- **Action:** Fix design issues OR delete if duplicate of #6

#### 11. 5 Ways to Invest in Property Without a Mortgage
- **ID:** 69b4779d68bafe357be173f1
- **Score:** 82.0/100 ❌
- **Design Score:** 62/100
- **Action:** Fix design components

#### 12. FCA Cryptoasset Rules — Fixed
- **ID:** 69b48068528195959496c6b5
- **Score:** 78.2/100 ❌
- **Issue:** Duplicate of #2
- **Action:** DELETE (keep original)

#### 13. Fractional Property Investment UK — Fixed
- **ID:** 69b4808c528195959496c6b7
- **Score:** 83.8/100 ❌
- **Issue:** Duplicate of #5
- **Action:** DELETE (keep original)

#### 14. How to Invest with £500 — Fixed
- **ID:** 69b4808f528195959496c6b9
- **Score:** 85.0/100 ❌
- **Issue:** Duplicate of #3
- **Action:** DELETE (keep original)

#### 15. Tokenized Real Estate vs REITs — Fixed
- **ID:** 69b48091528195959496c6bb
- **Score:** 77.5/100 ❌
- **Issue:** Duplicate of #4
- **Action:** DELETE (keep original)

---

## Design Requirements Checklist

All published articles should have:

### Required Components ✅/❌
- [x] Breadcrumb navigation (Home › Learn › Article)
- [x] Article category label
- [x] Article title (Playfair Display font)
- [x] Article subtitle
- [x] Article meta (date, read time)
- [x] **Risk warning callout** (critical for investment content)
- [x] Key takeaways box (3-5 bullets)
- [x] Disclaimer section
- [x] CTA strip
- [x] Google Fonts (Playfair Display + Inter)

### Typography
- [x] Headings: Playfair Display
- [x] Body: Inter
- [x] Max heading hierarchy: h2, h3 only (no h4+)

### Layout
- [x] Max content width: 720px
- [x] Line height: 1.75
- [x] Paragraph spacing: 20px

---

## Priority Action Plan

### 🔴 CRITICAL (Do Today)

1. **Delete duplicate "Fixed" versions** (5 articles):
   - `69b43ef1d2d694302bb345e9` — Tokenization FIXED
   - `69b441d71ce046130686b312` — Tokenization V2
   - `69b48068528195959496c6b5` — FCA Fixed
   - `69b4808c528195959496c6b7` — Fractional UK Fixed
   - `69b4808f528195959496c6b9` — £500 Fixed
   - `69b48091528195959496c6bb` — REITs Fixed

2. **Delete or rebuild oldest article**:
   - `6984bc29a65d4c23c2b804b8` — "How Fractional Property Ownership Works"
   - This is missing ALL design components and is only 367 words

3. **Review V3 Canonical versions**:
   - Determine if `69b443781ce046130686b32c` (V3 Canonical) is needed
   - If duplicate of `69b438cec1713c1335795eba` (canonical), delete V3

### 🟡 HIGH PRIORITY (This Week)

4. **Fix remaining design issues** in:
   - `69b4779d68bafe357be173f1` — 5 Ways to Invest (Design: 62/100)
   - Add missing breadcrumbs, key takeaways, disclaimers

5. **Standardize article template**:
   - Ensure all articles use same component structure
   - Verify all have risk warnings and disclaimers

### 🟢 MEDIUM PRIORITY (Next Week)

6. **Improve readability**:
   - Break up long sentences (>35 words)
   - Split long paragraphs (>5 sentences)
   - Most articles have 10-15 sentences that are too long

7. **Content audit**:
   - Ensure no conflicting information between articles
   - Update any outdated stats or claims

---

## API Endpoints for Cleanup

**Get all articles:**
```
GET https://settley.fly.dev/articles
```

**Delete article:**
```
DELETE https://settley.fly.dev/articles/delete/:id
```

**Articles to delete:**
```
DELETE /articles/delete/69b43ef1d2d694302bb345e9  # Tokenization FIXED
DELETE /articles/delete/69b441d71ce046130686b312  # Tokenization V2
DELETE /articles/delete/69b48068528195959496c6b5  # FCA Fixed
DELETE /articles/delete/69b4808c528195959496c6b7  # Fractional UK Fixed
DELETE /articles/delete/69b4808f528195959496c6b9  # £500 Fixed
DELETE /articles/delete/69b48091528195959496c6bb  # REITs Fixed
DELETE /articles/delete/6984bc29a65d4c23c2b804b8  # Oldest (or rebuild)
```

---

## Tool Usage

The QA tool is located at `tools/content_qa.py` and `tools/qa_published_articles.py`

**Check published articles:**
```bash
cd tools
python3 qa_published_articles.py
```

**Check local draft:**
```bash
python3 content_qa.py check content/articles/my-article.md
```

**Scan local folder:**
```bash
python3 content_qa.py scan content/articles/
```

---

## Next Steps

1. ✅ Review this report
2. ⏳ Approve deletion of 6-7 duplicate/old articles
3. ⏳ Execute deletions via API
4. ⏳ Fix design issues in remaining articles
5. ⏳ Re-run QA audit to verify 100% pass rate

---

**Report Generated:** 2026-03-14 21:15 GMT  
**Tool Version:** Content QA Tool v1.0 (with Design Checks)  
**Auditor:** Mira, Settley Growth Team  
**Full JSON Report:** `content/QA_PUBLISHED_ARTICLES_REPORT_2026-03-14.json`
