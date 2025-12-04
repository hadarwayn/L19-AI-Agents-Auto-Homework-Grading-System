"""
Agent 1 Parameter Collection

Prompts user for email search parameters.

Author: Hadar Wayn
Date: December 2025
"""

from rich.console import Console

console = Console()


def prompt_agent1_parameters() -> dict:
    """
    Prompt user for Agent 1 search parameters

    Returns:
        dict: Dictionary containing email_subject, sender_email, max_emails, query

    Example:
        >>> params = prompt_agent1_parameters()
        >>> params['email_subject']
        'GradingL19'
        >>> params['max_emails']
        10
    """
    console.print("\n[bold cyan]=====================================================================[/bold cyan]")
    console.print("[bold cyan]              AGENT 1: EMAIL EXTRACTION PARAMETERS                [/bold cyan]")
    console.print("[bold cyan]=====================================================================[/bold cyan]\n")

    # Email subject (optional)
    email_subject = console.input("[bold]Email Subject[/bold] (optional, press Enter to skip): ").strip()
    if not email_subject:
        email_subject = None
        console.print("   -> Will search all email subjects\n")
    else:
        console.print(f"   -> Will search for: [green]\"{email_subject}\"[/green]\n")

    # Sender email (optional)
    sender_email = console.input("[bold]Sender Email[/bold] (optional, press Enter to skip): ").strip()
    if not sender_email:
        sender_email = None
        console.print("   -> Will search all senders\n")
    else:
        # Basic email validation
        if '@' not in sender_email or '.' not in sender_email.split('@')[-1]:
            console.print("   [yellow][!] Invalid email format, will search all senders[/yellow]\n")
            sender_email = None
        else:
            console.print(f"   -> Will filter by sender: [green]{sender_email}[/green]\n")

    # Max emails (required, default 10)
    while True:
        max_emails_input = console.input("[bold]Max Emails (1-100)[/bold] [dim][Default: 10][/dim]: ").strip()
        if not max_emails_input:
            max_emails = 10
            console.print("   -> Using default: [green]10 emails[/green]\n")
            break
        else:
            try:
                max_emails = int(max_emails_input)
                if 1 <= max_emails <= 100:
                    console.print(f"   -> Will process up to [green]{max_emails} emails[/green]\n")
                    break
                else:
                    console.print("   [red][!] Please enter a number between 1 and 100[/red]")
            except ValueError:
                console.print("   [red][!] Please enter a valid number[/red]")

    # Build Gmail search query
    query = _build_gmail_query(email_subject, sender_email)

    console.print("[bold cyan]=====================================================================[/bold cyan]")
    console.print(f"[bold]Gmail Search Query:[/bold] [cyan]{query or '(all emails)'}[/cyan]")
    console.print(f"[bold]Max Results:[/bold] [cyan]{max_emails}[/cyan]")
    console.print("[bold cyan]=====================================================================[/bold cyan]\n")

    return {
        'email_subject': email_subject,
        'sender_email': sender_email,
        'max_emails': max_emails,
        'query': query
    }


def _build_gmail_query(email_subject: str = None, sender_email: str = None) -> str:
    """
    Build Gmail API search query from parameters

    Args:
        email_subject: Optional subject filter
        sender_email: Optional sender filter

    Returns:
        str: Gmail query string (empty string if no filters)
    """
    query_parts = []

    if email_subject:
        # Gmail search WITHOUT quotes works best
        # Use first 3 words for longer searches
        words = email_subject.split()

        if len(words) <= 3:
            # Short search (1-3 words): use all words
            query_parts.append(f'subject:{email_subject}')
        else:
            # Longer search (4+ words): use first 3 words for broad match
            # Python post-filter will ensure full phrase match
            key_words = ' '.join(words[:3])
            query_parts.append(f'subject:{key_words}')

    if sender_email:
        query_parts.append(f'from:{sender_email}')

    # Combine query parts (empty string if no filters)
    return ' '.join(query_parts)
