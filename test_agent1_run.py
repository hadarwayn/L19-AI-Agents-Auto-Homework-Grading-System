"""
Test Agent 1 execution through the UI system
"""
from src.ui.display import print_header, print_success, print_info
from src.utils.paths import ensure_directories

# Ensure directories exist
ensure_directories()

# Display header
print_header("Testing Agent 1 - Email Extractor")

# Simulate collected parameters (what would come from UI prompts)
agent_params = {
    'email_subject': 'AI Development Expert course - Homework - L',
    'sender_email': None,
    'max_emails': 10,
    'query': 'subject:{AI Development Expert course - Homework - L}'
}

print_info(f"Email Subject: {agent_params['email_subject']}")
print_info(f"Sender Email: (all senders)")
print_info(f"Max Emails: {agent_params['max_emails']}")
print_info(f"Gmail Query: {agent_params['query']}")

print("\n[*] Running Agent 1 extraction...")

# Run the actual extraction code
import subprocess
result = subprocess.run(['python', 'temp/run_agent1.py'], capture_output=True, text=True)

print(result.stdout)
if result.stderr:
    print("[!] Errors:", result.stderr)

if result.returncode == 0:
    print_success("Agent 1 completed successfully")
else:
    print(f"[!] Agent 1 failed with return code {result.returncode}")
