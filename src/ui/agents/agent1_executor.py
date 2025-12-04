"""
Agent 1 Executor - Email Extraction

Extracts homework emails from Gmail and creates Excel1.xlsx.

Author: Hadar Wayn
Date: December 2025
"""

import openpyxl
from rich.console import Console

from .gmail_auth import get_gmail_service
from .agent1_email_parser import extract_email_data
from .excel_utils import create_excel_workbook, auto_adjust_columns
from ...utils.paths import get_excel_dir

console = Console()


def execute_agent1(params: dict) -> bool:
    """
    Execute Agent 1 email extraction logic

    Args:
        params: Dictionary with email_subject, sender_email, max_emails, query

    Returns:
        bool: True if successful, False otherwise
    """
    try:
        # Extract parameters
        email_subject = params.get('email_subject')
        sender_email = params.get('sender_email')
        max_emails = params.get('max_emails', 10)
        query = params.get('query', '')

        # Log parameters
        console.print(f"[*] Email Subject: {email_subject or '(all subjects)'}")
        console.print(f"[*] Sender Email: {sender_email or '(all senders)'}")
        console.print(f"[*] Max Emails: {max_emails}")
        console.print(f"[*] Gmail Query: {query}\n")

        # Authenticate with Gmail
        service = get_gmail_service(console)

        # Search emails
        console.print("[*] Searching emails...")
        results = service.users().messages().list(
            userId='me',
            q=query,
            maxResults=max_emails
        ).execute()

        messages = results.get('messages', [])

        # Extract email data
        if not messages:
            console.print("[!] No emails found matching the criteria\n")
            submissions = []
        else:
            console.print(f"[+] Found {len(messages)} emails\n")
            submissions = extract_email_data(service, messages, email_subject)

        # Create Excel file
        _create_excel1(submissions)

        # Print summary
        _print_summary(submissions)

        return True

    except Exception as e:
        console.print(f"\n[red][!] Agent 1 execution failed: {e}[/red]\n")
        import traceback
        console.print(f"[dim]{traceback.format_exc()}[/dim]")
        return False


def _create_excel1(submissions: list):
    """
    Create Excel1.xlsx with submission data

    Args:
        submissions: List of submission dictionaries
    """
    console.print("\n[*] Creating Excel1.xlsx...")

    # Ensure directory exists
    excel_dir = get_excel_dir()
    excel_dir.mkdir(parents=True, exist_ok=True)

    # Create workbook with headers
    headers = [
        "email_id",
        "received_time",
        "email_subject",
        "sender_email",
        "github_url",
        "thread_id",
        "status"
    ]
    wb = create_excel_workbook("Email Submissions", headers)
    ws = wb.active

    # Add data rows
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
    auto_adjust_columns(ws)

    # Save file
    output_path = excel_dir / 'Excel1.xlsx'
    wb.save(output_path)
    console.print(f"[+] Excel1.xlsx created: {output_path}")


def _print_summary(submissions: list):
    """
    Print extraction summary statistics

    Args:
        submissions: List of submission dictionaries
    """
    # Calculate statistics
    ready_count = sum(1 for s in submissions if s['status'] == "Ready")
    missing_count = sum(1 for s in submissions if "Missing" in s['status'])
    error_count = sum(1 for s in submissions if "Error" in s['status'])

    # Print summary
    console.print("\n" + "="*70)
    console.print("EXTRACTION SUMMARY")
    console.print("="*70)
    console.print(f"[+] Processed: {len(submissions)} emails")
    console.print(f"\nStatus breakdown:")
    console.print(f"   - Ready (with GitHub URL): {ready_count}")
    console.print(f"   - Missing GitHub URL: {missing_count}")
    console.print(f"   - Errors: {error_count}")
    console.print("="*70 + "\n")
