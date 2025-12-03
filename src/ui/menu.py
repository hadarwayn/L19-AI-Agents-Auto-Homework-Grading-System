"""
Menu System - Main workflow menu

Author: Hadar Wayn
Date: December 2025
"""

from .display import console, display_banner, print_error, print_success, print_info


def display_main_menu() -> int:
    """
    Display main workflow menu

    Returns:
        int: User's menu choice (1-8)
    """
    console.clear()
    display_banner()

    menu = """
[bold cyan]=====================================================================[/bold cyan]
[bold cyan]                      MAIN MENU                                    [/bold cyan]
[bold cyan]=====================================================================[/bold cyan]

[bold cyan]   [1] Run Agent 1 - Email Extractor                              [/bold cyan]
[bold cyan]   [2] Run Agent 2 - Repository Analyzer                          [/bold cyan]
[bold cyan]   [3] Run Agent 3 - LLM Feedback Generator                       [/bold cyan]
[bold cyan]   [4] Run Agent 4 - Draft Creator                                [/bold cyan]
[bold cyan]   [5] Run All Agents Sequentially                                [/bold cyan]
[bold cyan]   [6] Reset System                                                [/bold cyan]
[bold cyan]   [7] System Status                                               [/bold cyan]
[bold cyan]   [8] Exit                                                        [/bold cyan]

[bold cyan]=====================================================================[/bold cyan]

[dim]Note: Agent 1 will prompt for search parameters (subject, sender, max emails)[/dim]
"""
    console.print(menu)

    while True:
        choice = console.input("\n[bold yellow]Enter choice (1-8): [/bold yellow]").strip()

        try:
            choice_int = int(choice)
            if 1 <= choice_int <= 8:
                return choice_int
            else:
                print_error("Invalid choice. Please select 1-8.")
        except ValueError:
            print_error("Invalid input. Please enter a number.")


def show_agent1_info() -> None:
    """
    Display information about Agent 1 parameters
    """
    console.print("\n[bold cyan]=====================================================================[/bold cyan]")
    console.print("[bold cyan]              AGENT 1: EMAIL EXTRACTION PARAMETERS                [/bold cyan]")
    console.print("[bold cyan]=====================================================================[/bold cyan]")
    console.print("")
    console.print("  Agent 1 will prompt you for:")
    console.print("")
    console.print("  [bold]Email Subject[/bold] (optional)")
    console.print("     - Partial subject match (case-insensitive)")
    console.print("     - Press Enter to search all subjects")
    console.print("")
    console.print("  [bold]Sender Email[/bold] (optional)")
    console.print("     - Filter by sender's email address")
    console.print("     - Press Enter to search all senders")
    console.print("")
    console.print("  [bold]Max Emails[/bold] (required)")
    console.print("     - Range: 1-100")
    console.print("     - Default: 10 (press Enter)")
    console.print("")
    console.print("[bold cyan]=====================================================================[/bold cyan]\n")


def confirm_reset() -> bool:
    """
    Confirm system reset with user

    Returns:
        bool: True if user confirms, False otherwise
    """
    console.print("\n[bold red][!] WARNING: SYSTEM RESET[/bold red]\n")
    console.print("[yellow]This will delete:[/yellow]")
    console.print("  - All generated Excel files (Excel1-4.xlsx)")
    console.print("  - All cloned repositories")
    console.print("  - Log files")
    console.print()

    confirmation = console.input("[bold red]Type 'yes' to confirm reset: [/bold red]").strip().lower()

    return confirmation == "yes"
