#!/usr/bin/env python3
"""
Automated Investor Outreach System for Settley
Researches, contacts, and tracks investor prospects at scale
"""

import requests
import json
import time
import re
from datetime import datetime, timedelta
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import csv
import openai
from bs4 import BeautifulSoup

# API Keys and Configuration
OPENROUTER_API_KEY = "sk-or-xxxxx"  # From .env
GMAIL_EMAIL = "mirasettley@gmail.com"
GMAIL_APP_PASSWORD = "hgtjqxdmaywxnfgj"

# Target investor categories
INVESTOR_CATEGORIES = {
    "UK PropTech VCs": [
        "Tangent Capital Partners",
        "Playfair Capital", 
        "Growth Street Ventures",
        "Eos Venture Partners",
        "Maven Capital Partners",
        "Stonehage Fleming Digital Assets",
        "Beringea",
        "Notion Capital"
    ],
    "Global PropTech VCs": [
        "MetaProp",
        "PropTech1",
        "Susa Ventures",
        "Zeeve",
        "RealVC",
        "Propel Venture Partners",
        "Perchwell Ventures",
        "Techstars"
    ],
    "Real Estate Tech VCs": [
        "Lofty Ventures",
        "RE/MAX Technology Ventures", 
        "RealT Investments",
        "PropTech VC",
        "Real Estate Technology Ventures",
        "Property Technology Ventures",
        "EstateGuru",
        "Housing.com Ventures"
    ],
    "AI/Blockchain VCs": [
        "a16z Crypto",
        "Paradigm",
        "Dragonfly Capital",
        "Polychain Capital",
        "Variant Fund",
        "Electric Capital",
        "Robot Ventures",
        "Decentraland Ventures"
    ]
}

# Email templates
EMAIL_TEMPLATES = {
    "uk_proptech": {
        "subject": "Settley: Tokenized Real Estate for UK Investors - 67% Conversion Rate",
        "body": """Hi {name},

I hope this message finds you well.

I'm Mira Settley, cofounder of Settley - building the infrastructure for fractional property ownership in UK/US markets.

We're seeing incredible traction with our approach:
🏠 **67% conversion rate** on our Founder's Pass
📊 **150+ users** (expanding from Nigeria to UK/US markets)
💰 **Tokenized real estate** starting from just £50

Why this matters for your portfolio:
- **Accessibility**: No £500k+ minimums for London property
- **Liquidity**: Trade 24/7 vs traditional property's 6-month sales cycle
- **Diversification**: Multiple properties, cities, and asset classes from one platform

We're currently expanding to UK markets and would love to explore how Settley might align with your investment thesis.

Would you be open to a brief chat next week to discuss our traction and roadmap?

Best regards,
Mira Settley | Cofounder & Chief Growth Officer
Settley.co | Tokenized Real Estate Platform"""
    },
    "global_proptech": {
        "subject": "Settley: Democratizing Property Investment via Tokenization - UK Expansion",
        "body": """Hi {name},

I'm reaching out as we expand Settley's tokenized real estate platform to global markets.

Key highlights:
🚀 **67% conversion rate** - exceptional product-market fit
🌍 **UK/US expansion** - targeting £50 entry points
📈 **150+ users** - growing from Nigerian market to global traction

Our platform makes property ownership accessible by:
- Fractionalizing prime real estate assets
- Enabling 24/7 liquidity (vs traditional property's illiquid nature)
- Providing blockchain transparency for retail investors

Given your focus on [specific portfolio company or area], I believe Settley's approach could complement your portfolio strategy.

Would you be interested in learning more about our traction and roadmap for 2026?

Best regards,
Mira Settley | Cofounder & Chief Growth Officer
Settley.co"""
    },
    "ai_blockchain": {
        "subject": "Settley: Autonomous Agents + Tokenized Real Estate - AI-Powered Property Investment",
        "body": """Hi {name},

I'm Mira Settley, cofounder of Settley - combining autonomous agents with tokenized real estate.

We're building an AI-powered platform where:
- Autonomous bots analyze and select investment properties
- Tokenization enables fractional ownership from £50
- 67% conversion rate demonstrates strong product-market fit

Our autonomous agent runtime on Base mainnet already powers 5 games with sophisticated onchain settlement logic.

As we expand to UK/US markets, we'd love to explore how our AI + tokenized real estate approach might align with your thesis.

Would you be open to a brief introduction to discuss our traction?

Best regards,
Mira Settley | Cofounder & Chief Growth Officer
Settley.co | Autonomous Arena + Tokenized Real Estate"""
    }
}

