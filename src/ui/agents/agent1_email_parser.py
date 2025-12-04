"""
Agent 1 Email Parser

Extracts and parses email data from Gmail messages.

Author: Hadar Wayn
Date: December 2025
"""

import re
import hashlib
import base64
from email.utils import parsedate_to_datetime
from rich.console import Console

console = Console()


def extract_email_data(service, messages: list, email_subject: str = None) -> list:
    """
    Extract data from Gmail messages

    Args:
        service: Gmail API service
        messages: List of message objects
        email_subject: Optional subject filter for post-filtering

    Returns:
        list: List of submission dictionaries
    """
    submissions = []

    for i, message in enumerate(messages, 1):
        try:
            console.print(f"Processing email {i}/{len(messages)}...")

            # Get full message
            msg = service.users().messages().get(
                userId='me',
                id=message['id'],
                format='full'
            ).execute()

            # Extract headers
            headers = msg['payload']['headers']
            sender = next((h['value'] for h in headers if h['name'] == 'From'), '')
            subject = next((h['value'] for h in headers if h['name'] == 'Subject'), '')
            date_str = next((h['value'] for h in headers if h['name'] == 'Date'), '')

            # Post-filter: verify substring match (case-insensitive)
            if email_subject and email_subject.lower() not in subject.lower():
                console.print(f"  [-] Subject doesn't contain '{email_subject}', skipping")
                continue

            # Extract sender email address
            email_match = re.search(r'<(.+?)>', sender)
            sender_email_extracted = email_match.group(1) if email_match else sender

            # Parse timestamp and thread ID
            received_time = parsedate_to_datetime(date_str).isoformat()
            thread_id = msg['threadId']

            # Extract email body
            body = get_email_body(msg['payload'])

            # Find GitHub URL in body
            github_pattern = r'https://github\.com/([a-zA-Z0-9_-]+)/([a-zA-Z0-9_.-]+)(\.git)?'
            github_match = re.search(github_pattern, body)

            # Generate unique email ID
            email_id = hashlib.sha256(
                f"{sender_email_extracted}|{subject}|{received_time}".encode()
            ).hexdigest()

            # Determine status based on GitHub URL presence
            if github_match:
                status = "Ready"
                github_url = github_match.group(0)
                console.print(f"  [+] Found GitHub URL: {github_url}")
            else:
                status = "Missing: github_url"
                github_url = ""
                console.print(f"  [!] No GitHub URL found")

            # Create submission record
            submissions.append({
                'email_id': email_id,
                'received_time': received_time,
                'email_subject': subject,
                'sender_email': sender_email_extracted,
                'github_url': github_url,
                'thread_id': thread_id,
                'status': status
            })

        except Exception as e:
            console.print(f"  [-] Error processing email: {e}")

    return submissions


def get_email_body(payload: dict) -> str:
    """
    Recursively extract email body from payload

    Args:
        payload: Gmail message payload

    Returns:
        str: Decoded email body text
    """
    # Check if body data is directly in payload
    if 'body' in payload and 'data' in payload['body']:
        try:
            return base64.urlsafe_b64decode(
                payload['body']['data']
            ).decode('utf-8', errors='ignore')
        except Exception:
            return ''

    # Recursively check parts
    if 'parts' in payload:
        for part in payload['parts']:
            body = get_email_body(part)
            if body:
                return body

    return ''
