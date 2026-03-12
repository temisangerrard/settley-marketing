#!/bin/bash
# Settley Twitter Posting Script
# Uses xurl for authenticated posting (OAuth1 already configured)

set -e

# Check xurl auth first
echo "🔐 Checking X auth..."
WHOAMI=$(xurl whoami 2>&1)
if echo "$WHOAMI" | grep -q "mirasettley"; then
    echo "✅ Authenticated as @mirasettley"
else
    echo "❌ Auth failed. Run: ./scripts/xurl_preflight.sh"
    exit 1
fi

# Post function
post_tweet() {
    local TWEET_TEXT="$1"
    
    if [ -z "$TWEET_TEXT" ]; then
        echo "❌ Usage: ./scripts/twitter-post.sh \"Your tweet text here\""
        exit 1
    fi
    
    echo "📝 Posting tweet..."
    RESULT=$(xurl post "$TWEET_TEXT")
    
    # Extract tweet ID from JSON
    TWEET_ID=$(echo "$RESULT" | grep -o '"id":"[^"]*"' | head -1 | cut -d'"' -f4)
    
    if [ -n "$TWEET_ID" ]; then
        echo "✅ Tweet posted successfully!"
        echo "🔗 URL: https://x.com/mirasettley/status/$TWEET_ID"
        echo "$TWEET_ID" > /tmp/last_tweet_id.txt
    else
        echo "❌ Failed to post. Raw output:"
        echo "$RESULT"
        exit 1
    fi
}

# Show usage if no args
if [ $# -eq 0 ]; then
    echo "🐦 Settley Twitter Poster"
    echo ""
    echo "Usage: $0 \"Your tweet text here\""
    echo ""
    echo "Examples:"
    echo "  $0 \"Just shipped Arena Play v1.0!\""
    echo "  $0 \"We're building tokenized real estate on Celo 🚀\""
    echo ""
    echo "Recent activity:"
    if [ -f /tmp/last_tweet_id.txt ]; then
        echo "  Last tweet: https://x.com/mirasettley/status/$(cat /tmp/last_tweet_id.txt)"
    fi
    exit 0
fi

# Post the tweet
post_tweet "$1"
