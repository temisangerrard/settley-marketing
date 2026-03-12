# Agency Agents – Adoption Plan for Settley

_Last updated: 2026-03-08_

## 1. Why this matters
- **Ready-made agent personas** with rules, workflows, and deliverables we can adapt to Settley immediately (saves days of persona engineering).
- **Multi-tool integration scripts** let us port these agents into Claude Code, Cursor, Gemini CLI, etc.—aligns with how we already work in Claude.
- **Battle-tested processes** covering growth, marketing, product, and engineering; we can cherry-pick the ones that reinforce our GTM motions (Reddit, Twitter, SEO, experimentation).

## 2. High-priority agents for Settley
| Division | Agent | Settley Use Case |
| --- | --- | --- |
| Marketing | Growth Hacker | Rapid UK/US traction experiments, test loops, reporting |
| Marketing | Reddit Community Builder | Authentic participation in r/UKInvesting, r/RealEstate, r/CryptoCurrency |
| Marketing | Twitter Engager | Daily X presence + compounding authority from @mirasettley |
| Marketing | Content Creator | Long-form explainers + SEO cluster execution |
| Product | Trend Researcher | Continuous insight on tokenized real estate, market shifts |
| Project Mgmt | Experiment Tracker | Enforce hypothesis-driven growth ops |
| Testing | Reality Checker | Final QA for anything public (tweets, landing pages) |

We can import the base persona files and layer Settley-specific context (market focus, tone, KPIs) so they become reusable “Mira agents”.

## 3. Recommended plan
1. **Fork or vendor the repo** under `research/vendor/agency-agents/` for local reference (no toolchain changes yet).
2. **Clone the top-priority agents** above into `skills/agents/` and rewrite their mission/rules with Settley context (UK/US tokenized real estate, zero-budget growth, investor narrative support).
3. **Wire into Claude Code**: copy customized agents into `~/.claude/agents/settley/` so every Claude session can hot-swap the relevant persona.
4. **Document invocation patterns** in `skills/README.md` so it’s obvious which agent to call for each workflow (e.g., tweet sweeps vs. Reddit spins).
5. **Expand to Cursor/Windsurf** only if we see heavy use in those tools; otherwise defer.

## 4. Immediate next steps (this week)
- [ ] Vendor repo snapshot locally for reference (git subtree or simple copy)
- [ ] Customize Growth Hacker + Reddit Community Builder files with Settley tone & KPIs
- [ ] Test activation in Claude Code and log findings in `EXPERIMENTS.md`
- [ ] Evaluate whether Experiment Tracker improves our existing growth retros template

## 5. Longer-term opportunities
- Build a **Settley Agent Catalog** mirroring their structure so every major GTM workflow (SEO, partnerships, outreach) has an agentized playbook.
- Publish a “tokenized real estate kit” agent bundle as a lead magnet once we refine our own versions (potential backlink + authority win).
- Use their `./scripts/convert.sh` approach as a blueprint for exporting our OpenClaw skills into other ecosystems when we want cross-distribution.
