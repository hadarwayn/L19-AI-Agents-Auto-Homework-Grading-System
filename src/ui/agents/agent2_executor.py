"""
Agent 2 Executor - Repository Analysis

Analyzes GitHub repositories and creates Excel2.xlsx with metrics.

Author: Hadar Wayn
Date: December 2025
"""

import openpyxl
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
from rich.console import Console

from .agent2_repo_analyzer import analyze_repository
from .excel_utils import create_excel_workbook, auto_adjust_columns
from ...utils.paths import get_excel_file, get_excel_dir

console = Console()


def execute_agent2() -> bool:
    """
    Execute Agent 2 repository analysis logic

    Returns:
        bool: True if successful, False otherwise
    """
    try:
        # Check if Excel1.xlsx exists
        excel1_path = get_excel_file('Excel1.xlsx')
        if not excel1_path.exists():
            console.print("[red][!] Excel1.xlsx not found. Please run Agent 1 first.[/red]\n")
            return False

        console.print(f"[*] Reading Excel1.xlsx: {excel1_path}\n")

        # Load ready repositories
        ready_rows = _load_ready_repositories(excel1_path)
        console.print(f"[+] Found {len(ready_rows)} repositories to analyze\n")

        # Analyze repositories
        if len(ready_rows) == 0:
            console.print("[!] No repositories to analyze. Creating empty Excel2.xlsx...\n")
            results = []
        else:
            results = _analyze_repositories_parallel(ready_rows)

        # Create Excel2.xlsx
        _create_excel2(results)

        # Print summary
        _print_summary(results)

        return True

    except Exception as e:
        console.print(f"\n[red][!] Agent 2 execution failed: {e}[/red]\n")
        import traceback
        console.print(f"[dim]{traceback.format_exc()}[/dim]")
        return False

def _load_ready_repositories(excel1_path: Path) -> list:
    """Load repositories with status='Ready' from Excel1"""
    wb = openpyxl.load_workbook(excel1_path)
    ws = wb.active

    ready_rows = []
    for row in ws.iter_rows(min_row=2, values_only=True):
        email_id, received_time, subject, sender, github_url, thread_id, status = row
        if status == "Ready":
            ready_rows.append({
                'email_id': email_id,
                'github_url': github_url
            })

    return ready_rows

def _analyze_repositories_parallel(ready_rows: list, max_workers: int = 5) -> list:
    """Analyze repositories in parallel using thread pool"""
    results = []
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        # Submit all analysis tasks
        futures = {
            executor.submit(analyze_repository, row['email_id'], row['github_url']): row
            for row in ready_rows
        }

        # Collect results as they complete
        for future in as_completed(futures):
            result = future.result()
            results.append(result)

    return results

def _create_excel2(results: list):
    """Create Excel2.xlsx with analysis results"""
    console.print("\n[*] Creating Excel2.xlsx...")

    excel_dir = get_excel_dir()
    excel_dir.mkdir(parents=True, exist_ok=True)

    # Create workbook with headers
    headers = [
        "email_id",
        "github_url",
        "total_files",
        "total_lines",
        "compliant_lines",
        "grade",
        "status"
    ]
    wb = create_excel_workbook("Repository Analysis", headers)
    ws = wb.active

    # Add data rows
    for result in results:
        ws.append([
            result['email_id'],
            result['github_url'],
            result['total_files'],
            result['total_lines'],
            result['compliant_lines'],
            result['grade'],
            result['status']
        ])

    # Auto-adjust columns
    auto_adjust_columns(ws)

    # Save file
    output_path = excel_dir / 'Excel2.xlsx'
    wb.save(output_path)
    console.print(f"[+] Excel2.xlsx created: {output_path}")

def _print_summary(results: list):
    """Print analysis summary statistics"""
    successful_count = sum(1 for r in results if r['status'] == 'Ready')
    failed_count = sum(1 for r in results if 'Failed' in r['status'])
    avg_grade = sum(r['grade'] for r in results) / len(results) if results else 0

    console.print("\n" + "="*70)
    console.print("ANALYSIS SUMMARY")
    console.print("="*70)
    console.print(f"[+] Total repositories: {len(results)}")
    console.print(f"[+] Successful: {successful_count}")
    console.print(f"[+] Failed: {failed_count}")
    console.print(f"[+] Average grade: {avg_grade:.2f}%")
    console.print("="*70 + "\n")
