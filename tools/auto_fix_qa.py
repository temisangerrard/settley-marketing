#!/usr/bin/env python3
"""
Auto-fix critical QA issues in articles:
- Add missing disclaimer
- Add missing CTA
"""

import os
import sys
from pathlib import Path

DISCLAIMER_HTML = """
<div class="disclaimer">
<div class="disclaimer-title">Disclaimer</div>
<p>This article is for educational purposes only. It is not financial, legal, or tax advice.</p>
<p>Investing involves risk. You may lose some or all of your capital.</p>
<p><strong>Capital at risk. Never invest money you cannot afford to lose.</strong></p>
</div>
"""

CTA_HTML = """
<div class="article-cta">
<div class="cta-text">
<h3>Want to learn more?</h3>
<p>Join the Settley waitlist for practical UK market explainers and launch updates.</p>
</div>
<a href="/signup" class="btn-cta">Join the waitlist →</a>
</div>
"""

def needs_disclaimer(content: str) -> bool:
    """Check if article is missing disclaimer."""
    markers = ['<div class="disclaimer">', 'disclaimer-title', 'This is not financial advice', 'Capital at risk']
    return not any(m.lower() in content.lower() for m in markers)

def needs_cta(content: str) -> bool:
    """Check if article is missing CTA."""
    markers = ['<div class="article-cta">', 'btn-cta', 'Join the waitlist', 'Get started']
    return not any(m.lower() in content.lower() for m in markers)

def fix_article(filepath: str) -> dict:
    """Fix missing disclaimer and CTA in an article."""
    with open(filepath, 'r') as f:
        content = f.read()
    
    fixes = []
    new_content = content
    
    # Add disclaimer if missing (before final closing)
    if needs_disclaimer(content):
        # Insert before the last occurrence of "---" or at end
        if '---' in new_content:
            parts = new_content.rsplit('---', 1)
            new_content = parts[0] + DISCLAIMER_HTML + '\n---' + parts[1]
        else:
            new_content = new_content.rstrip() + '\n' + DISCLAIMER_HTML
        fixes.append('added disclaimer')
    
    # Add CTA if missing (at very end, after disclaimer)
    if needs_cta(content):
        new_content = new_content.rstrip() + '\n' + CTA_HTML
        fixes.append('added CTA')
    
    if fixes:
        with open(filepath, 'w') as f:
            f.write(new_content)
    
    return {'file': filepath, 'fixes': fixes}

def main():
    if len(sys.argv) < 2:
        print("Usage: python auto_fix_qa.py <file1> [file2] ...")
        sys.exit(1)
    
    results = []
    for filepath in sys.argv[1:]:
        if not os.path.exists(filepath):
            print(f"⚠️  File not found: {filepath}")
            continue
        
        result = fix_article(filepath)
        results.append(result)
        
        if result['fixes']:
            print(f"✅ Fixed {os.path.basename(filepath)}: {', '.join(result['fixes'])}")
        else:
            print(f"⏭️  Skipped {os.path.basename(filepath)}: no fixes needed")
    
    total_fixes = sum(len(r['fixes']) for r in results)
    print(f"\n{'='*60}")
    print(f"Total fixes applied: {total_fixes}")

if __name__ == "__main__":
    main()
