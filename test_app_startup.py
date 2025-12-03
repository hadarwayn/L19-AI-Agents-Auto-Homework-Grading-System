"""
Test Application Startup
Verifies that all imports work and the application can initialize
"""

import sys
from pathlib import Path

# Set UTF-8 encoding for Windows console
if sys.platform == 'win32':
    import codecs
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')
    sys.stderr = codecs.getwriter('utf-8')(sys.stderr.buffer, 'strict')

print("Testing application startup...\n")

# Test imports
print("1. Testing imports...")
try:
    from src.ui.display import display_banner, print_success, print_error, print_info
    print("   ✓ UI display imports successful")
except Exception as e:
    print(f"   ✗ UI display imports failed: {e}")
    sys.exit(1)

try:
    from src.ui.menu import display_main_menu, show_agent1_info, confirm_reset
    print("   ✓ UI menu imports successful")
except Exception as e:
    print(f"   ✗ UI menu imports failed: {e}")
    sys.exit(1)

try:
    from src.ui.agent_runner import run_agent, run_all_agents
    print("   ✓ Agent runner imports successful")
except Exception as e:
    print(f"   ✗ Agent runner imports failed: {e}")
    sys.exit(1)

try:
    from src.utils.paths import ensure_directories, get_claude_agents_dir
    print("   ✓ Utils imports successful")
except Exception as e:
    print(f"   ✗ Utils imports failed: {e}")
    sys.exit(1)

# Test directory creation
print("\n2. Testing directory initialization...")
try:
    ensure_directories()
    print("   ✓ Directories created/verified")
except Exception as e:
    print(f"   ✗ Directory creation failed: {e}")
    sys.exit(1)

# Test agent files existence
print("\n3. Checking Claude Code agent files...")
agents_dir = get_claude_agents_dir()
agents = [
    "Agent1_Email_Extractor",
    "Agent2_Repository_Analyzer",
    "Agent3_LLM_Feedback",
    "Agent4_Draft_Creator"
]

all_found = True
for agent in agents:
    skill_file = agents_dir / agent / "SKILL.md"
    if skill_file.exists():
        print(f"   ✓ {agent}/SKILL.md found")
    else:
        print(f"   ✗ {agent}/SKILL.md NOT FOUND")
        all_found = False

# Check persona skills
print("\n4. Checking persona skill files...")
personas = ["trump_skill.md", "hason_skill.md", "lee_skill.md", "amsalem_skill.md"]
personas_dir = agents_dir / "Agent3_LLM_Feedback" / "personas"

for persona in personas:
    persona_file = personas_dir / persona
    if persona_file.exists():
        print(f"   ✓ {persona} found")
    else:
        print(f"   ✗ {persona} NOT FOUND")
        all_found = False

# Test banner display
print("\n5. Testing UI components...")
try:
    display_banner()
    print("\n   ✓ Banner displayed successfully")
except Exception as e:
    print(f"   ✗ Banner display failed: {e}")
    sys.exit(1)

# Final result
if all_found:
    print("\n✅ All startup tests passed!")
    print("   The application is ready to run.\n")
    sys.exit(0)
else:
    print("\n⚠ Some agent files are missing!")
    sys.exit(1)
