# Settley URL Structure — CRITICAL REFERENCE

**Created:** 2026-03-15 (after repeated mistakes)  
**Last Updated:** 2026-03-15 (corrected with actual URL format from founder)

---

## The Rule (DO NOT FORGET)

| Purpose | Domain | Example |
|---------|--------|---------|
| **API (Publishing)** | `settley.fly.dev` | `POST https://settley.fly.dev/articles/create` |
| **Live Articles** | `settley.co` | `https://settley.co/articles/69b6841a21185b6f7e6dda0a/` |

---

## Backlinks ALWAYS Point To

✅ **CORRECT:** `https://settley.co/articles/[MongoDB_ID]/`
❌ **WRONG:** `https://settley.fly.dev/articles/[id]`
❌ **WRONG:** `https://settley.co/articles/[slug]` (slugs are NOT used)

**Why:** fly.dev is the backend API. settley.co/articles/[ID]/ is where articles are served.

---

## Article URL Format

Articles on settley.co use **MongoDB Object IDs**, NOT slugs:

**Format:** `https://settley.co/articles/[24-character-hex-ID]/`

| Article Title | ID | URL |
|---------------|-----|-----|
| Complete Guide to Tokenized Real Estate UK | 69b67f48fd3d36453df2cdb6 | https://settley.co/articles/69b67f48fd3d36453df2cdb6/ |
| How Tokenization Actually Works | 69b67f49fd3d36453df2cdb8 | https://settley.co/articles/69b67f49fd3d36453df2cdb8/ |
| 5 Ways to Invest Property Without Mortgage | 69b67f4afd3d36453df2cdba | https://settley.co/articles/69b67f4afd3d36453df2cdba/ |
| Settley vs Lofty | 69b683d921185b6f7e6dd9f4 | https://settley.co/articles/69b683d921185b6f7e6dd9f4/ |
| Best Lofty Alternatives | 69b683dc21185b6f7e6dd9f8 | https://settley.co/articles/69b683dc21185b6f7e6dd9f8/ |

---

## Publishing Flow

```
1. POST to API: https://settley.fly.dev/articles/create
   → Returns: { _id: "69b6841a21185b6f7e6dda0a", title: "...", content: "..." }

2. Article is served at: https://settley.co/articles/69b6841a21185b6f7e6dda0a/
   → Uses MongoDB ID, NOT slug

3. Backlinks point to: https://settley.co/articles/[ID]/
   → NEVER to fly.dev URLs
   → NEVER use slugs (not used by settley.co)
```

---

## Memory Rule

**When creating backlinks, ALWAYS use:**
```
https://settley.co/articles/[MongoDB_ID]/
```

**NEVER use:**
```
https://settley.fly.dev/... (backend API only)
https://settley.co/articles/[slug] (slugs not used)
```

This has been corrected multiple times. Do not repeat this mistake.

---

**Last Updated:** 2026-03-15  
**Source:** Founder provided actual URL: https://settley.co/articles/69b6841a21185b6f7e6dda0a/
