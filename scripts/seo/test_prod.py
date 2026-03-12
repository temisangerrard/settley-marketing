#!/usr/bin/env python3
"""Test production endpoint"""
import requests

url = "https://settley.co/articles/create"

fields = {
    'title': (None, 'Test Production'),
    'content': (None, '<h1>Test</h1>'),
    'status': (None, 'draft')
}

response = requests.post(url, files=fields)

print(f"Status: {response.status_code}")
print(f"Content-Type: {response.headers.get('Content-Type')}")
print(f"Body (first 500 chars): {response.text[:500]}")
