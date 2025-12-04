"""
Search more broadly to find actual homework emails
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

# Try different queries
queries = [
    'subject:Homework',
    'subject:L17',
    'subject:"AI Development"',
    'from:hadar.wayn@gmail.com',
]

for query in queries:
    print(f"\nQuery: {query}")
    print("-"*70)

    results = service.users().messages().list(
        userId='me',
        q=query,
        maxResults=5
    ).execute()

    messages = results.get('messages', [])
    print(f"Found: {len(messages)} emails")

    if messages:
        for i, msg in enumerate(messages[:3], 1):
            full_msg = service.users().messages().get(userId='me', id=msg['id'], format='full').execute()
            headers = full_msg['payload']['headers']
            subject = next((h['value'] for h in headers if h['name'] == 'Subject'), '(no subject)')
            print(f"  {i}. {subject[:100]}")
    print()
