"""
Test script for new modular agent structure

Tests that all agents can be imported and executed correctly.

Author: Hadar Wayn
Date: December 2025
"""

import sys
from pathlib import Path

# Add project root to path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from rich.console import Console
from src.ui.agents import run_agent, run_all_agents, verify_agent_output, get_agent_status

console = Console()


def test_imports():
    """Test that all agent modules can be imported"""
    console.print("\n[bold cyan]Testing Agent Module Imports...[/bold cyan]")

    try:
        from src.ui.agents.agent1_params import prompt_agent1_parameters
        from src.ui.agents.agent1_email_parser import extract_email_data
        from src.ui.agents.agent1_executor import execute_agent1
        console.print("[+] Agent 1 modules imported successfully")

        from src.ui.agents.agent2_repo_analyzer import analyze_repository
        from src.ui.agents.agent2_executor import execute_agent2
        console.print("[+] Agent 2 modules imported successfully")

        from src.ui.agents.agent3_feedback_generator import generate_feedback
        from src.ui.agents.agent3_executor import execute_agent3
        console.print("[+] Agent 3 modules imported successfully")

        from src.ui.agents.agent4_executor import execute_agent4
        console.print("[+] Agent 4 module imported successfully")

        from src.ui.agents.gmail_auth import get_gmail_service
        from src.ui.agents.excel_utils import create_excel_workbook, auto_adjust_columns
        console.print("[+] Shared utility modules imported successfully")

        return True
    except ImportError as e:
        console.print(f"[red][!] Import failed: {e}[/red]")
        return False


def test_dispatcher_functions():
    """Test that dispatcher functions are accessible"""
    console.print("\n[bold cyan]Testing Agent Dispatcher Functions...[/bold cyan]")

    try:
        # Check that functions are callable
        assert callable(run_agent), "run_agent is not callable"
        console.print("[+] run_agent function accessible")

        assert callable(run_all_agents), "run_all_agents is not callable"
        console.print("[+] run_all_agents function accessible")

        assert callable(verify_agent_output), "verify_agent_output is not callable"
        console.print("[+] verify_agent_output function accessible")

        assert callable(get_agent_status), "get_agent_status is not callable"
        console.print("[+] get_agent_status function accessible")

        return True
    except AssertionError as e:
        console.print(f"[red][!] Dispatcher test failed: {e}[/red]")
        return False


def test_agent_status():
    """Test get_agent_status function"""
    console.print("\n[bold cyan]Testing Agent Status Check...[/bold cyan]")

    try:
        status = get_agent_status()
        console.print(f"[+] Agent status retrieved:")
        console.print(f"    - Agent 1 (Excel1.xlsx): {status['agent1']}")
        console.print(f"    - Agent 2 (Excel2.xlsx): {status['agent2']}")
        console.print(f"    - Agent 3 (Excel3.xlsx): {status['agent3']}")
        console.print(f"    - Agent 4 (Gmail drafts): {status['agent4']}")

        return True
    except Exception as e:
        console.print(f"[red][!] Status check failed: {e}[/red]")
        return False


def check_file_line_counts():
    """Verify all agent files are under 150 lines"""
    console.print("\n[bold cyan]Checking File Line Counts (PROJECT_GUIDELINES.md compliance)...[/bold cyan]")

    agent_files = [
        "src/ui/agents/__init__.py",
        "src/ui/agents/agent_dispatcher.py",
        "src/ui/agents/gmail_auth.py",
        "src/ui/agents/excel_utils.py",
        "src/ui/agents/agent1_params.py",
        "src/ui/agents/agent1_email_parser.py",
        "src/ui/agents/agent1_executor.py",
        "src/ui/agents/agent2_repo_analyzer.py",
        "src/ui/agents/agent2_executor.py",
        "src/ui/agents/agent3_feedback_generator.py",
        "src/ui/agents/agent3_executor.py",
        "src/ui/agents/agent4_executor.py",
    ]

    all_compliant = True

    for file_path in agent_files:
        full_path = project_root / file_path
        if full_path.exists():
            with open(full_path, 'r', encoding='utf-8') as f:
                line_count = len(f.readlines())

            status = "[green]OK[/green]" if line_count <= 150 else "[red]FAIL[/red]"
            console.print(f"{status} {file_path}: {line_count} lines")

            if line_count > 150:
                all_compliant = False
        else:
            console.print(f"[yellow]![/yellow] {file_path}: NOT FOUND")
            all_compliant = False

    return all_compliant


def main():
    """Run all tests"""
    console.print("\n" + "="*70)
    console.print("[bold]MODULAR AGENT STRUCTURE TESTS[/bold]")
    console.print("="*70)

    results = {
        "Imports": test_imports(),
        "Dispatcher Functions": test_dispatcher_functions(),
        "Agent Status": test_agent_status(),
        "File Line Counts": check_file_line_counts()
    }

    console.print("\n" + "="*70)
    console.print("[bold]TEST SUMMARY[/bold]")
    console.print("="*70)

    for test_name, passed in results.items():
        status = "[green]PASSED[/green]" if passed else "[red]FAILED[/red]"
        console.print(f"{status} - {test_name}")

    all_passed = all(results.values())

    if all_passed:
        console.print("\n[bold green]All tests passed![/bold green]")
    else:
        console.print("\n[bold red]Some tests failed![/bold red]")

    console.print("="*70 + "\n")

    return 0 if all_passed else 1


if __name__ == "__main__":
    sys.exit(main())
