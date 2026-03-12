#!/usr/bin/env python3
"""
Twitter Thread Poster using Typefully API
Posts the tokenized real estate beginner's guide thread
"""

import requests
import json
import os
from datetime import datetime, timedelta

# Typefully API Configuration
API_KEY = os.getenv('TYPEFULLY_API_KEY')  # From .env: rDlkwYBDVqNkdxRBYTMi6VGZeSMlGzsi
BASE_URL = "https://api.typefully.com/v1"

def post_twitter_thread():
    """Post the tokenized real estate thread to Twitter"""
    
    # Load the thread data
    with open('/Users/temisan/Downloads/settley-marketing/ops/social/twitter-thread-1.json', 'r') as f:
        thread_data = json.load(f)
    
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    
    print("🚀 Starting Twitter thread posting...")
    print("📝 Account: @mirasettley (Mira Settley)")
    
    # Post each tweet in the thread
    for tweet in thread_data['tweets']:
        tweet_data = {
            "text": tweet['text'],
            "thread": True,
            "thread_position": tweet['thread_position'],
            "schedule": tweet['scheduled_at'] if 'scheduled_at' in tweet else None
        }
        
        print(f"📝 Posting tweet {tweet['thread_position']}/5...")
        
        try:
            response = requests.post(
                f"{BASE_URL}/tweets",
                headers=headers,
                json=tweet_data
            )
            
            if response.status_code == 200:
                result = response.json()
                print(f"✅ Tweet {tweet['thread_position']} posted successfully!")
                print(f"   Tweet ID: {result.get('id', 'N/A')}")
                print(f"   Scheduled for: {tweet.get('scheduled_at', 'Immediately')}")
            else:
                print(f"❌ Error posting tweet {tweet['thread_position']}: {response.status_code}")
                print(f"   Response: {response.text}")
                
        except Exception as e:
            print(f"❌ Exception posting tweet {tweet['thread_position']}: {e}")
    
    print("\n🎉 Twitter thread posting complete!")
    print("📊 Thread summary:")
    print(f"   - 5 tweets in thread")
    print(f"   - Hashtags: {', '.join(thread_data['hashtags'][:5])}...")
    print(f"   - Engagement: {thread_data['engagement_strategy']['response_time']} response time")
    
    # Schedule additional engagement tweets
    schedule_engagement_tweets()

def schedule_engagement_tweets():
    """Schedule engagement tweets to boost thread visibility"""
    
    engagement_tweets = [
        {
            "text": "\"Tokenized real estate isn't just a technological curiosity—it's a fundamental shift in how we access and invest in property.\"\n\nThis is why I'm building Settley. We're making property markets accessible to everyone, not just the wealthy.\n\n#TokenizedRealEstate #PropertyTech",
            "schedule": (datetime.now() + timedelta(hours=2)).isoformat()
        },
        {
            "text": "Did you know? Traditional real estate has a 5-6 month average sales cycle.\n\nTokenized properties can often be traded 24/7 on secondary markets, giving investors unprecedented liquidity.\n\n#RealEstateFacts #Innovation",
            "schedule": (datetime.now() + timedelta(hours=4)).isoformat()
        },
        {
            "text": "Question for the community:\n\nWhat's the biggest barrier that's prevented you from investing in property?\n\nCost? Location? Complexity? Time?\n\nLet me know in the replies! 👇\n\n#RealEstateCommunity #PropertyInvestment",
            "schedule": (datetime.now() + timedelta(hours=6)).isoformat()
        }
    ]
    
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    
    print("\n💫 Scheduling engagement tweets...")
    
    for i, tweet in enumerate(engagement_tweets):
        try:
            response = requests.post(
                f"{BASE_URL}/tweets",
                headers=headers,
                json={"text": tweet["text"], "schedule": tweet["schedule"]}
            )
            
            if response.status_code == 200:
                print(f"✅ Engagement tweet {i+1} scheduled!")
            else:
                print(f"❌ Error scheduling engagement tweet {i+1}: {response.status_code}")
                
        except Exception as e:
            print(f"❌ Exception scheduling engagement tweet {i+1}: {e}")

if __name__ == "__main__":
    post_twitter_thread()