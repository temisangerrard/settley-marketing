# Content Creation Subagent Blueprint

## Purpose
- Handle long-form articles, landing page copy, email nurture content, and social posts.
- Take strategic briefs from Mira and execute drafts autonomously, returning markdown deliverables for review.

## When to Spawn
1. Any net-new content asset that will take more than a short outline.
2. Multi-section articles or comparison pages requiring research + structured writing.
3. Repurposing recorded calls, transcripts, or investor memos into publishable content.

## Invocation Template
Use `sessions_spawn` with runtime `subagent`, label `content-agent`, and pass the job brief in the `task` string. Example:

```
sessions_spawn({
  "task": "Write a 1,200-word comparison page: Settley vs Lofty.ai...",
  "label": "content-agent",
  "runtime": "subagent",
  "model": "openai/gpt-5.1-codex",
  "mode": "run",
  "timeoutSeconds": 600
})
```

Adjust `task` with:
- Audience + stage (e.g., UK retail investors, awareness stage)
- CTA / desired action
- Tone or voice constraints
- Source links or briefs

## Operating Notes
- Keep this subagent focused on creation; strategy and outlines stay with Mira.
- Always capture returned drafts in `content/drafts/` with ISO timestamp filenames.
- After each run, summarize outputs + next steps in-session so Temisan has visibility.
