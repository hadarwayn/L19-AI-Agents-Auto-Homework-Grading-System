"""
Quick Gmail search test to debug email finding
"""
from pathlib import Path
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

SCOPES = [
    'https://www.googleapis.com/auth/gmail.readonly',
    'https://www.googleapis.com/auth/gmail.compose'
]

print("=" * 70)
print("GMAIL SEARCH TEST")
print("=" * 70)

# Gmail Authentication
print("\n[1] Authenticating with Gmail API...")
creds = None
token_path = Path('Secrets/token.json')
credentials_path = Path('Secrets/credentials.json')

if token_path.exists():
    print(f"   - Found token.json")
    creds = Credentials.from_authorized_user_file(str(token_path), SCOPES)
else:
    print(f"   - No token.json found")

if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
        print(f"   - Refreshing expired token...")
        creds.refresh(Request())
    else:
        print(f"   - Need to authenticate...")
        flow = InstalledAppFlow.from_client_secrets_file(str(credentials_path), SCOPES)
        creds = flow.run_local_server(port=0)

    with open(token_path, 'w') as token:
        token.write(creds.to_json())
    print(f"   - Token saved")

print(f"[+] Authentication successful\n")

# Create Gmail service
service = build('gmail', 'v1', credentials=creds)

# Get profile to verify account
profile = service.users().getProfile(userId='me').execute()
print(f"[2] Authenticated as: {profile['emailAddress']}")
print(f"    Total messages in account: {profile['messagesTotal']}\n")

# Test different search queries
test_queries = [
    ('', 'Empty query (get recent 20)'),
    ('subject:GradingL19', 'Search: GradingL19'),
    ('subject:Homework', 'Search: Homework'),
    ('subject:AI', 'Search: AI'),
    ('subject:L17', 'Search: L17'),
]

print("[3] Testing different search queries:")
print("-" * 70)

for query, description in test_queries:
    try:
        results = service.users().messages().list(
            userId='me',
            q=query,
            maxResults=20
        ).execute()

        messages = results.get('messages', [])
        count = len(messages)

        print(f"\n{description}")
        print(f"   Query: '{query}'")
        print(f"   Results: {count} emails")

        if count > 0 and count <= 5:
            print(f"   Subjects:")
            for msg in messages[:3]:
                msg_data = service.users().messages().get(userId='me', id=msg['id'], format='metadata').execute()
                headers = msg_data['payload']['headers']
                subject = next((h['value'] for h in headers if h['name'] == 'Subject'), 'No subject')
                print(f"      - {subject[:80]}")
    except Exception as e:
        print(f"\n{description}")
        print(f"   Query: '{query}'")
        print(f"   ERROR: {e}")

print("\n" + "=" * 70)
print("TEST COMPLETE")
print("=" * 70)
