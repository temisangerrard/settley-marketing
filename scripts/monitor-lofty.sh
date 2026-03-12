#!/bin/bash
# Lofty.ai Competitor Monitor
# Uses PinchTab to track property listings, returns, and content updates

OUTPUT_DIR="ops/competitor-tracking/lofty"
mkdir -p "$OUTPUT_DIR"

TIMESTAMP=$(date +%Y%m%d_%H%M)
OUTPUT_FILE="$OUTPUT_DIR/scan-$TIMESTAMP.md"

echo "# Lofty.ai Competitor Scan" > "$OUTPUT_FILE"
echo "**Date:** $(date '+%Y-%m-%d %H:%M')" >> "$OUTPUT_FILE"
echo "**Source:** https://www.lofty.ai" >> "$OUTPUT_FILE"
echo "" >> "$OUTPUT_FILE"

# Navigate to Lofty
echo "🔄 Navigating to Lofty.ai..."
pinchtab nav https://www.lofty.ai > /dev/null 2>&1
sleep 2

# Get interactive elements
echo "📊 Extracting property listings..."
echo "## Current Property Listings" >> "$OUTPUT_FILE"
echo "" >> "$OUTPUT_FILE"

# Extract property links with returns
pinchtab snap -i -c 2>&1 | grep -E "^[e0-9]+:link.*%" | while read line; do
    echo "- $line" >> "$OUTPUT_FILE"
done

echo "" >> "$OUTPUT_FILE"
echo "## Page Structure" >> "$OUTPUT_FILE"
echo "" >> "$OUTPUT_FILE"

# Get element count
ELEMENT_COUNT=$(pinchtab snap -i -c 2>&1 | grep "nodes" | head -1)
echo "$ELEMENT_COUNT" >> "$OUTPUT_FILE"

echo "" >> "$OUTPUT_FILE"
echo "## Notes" >> "$OUTPUT_FILE"
echo "- Scan completed at $(date '+%H:%M GMT')" >> "$OUTPUT_FILE"
echo "- Use: pinchtabs text for full page content" >> "$OUTPUT_FILE"

echo "✅ Scan complete: $OUTPUT_FILE"
echo "📊 Summary:"
echo "   - Properties found: $(pinchtab snap -i -c 2>&1 | grep -c 'link.*%' || echo 0)"
echo "   - Total elements: $(echo $ELEMENT_COUNT | grep -oE '[0-9]+' | head -1 || echo 'unknown')"
