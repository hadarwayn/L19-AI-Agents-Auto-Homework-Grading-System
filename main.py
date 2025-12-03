"""
L19 AI Agents Auto Homework Grading System
Main Entry Point

Provides interactive menu for running Claude Code agents:
- Agent 1: Email Extractor (prompts for search parameters)
- Agent 2: Repository Analyzer
- Agent 3: LLM Feedback Generator
- Agent 4: Draft Email Creator

Author: Hadar Wayn
Date: December 2025
"""

import sys
from pathlib import Path

from src.ui.display import display_banner, print_success, print_error, print_info, print_warning, console
from src.ui.menu import display_main_menu, confirm_reset
from src.ui.agent_runner import run_agent, run_all_agents
from src.utils.paths import ensure_directories, clean_temp_repos, get_excel_dir
from src.utils.logger import setup_logger

# Initialize logger
logger = setup_logger("main")


def reset_system() -> None:
    """
    Reset system by cleaning temporary files and repos
    """
    print_info("Resetting system...")

    # Clean cloned repositories
    clean_temp_repos()
    print_success("✓ Cleaned cloned repositories")

    # Remove generated Excel files
    excel_dir = get_excel_dir()
    if excel_dir.exists():
        for excel_file in excel_dir.glob("*.xlsx"):
            try:
                excel_file.unlink()
                print_success(f"✓ Removed {excel_file.name}")
            except Exception as e:
                print_error(f"Failed to remove {excel_file.name}: {e}")

    print_success("🔄 System reset complete!")


def display_status() -> None:
    """
    Display current system status
    """
    from src.utils.paths import get_excel_dir, get_repos_dir, get_logs_dir

    excel_dir = get_excel_dir()
    repos_dir = get_repos_dir()
    logs_dir = get_logs_dir()

    console.print("\n[bold cyan]📊 System Status[/bold cyan]\n")

    # Check Excel files
    excel_files = list(excel_dir.glob("*.xlsx")) if excel_dir.exists() else []
    console.print(f"[yellow]Excel Files:[/yellow] {len(excel_files)}")
    for f in excel_files:
        console.print(f"  • {f.name}")

    # Check cloned repos
    repos = list(repos_dir.glob("*")) if repos_dir.exists() else []
    console.print(f"\n[yellow]Cloned Repositories:[/yellow] {len(repos)}")

    # Check log files
    log_files = list(logs_dir.glob("*.log")) if logs_dir.exists() else []
    console.print(f"\n[yellow]Log Files:[/yellow] {len(log_files)}")
    for f in log_files:
        size_kb = f.stat().st_size / 1024
        console.print(f"  • {f.name} ({size_kb:.1f} KB)")

    console.print()


def main():
    """
    Main application entry point
    """
    try:
        # Ensure all required directories exist
        ensure_directories()

        # Display banner
        display_banner()
        console.print("\n[dim]Starting AI Agents Auto Homework Grading System...[/dim]\n")
        console.input("[dim]Press Enter to continue...[/dim]")

        # Main menu loop
        while True:
            choice = display_main_menu()

            if choice == 1:
                # Run Agent 1 - Email Extractor
                logger.info("User selected: Run Agent 1")
                run_agent("Agent1_Email_Extractor")

            elif choice == 2:
                # Run Agent 2 - Repository Analyzer
                logger.info("User selected: Run Agent 2")
                run_agent("Agent2_Repository_Analyzer")

            elif choice == 3:
                # Run Agent 3 - LLM Feedback Generator
                logger.info("User selected: Run Agent 3")
                run_agent("Agent3_LLM_Feedback")

            elif choice == 4:
                # Run Agent 4 - Draft Creator
                logger.info("User selected: Run Agent 4")
                run_agent("Agent4_Draft_Creator")

            elif choice == 5:
                # Run All Agents Sequentially
                logger.info("User selected: Run All Agents")
                print_info("Running all agents sequentially...")
                success = run_all_agents()
                if success:
                    print_success("\n🎉 All agents completed successfully!")
                else:
                    print_error("\n❌ Agent pipeline failed. Check logs for details.")

            elif choice == 6:
                # Reset System
                logger.info("User selected: Reset System")
                if confirm_reset():
                    reset_system()
                else:
                    print_info("Reset cancelled.")

            elif choice == 7:
                # Display Status
                logger.info("User selected: Display Status")
                display_status()
                console.input("\n[dim]Press Enter to continue...[/dim]")

            elif choice == 8:
                # Exit
                logger.info("User selected: Exit")
                print_info("Goodbye! 👋")
                return 0

            else:
                print_error("Invalid choice. Please try again.")

    except KeyboardInterrupt:
        print_warning("\n\n⚠ Interrupted by user")
        logger.warning("Application interrupted by user (Ctrl+C)")
        return 1

    except Exception as e:
        print_error(f"Unexpected error: {e}")
        logger.exception("Unexpected error in main application")
        return 1


if __name__ == "__main__":
    sys.exit(main())
