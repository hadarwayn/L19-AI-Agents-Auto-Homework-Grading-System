"""
Agent 3 Executor - LLM Feedback Generation

Generates personalized feedback for submissions and creates Excel3.xlsx.

Author: Hadar Wayn
Date: December 2025
"""

import os
import time
import openpyxl
from pathlib import Path
from dotenv import load_dotenv
from rich.console import Console

from .agent3_feedback_generator import generate_feedback
from .excel_utils import create_excel_workbook, auto_adjust_columns
from ...utils.paths import get_excel_file, get_excel_dir

console = Console()


def execute_agent3() -> bool:
    """Execute Agent 3 LLM feedback generation logic"""
    try:
        load_dotenv()
        excel2_path = get_excel_file('Excel2.xlsx')
        if not excel2_path.exists():
            console.print("[red][!] Excel2.xlsx not found. Please run Agent 2 first.[/red]\n")
            return False
        gemini_api_key = os.getenv('GEMINI_API_KEY')
        if not gemini_api_key:
            console.print("[red][!] GEMINI_API_KEY not found. Set in .env file.[/red]\n")
            return False
        console.print(f"[*] Reading Excel2.xlsx: {excel2_path}\n")

        # Load ready submissions
        ready_rows = _load_ready_submissions(excel2_path)
        console.print(f"[+] Found {len(ready_rows)} submissions to generate feedback for\n")

        # Generate feedback
        if len(ready_rows) == 0:
            console.print("[!] No submissions to process. Creating empty Excel3.xlsx...\n")
            results = []
        else:
            results = _generate_all_feedback(ready_rows, gemini_api_key)

        # Create Excel3.xlsx
        _create_excel3(results)

        # Print summary
        _print_summary(results)

        return True

    except Exception as e:
        console.print(f"\n[red][!] Agent 3 execution failed: {e}[/red]\n")
        import traceback
        console.print(f"[dim]{traceback.format_exc()}[/dim]")
        return False

def _load_ready_submissions(excel2_path: Path) -> list:
    """Load submissions with status='Ready' from Excel2"""
    wb = openpyxl.load_workbook(excel2_path)
    ws = wb.active

    ready_rows = []
    for row in ws.iter_rows(min_row=2, values_only=True):
        email_id, github_url, total_files, total_lines, compliant_lines, grade, status = row
        if status == "Ready":
            ready_rows.append({
                'email_id': email_id,
                'github_url': github_url,
                'grade': grade
            })

    return ready_rows

def _generate_all_feedback(ready_rows: list, gemini_api_key: str) -> list:
    """Generate feedback for all submissions"""
    results = []

    for row in ready_rows:
        # Generate feedback for this submission
        result = generate_feedback(
            row['email_id'],
            row['grade'],
            row['github_url'],
            gemini_api_key
        )
        results.append(result)

        # Delay between API calls to avoid rate limiting
        time.sleep(2)

    return results

def _create_excel3(results: list):
    """Create Excel3.xlsx with feedback results"""
    console.print("\n[*] Creating Excel3.xlsx...")

    excel_dir = get_excel_dir()
    excel_dir.mkdir(parents=True, exist_ok=True)

    # Create workbook with headers
    headers = ["email_id", "grade", "grade_category", "persona", "response", "api_attempts", "status"]
    wb = create_excel_workbook("LLM Feedback", headers)
    ws = wb.active

    # Add data rows
    for result in results:
        ws.append([
            result['email_id'],
            result['grade'],
            result['grade_category'],
            result['persona'],
            result['response'],
            result['api_attempts'],
            result['status']
        ])

    # Auto-adjust columns (allow wider columns for response text)
    auto_adjust_columns(ws, max_width=80)

    # Save file
    output_path = excel_dir / 'Excel3.xlsx'
    wb.save(output_path)
    console.print(f"[+] Excel3.xlsx created: {output_path}")

def _print_summary(results: list):
    """Print feedback generation summary"""
    successful_count = sum(1 for r in results if r['status'] == 'Ready')
    failed_count = sum(1 for r in results if 'Missing' in r['status'])
    console.print("\n" + "="*70)
    console.print("FEEDBACK GENERATION SUMMARY")
    console.print("="*70)
    console.print(f"[+] Total submissions: {len(results)}")
    console.print(f"[+] Successful: {successful_count}")
    console.print(f"[+] Failed: {failed_count}")
    if results:
        console.print(f"\nPersonas used:")
        for persona in ['trump', 'hason', 'lee', 'amsalem']:
            count = sum(1 for r in results if r['persona'] == persona)
            if count > 0:
                console.print(f"   - {persona}: {count}")
    console.print("="*70 + "\n")
