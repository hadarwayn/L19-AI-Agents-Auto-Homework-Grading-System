"""
Agent 1: Email Extractor - Runtime Execution
Extracts GitHub URLs from Gmail based on search parameters
"""

from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import openpyxl
import re
import hashlib
from datetime import datetime
from pathlib import Path
from email.utils import parsedate_to_datetime
import base64

# Gmail API scopes
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

# User parameters (provided by user)
email_subject = "AI Development Expert course - Homework - L"
sender_email = None
max_emails = 10

print("="*70)
print("         AGENT 1: EMAIL EXTRACTION PARAMETERS")
print("="*70)
print(f"Email Subject: \"{email_subject}\"")
print(f"Sender Email: (all senders)")
print(f"Max Emails: {max_emails}")
print("="*70 + "\n")

# Step 2: Gmail Authentication
print("[*] Authenticating with Gmail API...")
creds = None
token_path = Path('Secrets/token.json')
credentials_path = Path('Secrets/credentials.json')

# Check for existing token
if token_path.exists():
    creds = Credentials.from_authorized_user_file(str(token_path), SCOPES)

# If no valid credentials, authenticate
if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
        print("   Refreshing expired token...")
        creds.refresh(Request())
    else:
        print("   Starting OAuth flow...")
        flow = InstalledAppFlow.from_client_secrets_file(str(credentials_path), SCOPES)
        creds = flow.run_local_server(port=0)

    # Save credentials for future use
    with open(token_path, 'w') as token:
        token.write(creds.to_json())

print("[+] Authentication successful\n")

# Create Gmail service
service = build('gmail', 'v1', credentials=creds)

# Step 3: Build Search Query
query_parts = []

if email_subject:
    # Use curly braces for phrase matching with partial match support
    query_parts.append(f'subject:{{{email_subject}}}')

if sender_email:
    query_parts.append(f'from:{sender_email}')

# Combine query parts (search all emails if no filters)
query = ' '.join(query_parts) if query_parts else ''

print(f"[*] Gmail Search Query: {query}")
print(f"[*] Max Results: {max_emails}\n")

# Search emails
print("[*] Searching emails...")
results = service.users().messages().list(
    userId='me',
    q=query,
    maxResults=max_emails
).execute()

messages = results.get('messages', [])

if not messages:
    print("[!] No emails found matching the criteria")
    print("   Creating empty Excel file with headers...\n")
else:
    print(f"[+] Found {len(messages)} emails\n")

# Step 4: Extract Data
submissions = []

for i, message in enumerate(messages, 1):
    try:
        print(f"Processing email {i}/{len(messages)}...")

        # Get email details
        msg = service.users().messages().get(userId='me', id=message['id'], format='full').execute()

        # Extract headers
        headers = msg['payload']['headers']
        sender = next((h['value'] for h in headers if h['name'] == 'From'), '')
        subject = next((h['value'] for h in headers if h['name'] == 'Subject'), '')
        date_str = next((h['value'] for h in headers if h['name'] == 'Date'), '')

        # Extract sender email from "Name <email@example.com>" format
        email_match = re.search(r'<(.+?)>', sender)
        sender_email_extracted = email_match.group(1) if email_match else sender

        # Parse received time
        received_time = parsedate_to_datetime(date_str).isoformat()

        # Get thread ID
        thread_id = msg['threadId']

        # Extract body
        def get_body(payload):
            if 'body' in payload and 'data' in payload['body']:
                return base64.urlsafe_b64decode(payload['body']['data']).decode('utf-8', errors='ignore')
            if 'parts' in payload:
                for part in payload['parts']:
                    body = get_body(part)
                    if body:
                        return body
            return ''

        body = get_body(msg['payload'])

        # Extract GitHub URL using regex
        github_pattern = r'https://github\.com/([a-zA-Z0-9_-]+)/([a-zA-Z0-9_.-]+)(\.git)?'
        github_match = re.search(github_pattern, body)

        # Generate email_id (SHA-256)
        email_id = hashlib.sha256(f"{sender_email_extracted}|{subject}|{received_time}".encode()).hexdigest()

        # Hash sender email for privacy
        hashed_email = hashlib.sha256(sender_email_extracted.encode()).hexdigest()

        # Determine status
        if github_match:
            status = "Ready"
            github_url = github_match.group(0)
            print(f"  [+] Found GitHub URL: {github_url}")
        else:
            status = "Missing: github_url"
            github_url = ""
            print(f"  [!] No GitHub URL found")

        # Add to submissions
        submissions.append({
            'email_id': email_id,
            'received_time': received_time,
            'email_subject': subject,
            'sender_email': sender_email_extracted,
            'hashed_email': hashed_email,
            'github_url': github_url,
            'thread_id': thread_id,
            'status': status
        })

    except Exception as e:
        print(f"  [-] Error processing email: {e}")
        # Add error entry
        submissions.append({
            'email_id': f"error_{i}",
            'received_time': '',
            'email_subject': '',
            'sender_email': '',
            'hashed_email': '',
            'github_url': '',
            'thread_id': '',
            'status': f"Error: {str(e)}"
        })

# Step 5: Create Excel1.xlsx
print("\n[*] Creating Excel1.xlsx...")

# Ensure results directory exists
Path('results/excel').mkdir(parents=True, exist_ok=True)

# Create workbook
wb = openpyxl.Workbook()
ws = wb.active
ws.title = "Email Submissions"

# Headers
headers = [
    "email_id",
    "received_time",
    "email_subject",
    "sender_email",
    "hashed_email",
    "github_url",
    "thread_id",
    "status"
]
ws.append(headers)

# Format headers
for cell in ws[1]:
    cell.font = openpyxl.styles.Font(bold=True)

# Add rows
for submission in submissions:
    ws.append([
        submission['email_id'],
        submission['received_time'],
        submission['email_subject'],
        submission['sender_email'],
        submission['hashed_email'],
        submission['github_url'],
        submission['thread_id'],
        submission['status']
    ])

# Auto-adjust column widths
for column in ws.columns:
    max_length = 0
    column_letter = column[0].column_letter
    for cell in column:
        try:
            if len(str(cell.value)) > max_length:
                max_length = len(str(cell.value))
        except:
            pass
    adjusted_width = min(max_length + 2, 50)
    ws.column_dimensions[column_letter].width = adjusted_width

# Save
output_path = Path('results/excel/Excel1.xlsx')
wb.save(output_path)

# Step 6: Output Summary
ready_count = sum(1 for s in submissions if s['status'] == "Ready")
missing_count = sum(1 for s in submissions if "Missing" in s['status'])
error_count = sum(1 for s in submissions if "Error" in s['status'])

print("\n" + "="*70)
print("EXTRACTION SUMMARY")
print("="*70)
print(f"[+] Processed: {len(submissions)} emails")
print(f"[+] Excel1.xlsx created: {output_path}")
print(f"\nStatus breakdown:")
print(f"   - Ready (with GitHub URL): {ready_count}")
print(f"   - Missing GitHub URL: {missing_count}")
print(f"   - Errors: {error_count}")
print("="*70 + "\n")
