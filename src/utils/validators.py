"""
Input Validators

Provides validation functions for:
- Email addresses
- GitHub URLs
- Pattern extraction

Author: Hadar Wayn
Date: December 2025
"""

import re
from typing import Optional


# Email regex pattern
EMAIL_PATTERN = re.compile(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$")

# GitHub URL pattern (from PRD)
GITHUB_URL_PATTERN = re.compile(
    r"https://github\.com/([a-zA-Z0-9_-]+)/([a-zA-Z0-9_.-]+)(\.git)?"
)

# Homework subject pattern (from PRD)
SUBJECT_PATTERN = re.compile(r"self\s+check\s+of\s+homework\s+(\d{1,3})", re.IGNORECASE)


def validate_email(email: str) -> bool:
    """
    Validate email address format

    Args:
        email: Email address to validate

    Returns:
        bool: True if valid, False otherwise
    """
    if not email:
        return False
    return EMAIL_PATTERN.match(email.strip()) is not None


def validate_github_url(url: str) -> bool:
    """
    Validate GitHub repository URL format

    Args:
        url: GitHub URL to validate

    Returns:
        bool: True if valid, False otherwise
    """
    if not url:
        return False
    return GITHUB_URL_PATTERN.match(url.strip()) is not None


def extract_github_url(text: str) -> Optional[str]:
    """
    Extract first GitHub URL from text

    Args:
        text: Text to search for GitHub URL

    Returns:
        Optional[str]: GitHub URL if found, None otherwise
    """
    if not text:
        return None

    match = GITHUB_URL_PATTERN.search(text)
    if match:
        # Return the full matched URL
        return match.group(0)
    return None


def extract_homework_number(subject: str) -> Optional[int]:
    """
    Extract homework number from email subject

    Args:
        subject: Email subject line

    Returns:
        Optional[int]: Homework number if found, None otherwise
    """
    if not subject:
        return None

    match = SUBJECT_PATTERN.search(subject)
    if match:
        try:
            return int(match.group(1))
        except ValueError:
            return None
    return None


def validate_subject_pattern(subject: str) -> bool:
    """
    Validate email subject matches homework pattern

    Args:
        subject: Email subject to validate

    Returns:
        bool: True if matches pattern, False otherwise
    """
    if not subject:
        return False
    return SUBJECT_PATTERN.search(subject) is not None


def extract_github_owner_repo(url: str) -> Optional[tuple[str, str]]:
    """
    Extract owner and repository name from GitHub URL

    Args:
        url: GitHub URL

    Returns:
        Optional[tuple[str, str]]: (owner, repo) if valid, None otherwise
    """
    if not url:
        return None

    match = GITHUB_URL_PATTERN.match(url.strip())
    if match:
        owner = match.group(1)
        repo = match.group(2)
        # Remove .git suffix if present
        if repo.endswith(".git"):
            repo = repo[:-4]
        return (owner, repo)
    return None
