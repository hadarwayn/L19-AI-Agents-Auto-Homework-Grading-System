"""
Direct execution of Agent 1 with specified parameters
"""
from src.ui.agent_runner import _prompt_agent1_parameters, _execute_agent1
from src.ui.display import print_header, print_success, print_error, console
from src.utils.paths import ensure_directories

# Ensure directories exist
ensure_directories()

# Display header
print_header("Running Agent 1 - Email Extractor")

# Use specified parameters (simulating user input)
agent_params = {
    'email_subject': 'AI Development Expert course - Homework - L',
    'sender_email': None,
    'max_emails': 10,
    'query': 'subject:{AI Development Expert course - Homework - L}'
}

console.print(f"\n[bold]Search Parameters:[/bold]")
console.print(f"  Email Subject: {agent_params['email_subject']}")
console.print(f"  Sender Email: (all senders)")
console.print(f"  Max Emails: {agent_params['max_emails']}")
console.print(f"  Gmail Query: [cyan]{agent_params['query']}[/cyan]\n")

# Execute Agent 1
console.print("[bold green][*] Executing Agent 1...[/bold green]\n")
success = _execute_agent1(agent_params)

if success:
    print_success("Agent 1 completed successfully")
else:
    print_error("Agent 1 execution failed")
