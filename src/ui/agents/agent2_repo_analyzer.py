"""
Agent 2 Repository Analyzer

Clones and analyzes GitHub repositories for code quality metrics.

Author: Hadar Wayn
Date: December 2025
"""

import git
import shutil
from pathlib import Path
from rich.console import Console

console = Console()


def analyze_repository(email_id: str, github_url: str) -> dict:
    """
    Clone and analyze a single GitHub repository

    Args:
        email_id: Unique email identifier
        github_url: GitHub repository URL

    Returns:
        dict: Analysis results with metrics
    """
    try:
        # Create unique temporary directory for this repo
        repo_dir = Path(f"temp/repos/{email_id[:8]}")

        # Remove directory if it already exists
        if repo_dir.exists():
            shutil.rmtree(repo_dir)

        # Clone repository (depth=1 for speed - only latest commit)
        console.print(f"[*] Cloning {github_url[:60]}...")
        git.Repo.clone_from(github_url, repo_dir, depth=1)

        # Analyze Python files
        metrics = _analyze_python_files(repo_dir)

        # Calculate grade based on 150-line compliance
        grade = _calculate_grade(metrics['total_lines'], metrics['compliant_lines'])

        console.print(f"  [+] {email_id[:8]} - Files: {metrics['file_count']}, Grade: {grade}%")

        return {
            'email_id': email_id,
            'github_url': github_url,
            'total_files': metrics['file_count'],
            'total_lines': metrics['total_lines'],
            'compliant_lines': metrics['compliant_lines'],
            'grade': grade,
            'status': 'Ready'
        }

    except git.GitCommandError as e:
        console.print(f"  [!] {email_id[:8]} - Clone failed")
        return _create_error_result(email_id, github_url, 'Failed: clone')

    except Exception as e:
        console.print(f"  [!] {email_id[:8]} - Error: {str(e)[:50]}")
        return _create_error_result(email_id, github_url, f'Failed: {str(e)[:50]}')


def _analyze_python_files(repo_dir: Path) -> dict:
    """
    Analyze all Python files in repository

    Args:
        repo_dir: Repository directory path

    Returns:
        dict: Metrics with total_lines, compliant_lines, file_count
    """
    # Find all Python files recursively
    python_files = list(repo_dir.rglob("*.py"))

    total_lines = 0
    compliant_lines = 0
    file_count = 0

    for py_file in python_files:
        try:
            with open(py_file, 'r', encoding='utf-8') as f:
                lines = len(f.readlines())
                total_lines += lines

                # Compliant files have <= 150 lines per PROJECT_GUIDELINES.md
                if lines <= 150:
                    compliant_lines += lines

                file_count += 1

        except Exception:
            # Skip files that can't be read (binary files, encoding issues, etc.)
            continue

    return {
        'total_lines': total_lines,
        'compliant_lines': compliant_lines,
        'file_count': file_count
    }


def _calculate_grade(total_lines: int, compliant_lines: int) -> float:
    """
    Calculate grade based on compliance with 150-line rule

    Args:
        total_lines: Total lines of code
        compliant_lines: Lines in files <= 150 lines

    Returns:
        float: Grade percentage (0-100)
    """
    if total_lines > 0:
        return round(100 * (compliant_lines / total_lines), 2)
    else:
        return 0.0


def _create_error_result(email_id: str, github_url: str, status: str) -> dict:
    """Create error result with zero metrics"""
    return {
        'email_id': email_id,
        'github_url': github_url,
        'total_files': 0,
        'total_lines': 0,
        'compliant_lines': 0,
        'grade': 0.0,
        'status': status
    }
