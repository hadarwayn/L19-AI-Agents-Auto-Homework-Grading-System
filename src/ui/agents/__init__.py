"""
Agents Package - Modular agent execution system

This package contains the agent execution logic split into
focused modules per PROJECT_GUIDELINES.md (max 150 lines per file).

Public API:
    - run_agent(agent_name) -> bool
    - run_all_agents() -> bool

Author: Hadar Wayn
Date: December 2025
"""

from .agent_dispatcher import run_agent, run_all_agents, verify_agent_output, get_agent_status

__all__ = [
    'run_agent',
    'run_all_agents',
    'verify_agent_output',
    'get_agent_status'
]
