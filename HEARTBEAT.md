# Heartbeat checklist

Output contract (strict):
- If no verified changes since last check, reply exactly `HEARTBEAT_OK`.
- Only report items backed by concrete evidence (file path + timestamp, commit SHA, or URL).
- Do not claim outreach/posting/publishing happened unless verifiable proof exists in this run.
- If something cannot be verified, mark it `UNVERIFIED`.
- If access/tooling is missing, mark it `BLOCKED` and state the exact dependency needed.

- Check mirasettley@gmail.com for replies to outreach, partnership requests, or anything needing a response — if urgent, message Temisan now
- Scan for breaking news or trending discussions about tokenized real estate, proptech, or fractional investing in UK/US — if something is worth acting on, flag it
- Check for new opportunities beyond Settley-only scope: grants, hackathons, accelerators, and agent tooling updates relevant to Temisan's active builds
- If Temisan shared new links recently, ensure each link has a logged action recommendation and next step
- Check if any content drafts in content/drafts/ are complete and ready to commit to the repo
- If a growth opportunity or tool access is blocked, message Temisan immediately with exactly what is needed and why
- If a prospecting/reachout initiative is in progress (investors/partners/distribution), make sure there is a live task list in ops/prospecting/ and update progress at least once per day
- If quiet for 8+ hours during daytime, send a brief status: what's in progress, what's ready, what's next
- For any active long task, resume via `memory/loops/<task-slug>.md` checkpoint (Ralph loop mode): execute only the next smallest step, then write a new checkpoint instead of re-running the whole task context
