"""
Direct execution of Agent 3 - LLM Feedback Generator
"""
from src.ui.agent_runner import _execute_agent3
from src.ui.display import print_header, print_success, print_error, console
from src.utils.paths import ensure_directories

# Ensure directories exist
ensure_directories()

# Display header
print_header("Running Agent 3 - LLM Feedback Generator")

# Execute Agent 3
console.print("[bold green][*] Executing Agent 3...[/bold green]\n")
success = _execute_agent3()

if success:
    print_success("Agent 3 completed successfully")
else:
    print_error("Agent 3 execution failed")
