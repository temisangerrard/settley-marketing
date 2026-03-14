# Settley Tools

Internal tools for content management, QA, and growth operations.

## Content QA Tool

**Purpose:** Automated quality assurance for Settley articles.

**Checks:**
- ✅ Duplicate content detection (compares against all past articles)
- ✅ Brand voice compliance (tone, avoided words, required elements)
- ✅ SEO best practices (title length, word count, structure)
- ✅ Content quality (sentence length, paragraph structure)

### Usage

```bash
# Check a single article
python tools/content_qa.py check content/articles/my-article.md

# Scan all articles in a folder
python tools/content_qa.py scan content/articles/

# Compare two articles for similarity
python tools/content_qa.py compare article1.md article2.md
```

### Output Example

```
======================================================================
QA REPORT: tokenized-real-estate-uk-guide.md
======================================================================

📊 SCORES:
   Overall: 85.3/100 ✅ PASS
   Brand:   90.0/100
   SEO:     80.0/100
   Quality: 85.0/100
   Words:   1247

📋 ISSUES (3 total):

   🟡 WARNINGS (2):
      • [seo] Article could be longer (1247 words)
        → Aim for at least 1500 words for better SEO
      • [brand] No mention of target markets (UK/US)
        → Mention UK/US markets to reinforce geographic focus

   🔵 INFO (1):
      • [quality] Sentence 12 is too long (42 words)
        → Break into shorter sentences for readability

======================================================================
```

### Brand Guidelines Enforced

**Voice & Tone:**
- Direct, confident, educational
- No hype words ("revolutionary", "game-changing", etc.)
- Prefer clear, proven, transparent language

**Required Elements:**
- ✅ Call-to-action (CTA)
- ✅ Legal disclaimer
- ⚠️ Target market mention (UK/US) - preferred

**SEO Requirements:**
- Title: 30-60 characters
- Meta description: 120-160 characters
- Minimum word count: 800 words
- Keyword density: 0.5-2.5%

### Integration

**Pre-commit hook:** Run QA check before committing articles

```bash
# Add to .git/hooks/pre-commit
python tools/content_qa.py check content/articles/*.md
```

**CI/CD:** Add to GitHub Actions workflow

```yaml
- name: Content QA
  run: python tools/content_qa.py scan content/articles/
```

## Other Tools

_(More tools coming soon)_

- `link_checker.py` - Verify all external links in articles
- `seo_analyzer.py` - Deep SEO analysis and recommendations
- `brand_monitor.py` - Track brand mentions across content
