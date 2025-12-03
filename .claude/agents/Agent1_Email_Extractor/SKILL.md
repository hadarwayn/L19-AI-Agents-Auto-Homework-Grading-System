# Agent 1: Email Extractor

**Description**: Extract GitHub repository URLs from Gmail based on user-specified search parameters and create Excel1.xlsx

## Responsibilities

1. **Prompt user for search parameters** (email subject, sender, max emails)
2. Connect to Gmail API using OAuth2
3. Search for emails matching user criteria
4. Extract GitHub URLs from email body
5. Generate unique email ID (SHA-256)
6. Create Excel1.xlsx with submission data

## User Input Parameters

**The agent MUST prompt the user for the following parameters at runtime:**

| Parameter | Type | Required | Default | Range | Description |
|-----------|------|----------|---------|-------|-------------|
| Email Subject | String | ❌ Optional | None | Any text | Partial subject match (case-insensitive). Press Enter to skip. |
| Sender Email | String | ❌ Optional | None | Valid email | Filter by sender's email address. Press Enter to skip. |
| Max Emails | Integer | ✅ Required | 10 | 1-100 | Maximum number of emails to process. |

## Instructions

### Step 1: Prompt User for Parameters
```python
# Import required libraries
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
import openpyxl
import re
import hashlib
from datetime import datetime
from pathlib import Path

# Gmail API scopes
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

# Display parameter prompt
print("╔══════════════════════════════════════════════════════════════════╗")
print("║              AGENT 1: EMAIL EXTRACTION PARAMETERS                ║")
print("╠══════════════════════════════════════════════════════════════════╣")

# Email subject (optional)
email_subject = input("📧 Email Subject (optional, press Enter to skip): ").strip()
if not email_subject:
    email_subject = None
    print("   → Will search all email subjects")
else:
    print(f"   → Will search for: \"{email_subject}\"")

# Sender email (optional)
sender_email = input("👤 Sender Email (optional, press Enter to skip): ").strip()
if not sender_email:
    sender_email = None
    print("   → Will search all senders")
else:
    # Basic email validation
    if '@' not in sender_email or '.' not in sender_email.split('@')[-1]:
        print("   ⚠ Invalid email format, will search all senders")
        sender_email = None
    else:
        print(f"   → Will filter by sender: {sender_email}")

# Max emails (required, default 10)
max_emails_input = input("🔢 Max Emails (1-100) [Default: 10]: ").strip()
if not max_emails_input:
    max_emails = 10
    print("   → Using default: 10 emails")
else:
    try:
        max_emails = int(max_emails_input)
        if max_emails < 1 or max_emails > 100:
            print("   ⚠ Invalid range, using default: 10")
            max_emails = 10
        else:
            print(f"   → Will process up to {max_emails} emails")
    except ValueError:
        print("   ⚠ Invalid input, using default: 10")
        max_emails = 10

print("╚══════════════════════════════════════════════════════════════════╝\n")
```

### Step 2: Gmail Authentication
```python
# Load credentials from Secrets/credentials.json
creds = None
token_path = Path('Secrets/token.json')
credentials_path = Path('Secrets/credentials.json')

# Check for existing token
if token_path.exists():
    creds = Credentials.from_authorized_user_file(str(token_path), SCOPES)

# If no valid credentials, authenticate
if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file(str(credentials_path), SCOPES)
        creds = flow.run_local_server(port=0)

    # Save credentials for future use
    with open(token_path, 'w') as token:
        token.write(creds.to_json())

# Create Gmail service
service = build('gmail', 'v1', credentials=creds)
```

