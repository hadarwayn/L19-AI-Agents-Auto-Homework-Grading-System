"""
Direct execution of Agent 2 - Repository Analyzer
"""
from src.ui.agent_runner import _execute_agent2
from src.ui.display import print_header, print_success, print_error, console
from src.utils.paths import ensure_directories

# Ensure directories exist
ensure_directories()

# Display header
print_header("Running Agent 2 - Repository Analyzer")

# Execute Agent 2
console.print("[bold green][*] Executing Agent 2...[/bold green]\n")
success = _execute_agent2()

if success:
    print_success("Agent 2 completed successfully")
else:
    print_error("Agent 2 execution failed")
