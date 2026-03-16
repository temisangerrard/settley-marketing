#!/bin/bash

# Settley Article Publisher
# Deletes broken articles and republishes with body-only format

API_BASE="https://settley.fly.dev/articles"

# Article IDs to delete (full HTML format - broken)
ARTICLES_TO_DELETE=(
  "69b324239b0dd5e8aac560f4"  # Complete Guide to Tokenized Real Estate UK
  "69b3cee4d79383944b72f316"  # FCA Cryptoasset Rules 2026
  "69b3d3f73129ce2d3d138291"  # How to Invest in Property with £500
  "69b3f912f37d8ada2c68f005"  # Tokenized Real Estate vs REITs
  "69b3fc8999e82c9d864609fb"  # Fractional Property Investment UK
  "69b438cec1713c1335795eba"  # How Tokenization Actually Works
)

echo "=== Settley Article Republisher ==="
echo ""

# Step 1: Delete broken articles
echo "Step 1: Deleting broken articles..."
for id in "${ARTICLES_TO_DELETE[@]}"; do
  echo "  Deleting $id..."
  curl -s -X DELETE "$API_BASE/delete/$id" | jq -r '.message // .error // "Unknown response"'
done

echo ""
echo "Step 2: Ready to republish with body-only format"
echo "Run the publish script to upload corrected articles"