### Step 3: Build Search Query and Search Emails
```python
# Build Gmail search query based on user input
query_parts = []

# Add subject filter (if provided)
if email_subject:
    # Use subject: without quotes for broad matching (post-filter ensures substring match)
    query_parts.append(f'subject:{email_subject}')

# Add sender filter (if provided)
if sender_email:
    query_parts.append(f'from:{sender_email}')

# Combine query parts (search all emails if no filters)
query = ' '.join(query_parts) if query_parts else ''

print(f"🔍 Gmail Search Query: {query}")
print(f"📊 Max Results: {max_emails}\n")

# Search emails
results = service.users().messages().list(
    userId='me',
    q=query,
    maxResults=max_emails
).execute()

messages = results.get('messages', [])

if not messages:
    print("⚠ No emails found matching the criteria")
    print("   Creating empty Excel file with headers...\n")
else:
    print(f"✓ Found {len(messages)} emails\n")
```

### Step 4: Extract Data
For each email:

```python
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

        # Post-filter: Verify subject contains search term (case-insensitive substring match)
        if email_subject and email_subject.lower() not in subject.lower():
            print(f"  ⊗ Subject doesn't contain '{email_subject}', skipping")
            continue

        # Extract sender email from "Name <email@example.com>" format
        email_match = re.search(r'<(.+?)>', sender)
        sender_email = email_match.group(1) if email_match else sender

        # Parse received time
        from email.utils import parsedate_to_datetime
        received_time = parsedate_to_datetime(date_str).isoformat()

        # Get thread ID
        thread_id = msg['threadId']

        # Extract body
        def get_body(payload):
            if 'body' in payload and 'data' in payload['body']:
                import base64
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
        email_id = hashlib.sha256(f"{sender_email}|{subject}|{received_time}".encode()).hexdigest()

        # Determine status
        if github_match:
            status = "Ready"
            github_url = github_match.group(0)
            print(f"  ✓ Found GitHub URL: {github_url}")
        else:
            status = "Missing: github_url"
            github_url = ""
            print(f"  ⚠ No GitHub URL found")

        # Add to submissions
        submissions.append({
            'email_id': email_id,
            'received_time': received_time,
            'email_subject': subject,
            'sender_email': sender_email,
            'github_url': github_url,
            'thread_id': thread_id,
            'status': status
        })

    except Exception as e:
        print(f"  ✗ Error processing email: {e}")
        # Add error entry
        submissions.append({
            'email_id': f"error_{i}",
            'received_time': '',
            'email_subject': '',
            'sender_email': '',
            'github_url': '',
            'thread_id': '',
            'status': f"Error: {str(e)}"
        })
```

### Step 5: Create Excel1.xlsx
```python
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
```

### Step 6: Output Summary
```python
# Count statistics
ready_count = sum(1 for s in submissions if s['status'] == "Ready")
missing_count = sum(1 for s in submissions if "Missing" in s['status'])
error_count = sum(1 for s in submissions if "Error" in s['status'])

print("\n" + "="*70)
print("📊 EXTRACTION SUMMARY")
print("="*70)
print(f"✅ Processed: {len(submissions)} emails")
print(f"✅ Excel1.xlsx created: {output_path}")
print(f"\nStatus breakdown:")
print(f"   - Ready (with GitHub URL): {ready_count}")
print(f"   - Missing GitHub URL: {missing_count}")
print(f"   - Errors: {error_count}")
print("="*70 + "\n")
```

## Expected Output

**Excel1.xlsx** (`results/excel/Excel1.xlsx`) with columns:
- `email_id`: SHA-256 hash (unique ID)
- `received_time`: ISO datetime string
- `email_subject`: Full subject line
- `sender_email`: Student's email address
- `github_url`: Extracted GitHub URL or empty
- `thread_id`: Gmail thread ID for replies
- `status`: "Ready" or "Missing: github_url" or "Error: [message]"

## Error Handling

- If Gmail auth fails: Exit with error message
- If no emails found: Create empty Excel with headers
- If email parsing fails: Set status = "Error: [description]"
- Continue processing remaining emails even if one fails
- Invalid user input: Use defaults with warning message

## Success Criteria

- User prompted for search parameters (subject, sender, max emails)
- Parameters validated with defaults applied where needed
- Excel1.xlsx exists in results/excel/
- All emails matching criteria are processed
- Status field correctly set for each row
- No exceptions thrown for valid inputs
