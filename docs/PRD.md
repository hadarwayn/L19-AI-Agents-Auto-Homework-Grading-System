# PRD.md - Product Requirements Document
# L19: AI Agents Auto Homework Grading System

**Version:** 3.2
**Created:** December 2025
**Author:** Hadar Wayn (AI Developer Expert Course Student)
**Status:** Awaiting Approval
**Last Updated:** December 3, 2025

---

## 📋 Table of Contents

1. [Executive Summary](#executive-summary)
2. [Project Overview](#project-overview)
3. [System Architecture](#system-architecture)
4. [Functional Requirements](#functional-requirements)
5. [Technical Specifications](#technical-specifications)
6. [Data Models](#data-models)
7. [API Integrations](#api-integrations)
8. [Security & Authentication](#security--authentication)
9. [Error Handling & Logging](#error-handling--logging)
10. [Performance Requirements](#performance-requirements)
11. [Testing Strategy](#testing-strategy)
12. [Configuration Management](#configuration-management)
13. [Future Enhancements](#future-enhancements)

---

## Executive Summary

The **AI Agents Auto Homework Grading System** is a comprehensive multi-agent Python package that automates the entire workflow of processing student homework submissions. The system connects to Gmail, extracts GitHub repository URLs from student emails, clones and analyzes code quality, generates personalized AI-powered feedback using different celebrity personas based on grade ranges, and creates draft email responses.

### Key Features

- ✅ **4-Agent Sequential Pipeline**: Email extraction → Repository analysis → LLM feedback → Draft creation
- ✅ **Gmail API Integration**: OAuth2 authentication, email search, draft creation
- ✅ **Multi-threaded Repository Cloning**: 5 concurrent workers for parallel processing
- ✅ **Line Count Grading Algorithm**: Grade based on files under 150 lines compliance
- ✅ **AI-Powered Personalized Feedback**: 4 celebrity persona styles (Trump, Shahar Hason, Bruce Lee, Dudi Amsalem)
- ✅ **Excel-Based Data Tracking**: Each agent produces its own Excel file for complete audit trail
- ✅ **Rich CLI Interface**: Color-coded interactive menu with progress indicators
- ✅ **Flexible Email Search**: User-defined subject, sender, and email count (1-100)
- ✅ **Graceful Error Handling**: Retry logic with configurable delays, status-based progression
- ✅ **System Reset**: One-click cleanup of all generated data

---

## Project Overview

### Purpose

Automate the workflow of receiving, grading, and responding to student homework submissions submitted via GitHub repository links sent through email.

### Target Users

- **Educators/Instructors**: Managing programming courses with code submissions
- **Teaching Assistants**: Handling code reviews at scale
- **Academic Institutions**: GitHub-based homework submission workflows

### Business Objectives

- **Automate grading workflow**: Reduce manual effort by 80%+
- **Consistent evaluation**: Apply uniform grading criteria
- **Timely feedback**: Generate personalized responses within minutes
- **Scalability**: Handle multiple concurrent submissions using multi-threading
- **Complete audit trail**: Maintain comprehensive logs and Excel data tracking
- **User control**: Granular control over agent execution and system reset

### Success Criteria

- [ ] Process 100% of submissions within 5 minutes of receipt
- [ ] Maintain 99% uptime for the agent system
- [ ] Generate contextually relevant feedback for each grade tier
- [ ] Zero data loss in storage and logging systems
- [ ] 100% success rate after retry mechanism for API failures

---

## System Architecture

### High-Level Architecture

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    AI AGENTS AUTO HOMEWORK GRADING SYSTEM               │
│                      (Claude Code Agent Framework)                      │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│                         ┌─────────────────────┐                         │
│                         │   Gmail Inbox       │                         │
│                         │  (Homework Emails)  │                         │
│                         └──────────┬──────────┘                         │
│                                    │                                    │
│                                    ▼                                    │
│  ┌─────────────────────────────────────────────────────────────────┐   │
│  │            CLAUDE CODE AGENT 1: Email Extractor                  │   │
│  │  • Skill: .claude/agents/Agent1_Email_Extractor/SKILL.md        │   │
│  │  • Gmail API Integration                                        │   │
│  │  • Regex-based URL Extraction                                   │   │
│  │  • SHA-256 Email ID Generation                                  │   │
│  │  • Output: Excel1.xlsx                                          │   │
│  └──────────────────────────────┬──────────────────────────────────┘   │
│                                 │                                       │
│                                 ▼                                       │
│  ┌─────────────────────────────────────────────────────────────────┐   │
│  │       CLAUDE CODE AGENT 2: Repository Analyzer                   │   │
│  │  • Skill: .claude/agents/Agent2_Repository_Analyzer/SKILL.md    │   │
│  │  • GitHub Repository Cloning (5 concurrent workers)             │   │
│  │  • Python File Detection & Line Counting                        │   │
│  │  • Grade Calculation (150-line compliance)                      │   │
│  │  • Output: Excel2.xlsx                                          │   │
│  └──────────────────────────────┬──────────────────────────────────┘   │
│                                 │                                       │
│                                 ▼                                       │
│  ┌─────────────────────────────────────────────────────────────────┐   │
│  │        CLAUDE CODE AGENT 3: LLM Feedback Generator               │   │
│  │  • Skill: .claude/agents/Agent3_LLM_Feedback/SKILL.md           │   │
│  │  • Sub-Skills (Personas):                                       │   │
│  │    - personas/trump_skill.md (90-100 grade)                     │   │
│  │    - personas/hason_skill.md (70-90 grade)                      │   │
│  │    - personas/lee_skill.md (55-70 grade)                        │   │
│  │    - personas/amsalem_skill.md (0-55 grade)                     │   │
│  │  • Gemini API Integration                                       │   │
│  │  • Grade-Based Persona Selection                                │   │
│  │  • Retry Logic with Exponential Backoff                         │   │
│  │  • Output: Excel3.xlsx                                          │   │
│  └──────────────────────────────┬──────────────────────────────────┘   │
│                                 │                                       │
│                                 ▼                                       │
│  ┌─────────────────────────────────────────────────────────────────┐   │
│  │          CLAUDE CODE AGENT 4: Draft Email Creator                │   │
│  │  • Skill: .claude/agents/Agent4_Draft_Creator/SKILL.md          │   │
│  │  • Gmail Draft API                                              │   │
│  │  • Student Name Mapping                                         │   │
│  │  • Personalized Email Composition                               │   │
│  │  • Creates Drafts (NOT sends)                                   │   │
│  └─────────────────────────────────────────────────────────────────┘   │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

### Data Flow Between Agents

```
Gmail API ──▶ [Agent 1] ──▶ Excel1.xlsx ──▶ [Agent 2] ──▶ Excel2.xlsx
                                                              │
                                                              ▼
Gmail Drafts ◀── [Agent 4] ◀── Excel3.xlsx ◀── [Agent 3] ◀───┘
```

### Agent Communication

- **Sequential Processing**: Each agent completes before the next begins
- **Excel as Data Layer**: Excel files serve as shared data storage
- **Status-Based Progression**: Only rows with `status = "Ready"` proceed to next agent
- **Error Isolation**: Failed rows don't block other submissions

### Dual Execution Mode Architecture

**This system supports TWO ways to run agents:**

#### **Mode 1: Manual Execution (Development/Testing)**
```bash
cd /mnt/c/2025AIDEV/L19
claude              # Start Claude Code interactive session
/agents             # List all available agents with descriptions
# Select agent from the list
# Claude Code reads SKILL.md and executes instructions
# Agent completes and creates output files
```

**Use Cases:**
- ✅ Testing individual agents during development
- ✅ Debugging agent logic
- ✅ Running single agent without full workflow
- ✅ Experimenting with agent parameters

---

#### **Mode 2: Automated Execution (Production Workflow)**
```bash
cd /mnt/c/2025AIDEV/L19
python main.py      # Rich UI menu appears
# Select option from menu (1-9)
# Python invokes Claude Code agent via subprocess/CLI
# Results displayed in Rich UI with progress
# Can run "All Agents" sequentially
```

**Use Cases:**
- ✅ Production workflow automation
- ✅ Running complete end-to-end pipeline
- ✅ Sequential execution with validation
- ✅ Consistent, repeatable processing

---

### How Both Modes Work

**Key Concept:** SKILL.md files are the **single source of truth**

```
┌─────────────────────────────────────────────────────────────┐
│                    SKILL.md Files                           │
│            (Single Source of Truth)                         │
│                                                             │
│  .claude/agents/Agent1_Email_Extractor/SKILL.md           │
│  .claude/agents/Agent2_Repository_Analyzer/SKILL.md       │
│  .claude/agents/Agent3_LLM_Feedback/SKILL.md              │
│  .claude/agents/Agent3_LLM_Feedback/personas/*.md         │
│  .claude/agents/Agent4_Draft_Creator/SKILL.md             │
└─────────────────────────────────────────────────────────────┘
                    ▲                           ▲
                    │                           │
        ┌───────────┘                           └───────────┐
        │                                                   │
┌───────────────────┐                         ┌─────────────────────┐
│  Manual Execution │                         │ Automated Execution │
│                   │                         │                     │
│  claude → /agents │                         │  python main.py     │
│                   │                         │                     │
│  Direct CLI       │                         │  subprocess.run()   │
│  invocation       │                         │  + Rich UI          │
└───────────────────┘                         └─────────────────────┘
```

**Agent Structure:**
```
.claude/
└── agents/
    ├── Agent1_Email_Extractor/
    │   └── SKILL.md              # Complete instructions for email extraction
    ├── Agent2_Repository_Analyzer/
    │   └── SKILL.md              # Multi-threaded repository analysis
    ├── Agent3_LLM_Feedback/
    │   ├── SKILL.md              # Main feedback generation logic
    │   └── personas/
    │       ├── trump_skill.md    # 90-100 grade persona
    │       ├── hason_skill.md    # 70-90 grade persona
    │       ├── lee_skill.md      # 55-70 grade persona
    │       └── amsalem_skill.md  # 0-55 grade persona
    └── Agent4_Draft_Creator/
        └── SKILL.md              # Gmail draft creation
```

**Why Claude Code Agents?**
- **No Python agent code needed**: Skills are markdown instructions
- **Claude executes the tasks**: Using its own tools and capabilities
- **Easier to maintain**: Skills are human-readable instructions
- **Flexible**: Can modify agent behavior by editing SKILL.md
- **Dual execution**: Run manually OR via Python automation
- **Native integration**: Works seamlessly with Claude Code framework

---

## Functional Requirements

### FR-1: Main Workflow Menu

**Description:** Interactive menu for agent execution and system management.

**Menu Display:**
```
╔══════════════════════════════════════════════════════════════════╗
║         🎓 AI AGENTS AUTO HOMEWORK GRADING SYSTEM 🎓             ║
║                      MAIN MENU                                   ║
╠══════════════════════════════════════════════════════════════════╣
║                                                                  ║
║   [1] 📧 Run Agent 1 - Extract Emails from Gmail                ║
║   [2] 📊 Run Agent 2 - Analyze Repositories & Calculate Grades  ║
║   [3] 🤖 Run Agent 3 - Generate AI Feedback with Personas       ║
║   [4] ✉️  Run Agent 4 - Create Gmail Draft Replies              ║
║   [5] 🚀 Run All Agents (1 → 2 → 3 → 4)                         ║
║   [6] 🗑️  Reset - Delete All Generated Files                     ║
║   [7] 📋 System Status                                           ║
║   [8] 🚪 Exit                                                    ║
║                                                                  ║
╚══════════════════════════════════════════════════════════════════╝
```

**Business Rules:**
- Agent 1 prompts for search parameters when selected (subject, sender, max emails)
- Agents 2-4 process data from previous agents
- "Run All" executes sequentially with error handling
- Reset requires user confirmation
- System Status displays current file states and logs

---

### FR-2: Agent 1 - Email Extraction

**Responsibilities:**
- Connect to Gmail API via OAuth2
- Prompt user for search parameters (subject, sender, max emails)
- Search for emails matching user-specified criteria
- Extract GitHub repository URLs from email body
- Generate unique email ID (SHA-256 hash)
- Create Excel1.xlsx with submission data

**User Input Parameters:**

When Agent 1 is executed, the system prompts for:

| Parameter | Type | Required | Default | Range | Description |
|-----------|------|----------|---------|-------|-------------|
| Email Subject | String | ❌ Optional | None | Any text | Partial subject match (case-insensitive). If empty, searches all subjects. |
| Sender Email | String | ❌ Optional | None | Valid email | Filter by sender's email address. If empty, searches all senders. |
| Max Emails | Integer | ✅ Required | 10 | 1-100 | Maximum number of emails to process |

**Prompt UI Example:**
```
╔══════════════════════════════════════════════════════════════════╗
║              AGENT 1: EMAIL EXTRACTION PARAMETERS                ║
╠══════════════════════════════════════════════════════════════════╣
║  📧 Email Subject (optional):                                    ║
║      [Enter partial subject or press Enter to skip]              ║
║                                                                  ║
║  👤 Sender Email (optional):                                     ║
║      [Enter sender email or press Enter to skip]                 ║
║                                                                  ║
║  🔢 Max Emails (1-100):                                          ║
║      [Default: 10]                                               ║
╚══════════════════════════════════════════════════════════════════╝
```

**Search Query Construction:**

```python
# Build Gmail search query based on user input
query_parts = []

# Add subject filter (if provided)
if email_subject:
    # For long phrases (>3 words), use first 3 words for Gmail search
    # Python post-filter ensures exact substring match (case-insensitive)
    words = email_subject.split()
    if len(words) > 3:
        key_words = ' '.join(words[:3])
        query_parts.append(f'subject:{key_words}')
    else:
        query_parts.append(f'subject:{email_subject}')

# Add sender filter (if provided)
if sender_email:
    query_parts.append(f'from:{sender_email}')

# Combine query parts (search all emails if no filters)
query = ' '.join(query_parts) if query_parts else ''

# Example queries:
# User enters: "AI Development Expert course - Homework - L"
# Gmail query: 'subject:AI Development Expert'
# Post-filter: Checks if "AI Development Expert course - Homework - L" is substring
#
# User enters: "awe1"
# Gmail query: 'subject:awe1'
# Post-filter: Checks if "awe1" is substring (matches "rawe1", "awe1r", not "awe")
```

**Email Pattern Recognition:**

```python
# GitHub URL pattern (always applied)
GITHUB_URL_PATTERN = r"https://github\.com/([a-zA-Z0-9_-]+)/([a-zA-Z0-9_.-]+)(\.git)?"

# Note: Subject pattern is now user-defined, not hardcoded
```

**Business Rules:**
- Empty subject = Search all email subjects
- Empty sender = Search all senders
- Max emails cannot exceed 100 (system limit)
- Default max emails = 10 (if user presses Enter)
- Search includes all emails (read and unread, all folders/labels)
- Results sorted by most recent first

**Output (Excel1.xlsx):**

| Column | Type | Description |
|--------|------|-------------|
| email_id | String | SHA-256 hash (primary key) |
| received_time | DateTime | Email receive timestamp |
| email_subject | String | Full subject line |
| sender_email | String | Student's email address |
| github_url | String | Extracted repository URL |
| thread_id | String | Gmail thread ID (required by Agent 4 for reply threading) |
| status | String | "Ready" or "Missing: [field]" |

**Note:** The `thread_id` column is required by Agent 4 to create Gmail drafts as replies to original emails.

---

### FR-3: Agent 2 - Repository Analysis

**Responsibilities:**
- Read Excel1.xlsx (only "Ready" rows)
- Clone repositories using multi-threaded workers (5 concurrent)
- Detect all Python files (.py extension)
- Count lines of code in each file
- Calculate grade based on 150-line compliance rule
- Create Excel2.xlsx with grade data

**Grading Algorithm:**

```python
# Grade Formula (as specified in requirements)
grade = 100 * (lines_in_compliant_files / total_lines)

# Where:
# - compliant_files = files with <= 150 lines
# - total_lines = sum of all lines in all Python files
```

**Example:**
```
Repository contents:
- main.py: 45 lines ✅ (compliant)
- utils.py: 200 lines ❌ (non-compliant)
- helpers.py: 80 lines ✅ (compliant)

Total lines = 45 + 200 + 80 = 325
Compliant lines = 45 + 80 = 125
Grade = 100 × (125 / 325) = 38.46
```

**Output (Excel2.xlsx):**

| Column | Type | Description |
|--------|------|-------------|
| email_id | String | Links to Agent 1 |
| github_url | String | Repository URL |
| total_files | Integer | Count of .py files |
| total_lines | Integer | Sum of all lines |
| compliant_lines | Integer | Lines in files ≤150 |
| grade | Float | 0-100 score |
| analysis_time | Float | Seconds to analyze |
| status | String | "Ready" or error message |

**Multi-threading Specification:**
- **Thread Pool Size**: 5 workers (configurable)
- **Per-Thread Logging**: Each thread maintains individual log
- **Error Isolation**: Thread failures don't affect others
- **Timeout**: 60 seconds per repository clone

---

### FR-4: Agent 3 - LLM Feedback Generation

**Responsibilities:**
- Read Excel2.xlsx (only "Ready" rows)
- Determine grade category and select persona
- Generate AI feedback using Gemini API
- Handle API failures with retry logic
- Create Excel3.xlsx with feedback data

**Grade Categories & Personas:**

| Grade Range | Category | Persona | Style |
|-------------|----------|---------|-------|
| 90-100 | Excellent | Donald Trump | Enthusiastic, superlatives, "tremendous", "fantastic" |
| 70-90 | Good | Shahar Hason | Israeli comedian, witty, humorous observations |
| 55-70 | Pass | Bruce Lee | Martial arts philosophy, wisdom, encouragement |
| 0-55 | Needs Work | Dudi Amsalem | Israeli politician, direct, blunt, firebrand |

**Persona Skills (stored as markdown sub-skills):**

Each persona has its own SKILL.md file in `.claude/agents/Agent3_LLM_Feedback/personas/`:

**trump_skill.md** (90-100 grade):
- Enthusiastic, uses superlatives
- Phrases: "tremendous", "fantastic", "winner", "the best"
- Tone: Celebratory and congratulatory
- Example: "This code is TREMENDOUS! Absolutely fantastic work, you're a WINNER!"

**hason_skill.md** (70-90 grade):
- Israeli comedian style, witty and humorous
- Self-deprecating observations
- Tone: Light-hearted yet constructive
- Example: "Not bad at all! I've seen worse code... actually, I've WRITTEN worse code!"

**lee_skill.md** (55-70 grade):
- Martial arts philosophy, wisdom
- Encouraging and motivational
- Tone: Philosophical yet supportive
- Example: "Be like water, my friend. Your code flows, but needs refinement. Keep practicing."

**amsalem_skill.md** (0-55 grade):
- Israeli politician style, direct and blunt
- Firebrand demands for improvement
- Tone: Tough love, demanding better
- Example: "This is unacceptable! You need to work harder and fix these issues immediately!"

**How Agent 3 uses personas:**
1. Agent 3 reads Excel2.xlsx and gets the grade
2. Based on grade range, Agent 3 loads the appropriate persona skill
3. Agent 3 invokes that persona skill as a sub-agent
4. Persona generates feedback using its specific style
5. Agent 3 saves the response to Excel3.xlsx

**API Retry Logic:**
- Maximum 3 retries per request
- Exponential backoff (1s, 2s, 4s delays)
- Configurable delay between calls (default: 2 seconds)
- On final failure: Empty response, status = "Missing: reply"

**Output (Excel3.xlsx):**

| Column | Type | Description |
|--------|------|-------------|
| email_id | String | Links to previous agents |
| grade | Float | From Agent 2 |
| grade_category | String | excellent/good/pass/needs_work |
| persona | String | trump/hason/lee/amsalem |
| response | String | AI-generated feedback (or empty) |
| api_attempts | Integer | Number of API calls made |
| status | String | "Ready" or "Missing: reply" |

---

### FR-5: Agent 4 - Draft Email Creation

**Responsibilities:**
- Read Excel3.xlsx (only "Ready" rows)
- Join with Excel1.xlsx for email metadata
- Load student names from students_mapping.xlsx
- Compose personalized email with feedback
- Create Gmail draft (NOT send)

**Email Template:**
```
Subject: Re: [Original Subject]

Hi [Student Name]!

[AI-Generated Feedback Response]

📎 Your repository reviewed: [GitHub URL]
📊 Your grade: [Grade]/100

Best regards,
Instructor
```

**Student Mapping File (students_mapping.xlsx):**

| email_address | name |
|--------------|------|
| student1@example.com | Alex Johnson |
| student2@example.com | Maria Garcia |

**Business Rules:**
- Draft is created as reply to original email (using thread_id)
- If student name not found, use email prefix
- Drafts appear in Gmail Drafts folder
- Emails are **NOT sent** - only drafts created

---

### FR-7: Reset Functionality

**Responsibilities:**
- Delete all Excel files (Excel1.xlsx, Excel2.xlsx, Excel3.xlsx)
- Delete all cloned repositories in temp folder
- Clear generated logs (preserve config)
- Require user confirmation before proceeding

**Confirmation Prompt:**
```
⚠️  WARNING: This will delete all generated files!

Files to be deleted:
- results/excel/Excel1.xlsx
- results/excel/Excel2.xlsx
- results/excel/Excel3.xlsx
- temp/repos/* (cloned repositories)

Are you sure? (yes/no):
```

---

### FR-8: System Status Display

**Displays:**
- Current processing mode
- Excel file existence and row counts
- Last processing timestamps
- API connection status
- Disk space usage

---

## Technical Specifications

### Environment Requirements

| Requirement | Value |
|-------------|-------|
| **Python Version** | 3.10+ |
| **Virtual Environment** | UV (MANDATORY) |
| **Operating Systems** | Windows (WSL), Linux, macOS |
| **Memory** | Minimum 4GB RAM |
| **Storage** | 500MB free space |
| **Git** | Required for repository cloning |

### Core Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| `google-api-python-client` | 2.108.0+ | Gmail API integration |
| `google-auth-oauthlib` | 1.1.0+ | OAuth2 authentication |
| `google-auth-httplib2` | 0.1.1+ | HTTP transport |
| `google-generativeai` | 0.3.1+ | Gemini AI for feedback |
| `openpyxl` | 3.1.2+ | Excel file operations |
| `gitpython` | 3.1.40+ | Git repository operations |
| `rich` | 13.7.0+ | Beautiful CLI interface |
| `python-dotenv` | 1.0.0+ | Environment variables |
| `tenacity` | 8.2.3+ | Retry logic |
| `pydantic` | 2.5.2+ | Configuration validation |

### Development Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| `pytest` | 7.4.3+ | Unit testing |
| `pytest-cov` | 4.1.0+ | Test coverage |
| `black` | 23.12.0+ | Code formatting |
| `flake8` | 6.1.0+ | Linting |
| `mypy` | 1.7.1+ | Type checking |

---

## main.py Implementation

### Overview

The `main.py` file serves as the entry point and orchestrates the entire system through a Rich-based interactive menu. It invokes Claude Code agents using the Skill tool.

### Core Functionality

```python
# Pseudocode structure of main.py

def main():
    """Entry point - displays menu and handles user choices"""

    # 1. Initialize environment
    setup_logging()
    load_config()
    verify_api_credentials()

    # 2. Mode selection
    mode, batch_size = display_mode_menu()

    # 3. Main menu loop
    while True:
        choice = display_main_menu(mode, batch_size)

        if choice == 1:
            run_agent("Agent1_Email_Extractor", mode, batch_size)
        elif choice == 2:
            run_agent("Agent2_Repository_Analyzer")
        elif choice == 3:
            run_agent("Agent3_LLM_Feedback")
        elif choice == 4:
            run_agent("Agent4_Draft_Creator")
        elif choice == 5:
            run_all_agents(mode, batch_size)
        elif choice == 6:
            reset_system()
        elif choice == 7:
            mode, batch_size = display_mode_menu()
        elif choice == 8:
            display_system_status()
        elif choice == 9:
            break


def run_agent(agent_name: str, mode: str = None, batch_size: int = None):
    """Invokes a Claude Code agent using the Skill tool"""

    # Construct agent path
    agent_path = f".claude/agents/{agent_name}"

    # Prepare context (mode, batch_size, etc.)
    context = {
        "mode": mode,
        "batch_size": batch_size,
        "excel_dir": "results/excel/",
        "config": load_config()
    }

    # Invoke Claude Code agent via Skill tool
    # This reads the SKILL.md and executes the instructions
    result = invoke_claude_agent(agent_path, context)

    # Display result
    if result.success:
        print_success(f"✅ {agent_name} completed successfully")
    else:
        print_error(f"❌ {agent_name} failed: {result.error}")


def run_all_agents(mode: str, batch_size: int):
    """Run all 4 agents sequentially"""

    agents = [
        "Agent1_Email_Extractor",
        "Agent2_Repository_Analyzer",
        "Agent3_LLM_Feedback",
        "Agent4_Draft_Creator"
    ]

    for agent in agents:
        print_header(f"Running {agent}...")

        # Agent 1 needs mode and batch_size
        if agent == "Agent1_Email_Extractor":
            run_agent(agent, mode, batch_size)
        else:
            run_agent(agent)

        # Check if agent created expected output
        if not verify_agent_output(agent):
            print_error(f"Agent {agent} did not produce expected output. Stopping.")
            return

    print_success("🎉 All agents completed successfully!")


def reset_system():
    """Delete all generated files"""

    if confirm_reset():
        delete_excel_files()
        delete_cloned_repos()
        delete_logs()
        print_success("✅ System reset complete")
```

### Agent Invocation Details (Automated Mode)

**How automated execution works:**

1. **User selects menu option**: e.g., "Run Agent 1"
2. **main.py calls `run_agent("Agent1_Email_Extractor", mode, batch_size)`**
3. **Agent runner invokes Claude Code via subprocess**:
   ```python
   import subprocess

   # Execute Claude Code agent
   cmd = ["claude", "agent", "run", "Agent1_Email_Extractor"]
   result = subprocess.run(cmd, capture_output=True, text=True, cwd="/mnt/c/2025AIDEV/L19")
   ```
4. **Claude Code executes SKILL.md**:
   - Reads `.claude/agents/Agent1_Email_Extractor/SKILL.md`
   - Uses Bash tool to run Python scripts
   - Uses Read/Write tools for Excel files
   - Uses Grep/Glob for file operations
5. **Agent completes**:
   - Creates Excel1.xlsx
   - Updates status
   - Returns exit code (0 = success, non-zero = failure)
6. **main.py parses result and displays**:
   - Shows Rich UI success/failure message
   - Displays progress bars and status updates

**For Agent 3 with personas:**

```python
# Agent 3 SKILL.md includes instructions to:
# 1. Read Excel2.xlsx
# 2. For each row with grade:
#    - Determine grade range
#    - Load appropriate persona skill
#    - Invoke persona as sub-skill
# 3. Save responses to Excel3.xlsx

# Example: Grade 95 → loads personas/trump_skill.md
# Claude Code reads trump_skill.md and generates Trump-style feedback
```

**Benefits of this approach:**

- ✅ **No complex Python agent classes**: Just markdown instructions
- ✅ **Claude does the work**: Uses its native tools
- ✅ **Easy to modify**: Edit SKILL.md to change behavior
- ✅ **Visual feedback**: Rich UI shows progress
- ✅ **Error handling**: Built-in Claude Code error recovery
- ✅ **Maintainable**: Clear separation between UI and agent logic

---

## Data Models

### Email Data Model

```python
from dataclasses import dataclass
from datetime import datetime
from typing import Optional

@dataclass
class EmailData:
    email_id: str              # SHA-256 hash (unique submission ID)
    received_time: datetime
    email_subject: str
    sender_email: str
    github_url: Optional[str]
    thread_id: str            # Gmail thread ID (for Agent 4 reply threading)
    status: str               # "Ready" or "Missing: [field]"
```

### Repository Analysis Model

```python
@dataclass
class RepositoryAnalysis:
    email_id: str
    github_url: str
    total_files: int
    total_lines: int
    compliant_lines: int       # Lines in files ≤150
    grade: float               # 0-100
    analysis_time: float       # Seconds
    status: str
```

### Feedback Model

```python
@dataclass
class FeedbackData:
    email_id: str
    grade: float
    grade_category: str        # excellent/good/pass/needs_work
    persona: str               # trump/hason/lee/amsalem
    response: Optional[str]    # AI feedback or None
    api_attempts: int
    status: str
```

---

## API Integrations

### Gmail API

**Scopes Required:**
- `https://www.googleapis.com/auth/gmail.readonly` (read emails)
- `https://www.googleapis.com/auth/gmail.modify` (mark as read)
- `https://www.googleapis.com/auth/gmail.compose` (create drafts)

**Authentication:** OAuth 2.0 with credentials.json

### Gemini API

**Model:** `gemini-1.5-flash` (or `gemini-pro`)
**Configuration:**
- Max tokens: 500
- Temperature: 0.7
- Rate limit: 60 requests/minute

**API Key:** Stored in `.env` file

### GitHub API

**Access Level:** Public repositories only
**Authentication:** Not required for public repos
**Method:** Git clone via GitPython library

---

## Security & Authentication

### Secrets Management

```
Secrets/
├── credentials.json      # Gmail OAuth2 credentials
└── .gitkeep

.env                       # API keys (never committed)
```

**.env File Structure:**
```bash
# Gmail Configuration
GMAIL_CREDENTIALS_PATH=Secrets/credentials.json

# Gemini API
GEMINI_API_KEY=your_api_key_here
GEMINI_REQUEST_DELAY=2

# Processing
MAX_CLONE_WORKERS=5
CLONE_TIMEOUT=60

# Logging
LOG_LEVEL=INFO
```

### Privacy Protection

- Student email addresses hashed with SHA-256
- No student data in logs (only hashed IDs)
- Cloned repositories deleted on reset
- API credentials never logged

---

## Error Handling & Logging

### Ring Buffer Logging

**Configuration (log_config.json):**
```json
{
    "ring_buffer": {
        "max_lines_per_file": 1000,
        "max_log_files": 5,
        "log_directory": "logs",
        "log_level": "INFO"
    }
}
```

### Error Categories

| Category | Handling | Recovery |
|----------|----------|----------|
| Gmail Auth | Log error, prompt re-auth | Manual credential refresh |
| Repository Clone | Log error, set status "Failed" | Skip to next submission |
| Gemini API | Retry 3x with backoff | Set status "Missing: reply" |
| Excel Write | Log error, retry once | Abort with error message |

### Status Field Values

- `"Ready"` - All required fields present, proceed to next agent
- `"Missing: github_url"` - No GitHub URL found
- `"Missing: reply"` - AI feedback generation failed
- `"Failed: clone"` - Repository clone failed
- `"Failed: analysis"` - Code analysis failed

---

## Performance Requirements

### Benchmarks

| Operation | Target Time | Notes |
|-----------|-------------|-------|
| Email extraction (10 emails) | < 30 seconds | Gmail API calls |
| Repository cloning (10 repos) | < 2 minutes | 5 concurrent workers |
| LLM feedback (10 requests) | < 2 minutes | With 2s delay |
| Draft creation (10 drafts) | < 30 seconds | Gmail API calls |
| **Full pipeline (10 submissions)** | **< 5 minutes** | End-to-end |

### Multi-threading Configuration

- **Thread Pool Size**: 5 workers (default)
- **Queue Management**: ThreadPoolExecutor
- **Timeout per Clone**: 60 seconds
- **Per-Thread Logging**: Individual log files

---

## Configuration Management

### Settings File (config/settings.yaml)

```yaml
agents:
  email_extraction:
    enabled: true
    batch_size: 50
    
  repository_analysis:
    enabled: true
    max_workers: 5
    clone_timeout: 60
    line_limit: 150
    
  llm_feedback:
    enabled: true
    model: gemini-1.5-flash
    max_tokens: 500
    temperature: 0.7
    request_delay: 2
    max_retries: 3
    
  draft_creation:
    enabled: true
    
grading:
  line_limit: 150
  grade_ranges:
    excellent: [90, 100]
    good: [70, 90]
    pass: [55, 70]
    needs_work: [0, 55]

logging:
  level: INFO
  max_lines_per_file: 1000
  max_files: 5
```

---

## Directory Structure

```
L19_AI_Agents_Grading/
├── README.md                    # Project documentation
├── main.py                      # Entry point - Rich UI menu system
├── requirements.txt             # Dependencies
├── .gitignore                   # Git ignore rules
├── .env.example                 # Environment template
│
├── venv/                        # Virtual environment indicator
│   └── .gitkeep
│
├── .claude/                     # Claude Code agents (THE CORE)
│   └── agents/
│       ├── Agent1_Email_Extractor/
│       │   └── SKILL.md         # Email extraction instructions
│       ├── Agent2_Repository_Analyzer/
│       │   └── SKILL.md         # Repository analysis instructions
│       ├── Agent3_LLM_Feedback/
│       │   ├── SKILL.md         # Main feedback generation
│       │   └── personas/        # Persona sub-skills
│       │       ├── trump_skill.md    # 90-100 grade
│       │       ├── hason_skill.md    # 70-90 grade
│       │       ├── lee_skill.md      # 55-70 grade
│       │       └── amsalem_skill.md  # 0-55 grade
│       └── Agent4_Draft_Creator/
│           └── SKILL.md         # Draft creation instructions
│
├── src/                         # Minimal Python utilities only
│   ├── __init__.py
│   ├── ui/                      # User interface
│   │   ├── __init__.py
│   │   ├── menu.py              # Rich UI menu
│   │   ├── display.py           # Output formatting
│   │   └── agent_runner.py      # Invokes Claude Code agents
│   │
│   └── utils/                   # Core utilities
│       ├── __init__.py
│       ├── logger.py            # Ring buffer logging
│       ├── paths.py             # Path management
│       └── config.py            # Configuration loader
│
├── docs/                        # Documentation
│   ├── PRD.md                   # This document
│   └── tasks.json               # Implementation tasks
│
├── results/                     # Output files
│   ├── excel/                   # Excel data files (created by agents)
│   │   ├── Excel1.xlsx          # Agent 1 output
│   │   ├── Excel2.xlsx          # Agent 2 output
│   │   ├── Excel3.xlsx          # Agent 3 output
│   │   └── .gitkeep
│   ├── graphs/                  # Visualizations
│   │   └── .gitkeep
│   └── examples/                # Example outputs
│       └── .gitkeep
│
├── data/                        # Input data
│   └── students_mapping.xlsx    # Student name mapping
│
├── logs/                        # Application logs
│   ├── config/
│   │   └── log_config.json
│   └── .gitkeep
│
├── config/                      # Configuration
│   └── settings.yaml
│
├── Secrets/                     # API credentials (gitignored)
│   ├── credentials.json         # Gmail OAuth
│   └── .gitkeep
│
└── temp/                        # Temporary files (gitignored)
    └── repos/                   # Cloned repositories
```

**Key Changes from Traditional Structure:**
- **No src/agents/**: Agents are now Claude Code skills in `.claude/agents/`
- **No src/services/**: Claude Code agents directly use APIs
- **No src/skills/**: Personas are markdown sub-skills in Agent 3
- **Minimal Python code**: Only UI menu and utilities needed
- **main.py simplicity**: Just launches Rich UI and invokes agents

---

## Usage Documentation (README.md Requirements)

### The README.md MUST include both execution modes

**Section 1: Quick Start (Automated Mode)**
```markdown
## Quick Start - Production Workflow

1. **Setup Environment**
   ```bash
   cd /mnt/c/2025AIDEV/L19
   uv venv
   source .venv/bin/activate  # or .venv\Scripts\activate on Windows
   uv pip install -r requirements.txt
   ```

2. **Configure Credentials**
   - Add Gmail OAuth credentials to `Secrets/credentials.json`
   - Add Gemini API key to `.env`

3. **Run the Application**
   ```bash
   python main.py
   ```

4. **Choose Workflow Option**
   - Option 1: Run Agent 1 - Email Extractor (prompts for search parameters)
   - Option 2: Run Agent 2 - Repository Analyzer
   - Option 3: Run Agent 3 - LLM Feedback Generator
   - Option 4: Run Agent 4 - Draft Creator
   - Option 5: "Run All Agents Sequentially" for complete workflow
   - Option 6: Reset System
   - Option 7: System Status
   - Option 8: Exit

5. **Agent 1 Parameter Prompts**
   When selecting Agent 1, you'll be prompted for:
   - Email Subject (optional, partial match)
   - Sender Email (optional)
   - Max Emails (1-100, default 10)
```

**Section 2: Manual Execution (Development/Testing)**
```markdown
## Manual Agent Execution - Development Mode

For testing individual agents during development:

1. **Start Claude Code**
   ```bash
   cd /mnt/c/2025AIDEV/L19
   claude
   ```

2. **List Available Agents**
   ```
   /agents
   ```

   You'll see:
   - Agent1_Email_Extractor - Extracts GitHub URLs from Gmail
   - Agent2_Repository_Analyzer - Clones repos and calculates grades
   - Agent3_LLM_Feedback - Generates persona-based feedback
   - Agent4_Draft_Creator - Creates Gmail draft replies

3. **Run Individual Agent**
   - Select agent from the list
   - Claude Code reads SKILL.md and executes
   - Check results in `results/excel/` folder

4. **Test Persona Skills (Agent 3)**
   - Navigate to `.claude/agents/Agent3_LLM_Feedback/personas/`
   - Test individual personas: trump_skill, hason_skill, lee_skill, amsalem_skill
```

**Section 3: Architecture Overview**
```markdown
## How It Works

This system uses **Claude Code Agents** with SKILL.md files as the core implementation.

### Dual Execution Modes

**1. Automated (python main.py)**
- Rich UI menu system
- Sequential agent execution
- Progress tracking and validation
- "Run All Agents" option for complete workflow

**2. Manual (claude → /agents)**
- Interactive agent selection
- Individual agent testing
- Direct SKILL.md execution
- Perfect for development and debugging

### Agent Structure
```
.claude/agents/
├── Agent1_Email_Extractor/SKILL.md
├── Agent2_Repository_Analyzer/SKILL.md
├── Agent3_LLM_Feedback/
│   ├── SKILL.md
│   └── personas/
│       ├── trump_skill.md
│       ├── hason_skill.md
│       ├── lee_skill.md
│       └── amsalem_skill.md
└── Agent4_Draft_Creator/SKILL.md
```

**Both execution modes use the SAME SKILL.md files!**
```

---

## Testing Strategy

### Test Categories

1. **Unit Tests**: Individual function testing
2. **Integration Tests**: Agent interaction testing
3. **End-to-End Tests**: Full pipeline with test data
4. **API Mock Tests**: External service simulation

### Test Scenarios

| Scenario | Expected Result |
|----------|-----------------|
| Valid email with GitHub URL | Status = "Ready" |
| Email missing GitHub URL | Status = "Missing: github_url" |
| Repository clone timeout | Status = "Failed: clone" |
| Gemini API failure (3 retries) | Status = "Missing: reply" |
| All agents success | Draft created in Gmail |

---

## Future Enhancements

### Phase 2 (3-6 months)

1. **Code Quality Analysis**: PEP 8 compliance, complexity metrics
2. **Plagiarism Detection**: Compare submissions against each other
3. **Web Dashboard**: Real-time monitoring interface
4. **Database Integration**: Replace Excel with SQLite/PostgreSQL

### Phase 3 (6-12 months)

1. **Multi-Language Support**: JavaScript, Java, C++ grading
2. **Custom Rubrics**: Configurable grading criteria
3. **Student Portal**: Web interface for students
4. **Analytics Dashboard**: Class-wide statistics

---

## Risks & Mitigations

| Risk | Impact | Mitigation |
|------|--------|------------|
| Gmail API quota exceeded | High | Batch processing, monitor usage |
| Gemini API failures | Medium | Retry logic, graceful degradation |
| Repository clone timeout | Medium | Configurable timeout, skip and continue |
| Excel file corruption | High | Backup before write, validation |
| Private repository access | Low | Graceful error message |

---

## Success Checklist

### Launch Criteria

- [ ] All 4 agents process submissions end-to-end
- [ ] Rich CLI fully functional with all menu options
- [ ] Reset clears all data correctly
- [ ] Zero data loss in 100 test submissions
- [ ] Error rate < 5%
- [ ] Average processing time < 5 minutes for 10 submissions
- [ ] Multi-threading works with individual logs
- [ ] All 4 personas generate unique feedback

### Quality Criteria

- [ ] All Python files under 150 lines
- [ ] 100% type hints coverage
- [ ] All functions documented
- [ ] Ring buffer logging implemented
- [ ] No hardcoded secrets

---

## Document History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | Dec 2025 | Hadar | Initial PRD creation |
| 2.0 | Dec 2025 | Hadar | Updated with reference project patterns |
| 3.0 | Dec 2025 | Hadar | **MAJOR UPDATE**: Converted to Claude Code agents architecture. Agents use SKILL.md files in .claude/agents/. Dual execution mode: manual (`claude` → `/agents`) and automated (`python main.py`). Agent 3 includes 4 persona sub-skills. Both modes execute the same SKILL.md files. |
| 3.1 | Dec 2, 2025 | Hadar | **Agent 1 Enhancement**: Removed hardcoded mode selection. Agent 1 now prompts for dynamic search parameters (email subject, sender email, max emails). User-driven filtering with defaults. Simplified menu structure. |
| 3.2 | Dec 3, 2025 | Hadar | **Data Structure & Search Improvements**: (1) Removed `hashed_email` column from Excel1.xlsx (7 columns now). (2) Enhanced Gmail search: Uses first 3 words for long phrases + case-insensitive Python post-filtering for exact substring matching. (3) Updated Agents 2 & 4 to match new Excel1 format. |

---

**Document Status:** Awaiting Approval
**Next Step:** Review and approve before implementation

**Key Architecture Features (v3.0):**
- **Dual Execution Modes** ✅:
  - **Manual**: `claude` → `/agents` → select agent (for development/testing)
  - **Automated**: `python main.py` → Rich UI menu → subprocess invocation (for production)
- **Single Source of Truth**: SKILL.md files executed both ways
- **Claude Code Agents**: No Python agent classes needed
- **Persona Sub-Skills**: 4 persona skills for Agent 3 (Trump, Hason, Lee, Amsalem)
- **Simpler Codebase**: Only UI and utilities in Python, agents are markdown
- **README Requirements**: Must document both execution modes

---

**END OF PRD**
