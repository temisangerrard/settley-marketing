# Blogger SEO Backlink Agent

**Purpose:** Automated creation of Blogger blogs for dofollow backlinks to settley.co  
**Type:** Ralph loop agent (1 blog per loop, ~10 min each)  
**Target:** 10 blogs in 30 days

---

## Agent Configuration

```yaml
agent:
  name: blogger-seo-agent
  type: ralph-loop
  task: Create Blogger blogs with dofollow links
  loop_size: 1 blog per loop
  loops_target: 10
  timeout_per_loop: 900s (15 min)
  
credentials:
  primary: mirasettley@gmail.com
  backup: [create as needed if rate limited]
  
workspace:
  checkpoint_file: memory/loops/blogger-backlinks.md
  pipeline_doc: ops/seo/blogger-backlink-pipeline.md
```

---

## Loop Execution Protocol

### Pre-Loop Check
1. Read checkpoint file (memory/loops/blogger-backlinks.md)
2. Confirm current loop number (e.g., "Loop #2 of 10")
3. Review suggested blog name/URL for this loop
4. Verify browser access available

### Loop Steps
1. **Navigate** to blogger.com
2. **Sign in** with mirasettley@gmail.com (or backup account)
3. **Create blog:**
   - Click "Create your blog" or "New Blog"
   - Enter blog name (use suggested angle)
   - Choose URL (use suggested format)
   - Set display name
4. **Add description:**
   - Go to Settings → Description
   - Add templated description with settley.co link
   - Save
5. **Create post:**
   - Click "New post"
   - Write title (use suggested angle)
   - Write content (100-200 words with contextual link)
   - Publish
6. **Verify:**
   - View blog to confirm live
   - Check description has link
   - Check post has link
7. **Log results:**
   - Update checkpoint file with blog URL, post URL
   - Mark loop as DONE
   - Write next loop instructions
8. **Checkpoint:**
   - Write status: CONTINUE (if <10) or DONE (if 10/10)
   - Include evidence (URLs)
   - Specify next loop's suggested name/URL

### Post-Loop
- Announce completion to parent session
- Include: loop number, blog URL, post URL, progress (X/10)
- If 10/10 complete: mark task DONE, summarize all 10 blogs

---

## Content Templates

### Description Template
```
[Company] provides [product/service] for [target market]. [Key benefit]. Visit https://settley.co to [CTA].
```

### Post Template (100-200 words)
```
Title: [Keyword-rich title]

[Hook - question or pain point]

[Solution - what Settley offers]

[CTA with link] - Visit https://settley.co to [specific action].

[Optional: 1-2 sentences of additional context]
```

### Angle Variations (to avoid duplicate content)

| Angle | Focus | Example Title |
|-------|-------|---------------|
| Tokenized | Blockchain/tech | "Tokenized Real Estate Explained" |
| Fractional | Accessibility | "Fractional Property from £100" |
| Passive Income | Returns | "Passive Income from Property" |
| Beginner | Education | "Property Investment for Beginners" |
| Portfolio | Diversification | "Build a Property Portfolio" |
| Alternative | Non-traditional | "Alternative Property Investment" |
| Crowdfunding | Platform model | "Property Crowdfunding UK" |
| Digital | Modern/tech | "Digital Real Estate Investment" |
| Smart | Intelligent investing | "Smart Property Investment" |
| UK-focused | Geographic | "UK Property Investment Guide" |

---

## Error Handling

**If sign-in fails:**
- Try backup Google account
- If no backup, create new Gmail account
- Log new credentials securely

**If URL taken:**
- Add hyphen or number variation
- Example: uk-property-invest-2026.blogspot.com

**If rate limited:**
- Wait 24 hours before next loop
- Or use different Google account

**If blog flagged/removed:**
- Document reason if provided
- Create replacement with different content
- Note in tracker

---

## Quality Checks

**Each blog must have:**
- [ ] Unique blog name (not identical to others)
- [ ] Working description with settley.co link
- [ ] At least 1 published post
- [ ] Post contains contextual link to settley.co
- [ ] Blog is publicly viewable

**Content variation:**
- [ ] Description differs from other blogs
- [ ] Post title is unique
- [ ] Post content is not copy-paste (rephrase for each)

---

## Completion Criteria

**Task is DONE when:**
- 10/10 blogs created and published
- All blogs have working links to settley.co
- All URLs logged in checkpoint file
- Summary provided to parent session

**Summary should include:**
- Total blogs created (10)
- List of all blog URLs
- List of all post URLs
- Date range (start → end)
- Any issues encountered

---

## Parent Session Handoff

**To spawn this agent:**

```
sessions_spawn with:
  task: "Execute Blogger SEO backlink campaign - create 10 Blogger blogs with dofollow links to settley.co"
  mode: "session" (persistent across loops)
  runtime: "subagent"
  label: "blogger-seo-agent"
```

**To check progress:**
```
sessions_send with:
  sessionKey: [agent session key]
  message: "Status check - how many blogs created so far?"
```

**To steer/adjust:**
```
subagents with:
  action: "steer"
  target: [agent id]
  message: "Adjustment: focus more on 'fractional property' angle for next 3 blogs"
```

---

**Created:** 2026-03-15  
**Pipeline Doc:** ops/seo/blogger-backlink-pipeline.md  
**Checkpoint File:** memory/loops/blogger-backlinks.md  
**Owner:** Mira (Settley Growth)
