"""
Check what homework emails are actually available in Gmail
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

# Search for all homework emails
query = 'subject:Homework'
print(f"Gmail Query: {query}")
print("="*70 + "\n")

results = service.users().messages().list(
    userId='me',
    q=query,
    maxResults=50
).execute()

messages = results.get('messages', [])
print(f"Found {len(messages)} emails with 'Homework' in subject\n")

if messages:
    print("Homework email subjects:")
    print("-"*70)
    for i, msg in enumerate(messages, 1):
        full_msg = service.users().messages().get(userId='me', id=msg['id'], format='full').execute()
        headers = full_msg['payload']['headers']
        subject = next((h['value'] for h in headers if h['name'] == 'Subject'), '(no subject)')

        # Check if it matches the pattern
        contains_L = 'Homework - L' in subject
        marker = ' <-- MATCHES' if contains_L else ''

        print(f"{i}. {subject}{marker}")

print("\n" + "="*70)
print("Looking for emails matching: 'AI Development Expert course - Homework - L'")
