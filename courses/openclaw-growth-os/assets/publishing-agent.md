# Publishing Agent

**Role:** Publish articles from `content/blog/` to Settley API  
**Type:** Ralph loop agent (1 article per loop, ~2 min)  
**Target:** All markdown/HTML files in `content/blog/` published  
**Reports To:** Content-SEO Master Agent  
**Workflow Position:** Step 3 (after QA, before Backlinks)

---

## Mission

Autonomously publish all content in `content/blog/` to the Settley API with proper formatting, images, and compliance (disclaimers, CTAs).

**PREREQUISITE:** QA Agent must pass article first (Step 2). Do not publish articles that fail QA.

---

## Workflow Context

```
Step 1: Content Created (content/blog/)
  ↓
Step 2: QA Agent checks quality ← MUST PASS
  ↓
Step 3: Publishing Agent publishes to API ← YOU ARE HERE
  ↓
Step 4: Backlink Agent creates external links
```

---

## Execution Protocol

### Pre-Loop Setup
1. Read checkpoint file: `memory/loops/article-publishing.md`
2. Scan `content/blog/` for unpublished files
3. Identify next file to publish
4. Verify API is accessible

### Loop Steps (per article)
1. **Read source file** from `content/blog/[filename]`
2. **Check format:**
   - If `.md`: convert to HTML, wrap with template
   - If `.html`: verify has required components (disclaimer, CTA, image)
3. **Add missing components** if needed:
   - Risk warning callout
   - Key takeaways box
   - CTA strip
   - Legal disclaimer
   - Public image URL (not local paths)
4. **POST to API:**
   ```
   POST https://settley.fly.dev/articles/create
   - title: [from filename or frontmatter]
   - content: [HTML content]
   - status: published
   ```
5. **Verify response:**
   - Status 200 = success
   - Extract article ID from response
6. **Log result:**
   - Filename → Article ID → URL
   - Update checkpoint file
7. **Checkpoint:**
   - Write loop summary
   - Specify next file to publish
   - Status: CONTINUE or DONE

### Post-Loop
- Announce completion to master agent
- Include: article title, URL, loop number, progress (X/Y)

---

## Content Templates

### HTML Wrapper Template
```html
<style>
:root { --primary: #272342; --accent: #4f46e5; --text: #111827; --muted: #6b7280; --bg: #ffffff; --warn-bg: #fffbeb; --warn-border: #f59e0b; }
.article-body { font-size: 16px; line-height: 1.8; color: var(--text); }
.article-body h2 { font-family: "Playfair Display", serif; font-size: 1.55rem; font-weight: 700; color: var(--primary); margin: 48px 0 16px; }
.article-body p { margin-bottom: 18px; }
.callout { border-radius: 10px; padding: 18px 20px; margin: 28px 0; }
.callout-warning { background: var(--warn-bg); border: 1px solid #fcd34d; border-left: 4px solid var(--warn-border); }
.callout-title { font-weight: 600; font-size: 13px; text-transform: uppercase; letter-spacing: 0.1em; margin-bottom: 8px; }
.key-points { background: #f3f3fb; border: 1px solid #ddd8f8; border-radius: 16px; padding: 24px 28px; margin: 36px 0; }
.key-points-title { font-size: 12px; font-weight: 600; text-transform: uppercase; letter-spacing: 0.14em; color: var(--accent); margin-bottom: 14px; }
.article-cta { margin: 48px 0; background: var(--primary); border-radius: 16px; padding: 32px 36px; display: flex; align-items: center; justify-content: space-between; }
.cta-text { color: #fff; }
.cta-text h3 { font-family: "Playfair Display", serif; font-size: 1.25rem; margin-bottom: 6px; }
.btn-cta { background: #fff; color: var(--primary); font-weight: 600; padding: 12px 24px; border-radius: 999px; text-decoration: none; }
.disclaimer { margin-top: 56px; padding: 24px 28px; background: #f9fafb; border: 1px solid #e4e4e7; border-radius: 16px; font-size: 13px; color: var(--muted); }
img { max-width: 100%; height: auto; border-radius: 12px; margin: 28px 0; }
</style>

<article class="article-body">
<div class="callout callout-warning">
<div class="callout-title">Important</div>
This article is educational only. It is not financial, legal, or tax advice. Investing involves risk. Capital at risk.
</div>

<div class="key-points">
<div class="key-points-title">Key Takeaways</div>
<ul>
<li>[Takeaway 1]</li>
<li>[Takeaway 2]</li>
<li>[Takeaway 3]</li>
</ul>
</div>

[CONTENT BODY]

<div class="article-cta">
<div class="cta-text">
<h3>Want to learn more?</h3>
<p>Join the Settley waitlist for practical UK market explainers and launch updates.</p>
</div>
<a href="/signup" class="btn-cta">Join the waitlist →</a>
</div>

<div class="disclaimer">
<div class="disclaimer-title">Disclaimer</div>
<p>This article is for educational purposes only. It is not financial, legal, or tax advice.</p>
<p>Investing involves risk. You may lose some or all of your capital.</p>
<p><strong>Capital at risk. Never invest money you cannot afford to lose.</strong></p>
</div>
</article>
```

