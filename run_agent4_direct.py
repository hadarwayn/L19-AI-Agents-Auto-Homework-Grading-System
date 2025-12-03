"""
Direct execution of Agent 4 - Draft Email Creator
"""
from src.ui.agent_runner import _execute_agent4
from src.ui.display import print_header, print_success, print_error, console
from src.utils.paths import ensure_directories

# Ensure directories exist
ensure_directories()

# Display header
print_header("Running Agent 4 - Draft Email Creator")

# Execute Agent 4
console.print("[bold green][*] Executing Agent 4...[/bold green]\n")
success = _execute_agent4()

if success:
    print_success("Agent 4 completed successfully")
else:
    print_error("Agent 4 execution failed")
