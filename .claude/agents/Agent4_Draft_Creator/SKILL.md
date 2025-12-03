# Agent 4: Draft Email Creator

**Description**: Create Gmail draft replies with personalized feedback for each student

## Responsibilities

1. Read Excel3.xlsx (only "Ready" rows)
2. Join with Excel1.xlsx to get email metadata
3. Load student names from students_mapping.xlsx
4. Compose personalized email with feedback
5. Create Gmail draft (NOT send)

## Prerequisites

- Excel3.xlsx must exist (from Agent 3)
- Excel1.xlsx must exist (from Agent 1)
- data/students_mapping.xlsx exists
- Gmail API credentials configured

## Instructions

### Step 1: Read Excel Files
```python
import openpyxl
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from email.mime.text import MIMEText
import base64

# Load Excel3 (feedback)
wb3 = openpyxl.load_workbook('results/excel/Excel3.xlsx')
ws3 = wb3.active

feedback_data = {}
for row in ws3.iter_rows(min_row=2, values_only=True):
    email_id, grade, category, persona, response, attempts, status = row
    if status == "Ready" and response:
        feedback_data[email_id] = {
            'grade': grade,
            'response': response
        }

print(f"Found {len(feedback_data)} submissions with feedback")

# Load Excel1 (email metadata)
wb1 = openpyxl.load_workbook('results/excel/Excel1.xlsx')
ws1 = wb1.active

email_metadata = {}
for row in ws1.iter_rows(min_row=2, values_only=True):
    email_id, received_time, subject, sender, hashed, github_url, thread_id, status = row
    email_metadata[email_id] = {
        'sender': sender,
        'subject': subject,
        'thread_id': thread_id,
        'github_url': github_url
    }

# Load student mapping
wb_mapping = openpyxl.load_workbook('data/students_mapping.xlsx')
ws_mapping = wb_mapping.active

student_names = {}
for row in ws_mapping.iter_rows(min_row=2, values_only=True):
    email, name = row
    student_names[email.lower().strip()] = name
```

### Step 2: Gmail Authentication
```python
# Gmail API scopes
SCOPES = ['https://www.googleapis.com/auth/gmail.compose']

# Authenticate
# Load credentials from Secrets/credentials.json
# Create Gmail service
service = build('gmail', 'v1', credentials=creds)
```

### Step 3: Create Draft for Each Student
```python
drafts_created = 0
drafts_failed = 0

for email_id, feedback in feedback_data.items():
    # Get email metadata
    metadata = email_metadata.get(email_id)
    if not metadata:
        print(f"  ⚠ No metadata for {email_id[:8]}, skipping")
        continue

    sender_email = metadata['sender']
    original_subject = metadata['subject']
    thread_id = metadata['thread_id']
    github_url = metadata['github_url']
    grade = feedback['grade']
    response_text = feedback['response']

    # Get student name (or use email prefix)
    student_name = student_names.get(sender_email.lower(), sender_email.split('@')[0])

    # Compose email
    email_body = f"""Hi {student_name}!

{response_text}

📎 Your repository reviewed: {github_url}
📊 Your grade: {grade}/100

Best regards,
Instructor
"""

    # Create MIME message
    message = MIMEText(email_body)
    message['to'] = sender_email
    message['subject'] = f"Re: {original_subject}"

    # Encode message
    raw_message = base64.urlsafe_b64encode(message.as_bytes()).decode('utf-8')

    # Create draft as reply (using thread_id)
    try:
        draft = {
            'message': {
                'raw': raw_message,
                'threadId': thread_id
            }
        }

        created_draft = service.users().drafts().create(
            userId='me',
            body=draft
        ).execute()

        print(f"  ✓ Draft created for {student_name} ({sender_email})")
        drafts_created += 1

    except Exception as e:
        print(f"  ✗ Failed to create draft for {sender_email}: {e}")
        drafts_failed += 1
```

### Step 4: Output
```python
print(f"\n✅ Draft creation complete!")
print(f"   - Total drafts created: {drafts_created}")
print(f"   - Failed: {drafts_failed}")
print(f"\n📧 Check your Gmail Drafts folder to review before sending!")
```

## Email Template

```
Subject: Re: [Original Subject]

Hi [Student Name]!

[AI-Generated Feedback Response]

📎 Your repository reviewed: [GitHub URL]
📊 Your grade: [Grade]/100

Best regards,
Instructor
```

## Name Mapping

**students_mapping.xlsx** format:
| email_address | name |
|--------------|------|
| student1@example.com | Alex Johnson |
| student2@example.com | Maria Garcia |

- If email found: Use mapped name
- If not found: Use email prefix (before @)

## Expected Behavior

- **Drafts are created** (NOT sent automatically)
- Drafts appear in Gmail Drafts folder
- Each draft is a **reply** to original email (uses thread_id)
- Instructor can review drafts before sending
- Personalized with student name and feedback

## Error Handling

- Missing metadata: Skip and log warning
- No student name: Use email prefix
- Gmail API failure: Log error, continue with others
- Invalid thread_id: Create new thread

## Success Criteria

- All ready submissions from Excel3 processed
- Drafts created in Gmail (visible in web interface)
- Emails are replies to original threads
- No emails sent automatically
- Student names correctly mapped
