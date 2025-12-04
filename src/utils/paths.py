"""
Path Management Utilities

Provides centralized path management using pathlib.Path for cross-platform compatibility.
All paths are relative to the project root.

Author: Hadar Wayn
Date: December 2025
"""

from pathlib import Path
from typing import Union


def get_project_root() -> Path:
    """Get the project root directory"""
    return Path(__file__).parent.parent.parent


def get_src_dir() -> Path:
    """Get src/ directory"""
    return get_project_root() / "src"


def get_results_dir() -> Path:
    """Get results/ directory"""
    return get_project_root() / "results"


def get_excel_dir() -> Path:
    """Get results/excel/ directory for Excel files"""
    return get_results_dir() / "excel"


def get_graphs_dir() -> Path:
    """Get results/graphs/ directory for visualizations"""
    return get_results_dir() / "graphs"


def get_examples_dir() -> Path:
    """Get results/examples/ directory for example outputs"""
    return get_results_dir() / "examples"


def get_logs_dir() -> Path:
    """Get logs/ directory"""
    return get_project_root() / "logs"


def get_log_config_dir() -> Path:
    """Get logs/config/ directory"""
    return get_logs_dir() / "config"


def get_temp_dir() -> Path:
    """Get temp/ directory"""
    return get_project_root() / "temp"


def get_repos_dir() -> Path:
    """Get temp/repos/ directory for cloned repositories"""
    return get_temp_dir() / "repos"


def get_secrets_dir() -> Path:
    """Get Secrets/ directory"""
    return get_project_root() / "Secrets"


def get_data_dir() -> Path:
    """Get data/ directory"""
    return get_project_root() / "data"


def get_config_dir() -> Path:
    """Get config/ directory"""
    return get_project_root() / "config"


def get_claude_agents_dir() -> Path:
    """Get .claude/agents/ directory"""
    return get_project_root() / ".claude" / "agents"


def ensure_directories() -> None:
    """Ensure all required directories exist"""
    directories = [
        get_results_dir(),
        get_excel_dir(),
        get_graphs_dir(),
        get_examples_dir(),
        get_logs_dir(),
        get_log_config_dir(),
        get_temp_dir(),
        get_repos_dir(),
        get_secrets_dir(),
        get_data_dir(),
        get_config_dir(),
        get_claude_agents_dir(),
    ]

    for directory in directories:
        directory.mkdir(parents=True, exist_ok=True)


def get_excel_file(filename: str) -> Path:
    """Get path to Excel file in results/excel/"""
    return get_excel_dir() / filename


def get_config_file(filename: str) -> Path:
    """Get path to configuration file"""
    return get_config_dir() / filename


def get_log_file(filename: str) -> Path:
    """Get path to log file"""
    return get_logs_dir() / filename


def clean_temp_repos() -> None:
    """Clean all cloned repositories from temp/repos/"""
    repos_dir = get_repos_dir()
    if repos_dir.exists():
        for item in repos_dir.iterdir():
            if item.is_dir():
                import shutil
                shutil.rmtree(item)
