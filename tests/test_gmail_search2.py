"""
Test Gmail search for specific terms
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

# Test queries based on the screenshot
queries = [
    'subject:L17',
    'subject:GradingL19',
    'subject:"AI Development Expert course"',
    'subject:{AI Development Expert course}',
    'subject:Homework L17',
    'AI Development Expert course',
]

print("Testing Gmail searches for specific terms:")
print("="*70)

for query in queries:
    try:
        results = service.users().messages().list(
            userId='me',
            q=query,
            maxResults=10
        ).execute()

        messages = results.get('messages', [])
        print(f"\nQuery: {query}")
        print(f"Found: {len(messages)} emails")

        if messages:
            # Get first few subjects
            for i, msg in enumerate(messages[:5], 1):
                try:
                    full_msg = service.users().messages().get(userId='me', id=msg['id'], format='full').execute()
                    headers = full_msg['payload']['headers']
                    subject = next((h['value'] for h in headers if h['name'] == 'Subject'), '(no subject)')
                    # Print first 100 chars to avoid encoding issues
                    subject_preview = subject[:100] if subject else '(no subject)'
                    print(f"  {i}. {subject_preview}")
                except UnicodeEncodeError:
                    print(f"  {i}. [encoding error]")

    except Exception as e:
        print(f"  Error: {e}")

print("\n" + "="*70)
