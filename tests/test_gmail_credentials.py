"""
Test Gmail API Credentials
Verifies that the credentials.json file works correctly
"""

import os
import sys
from pathlib import Path

# Set UTF-8 encoding for Windows console
if sys.platform == 'win32':
    import codecs
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')
    sys.stderr = codecs.getwriter('utf-8')(sys.stderr.buffer, 'strict')

try:
    from google.oauth2.credentials import Credentials
    from google_auth_oauthlib.flow import InstalledAppFlow
    from google.auth.transport.requests import Request
    from googleapiclient.discovery import build
except ImportError:
    print("ERROR: Required packages not installed")
    print("Please run: pip install google-api-python-client google-auth-oauthlib")
    sys.exit(1)

# Gmail API scopes
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

def test_gmail_credentials():
    """Test Gmail API credentials"""

    print("🔍 Testing Gmail API Credentials...\n")

    # Check if credentials.json exists
    credentials_path = Path("Secrets/credentials.json")
    if not credentials_path.exists():
        print(f"❌ Credentials file not found: {credentials_path}")
        return False

    print(f"✓ Found credentials file: {credentials_path}")

    # Check for existing token
    token_path = Path("Secrets/token.json")
    creds = None

    if token_path.exists():
        print(f"✓ Found existing token: {token_path}")
        try:
            creds = Credentials.from_authorized_user_file(str(token_path), SCOPES)
        except Exception as e:
            print(f"⚠ Warning: Could not load existing token: {e}")
            creds = None

    # If no valid credentials, authenticate
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            print("🔄 Refreshing expired token...")
            try:
                creds.refresh(Request())
                print("✓ Token refreshed successfully")
            except Exception as e:
                print(f"❌ Failed to refresh token: {e}")
                creds = None

        if not creds:
            print("\n🔐 Starting OAuth 2.0 authentication flow...")
            print("   A browser window will open for you to authorize the application.")
            print("   Please log in with your Gmail account and grant permissions.\n")

            try:
                flow = InstalledAppFlow.from_client_secrets_file(
                    str(credentials_path), SCOPES
                )
                creds = flow.run_local_server(port=0)
                print("✓ Authentication successful!")

                # Save the token for future use
                with open(token_path, 'w') as token:
                    token.write(creds.to_json())
                print(f"✓ Token saved to: {token_path}")

            except Exception as e:
                print(f"❌ Authentication failed: {e}")
                return False
    else:
        print("✓ Using existing valid credentials")

    # Test the connection by listing some emails
    print("\n📧 Testing Gmail API connection...")
    try:
        service = build('gmail', 'v1', credentials=creds)

        # Get user profile
        profile = service.users().getProfile(userId='me').execute()
        email_address = profile.get('emailAddress')
        total_messages = profile.get('messagesTotal', 0)

        print(f"✓ Connected to Gmail API successfully!")
        print(f"   Email: {email_address}")
        print(f"   Total messages: {total_messages}")

        # Try to list a few recent messages
        print("\n📬 Fetching recent messages...")
        results = service.users().messages().list(
            userId='me',
            maxResults=5
        ).execute()

        messages = results.get('messages', [])
        print(f"✓ Successfully retrieved {len(messages)} recent messages")

        if messages:
            print("\n   Recent message IDs:")
            for msg in messages[:3]:
                print(f"   - {msg['id']}")

        print("\n✅ Gmail API credentials verified successfully!")
        print("   The credentials are working correctly.\n")
        return True

    except Exception as e:
        print(f"❌ Failed to connect to Gmail API: {e}")
        return False

if __name__ == "__main__":
    success = test_gmail_credentials()
    sys.exit(0 if success else 1)
