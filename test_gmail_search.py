"""
Test Gmail search with different queries
"""
from pathlib import Path
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build

SCOPES = [
    'https://www.googleapis.com/auth/gmail.readonly',
    'https://www.googleapis.com/auth/gmail.compose'
]

print("Authenticating...")
creds = None
token_path = Path('Secrets/token.json')
credentials_path = Path('Secrets/credentials.json')

if token_path.exists():
    creds = Credentials.from_authorized_user_file(str(token_path), SCOPES)

if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file(str(credentials_path), SCOPES)
        creds = flow.run_local_server(port=0)

    with open(token_path, 'w') as token:
        token.write(creds.to_json())

service = build('gmail', 'v1', credentials=creds)

# Test different queries
queries = [
    ('', 'All emails (no filter)'),
    ('subject:"AI"', 'Subject contains "AI"'),
    ('subject:"Homework"', 'Subject contains "Homework"'),
    ('subject:"AI Development Expert course - Homework - L"', 'Full phrase'),
    ('subject:AI Development', 'Without quotes'),
]

print("\nTesting Gmail searches:")
print("="*70)

for query, description in queries:
    try:
        results = service.users().messages().list(
            userId='me',
            q=query,
            maxResults=5
        ).execute()

        messages = results.get('messages', [])
        count = len(messages)

        print(f"\n{description}")
        print(f"Query: {query if query else '(empty)'}")
        print(f"Found: {count} emails")

        if count > 0:
            print("First email subjects:")
            for msg in messages[:3]:
                full_msg = service.users().messages().get(userId='me', id=msg['id'], format='full').execute()
                headers = full_msg['payload']['headers']
                subject = next((h['value'] for h in headers if h['name'] == 'Subject'), '(no subject)')
                print(f"  - {subject}")

    except Exception as e:
        print(f"Error: {e}")

print("\n" + "="*70)
