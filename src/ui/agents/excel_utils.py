"""
Excel Utilities

Shared utilities for creating and formatting Excel files.

Author: Hadar Wayn
Date: December 2025
"""

import openpyxl
from pathlib import Path


def create_excel_workbook(title: str, headers: list) -> openpyxl.Workbook:
    """
    Create a new Excel workbook with formatted headers

    Args:
        title: Worksheet title
        headers: List of column headers

    Returns:
        openpyxl.Workbook object with formatted headers
    """
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = title

    # Add headers
    ws.append(headers)

    # Format headers (bold)
    for cell in ws[1]:
        cell.font = openpyxl.styles.Font(bold=True)

    return wb


def auto_adjust_columns(ws: openpyxl.worksheet.worksheet.Worksheet, max_width: int = 50):
    """
    Auto-adjust column widths based on content

    Args:
        ws: Worksheet to adjust
        max_width: Maximum column width (default: 50)
    """
    for column in ws.columns:
        max_length = 0
        column_letter = column[0].column_letter

        # Find maximum length in column
        for cell in column:
            try:
                cell_length = len(str(cell.value))
                if cell_length > max_length:
                    max_length = cell_length
            except:
                pass

        # Set adjusted width (with padding, capped at max_width)
        adjusted_width = min(max_length + 2, max_width)
        ws.column_dimensions[column_letter].width = adjusted_width


def save_excel_file(wb: openpyxl.Workbook, filepath: Path, console=None) -> bool:
    """
    Save Excel workbook to file

    Args:
        wb: Workbook to save
        filepath: Destination path
        console: Optional Rich console for logging

    Returns:
        bool: True if successful, False otherwise
    """
    try:
        # Ensure parent directory exists
        filepath.parent.mkdir(parents=True, exist_ok=True)

        # Save workbook
        wb.save(filepath)

        if console:
            console.print(f"[+] Excel file created: {filepath}")

        return True

    except Exception as e:
        if console:
            console.print(f"[red][!] Failed to save Excel file: {e}[/red]")
        return False
