#!/usr/bin/env python3
"""
Settley Article Updater

Updates existing articles on settley.fly.dev/articles/update/:id

Usage:
    python scripts/seo/update_article.py --id <article_id> --title "New Title" --content "article.md" --status "published"
"""

import requests
import argparse
import markdown
import os
from pathlib import Path

# API Configuration
BASE_URL = "https://settley.fly.dev"
UPDATE_ENDPOINT = f"{BASE_URL}/articles/update/"

def markdown_to_html(md_content: str) -> str:
    """Convert markdown to HTML with extensions."""
    html = markdown.markdown(
        md_content,
        extensions=['tables', 'fenced_code', 'codehilite', 'toc', 'nl2br']
    )
    return html

def read_file(filepath: str) -> str:
    """Read content from file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()

def update_article(article_id: str, title: str, content: str, status: str = "draft") -> dict:
    """
    Update article on Settley API.
    
    Args:
        article_id: Article ID to update
        title: New article title
        content: New article content (markdown or HTML)
        status: "draft" or "published"
    
    Returns:
        API response dict
    """
    # Convert markdown to HTML if content looks like markdown
    if content.strip().startswith('#') or '**' in content:
        content = markdown_to_html(content)
    
    # Prepare multipart/form-data
    fields = {
        'title': (None, title),
        'content': (None, content),
        'status': (None, status)
    }
    
    files = fields
    
    url = f"{UPDATE_ENDPOINT}{article_id}"
    
    print(f"📝 Updating article: {article_id}")
    print(f"📝 Title: {title}")
    print(f"📊 Status: {status}")
    print(f"🔗 Endpoint: {url}")
    
    try:
        response = requests.put(url, files=files)
        print(f"📡 Response status: {response.status_code}")
        
        response.raise_for_status()
        result = response.json()
        
        if result.get('status') == 200:
            print(f"✅ Article updated successfully!")
            print(f"🔗 URL: {BASE_URL}/articles/{article_id}")
        else:
            print(f"⚠️ Unexpected response: {result}")
        
        return result
        
    except requests.exceptions.RequestException as e:
        print(f"❌ Error updating article: {e}")
        if hasattr(e, 'response') and e.response is not None:
            print(f"Response: {e.response.text}")
        return {'error': str(e)}

def main():
    parser = argparse.ArgumentParser(description='Update articles on Settley')
    parser.add_argument('--id', required=True, help='Article ID to update')
    parser.add_argument('--title', required=True, help='New article title')
    parser.add_argument('--content', required=True, help='Path to markdown file or HTML content')
    parser.add_argument('--status', choices=['draft', 'published'], default='draft', help='Article status')
    
    args = parser.parse_args()
    
    # Check if content is a file path or direct content
    if os.path.exists(args.content):
        content = read_file(args.content)
    else:
        content = args.content
    
    # Update
    result = update_article(
        article_id=args.id,
        title=args.title,
        content=content,
        status=args.status
    )
    
    # Exit with appropriate code
    if 'error' in result:
        exit(1)
    else:
        exit(0)

if __name__ == '__main__':
    main()
