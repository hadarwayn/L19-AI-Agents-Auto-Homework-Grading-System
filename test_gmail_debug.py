"""
Debug: See what email subjects Gmail is actually returning
"""
from pathlib import Path
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from google.auth.transport.requests import Request

SCOPES = ['https://www.googleapis.com/auth/gmail.readonly', 'https://www.googleapis.com/auth/gmail.compose']

creds = Credentials.from_authorized_user_file('Secrets/token.json', SCOPES)
if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())

service = build('gmail', 'v1', credentials=creds)

# Test the exact query that's failing
query = 'subject:"AI Development Expert course"'
print(f"Gmail Query: {query}")
print("="*70 + "\n")

results = service.users().messages().list(
    userId='me',
    q=query,
    maxResults=10
).execute()

messages = results.get('messages', [])
print(f"Found {len(messages)} emails\n")

if messages:
    print("Email subjects returned by Gmail:")
    print("-"*70)
    for i, msg in enumerate(messages[:10], 1):
        full_msg = service.users().messages().get(userId='me', id=msg['id'], format='full').execute()
        headers = full_msg['payload']['headers']
        subject = next((h['value'] for h in headers if h['name'] == 'Subject'), '(no subject)')

        # Check if our search term is in the subject
        search_term = "AI Development Expert course"
        contains = search_term.lower() in subject.lower()

        print(f"\n{i}. Subject: {subject}")
        print(f"   Contains '{search_term}': {contains}")

        # Show character-by-character comparison for first few
        if i <= 2 and len(subject) < 200:
            print(f"   First 80 chars: '{subject[:80]}'")
