"""
Test different Gmail queries to find all 8 homework emails
"""
from pathlib import Path
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from google.auth.transport.requests import Request

SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

creds = Credentials.from_authorized_user_file('Secrets/token.json', SCOPES)
if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())

service = build('gmail', 'v1', credentials=creds)

# Test different queries
queries = [
    'subject:AI Development Expert',
    'subject:AI Development Expert course',
    'subject:Homework',
    'subject:GradingL19',
    'subject:(Homework L11 OR L12 OR L13)',
]

for query in queries:
    print(f"\nQuery: {query}")
    print("="*70)

    results = service.users().messages().list(
        userId='me',
        q=query,
        maxResults=50
    ).execute()

    messages = results.get('messages', [])
    print(f"Found: {len(messages)} emails")

    if messages:
        # Count how many match "AI Development Expert course - Homework - L"
        matching = 0
        print("\nMatching homework emails (L11-L18):")
        for msg in messages[:50]:
            full_msg = service.users().messages().get(userId='me', id=msg['id'], format='full').execute()
            headers = full_msg['payload']['headers']
            subject = next((h['value'] for h in headers if h['name'] == 'Subject'), '(no subject)')

            if 'AI Development Expert course - Homework - L' in subject:
                matching += 1
                # Extract lesson number
                if '- L' in subject:
                    lesson = subject.split('- L')[1].split('-')[0].strip()
                    print(f"  L{lesson}")

        print(f"\nTotal matching: {matching}/8")
