# GitHub Operations Gotchas

**Last Updated:** 2026-03-17  
**Source:** Common failures from GitHub operations

---

## 🚫 Most Common Mistakes

### 1. **Creating PRs Without Context**
**Wrong:**
> `gh pr create --title "Fix bug"`

**Right:**
> `gh pr create --title "Fix: User authentication timeout on mobile" --body "Fixes #123. Timeout was caused by... Tested on iOS/Android."`

**Why:** PRs need context for reviewers. Vague titles = delayed reviews.

---

### 2. **Not Checking Out Issue Context**
**Wrong:**
> Immediately start coding without reading issue comments, linked PRs, or related issues

**Right:**
> `gh issue view <number>` → Read all comments → Check linked PRs → Search for related issues → Then code

**Why:** Missing context leads to wrong solutions and wasted work.

---

### 3. **Skipping Local Testing**
**Wrong:**
> Push directly to remote, rely on CI for testing

**Right:**
> Run tests locally → Fix failures → Push → Monitor CI

**Why:** CI wait times waste time. Catch failures locally first.

---

### 4. **Not Linking Issues to PRs**
**Wrong:**
> Create PR without referencing issue number

**Right:**
> `gh pr create --body "Fixes #123"` or include "Fixes #123" in PR description

**Why:** Auto-closes issues, provides traceability.

---

### 5. **Ignoring Branch Naming**
**Wrong:**
> `git checkout -b fix` or `git checkout -b temp-branch`

**Right:**
> `git checkout -b fix/issue-123-auth-timeout` or `git checkout -b feature/user-dashboard`

**Why:** Clear branch names help with organization and cleanup.

---

### 6. **Not Setting PR Reviewers**
**Wrong:**
> Create PR and wait for someone to notice

**Right:**
> `gh pr create --reviewer @username` or manually add reviewers after creation

**Why:** PRs without assigned reviewers sit stale.

---

### 7. **Forgetting to Update Branch**
**Wrong:**
> Let PR branch get behind main, accumulate merge conflicts

**Right:**
> `gh pr checkout <number>` → `git pull origin main` → Resolve conflicts → Push

**Why:** Fresh branches merge cleanly. Stale branches create conflict nightmares.

---

### 8. **Not Using Draft PRs**
**Wrong:**
> Create full PR for work-in-progress, get premature feedback

**Right:**
> `gh pr create --draft` → Mark as ready when complete

**Why:** Draft PRs signal "work in progress" and prevent premature reviews.

---

### 9. **Skipping CI Status Checks**
**Wrong:**
> Merge PR without checking if CI passed

**Right:**
> Check all CI checks → Review failures → Fix → Merge

**Why:** Merging failing CI breaks main branch.

---

### 10. **Not Cleaning Up Branches**
**Wrong:**
> Leave merged branches lying around forever

**Right:**
> `gh pr merge <number> --delete-branch` or manually delete after merge

**Why:** Cluttered branch list makes navigation harder.

---

## 📊 GitHub Workflow Benchmarks

| Metric | Good | Great | Industry Average |
|--------|------|-------|------------------|
| **PR Size** | < 400 lines | < 200 lines | 500+ lines |
| **PR Review Time** | < 24 hours | < 4 hours | 48+ hours |
| **CI Pass Rate** | 95%+ | 99%+ | 85% |
| **Branch Age** | < 3 days | < 1 day | 7+ days |

**If below benchmarks:** Improve PR descriptions, add reviewers, run tests locally.

---

## 🧪 Pre-PR Checklist

Before creating a PR:

- [ ] **Tests pass locally** (run full test suite)
- [ ] **Issue linked** (Fixes #123 in description)
- [ ] **Clear title** (conveys what and why)
- [ ] **Descriptive body** (context, testing notes, screenshots if UI)
- [ ] **Reviewers assigned** (at least 1, ideally 2)
- [ ] **Branch up to date** (pulled latest from main)
- [ ] **No debug code** (removed console.log, temporary files)
- [ ] **Commit messages clear** (conventional commits preferred)
- [ ] **Draft flag set** (if work-in-progress)
- [ ] **Labels added** (bug, feature, enhancement, etc.)

---

## 🔁 Common Revision Patterns

### Pattern 1: "PR Stale for Days"
**Diagnosis:** No reviewers assigned or unclear value  
**Fix:** 
- Add specific reviewers (@username)
- Improve PR title/description
- Comment tagging reviewers
- Consider breaking into smaller PRs

---

### Pattern 2: "CI Always Failing"
**Diagnosis:** Not running tests locally before pushing  
**Fix:**
- Run full test suite locally
- Fix failures before pushing
- Use pre-commit hooks
- Check CI config for environment differences

---

### Pattern 3: "PR Too Large to Review"
**Diagnosis:** Multiple concerns in one PR  
**Fix:**
- Split into focused PRs (one concern per PR)
- Keep PRs < 400 lines
- Use draft PRs for large refactors
- Add "See individual commits" note if logically separated

---

### Pattern 4: "Merge Conflicts Every Time"
**Diagnosis:** Branch not updated from main regularly  
**Fix:**
- Pull from main daily
- Rebase frequently (not just before merge)
- Communicate with team about overlapping work
- Use feature flags for incomplete features

---

## 📝 Branch Naming Conventions

### ✅ Good Patterns:
- `fix/issue-123-auth-timeout`
- `feature/user-dashboard`
- `refactor/payment-service`
- `docs/api-documentation`
- `test/add-integration-tests`
- `chore/dependency-updates`

### ❌ Bad Patterns:
- `fix`
- `temp`
- `test-branch`
- `my-branch`
- `WIP`
- `asdf`

---

## 🏷️ Label Usage Guide

| Label | When to Use |
|-------|-------------|
| `bug` | Fixing broken functionality |
| `feature` | New functionality |
| `enhancement` | Improvement to existing feature |
| `documentation` | Docs only changes |
| `refactor` | Code restructuring (no behavior change) |
| `test` | Test additions/changes |
| `chore` | Maintenance (dependencies, config) |
| `breaking` | Breaking changes (requires major version bump) |
| `urgent` | Needs immediate attention |
| `blocked` | Waiting on external dependency |

---

## 🛡️ Security Checklist

- [ ] **No secrets committed** (API keys, passwords, tokens)
- [ ] **No sensitive data** in logs or comments
- [ ] **Dependencies scanned** (run `npm audit` or equivalent)
- [ ] **No hardcoded credentials** (use environment variables)
- [ ] **Access controls reviewed** (permissions, roles)
- [ ] **Input validation added** (for user inputs)
- [ ] **Security-sensitive changes reviewed** (by security team if applicable)

---

## ⚡ gh CLI Pro Tips

### Quick Issue Triage:
```bash
# List issues assigned to you
gh issue list --assignee @me

# View issue with comments
gh issue view <number> --comments

# Create issue from template
gh issue create --template "Bug Report"
```

### PR Workflow:
```bash
# Create PR with reviewers
gh pr create --reviewer @username --assignee @me

# Checkout PR locally
gh pr checkout <number>

# Merge and delete branch
gh pr merge <number> --delete-branch --squash

# List your PRs
gh pr list --author @me
```

### Review Management:
```bash
# List PRs needing your review
gh pr list --review-requested @me

# Approve PR
gh pr review <number> --approve

# Comment on PR
gh pr comment <number> --body "LGTM with minor fixes"
```

---

**Update This File:** After each GitHub operation session, add new gotchas and learnings. This file should grow smarter over time.
