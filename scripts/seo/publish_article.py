#!/usr/bin/env python3
"""
Settley Article Publisher

Publishes educational articles to settley.fly.dev/articles/create

Usage:
    python scripts/seo/publish_article.py --title "Article Title" --content "article.md" --status "published"
    python scripts/seo/publish_article.py --title "Article Title" --content "article.md" --status "draft"
"""

import requests
import argparse
import markdown
import os
from pathlib import Path

# API Configuration
BASE_URL = "https://settley.fly.dev"
CREATE_ENDPOINT = f"{BASE_URL}/articles/create"

# Authentication (if needed - add to .env)
# API_TOKEN = os.environ.get("SETTLEY_API_TOKEN", "")

def markdown_to_html(md_content: str) -> str:
    """Convert markdown to HTML with extensions for tables, code blocks, etc."""
    html = markdown.markdown(
        md_content,
        extensions=[
            'tables',
            'fenced_code',
            'codehilite',
            'toc',
            'nl2br'
        ]
    )
    return html

def read_file(filepath: str) -> str:
    """Read content from file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()

def publish_article(title: str, content: str, status: str = "draft", cover_image_path: str = None) -> dict:
    """
    Publish article to Settley API.
    
    Args:
        title: Article title
        content: Article content (markdown or HTML)
        status: "draft" or "published"
        cover_image_path: Optional path to cover image
    
    Returns:
        API response dict
    """
    # Convert markdown to HTML if content looks like markdown
    if content.strip().startswith('#') or '**' in content:
        content = markdown_to_html(content)
    
    # Prepare multipart/form-data (required by multer)
    # Use tuples (None, value) to send fields as multipart without files
    fields = {
        'title': (None, title),
        'content': (None, content),
        'status': (None, status)
    }
    
    # Add cover image if provided
    if cover_image_path and os.path.exists(cover_image_path):
        fields['cover'] = (
            os.path.basename(cover_image_path),
            open(cover_image_path, 'rb'),
            'image/jpeg'
        )
    
    files = fields
    
    # Make request
    print(f"📝 Publishing article: {title}")
    print(f"📊 Status: {status}")
    print(f"🔗 Endpoint: {CREATE_ENDPOINT}")
    
    try:
        # Don't set Content-Type header - requests will set it automatically for multipart
        response = requests.post(
            CREATE_ENDPOINT,
            files=files if files else None
        )
        print(f"📡 Response status: {response.status_code}")
        
        # Close file handle
        if files and 'cover' in files:
            files['cover'][1].close()
        
        response.raise_for_status()
        
        result = response.json()
        
        if result.get('status') == 200:
            article_id = result.get('data', {}).get('_id', 'unknown')
            print(f"✅ Article published successfully!")
            print(f"📄 ID: {article_id}")
            print(f"🔗 URL: {BASE_URL}/articles/{article_id}")
        else:
            print(f"⚠️ Unexpected response: {result}")
        
        return result
        
    except requests.exceptions.RequestException as e:
        print(f"❌ Error publishing article: {e}")
        if hasattr(e, 'response') and e.response is not None:
            print(f"Response: {e.response.text}")
        return {'error': str(e)}

def main():
    parser = argparse.ArgumentParser(description='Publish articles to Settley')
    parser.add_argument('--title', required=True, help='Article title')
    parser.add_argument('--content', required=True, help='Path to markdown file or HTML content')
    parser.add_argument('--status', choices=['draft', 'published'], default='draft', help='Article status')
    parser.add_argument('--cover', help='Path to cover image (optional)')
    
    args = parser.parse_args()
    
    # Check if content is a file path or direct content
    if os.path.exists(args.content):
        content = read_file(args.content)
    else:
        content = args.content
    
    # Publish
    result = publish_article(
        title=args.title,
        content=content,
        status=args.status,
        cover_image_path=args.cover
    )
    
    # Exit with appropriate code
    if 'error' in result:
        exit(1)
    else:
        exit(0)

if __name__ == '__main__':
    main()
