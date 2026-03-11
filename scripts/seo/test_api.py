#!/usr/bin/env python3
import requests
from io import BytesIO

url = "https://settley.fly.dev/articles/create"

# Test data - send as multipart/form-data (required by multer)
data = {
    'title': 'Test Article from Script',
    'content': '<h1>Test Content</h1><p>This is a test.</p>',
    'status': 'draft'
}

print(f"Sending POST to {url}")
print(f"Data: {data}")

# Send with files parameter to trigger multipart/form-data
# Use a dummy file to force multipart encoding
files = {
    'title': (None, data['title']),
    'content': (None, data['content']),
    'status': (None, data['status'])
}

response = requests.post(url, files=files)

print(f"Status: {response.status_code}")
print(f"Headers: {response.headers}")
print(f"Body: {response.text}")
