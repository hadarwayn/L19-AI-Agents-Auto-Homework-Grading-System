"""
Hash Utilities

Provides SHA-256 hashing functions for:
- Email ID generation
- Email address hashing (privacy)

Author: Hadar Wayn
Date: December 2025
"""

import hashlib
from datetime import datetime
from typing import Union


def hash_string(text: str) -> str:
    """
    Generate SHA-256 hash of a string

    Args:
        text: Text to hash

    Returns:
        str: Hex digest of SHA-256 hash
    """
    return hashlib.sha256(text.encode('utf-8')).hexdigest()


def hash_email_address(email: str) -> str:
    """
    Hash email address for privacy

    Args:
        email: Email address to hash

    Returns:
        str: SHA-256 hash of email address
    """
    return hash_string(email.lower().strip())


def generate_email_id(sender: str, subject: str, received_time: Union[datetime, str]) -> str:
    """
    Generate unique email ID using SHA-256

    Combines sender email, subject, and timestamp to create unique identifier.

    Args:
        sender: Sender email address
        subject: Email subject
        received_time: Email received timestamp (datetime or ISO string)

    Returns:
        str: SHA-256 hash (unique email ID)
    """
    # Convert datetime to string if needed
    if isinstance(received_time, datetime):
        time_str = received_time.isoformat()
    else:
        time_str = str(received_time)

    # Combine all components
    combined = f"{sender.lower().strip()}|{subject.strip()}|{time_str}"

    # Generate hash
    return hash_string(combined)


def generate_file_hash(file_path: str) -> str:
    """
    Generate SHA-256 hash of a file

    Args:
        file_path: Path to file

    Returns:
        str: SHA-256 hash of file contents
    """
    sha256_hash = hashlib.sha256()

    with open(file_path, "rb") as f:
        # Read file in chunks to handle large files
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)

    return sha256_hash.hexdigest()


def verify_hash(text: str, expected_hash: str) -> bool:
    """
    Verify text matches expected hash

    Args:
        text: Text to verify
        expected_hash: Expected SHA-256 hash

    Returns:
        bool: True if hash matches, False otherwise
    """
    actual_hash = hash_string(text)
    return actual_hash == expected_hash