def enrich_investor_data(investor_name, company):
    """Use OpenRouter to research investor contacts and company details"""
    prompt = f"""
Research the following investor and provide:
1. Most likely email address pattern
2. Name of the key contact/decision maker
3. Recent investments or portfolio focus
4. Best outreach angle
5. Any specific triggers or timing cues

Investor: {investor_name}
Company: {company}

Return as JSON with: email_pattern, contact_name, recent_investments, outreach_angle, timing_signals
"""
    
    try:
        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {OPENROUTER_API_KEY}",
                "Content-Type": "application/json"
            },
            json={
                "model": "anthropic/claude-3.5-sonnet",
                "messages": [{"role": "user", "content": prompt}],
                "temperature": 0.3
            }
        )
        
        if response.status_code == 200:
            result = response.json()
            content = result['choices'][0]['message']['content']
            # Extract JSON from response
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
    except Exception as e:
        print(f"Error enriching {investor_name}: {e}")
    
    return None

def send_email_via_smtp(to_email, subject, body):
    """Send email via Gmail SMTP"""
    try:
        msg = MIMEMultipart()
        msg['From'] = GMAIL_EMAIL
        msg['To'] = to_email
        msg['Subject'] = subject
        
        msg.attach(MIMEText(body, 'plain'))
        
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(GMAIL_EMAIL, GMAIL_APP_PASSWORD)
        
        text = msg.as_string()
        server.sendmail(GMAIL_EMAIL, to_email, text)
        server.quit()
        
        return True
    except Exception as e:
        print(f"Failed to send to {to_email}: {e}")
        return False

def track_outreach(contact_name, company, email, category, status="sent"):
    """Track outreach in CSV file"""
    timestamp = datetime.now().isoformat()
    
    # Read existing data
    try:
        with open('/Users/temisan/Downloads/settley-marketing/ops/prospecting/investor-outreach.csv', 'r') as f:
            reader = csv.DictReader(f)
            data = list(reader)
    except FileNotFoundError:
        data = []
    
    # Add new entry
    new_entry = {
        'timestamp': timestamp,
        'contact_name': contact_name,
        'company': company,
        'email': email,
        'category': category,
        'status': status,
        'notes': ''
    }
    
    data.append(new_entry)
    
    # Write back
    with open('/Users/temisan/Downloads/settley-marketing/ops/prospecting/investor-outreach.csv', 'w', newline='') as f:
        if data:
            writer = csv.DictWriter(f, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)

def main():
    """Main outreach automation function"""
    print("🚀 Starting automated investor outreach...")
    
    # Count sent emails
    try:
        with open('/Users/temisan/Downloads/settley-marketing/ops/prospecting/investor-outreach.csv', 'r') as f:
            reader = csv.DictReader(f)
            sent_count = sum(1 for row in reader if row['status'] == 'sent')
    except FileNotFoundError:
        sent_count = 0
    
    print(f"📊 Starting from {sent_count}/50 sent emails")
    
    # Process each investor category
    for category, investors in INVESTOR_CATEGORIES.items():
        print(f"\n🎯 Processing {category}...")
        
        template_key = category.lower().replace(" ", "_").replace("/", "_")
        if template_key not in EMAIL_TEMPLATES:
            template_key = "global_proptech"  # fallback
        
        for investor in investors:
            if sent_count >= 50:
                print(f"✅ Reached 50 email limit!")
                return
            
            print(f"  🔍 Researching {investor}...")
            
            # Get investor details
            investor_data = enrich_investor_data(investor, category)
            
            if not investor_data:
                print(f"  ⚠️  Could not enrich {investor}, skipping...")
                continue
            
            # Get template
            template = EMAIL_TEMPLATES[template_key]
            subject = template['subject'].format(name=investor_data.get('contact_name', 'Team'))
            body = template['body'].format(
                name=investor_data.get('contact_name', 'Team'),
                portfolio_focus=investor_data.get('recent_investments', 'proptech and real estate')
            )
            
            # Send email
            print(f"  📤 Sending to {investor_data.get('email', 'N/A')}...")
            success = send_email_via_smtp(
                investor_data.get('email', ''),
                subject,
                body
            )
            
            if success:
                sent_count += 1
                track_outreach(
                    investor_data.get('contact_name', ''),
                    investor,
                    investor_data.get('email', ''),
                    category,
                    'sent'
                )
                print(f"  ✅ Sent! Total: {sent_count}/50")
                
                # Rate limiting
                time.sleep(2)
            else:
                track_outreach(
                    investor_data.get('contact_name', ''),
                    investor,
                    investor_data.get('email', ''),
                    category,
                    'failed'
                )
                print(f"  ❌ Failed to send")
    
    print(f"\n🎉 Outreach complete! {sent_count} emails sent.")

if __name__ == "__main__":
    main()