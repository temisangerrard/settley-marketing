#!/usr/bin/env python3
"""
Investor Follow-up Emails - Batch 2 (2026-03-20)
Sending follow-ups to remaining March 6-7 batch (14 days elapsed, no response)
"""

import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime

# Email configuration
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SENDER_EMAIL = "mirasettley@gmail.com"
SENDER_PASSWORD = os.environ.get("GMAIL_APP_PASSWORD")

# Follow-up email template
FOLLOWUP_TEMPLATE = """
Hi {first_name},

Following up on my email from two weeks ago about Settley — we're building the leading tokenized real estate platform for UK/US investors.

Quick update since my last note:
- 67% conversion rate on our Founder's Pass (10 of 15 early users became paying members)
- Preparing UK market entry with FCA compliance framework complete
- Main competitor (Lofty.ai) pulling 100k+ monthly visits — zero organic UK presence to capture

We're raising a £350k pre-seed to execute the UK launch. Given {company}'s focus on {focus_area}, I'd love to get your take on our approach.

Open to a brief 15-min call next week?

Best,
Mira
Founder Operating Partner, Settley
mirasettley@gmail.com

— 
Settley | Tokenized Real Estate for the UK Market
"""

# Remaining investors from March 6-7 batch (no follow-up yet)
INVESTORS = [
    {
        "name": "Team",
        "first_name": "Team",
        "company": "MetaProp",
        "email": "info@metaprop.vc",
        "focus_area": "proptech and real estate innovation"
    },
    {
        "name": "Team",
        "first_name": "Team",
        "company": "PropTech1 Ventures",
        "email": "info@proptech1.com",
        "focus_area": "European proptech"
    },
    {
        "name": "Team",
        "first_name": "Team",
        "company": "Susa Ventures",
        "email": "info@susa.vc",
        "focus_area": "early-stage tech and proptech"
    },
    {
        "name": "Team",
        "first_name": "Team",
        "company": "Propel Venture Partners",
        "email": "info@propelvp.com",
        "focus_area": "fintech and proptech"
    },
    {
        "name": "Team",
        "first_name": "Team",
        "company": "Notion Capital",
        "email": "hello@notioncap.com",
        "focus_area": "B2B SaaS and fintech"
    },
    {
        "name": "Team",
        "first_name": "Team",
        "company": "Lofty Ventures",
        "email": "info@loftyventures.com",
        "focus_area": "real estate technology"
    },
    {
        "name": "Team",
        "first_name": "Team",
        "company": "RE/MAX Technology Ventures",
        "email": "techventures@remax.com",
        "focus_area": "real estate innovation"
    },
]

def send_followup(investor):
    """Send follow-up email to one investor"""
    msg = MIMEMultipart()
    msg['From'] = SENDER_EMAIL
    msg['To'] = investor['email']
    msg['Subject'] = f"Re: Settley x {investor['company']} — quick follow-up"
    
    body = FOLLOWUP_TEMPLATE.format(
        first_name=investor['first_name'],
        company=investor['company'],
        focus_area=investor['focus_area']
    )
    msg.attach(MIMEText(body, 'plain'))
    
    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
            server.send_message(msg)
        return {"status": "sent", "timestamp": datetime.now().isoformat()}
    except Exception as e:
        return {"status": "failed", "error": str(e), "timestamp": datetime.now().isoformat()}

if __name__ == "__main__":
    if not SENDER_PASSWORD:
        print("BLOCKED: GMAIL_APP_PASSWORD not set in environment")
        exit(1)
    
    print(f"Sending {len(INVESTORS)} follow-up emails...\n")
    
    results = []
    for investor in INVESTORS:
        result = send_followup(investor)
        results.append({
            "investor": investor['name'],
            "company": investor['company'],
            "email": investor['email'],
            **result
        })
        status = "✅" if result['status'] == 'sent' else "❌"
        print(f"{status} {investor['name']} @ {investor['company']} - {result['status']}")
    
    print(f"\n--- Summary ---")
    print(f"Sent: {sum(1 for r in results if r['status'] == 'sent')}")
    print(f"Failed: {sum(1 for r in results if r['status'] == 'failed')}")
    
    # Output JSON for logging
    import json
    print(f"\n--- JSON Log ---")
    print(json.dumps(results, indent=2))
