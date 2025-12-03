"""
Display Utilities using Rich

Provides formatted output for the CLI interface.

Author: Hadar Wayn
Date: December 2025
"""

from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TextColumn
from typing import List

console = Console()


def print_header(text: str) -> None:
    """Print formatted header"""
    console.print(f"\n[bold cyan]{text}[/bold cyan]\n")


def print_success(text: str) -> None:
    """Print success message"""
    console.print(f"[green][+] {text}[/green]")


def print_error(text: str) -> None:
    """Print error message"""
    console.print(f"[red][!] {text}[/red]")


def print_warning(text: str) -> None:
    """Print warning message"""
    console.print(f"[yellow][!] {text}[/yellow]")


def print_info(text: str) -> None:
    """Print info message"""
    console.print(f"[blue][*] {text}[/blue]")


def display_banner() -> None:
    """Display application banner"""
    banner = """
[bold cyan]=====================================================================[/bold cyan]
[bold cyan]      AI AGENTS AUTO HOMEWORK GRADING SYSTEM                        [/bold cyan]
[bold cyan]              Claude Code Agents Architecture                        [/bold cyan]
[bold cyan]=====================================================================[/bold cyan]
"""
    console.print(banner)


def display_table(title: str, headers: List[str], rows: List[List[str]]) -> None:
    """Display formatted table"""
    table = Table(title=title)

    for header in headers:
        table.add_column(header, style="cyan")

    for row in rows:
        table.add_row(*[str(cell) for cell in row])

    console.print(table)


def display_panel(content: str, title: str = "", style: str = "cyan") -> None:
    """Display content in a panel"""
    panel = Panel(content, title=title, border_style=style)
    console.print(panel)
