"""
Gmail Authentication Helper

Provides shared Gmail API authentication for agents.

Author: Hadar Wayn
Date: December 2025
"""

from pathlib import Path
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request


# Gmail API scopes
GMAIL_SCOPES = [
    'https://www.googleapis.com/auth/gmail.readonly',
    'https://www.googleapis.com/auth/gmail.compose'
]


def get_gmail_service(console=None):
    """
    Authenticate and return Gmail API service

    Args:
        console: Optional Rich console for logging

    Returns:
        Gmail API service object

    Raises:
        FileNotFoundError: If credentials.json not found
        Exception: If authentication fails
    """
    if console:
        console.print("[*] Authenticating with Gmail API...")

    # Paths
    token_path = Path('Secrets/token.json')
    credentials_path = Path('Secrets/credentials.json')

    if not credentials_path.exists():
        raise FileNotFoundError(
            f"Gmail credentials not found at {credentials_path}\n"
            "Please download credentials.json from Google Cloud Console"
        )

    # Load existing credentials
    creds = None
    if token_path.exists():
        creds = Credentials.from_authorized_user_file(str(token_path), GMAIL_SCOPES)

    # Refresh or create new credentials
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                str(credentials_path),
                GMAIL_SCOPES
            )
            creds = flow.run_local_server(port=0)

        # Save credentials
        token_path.parent.mkdir(parents=True, exist_ok=True)
        with open(token_path, 'w') as token:
            token.write(creds.to_json())

    if console:
        console.print("[+] Authentication successful\n")

    # Build and return service
    return build('gmail', 'v1', credentials=creds)
