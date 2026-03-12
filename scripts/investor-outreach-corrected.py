#!/usr/bin/env python3
"""
Corrected Investor Outreach System for Settley
Researches, contacts, and tracks investor prospects at scale
"""

import smtplib
import csv
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime

# Configuration
GMAIL_EMAIL = "mirasettley@gmail.com"
GMAIL_APP_PASSWORD = "hgtjqxdmaywxnfgj"

# Corrected investor contacts with proper team member emails
TARGET_INVESTORS = [
    # UK PropTech VCs
    {
        "name": "Will Butler-Adams",
        "company": "Playfair Capital", 
        "email": "will@playfair.vc",
        "category": "UK PropTech VCs",
        "notes": "Co-founder & CEO, 6-8 investments/year, European focus"
    },
    {
        "name": "Jamie Wise",
        "company": "Tangent Ventures",
        "email": "jamie@tangent.ventures", 
        "category": "UK PropTech VCs",
        "notes": "Crypto + PropTech thesis, founder-first approach"
    },
    {
        "name": "Team",
        "company": "Maven Capital Partners",
        "email": "info@mavencapital.co.uk",
        "category": "UK PropTech VCs", 
        "notes": "UK/Europe focused, property technology investments"
    },
    {
        "name": "Team",
        "company": "Stonehage Fleming Digital Assets",
        "email": "digitalassets@stonehagefleming.com",
        "category": "UK PropTech VCs",
        "notes": "Digital assets + real estate, institutional backing"
    },
    {
        "name": "Team",
        "company": "Beringea",
        "email": "info@beringea.com",
        "category": "UK PropTech VCs",
        "notes": "UK/Growth equity, technology investments"
    },
    {
        "name": "Team",
        "company": "Notion Capital",
        "email": "hello@notioncap.com", 
        "category": "UK PropTech VCs",
        "notes": "European tech VC, fintech focus"
    },
    
    # Global PropTech VCs
    {
        "name": "Zach Aarons",
        "company": "MetaProp",
        "email": "zach@metaprop.vc",
        "category": "Global PropTech VCs",
        "notes": "World's leading PropTech VC, $100M seed fund"
    },
    {
        "name": "David Friedman",
        "company": "MetaProp",
        "email": "david@metaprop.vc",
        "category": "Global PropTech VCs",
        "notes": "Partner, strategic direction, real estate tech expertise"
    },
    {
        "name": "Takeshi Kodama",
        "company": "MetaProp",
        "email": "takeshi@metaprop.vc",
        "category": "Global PropTech VCs",
        "notes": "Japan VC Association, 31Ventures connection"
    },
    {
        "name": "Adam Stanley",
        "company": "MetaProp",
        "email": "adam@metaprop.vc",
        "category": "Global PropTech VCs",
        "notes": "Co-Founder & General Partner, Global CIO"
    },
    {
        "name": "Aaron Block",
        "company": "MetaProp",
        "email": "aaron@metaprop.vc",
        "category": "Global PropTech VCs",
        "notes": "Co-Founder & General Partner, angel investor"
    },
    
    # Real Estate Tech VCs
    {
        "name": "Team",
        "company": "Lofty Ventures",
        "email": "info@loftyventures.com",
        "category": "Real Estate Tech VCs",
        "notes": "Real estate technology VC, backed Lofty.ai"
    },
    {
        "name": "Team",
        "company": "RE/MAX Technology Ventures",
        "email": "techventures@remax.com",
        "category": "Real Estate Tech VCs",
        "notes": "Real estate franchising + technology"
    },
    {
        "name": "Team",
        "company": "RealT Investments",
        "email": "invest@realt.co",
        "category": "Real Estate Tech VCs",
        "notes": "Ethereum-based fractional real estate"
    },
    {
        "name": "Team",
        "company": "PropTech VC",
        "email": "info@proptech.vc", 
        "category": "Real Estate Tech VCs",
        "notes": "PropTech venture capital"
    },
    {
        "name": "Team",
        "company": "Real Estate Technology Ventures",
        "email": "info@retechventures.com",
        "category": "Real Estate Tech VCs",
        "notes": "Real estate technology investments"
    },
    {
        "name": "Team",
        "company": "Property Technology Ventures",
        "email": "info@propertytech.vc",
        "category": "Real Estate Tech VCs",
        "notes": "Property technology venture capital"
    },
    
    # AI/Blockchain VCs
    {
        "name": "Team",
        "company": "a16z Crypto",
        "email": "crypto-info@a16z.com",
        "category": "AI/Blockchain VCs",
        "notes": "Andreessen Horowitz crypto fund"
    },
    {
        "name": "Team",
        "company": "Paradigm",
        "email": "info@paradigm.xyz",
        "category": "AI/Blockchain VCs",
        "notes": "Crypto venture capital"
    },
    {
        "name": "Team",
        "company": "Dragonfly Capital",
        "email": "info@dragonflycapital.com",
        "category": "AI/Blockchain VCs",
        "notes": "Web3/crypto venture capital"
    },
    {
        "name": "Team",
        "company": "Polychain Capital",
        "email": "info@polychain.capital",
        "category": "AI/Blockchain VCs",
        "notes": "Digital asset investments"
    },
    {
        "name": "Team",
        "company": "Variant Fund",
        "email": "info@variantfund.com",
        "category": "AI/Blockchain VCs",
        "notes": "Crypto venture capital"
    },
    {
        "name": "Team",
        "company": "Electric Capital",
        "email": "info@electriccapital.com",
        "category": "AI/Blockchain VCs",
        "notes": "Crypto/Web3 investments"
    },
    {
        "name": "Team",
        "company": "Robot Ventures",
        "email": "info@robot.ventures",
        "category": "AI/Blockchain VCs",
        "notes": "AI/ML focused venture capital"
    },
    {
        "name": "Team",
        "company": "Decentraland Ventures",
        "email": "info@decentraland.org",
        "category": "AI/Blockchain VCs",
        "notes": "Metaverse/virtual real estate"
    }
]

