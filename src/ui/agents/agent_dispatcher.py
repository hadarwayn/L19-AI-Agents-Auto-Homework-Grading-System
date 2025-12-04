"""
Agent Dispatcher - Main Entry Points

Provides unified interface for running individual agents or the full pipeline.

Author: Hadar Wayn
Date: December 2025
"""

from pathlib import Path
from rich.console import Console

from .agent1_params import prompt_agent1_parameters
from .agent1_executor import execute_agent1
from .agent2_executor import execute_agent2
from .agent3_executor import execute_agent3
from .agent4_executor import execute_agent4
from ...utils.paths import get_excel_file

console = Console()


def run_agent(agent_number: int, params: dict = None) -> bool:
    """
    Run a single agent

    Args:
        agent_number: Agent number (1-4)
        params: Optional parameters (required for Agent 1)

    Returns:
        bool: True if successful, False otherwise
    """
    console.print(f"\n[bold cyan]{'='*70}[/bold cyan]")
    console.print(f"[bold cyan]RUNNING AGENT {agent_number}[/bold cyan]")
    console.print(f"[bold cyan]{'='*70}[/bold cyan]\n")

    if agent_number == 1:
        if params is None:
            params = prompt_agent1_parameters()
        return execute_agent1(params)
    elif agent_number == 2:
        return execute_agent2()
    elif agent_number == 3:
        return execute_agent3()
    elif agent_number == 4:
        return execute_agent4()
    else:
        console.print(f"[red][!] Invalid agent number: {agent_number}[/red]\n")
        return False


def run_all_agents(params: dict = None) -> bool:
    """
    Run all 4 agents in sequence

    Args:
        params: Optional parameters for Agent 1

    Returns:
        bool: True if all agents succeeded, False otherwise
    """
    console.print("\n[bold green]" + "="*70 + "[/bold green]")
    console.print("[bold green]STARTING FULL PIPELINE (4 AGENTS)[/bold green]")
    console.print("[bold green]" + "="*70 + "[/bold green]\n")

    # Agent 1: Email Extraction
    if params is None:
        params = prompt_agent1_parameters()

    if not run_agent(1, params):
        console.print("[red][!] Pipeline stopped: Agent 1 failed[/red]\n")
        return False

    # Agent 2: Repository Analysis
    if not run_agent(2):
        console.print("[red][!] Pipeline stopped: Agent 2 failed[/red]\n")
        return False

    # Agent 3: LLM Feedback Generation
    if not run_agent(3):
        console.print("[red][!] Pipeline stopped: Agent 3 failed[/red]\n")
        return False

    # Agent 4: Draft Email Creation
    if not run_agent(4):
        console.print("[red][!] Pipeline stopped: Agent 4 failed[/red]\n")
        return False

    console.print("\n[bold green]" + "="*70 + "[/bold green]")
    console.print("[bold green]PIPELINE COMPLETED SUCCESSFULLY![/bold green]")
    console.print("[bold green]" + "="*70 + "[/bold green]\n")

    return True


def verify_agent_output(agent_number: int) -> bool:
    """
    Verify that an agent's output file exists

    Args:
        agent_number: Agent number (1-4)

    Returns:
        bool: True if output file exists, False otherwise
    """
    output_files = {
        1: 'Excel1.xlsx',
        2: 'Excel2.xlsx',
        3: 'Excel3.xlsx',
        4: None  # Agent 4 creates Gmail drafts, not files
    }

    if agent_number not in output_files:
        console.print(f"[red][!] Invalid agent number: {agent_number}[/red]")
        return False

    if agent_number == 4:
        console.print("[*] Agent 4 creates Gmail drafts (no file output)")
        return True

    output_file = output_files[agent_number]
    file_path = get_excel_file(output_file)

    if file_path.exists():
        console.print(f"[+] {output_file} exists: {file_path}")
        return True
    else:
        console.print(f"[!] {output_file} not found: {file_path}")
        return False


def get_agent_status() -> dict:
    """
    Get status of all agent output files

    Returns:
        dict: Status of each agent's output
    """
    return {
        'agent1': verify_agent_output(1),
        'agent2': verify_agent_output(2),
        'agent3': verify_agent_output(3),
        'agent4': True  # Agent 4 always returns True (drafts in Gmail)
    }