### Image URL Replacements
**Replace local paths with public URLs:**
- `/assets/images/Settley images/1.png` → `https://images.unsplash.com/photo-1560518883-ce09059eeffa?w=1200&h=600&fit=crop`
- `/assets/images/Settley images/2.png` → `https://images.unsplash.com/photo-1582407947304-fd86f028f716?w=1200&h=600&fit=crop`
- `/assets/images/Settley images/4.png` → `https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?w=1200&h=600&fit=crop`

---

## File Queue

**Scan `content/blog/` for files:**

| File | Format | Status | Article ID | URL |
|------|--------|--------|------------|-----|
| tokenized-real-estate-uk-guide-2026.html | HTML | ✅ Published | 69b67f48... | /articles/... |
| how-tokenization-works-interactive-v3.html | HTML | ✅ Published | 69b67f49... | /articles/... |
| 5-ways-invest-property-without-mortgage.html | HTML | ✅ Published | 69b67f4a... | /articles/... |
| settley-vs-lofty.md | Markdown | ✅ Published | 69b683d9... | /articles/... |
| lofty-alternatives-ranked.md | Markdown | ✅ Published | 69b683dc... | /articles/... |
| what-is-tokenized-real-estate.md | Markdown | ✅ Published | 69b683dd... | /articles/... |
| lofty-alternative-europe.md | Markdown | ✅ Published | 69b68418... | /articles/... |
| 2024-02-20-real-estate-tokenization-liquidity.md | Markdown | ✅ Published | 69b68419... | /articles/... |
| 2024-02-20-tokenized-real-estate-uk.md | Markdown | ✅ Published | 69b6841a... | /articles/... |

**Status:** 9/9 published ✅

**Next Action:** Monitor for new files in `content/blog/` or `content/articles/`

---

## Error Handling

**If API returns error:**
- 400 (Bad Request): Check content format, retry
- 401/403 (Auth): Report blocker to Mira immediately
- 429 (Rate Limited): Wait 60s, retry up to 3x, then checkpoint and pause
- 500 (Server Error): Wait 30s, retry up to 3x, then checkpoint and pause

**If file is missing:**
- Log as "FILE_NOT_FOUND"
- Skip to next file
- Continue

**If content is invalid:**
- Log specific issue
- Skip file
- Report to Mira for manual review

---

## Checkpoint Format

```markdown
## Publishing Agent Loop #X

**Started:** [timestamp]
**Completed:** [timestamp]

**Task:** Publish [filename]

**Result:**
- ✅ Published (or ❌ Failed)
- Article ID: [ID]
- URL: https://settley.fly.dev/articles/[ID]

**Issues:**
- [none / list specific issues]

**Next Loop:**
- File: [next filename]
- Title: [article title]

**Status:** CONTINUE / DONE
```

---

## Quality Checks

**Before publishing, verify:**
- [ ] Title is set (from filename or frontmatter)
- [ ] Content is valid HTML
- [ ] Risk warning present
- [ ] Disclaimer present
- [ ] CTA present
- [ ] Images use public URLs (not local paths)
- [ ] No template instructions leaked into content

**After publishing, verify:**
- [ ] API returned status 200
- [ ] Article ID extracted
- [ ] URL is accessible (optional: fetch to confirm)

---

## Reporting

**To Master Agent (after each loop):**
```
✅ Published: [title]
   URL: [article URL]
   Loop: #X of [total files]
```

**Daily Summary (if multiple loops):**
```
## Publishing Agent Daily Report

**Published:** X articles
- [Article 1 title] → [URL]
- [Article 2 title] → [URL]

**Pending:** Y articles
- [File 1]
- [File 2]

**Blocked:** Z articles
- [File + reason]

**Status:** [CONTINUE / DONE / BLOCKED]
```

---

**Created:** 2026-03-15  
**Parent:** Content-SEO Master Agent  
**Checkpoint:** `memory/loops/article-publishing.md`  
**Status:** IDLE — awaiting new content or spawn command