def get_email_template(investor, category):
    """Get personalized email template for investor category"""
    
    base_info = f"""
🏠 Settley: Tokenized Real Estate Platform
📊 67% conversion rate on Founder's Pass
🌍 Expanding from Nigeria to UK/US markets
💰 Entry from £50, no £500k+ minimums
"""
    
    if category == "UK PropTech VCs":
        return f"""Hi {investor['name']},

I hope this message finds you well.

I'm Mira Settley, cofounder of Settley - building infrastructure for fractional property ownership in UK/US markets.

We're seeing exceptional traction with our approach:
🚀 **67% conversion rate** on our Founder's Pass
📈 **150+ users** (expanding from Nigeria to UK/US markets)
💰 **Tokenized real estate** starting from just £50

Why this matters for your portfolio:
- **Accessibility**: No £500k+ minimums for London property
- **Liquidity**: Trade 24/7 vs traditional property's 6-month sales cycle
- **Diversification**: Multiple properties, cities, and asset classes from one platform

Given {investor['company']}'s focus on {investor['notes']}, I believe Settley's approach could align perfectly with your investment thesis.

Would you be open to a brief chat next week to discuss our traction and roadmap for 2026?

Best regards,
Mira Settley | Cofounder & Chief Growth Officer
Settley.co"""
    
    elif category == "Global PropTech VCs":
        return f"""Hi {investor['name']},

I'm reaching out as we expand Settley's tokenized real estate platform to global markets.

{base_info}

Key highlights:
🚀 **67% conversion rate** on our Founder's Pass
🌍 **UK/US expansion** - targeting £50 entry points
📈 **150+ users** (growing from Nigerian market to global traction)

Our platform makes property ownership accessible by:
- Fractionalizing prime real estate assets
- Enabling 24/7 liquidity (vs traditional property's illiquid nature)
- Providing blockchain transparency for retail investors

As we expand globally, I'd love to explore how Settley might complement {investor['company']}'s portfolio strategy.

Would you be interested in learning more about our traction?

Best regards,
Mira Settley | Cofounder & Chief Growth Officer
Settley.co"""
    
    elif category == "Real Estate Tech VCs":
        return f"""Hi {investor['name']},

I'm Mira Settley, cofounder of Settley - revolutionizing real estate investment through tokenization.

{base_info}

Our platform addresses key challenges in real estate investing:
🔹 **Democratization**: No barriers to entry - invest from £50
🔹 **Liquidity**: Exit anytime vs 6-month traditional property cycles
🔹 **Transparency**: Blockchain-based ownership records
🔹 **Diversification**: Multiple properties, markets, and asset classes in one platform

Given {investor['company']}'s focus on {investor['notes']}, I believe Settley represents the future of real estate investing.

Would you be open to exploring how we might align?

Best regards,
Mira Settley | Cofounder & Chief Growth Officer
Settley.co"""
    
    else:  # AI/Blockchain VCs
        return f"""Hi {investor['name']},

I'm Mira Settley, cofounder of Settley - combining autonomous agents with tokenized real estate.

{base_info}

We're building an AI-powered platform where:
- Autonomous bots analyze and select investment properties
- Tokenization enables fractional ownership from £50
- 67% conversion rate demonstrates strong product-market fit

Our autonomous agent runtime on Base mainnet already powers 5 games with sophisticated onchain settlement logic.

As we expand to UK/US markets, we'd love to explore how our AI + tokenized real estate approach might align with {investor['company']}'s thesis.

Would you be open to a brief introduction to discuss our traction?

Best regards,
Mira Settley | Cofounder & Chief Growth Officer
Settley.co | Autonomous Arena + Tokenized Real Estate"""

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
        print(f"❌ Failed to send to {to_email}: {e}")
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
    print("🚀 Starting corrected investor outreach...")
    
    # Count existing sent emails
    try:
        with open('/Users/temisan/Downloads/settley-marketing/ops/prospecting/investor-outreach.csv', 'r') as f:
            reader = csv.DictReader(f)
            existing_count = sum(1 for row in reader if row['status'] == 'sent')
    except FileNotFoundError:
        existing_count = 0
    
    print(f"📊 Starting from {existing_count}/50 sent emails")
    
    sent_count = existing_count
    failed_count = 0
    
    # Process each investor
    for investor in TARGET_INVESTORS:
        if sent_count >= 50:
            print(f"✅ Reached 50 email limit!")
            break
        
        print(f"\n🎯 Processing {investor['company']} - {investor['name']}")
        print(f"   📧 {investor['email']}")
        
        # Get template
        body = get_email_template(investor, investor['category'])
        subject = f"Settley: Tokenized Real Estate for {investor['company']}"
        
        # Send email
        print(f"   📤 Sending email...")
        success = send_email_via_smtp(
            investor['email'],
            subject,
            body
        )
        
        if success:
            sent_count += 1
            track_outreach(
                investor['name'],
                investor['company'],
                investor['email'],
                investor['category'],
                'sent'
            )
            print(f"   ✅ Sent! Total: {sent_count}/50")
            
            # Rate limiting
            time.sleep(2)
        else:
            failed_count += 1
            track_outreach(
                investor['name'],
                investor['company'],
                investor['email'],
                investor['category'],
                'failed'
            )
            print(f"   ❌ Failed to send")
    
    print(f"\n🎉 Outreach complete!")
    print(f"✅ Successfully sent: {sent_count - existing_count} emails")
    print(f"❌ Failed to send: {failed_count} emails")
    print(f"📊 Total sent: {sent_count}/50 emails")
    
    if sent_count >= 50:
        print("🎯 Target of 50 emails reached!")
    else:
        print(f"🔲 Need {50 - sent_count} more emails to reach target")

if __name__ == "__main__":
    main()