# L19: AI Agents Auto Homework Grading System

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-Agents-purple.svg)](https://claude.ai/claude-code)

**Automated homework grading system using Claude Code agents architecture with dual execution modes.**

---

## 📋 Table of Contents

- [Overview](#overview)
- [Architecture](#architecture)
- [Dual Execution Modes](#dual-execution-modes)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
  - [Automated Mode](#automated-mode-production)
  - [Manual Mode](#manual-mode-developmenttesting)
- [Agents](#agents)
- [Project Structure](#project-structure)
- [Results](#results)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)

---

## 🎯 Overview

L19 is an intelligent homework grading system that automates the entire grading pipeline for programming assignments submitted via email. The system uses **Claude Code Agents** to:

1. Extract homework submissions from Gmail
2. Analyze GitHub repositories for code quality
3. Generate personalized AI feedback with unique personas
4. Create Gmail draft replies ready to send

**Key Features:**
- 🤖 **Claude Code Agents Architecture** - Agents defined as SKILL.md files
- 🎭 **Persona-based Feedback** - 4 unique AI personas (Trump, Hason, Lee, Amsalem)
- 📊 **Automated Grading** - Based on Python code line limits (≤150 lines per file)
- ✉️ **Gmail Integration** - Reads emails and creates draft replies
- 🔄 **Dual Execution Modes** - Run via Python UI or Claude CLI

---

## 🏗️ Architecture

### Dual Execution Mode Architecture

The system supports **two execution modes** that share the same agent logic:

```
┌─────────────────────────────────────────────────────────────┐
│                    SKILL.md FILES                           │
│              (Single Source of Truth)                       │
│                                                             │
│  • Agent1_Email_Extractor/SKILL.md                         │
│  • Agent2_Repository_Analyzer/SKILL.md                     │
│  • Agent3_LLM_Feedback/SKILL.md                            │
│  • Agent4_Draft_Creator/SKILL.md                           │
└─────────────────────────────────────────────────────────────┘
              ▲                                    ▲
              │                                    │
    ┌─────────┴───────┐                 ┌─────────┴──────────┐
    │  MANUAL MODE    │                 │  AUTOMATED MODE    │
    │  (Development)  │                 │   (Production)     │
    │                 │                 │                    │
    │  claude         │                 │  python main.py    │
    │  /agents        │                 │  → Rich UI Menu    │
    │  → Select agent │                 │  → Subprocess      │
    └─────────────────┘                 └────────────────────┘
```

**Benefits:**
- ✅ **Single Source of Truth**: All agent logic in SKILL.md files
- ✅ **Development Flexibility**: Test agents manually via Claude CLI
- ✅ **Production Automation**: Run full pipeline via Python UI
- ✅ **Consistency**: Both modes execute identical agent code

---

## 🔄 Dual Execution Modes

### Mode 1: Automated Mode (Production)

**Use Case:** Run the complete grading pipeline with a rich interactive menu

```bash
python main.py
```

**Features:**
- 🎨 Rich terminal UI with colors and formatting
- 🔄 Sequential pipeline execution with output verification
- 📈 Real-time status and progress tracking
- 🔄 System reset and status monitoring
- 📧 Dynamic Agent 1 parameters (subject, sender, max emails)

**Menu Options:**
1. Run Agent 1 - Email Extractor (prompts for search parameters)
2. Run Agent 2 - Repository Analyzer
3. Run Agent 3 - LLM Feedback Generator
4. Run Agent 4 - Draft Creator
5. Run All Agents Sequentially
6. Reset System
7. System Status
8. Exit

### Mode 2: Manual Mode (Development/Testing)

**Use Case:** Test individual agents during development

```bash
# 1. Start Claude Code CLI
claude

# 2. Access agents menu
/agents

# 3. Select agent from list:
#    - Agent1_Email_Extractor
#    - Agent2_Repository_Analyzer
#    - Agent3_LLM_Feedback
#    - Agent4_Draft_Creator
```

**Benefits:**
- 🔍 Test single agents in isolation
- 🐛 Debug agent logic and outputs
- 📝 Verify SKILL.md instructions
- ⚡ Faster iteration during development

---

## ✅ Prerequisites

### Software Requirements

- **Python 3.10+** - [Download](https://www.python.org/downloads/)
- **Git** - [Download](https://git-scm.com/downloads)
- **Claude Code CLI** - [Installation Guide](https://docs.anthropic.com/claude-code)
- **WSL** (Windows Subsystem for Linux) - *Windows users only*

### API Requirements

1. **Gmail API Credentials**
   - Google Cloud Project with Gmail API enabled
   - OAuth 2.0 credentials (Desktop app)
   - Download `credentials.json`

2. **Gemini API Key**
   - Google AI Studio account
   - Gemini API key for LLM feedback generation

### System Requirements

- **OS:** Windows 10/11 (with WSL), macOS, or Linux
- **RAM:** 4GB minimum (8GB recommended)
- **Disk:** 500MB free space

---

## 📦 Installation

### 1. Clone Repository

```bash
git clone <repository-url>
cd L19
```

### 2. Set Up UV Virtual Environment

**Important:** You must create and activate a virtual environment before installing dependencies.

#### Install UV (if not already installed)

```bash
# Linux/WSL/macOS
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows (PowerShell)
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

#### Create Virtual Environment

```bash
uv venv
```

#### Activate Virtual Environment

**Linux/WSL/macOS:**
```bash
source .venv/bin/activate
```

**Windows (PowerShell):**
```powershell
.venv\Scripts\Activate.ps1
```

**Windows (CMD):**
```cmd
.venv\Scripts\activate.bat
```

You should see `(.venv)` appear in your terminal prompt, indicating the virtual environment is active.

### 3. Install Python Dependencies

**With virtual environment activated:**

```bash
uv pip install -r requirements.txt
```

**Or using standard pip:**
```bash
pip install -r requirements.txt
```

**Required packages:**
- `google-api-python-client` - Gmail API
- `google-generativeai` - Gemini AI
- `openpyxl` - Excel file handling
- `gitpython` - Git operations
- `rich` - Terminal UI
- `pydantic` - Configuration management
- `python-dotenv` - Environment variables

### 4. Verify Installation

**Ensure virtual environment is still activated**, then run:

```bash
python test_app_startup.py
```

Expected output:
```
✓ All startup tests passed!
  The application is ready to run.
```

**Note:** Always activate the virtual environment before running the application or installing packages.

---

## ⚙️ Configuration

### 1. Gmail API Credentials

Copy your Gmail OAuth 2.0 credentials to the Secrets folder:

```bash
# Place your credentials.json here:
cp /path/to/your/credentials.json Secrets/credentials.json
```

**First-time authentication:**
- A browser window will open
- Sign in with your Gmail account
- Grant permissions to the application
- Token will be saved to `Secrets/token.json`

**Verify credentials:**
```bash
python test_gmail_credentials.py
```

### 2. Environment Variables

Create `.env` file from template:

```bash
cp .env.example .env
```

**Edit `.env` and configure:**

```bash
# Gmail Configuration
GMAIL_CREDENTIALS_PATH=Secrets/credentials.json

# Gemini API (REQUIRED - Add your key here!)
GEMINI_API_KEY=your_gemini_api_key_here
GEMINI_MODEL=gemini-1.5-flash
GEMINI_MAX_TOKENS=500
GEMINI_TEMPERATURE=0.7
GEMINI_REQUEST_DELAY=2

# Processing
MAX_CLONE_WORKERS=5
CLONE_TIMEOUT=60

# Logging
LOG_LEVEL=INFO
LOG_MAX_LINES_PER_FILE=1000
LOG_MAX_FILES=5

# Grading
LINE_LIMIT=150
```

### 3. Application Settings

Configuration file: `config/settings.yaml`

```yaml
agents:
  email_extraction:
    enabled: true
    batch_size: 50
    subject_pattern: "self check of homework (\\d{1,3})"
    github_url_pattern: "https://github\\.com/([^/]+)/([^/]+)"

  repository_analysis:
    enabled: true
    max_workers: 5
    clone_timeout: 60
    line_limit: 150

  llm_feedback:
    enabled: true
    model: "gemini-1.5-flash"
    max_tokens: 500
    temperature: 0.7
    request_delay: 2
    max_retries: 3

grading:
  line_limit: 150
  grade_ranges:
    excellent: [90, 100]    # Trump persona
    good: [70, 90]          # Hason persona
    pass: [55, 70]          # Lee persona
    needs_work: [0, 55]     # Amsalem persona

  personas:
    excellent: trump
    good: hason
    pass: lee
    needs_work: amsalem
```

### 4. Student Name Mapping

**File:** `data/students_mapping.xlsx`

| email_address              | name         |
|---------------------------|--------------|
| student1@university.edu   | John Doe     |
| student2@university.edu   | Jane Smith   |

- Used by Agent 4 to personalize draft emails
- If email not found, uses email prefix (before @)

---

## 🚀 Usage

### Automated Mode (Production)

#### Step 1: Activate Virtual Environment

**Before running the application, always activate the virtual environment:**

**Linux/WSL/macOS:**
```bash
source .venv/bin/activate
```

**Windows (PowerShell):**
```powershell
.venv\Scripts\Activate.ps1
```

**Windows (CMD):**
```cmd
.venv\Scripts\activate.bat
```

You should see `(.venv)` in your terminal prompt.

#### Step 2: Start the Application

```bash
python main.py
```

#### Step 3: Main Menu

The main menu will appear directly (no mode selection):

```
╔══════════════════════════════════════════════════════════════════╗
║                      MAIN MENU                                   ║
╠══════════════════════════════════════════════════════════════════╣
║                                                                  ║
║   [1] 📧 Run Agent 1 - Email Extractor                          ║
║   [2] 📊 Run Agent 2 - Repository Analyzer                      ║
║   [3] 🤖 Run Agent 3 - LLM Feedback Generator                   ║
║   [4] ✉️  Run Agent 4 - Draft Creator                            ║
║   [5] 🚀 Run All Agents Sequentially                            ║
║   [6] 🗑️  Reset System                                           ║
║   [7] 📋 System Status                                           ║
║   [8] 🚪 Exit                                                    ║
║                                                                  ║
╚══════════════════════════════════════════════════════════════════╝

Note: Agent 1 will prompt for search parameters (subject, sender, max emails)

Enter choice (1-8):
```

#### Step 4: Run Agent 1 (Email Extractor)

When you select Agent 1, it will prompt you for search parameters:

```
╔══════════════════════════════════════════════════════════════════╗
║              AGENT 1: EMAIL EXTRACTION PARAMETERS                ║
╠══════════════════════════════════════════════════════════════════╣

  Agent 1 will prompt you for:

  📧 Email Subject (optional)
     • Partial subject match (case-insensitive)
     • Press Enter to search all subjects

  👤 Sender Email (optional)
     • Filter by sender's email address
     • Press Enter to search all senders

  🔢 Max Emails (required)
     • Range: 1-100
     • Default: 10 (press Enter)

╚══════════════════════════════════════════════════════════════════╝
```

**Example:**
```
📧 Email Subject: homework
   → Will search for: "homework"

👤 Sender Email: student@example.com
   → Will filter by sender: student@example.com

🔢 Max Emails (1-100) [Default: 10]: 5
   → Will process up to 5 emails

🔍 Gmail Search Query: subject:{homework} from:student@example.com
📊 Max Results: 5
```

#### Step 5: Monitor Progress

The system will:
1. ✅ Run each agent
2. ✅ Verify output files exist
3. ✅ Display success/failure status
4. ✅ Create Excel files: `results/excel/Excel1-4.xlsx`
5. ✅ Create Gmail drafts in your account

#### Step 6: Review Results

**Generated Files:**
- `results/excel/Excel1.xlsx` - Extracted email data
- `results/excel/Excel2.xlsx` - Repository analysis + grades
- `results/excel/Excel3.xlsx` - AI-generated feedback
- Gmail Drafts - Ready to review and send

**Check Status:**
```
Option 8 - Display System Status
```

Shows:
- Excel files created
- Cloned repositories
- Log files

---

### Manual Mode (Development/Testing)

#### Step 1: Start Claude Code CLI

```bash
claude
```

#### Step 2: Access Agents Menu

```
/agents
```

#### Step 3: Select Agent

```
Available agents:
  • Agent1_Email_Extractor
  • Agent2_Repository_Analyzer
  • Agent3_LLM_Feedback
  • Agent4_Draft_Creator

Select agent to run:
```

#### Step 4: Agent Executes

Claude Code reads the SKILL.md file and executes the agent instructions.

**Note:** Agent 1 will prompt you for search parameters:
- Email Subject (optional)
- Sender Email (optional)
- Max Emails (1-100, default 10)

#### Step 5: Verify Output

Check `results/excel/` folder for generated Excel files.

---

## 🤖 Agents

### Agent 1: Email Extractor

**File:** `.claude/agents/Agent1_Email_Extractor/SKILL.md`

**User Input Parameters:**

When Agent 1 runs, it prompts for:
- **Email Subject** (optional): Partial subject match (case-insensitive)
- **Sender Email** (optional): Filter by sender's email address
- **Max Emails** (required): 1-100 emails, default 10

**Responsibilities:**
- Prompt user for search parameters
- Build dynamic Gmail search query
- Connect to Gmail API and search emails (all folders/labels)
- Extract GitHub URLs from email body
- Generate unique email IDs (SHA-256)
- Create `Excel1.xlsx`

**Example Search:**
```
📧 Email Subject: AI Development Expert course - Homework - L
👤 Sender Email: (optional, leave empty for all)
🔢 Max Emails: 20

→ Gmail Query: subject:AI Development Expert
→ Post-Filter: Case-insensitive substring match for full phrase
→ Processes up to 20 matching emails
```

**Search Behavior:**
- Long phrases (>3 words): Uses first 3 words in Gmail search + Python post-filtering
- Short terms: Direct Gmail search + Python post-filtering for exact substring match
- Case-insensitive matching: "awe1" matches "RAWE1", "awe1r" (but not "awe")

**Output:** `results/excel/Excel1.xlsx`

| email_id | received_time | email_subject | sender_email | github_url | thread_id | status |
|----------|---------------|---------------|--------------|------------|-----------|--------|
| abc123... | 2024-12-01 10:30 | AI Development Expert course - Homework - L17 | student@example.com | https://github.com/... | thread_abc | Ready |

---

### Agent 2: Repository Analyzer

**File:** `.claude/agents/Agent2_Repository_Analyzer/SKILL.md`

**Responsibilities:**
- Read `Excel1.xlsx` (only "Ready" rows)
- Clone GitHub repositories (5 concurrent workers)
- Find all `.py` files
- Count total lines and files
- Calculate grade: `100 * (compliant_files / total_files)`
  - Compliant = files with ≤150 lines
- Create `Excel2.xlsx`

**Output:** `results/excel/Excel2.xlsx`

| email_id | github_url | total_files | total_lines | compliant_lines | grade | status |
|----------|------------|-------------|-------------|-----------------|-------|--------|
| abc123... | https://... | 10 | 1500 | 1200 | 80 | Ready |

**Grading Formula:**
```python
compliant_files = [files with lines <= 150]
grade = 100 * (len(compliant_files) / total_files)
```

---

### Agent 3: LLM Feedback Generator

**File:** `.claude/agents/Agent3_LLM_Feedback/SKILL.md`

**Responsibilities:**
- Read `Excel2.xlsx` (only "Ready" rows)
- Determine grade category
- Load appropriate persona skill
- Generate feedback via Gemini API
- Retry logic (3 attempts, exponential backoff)
- Create `Excel3.xlsx`

**Output:** `results/excel/Excel3.xlsx`

| email_id | grade | grade_category | persona | response | api_attempts | status |
|----------|-------|----------------|---------|----------|--------------|--------|
| abc123... | 92 | excellent | trump | TREMENDOUS work! This is... | 1 | Ready |

#### Persona Skills

**1. Trump (90-100) - Enthusiastic**

File: `.claude/agents/Agent3_LLM_Feedback/personas/trump_skill.md`

Style: Superlatives, "tremendous," "fantastic," "WINNER!"

Example:
> "TREMENDOUS work! This is absolutely FANTASTIC! You're a WINNER! Your code is INCREDIBLE, probably the best I've seen all week! KEEP IT UP!"

---

**2. Hason (70-90) - Israeli Comedian**

File: `.claude/agents/Agent3_LLM_Feedback/personas/hason_skill.md`

Style: Witty, self-deprecating humor, Israeli slang

Example:
> "Not bad at all! I've seen worse code... actually, I've WRITTEN worse code! 😄 Your functions are decent, though I'd suggest breaking down that 180-line monster. אבל אחלה עבודה!"

---

**3. Lee (55-70) - Martial Arts Philosophy**

File: `.claude/agents/Agent3_LLM_Feedback/personas/lee_skill.md`

Style: "Be like water," wisdom, philosophical

Example:
> "Be like water, my friend. Your code flows, but needs refinement. Adapt to the constraints. A file with 200 lines is rigid. Break it into smaller, flexible pieces. Empty your mind. Be formless."

---

**4. Amsalem (0-55) - Israeli Politician**

File: `.claude/agents/Agent3_LLM_Feedback/personas/amsalem_skill.md`

Style: Direct, blunt, tough-love, Israeli politician

Example:
> "This is unacceptable! You can do better and you know it! 300 lines in ONE file?! What were you thinking?! I expect excellence, not this. תתעשת! Fix it and resubmit!"

---

### Agent 4: Draft Creator

**File:** `.claude/agents/Agent4_Draft_Creator/SKILL.md`

**Responsibilities:**
- Read `Excel3.xlsx` (only "Ready" rows)
- Join with `Excel1.xlsx` for email metadata
- Load student names from `data/students_mapping.xlsx`
- Compose personalized email
- Create Gmail draft (NOT send)
- Draft is a reply to original email thread

**Output:** Gmail Drafts (visible in Gmail web interface)

**Email Template:**
```
Subject: Re: Self check of homework 5

Hi Alex Johnson!

[AI-Generated Feedback Response]

📎 Your repository reviewed: https://github.com/alex/homework5
📊 Your grade: 92/100

Best regards,
Instructor
```

**Key Features:**
- ✉️ Drafts created, NOT sent automatically
- 🧵 Reply to original email thread (uses thread_id)
- 👤 Personalized with student name
- 📊 Includes grade and repository link

---

## 📂 Project Structure

```
L19/
├── .claude/
│   └── agents/                         # Claude Code Agents
│       ├── Agent1_Email_Extractor/
│       │   └── SKILL.md               # Email extraction logic
│       ├── Agent2_Repository_Analyzer/
│       │   └── SKILL.md               # Repo analysis logic
│       ├── Agent3_LLM_Feedback/
│       │   ├── SKILL.md               # Feedback generation logic
│       │   └── personas/
│       │       ├── trump_skill.md     # Trump persona
│       │       ├── hason_skill.md     # Hason persona
│       │       ├── lee_skill.md       # Lee persona
│       │       └── amsalem_skill.md   # Amsalem persona
│       └── Agent4_Draft_Creator/
│           └── SKILL.md               # Draft creation logic
│
├── src/
│   ├── ui/                            # User Interface
│   │   ├── display.py                # Rich terminal UI components
│   │   ├── menu.py                   # Interactive menus
│   │   └── agent_runner.py           # Agent invocation
│   └── utils/                         # Utilities
│       ├── paths.py                  # Path management
│       ├── config.py                 # Configuration loader
│       ├── logger.py                 # Ring buffer logging
│       ├── validators.py             # Input validation
│       └── hash_utils.py             # SHA-256 hashing
│
├── config/
│   └── settings.yaml                 # Application settings
│
├── Secrets/
│   ├── credentials.json              # Gmail OAuth credentials
│   └── token.json                    # Gmail access token (auto-generated)
│
├── data/
│   └── students_mapping.xlsx         # Email → Name mapping
│
├── results/
│   ├── excel/                        # Generated Excel files
│   │   ├── Excel1.xlsx              # Email extractions
│   │   ├── Excel2.xlsx              # Repository analysis
│   │   └── Excel3.xlsx              # LLM feedback
│   ├── graphs/                       # (Future: visualizations)
│   └── examples/                     # (Future: example outputs)
│
├── temp/
│   └── repos/                        # Cloned repositories (temporary)
│
├── logs/
│   ├── config/
│   │   └── log_config.json          # Logging configuration
│   └── *.log                         # Ring buffer log files
│
├── docs/
│   ├── PRD.md                        # Product Requirements Document
│   ├── tasks.json                    # Task tracking (v3.0)
│   └── PROJECT_GUIDELINES.md         # Development guidelines
│
├── main.py                           # Application entry point
├── requirements.txt                  # Python dependencies
├── .env                              # Environment variables (gitignored)
├── .env.example                      # Environment template
├── .gitignore                        # Git ignore rules
└── README.md                         # This file
```

---

## 🔧 Troubleshooting

### Gmail Authentication Issues

**Problem:** "Failed to authenticate with Gmail API"

**Solution:**
1. Verify `Secrets/credentials.json` exists
2. Delete `Secrets/token.json` and re-authenticate
3. Run `python test_gmail_credentials.py`
4. Ensure Gmail API is enabled in Google Cloud Console

---

### Missing Gemini API Key

**Problem:** "GEMINI_API_KEY not found"

**Solution:**
1. Get API key from [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Add to `.env` file:
   ```bash
   GEMINI_API_KEY=your_actual_api_key_here
   ```

---

### Import Errors

**Problem:** `ModuleNotFoundError: No module named 'rich'`

**Solution:**
```bash
pip install -r requirements.txt
```

---

### Repository Clone Failures

**Problem:** "Failed to clone repository"

**Possible causes:**
1. **Private repository** - No access
2. **Invalid URL** - Typo or deleted repo
3. **Network issues** - Check internet connection
4. **Git not installed** - Install Git

**Solution:**
- Check repo URL in browser
- Verify network connection
- Check logs: `logs/app_*.log`

---

### Excel Files Not Created

**Problem:** Agent completes but no Excel file

**Solution:**
1. Check agent status in logs
2. Verify previous agent completed successfully
3. Check `results/excel/` directory permissions
4. Run Agent 1 with max_emails=1 to debug with a single email

---

### Persona Not Loading

**Problem:** "Failed to load persona skill"

**Solution:**
1. Verify persona file exists:
   ```bash
   ls .claude/agents/Agent3_LLM_Feedback/personas/
   ```
2. Check grade ranges in `config/settings.yaml`
3. Verify persona name matches grade category

---

### Claude Code CLI Not Found

**Problem:** `claude: command not found`

**Solution:**
1. Install Claude Code CLI:
   ```bash
   npm install -g @anthropic/claude-code
   ```
2. Verify installation:
   ```bash
   claude --version
   ```

---

## 🤝 Contributing

Contributions are welcome! Please follow these guidelines:

### Development Setup

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Install dev dependencies: `pip install -r requirements.txt`
4. Run tests: `pytest`
5. Format code: `black src/`
6. Lint: `flake8 src/`
7. Type check: `mypy src/`

### Testing

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=src tests/

# Test specific module
pytest tests/test_validators.py
```

### Code Style

- Follow PEP 8
- Use type hints
- Write docstrings (Google style)
- Keep functions < 50 lines
- Keep files < 500 lines

### Commit Messages

```
feat: add new persona skill
fix: correct grade calculation
docs: update README installation steps
refactor: simplify path management
test: add unit tests for validators
```

---

## 📊 Results

This section showcases the system in action with real examples from the automated grading pipeline.

### System Execution

The grading system successfully processes student homework submissions through all 4 agents:

**Pipeline Flow:**
1. **Agent 1** extracts 8 homework emails (L11-L18) from Gmail
2. **Agent 2** clones GitHub repositories and analyzes code quality
3. **Agent 3** generates personalized AI feedback using celebrity personas
4. **Agent 4** creates Gmail draft replies ready to send

### Screenshots

#### Main Menu Interface

*[Screenshot will be added showing the Rich terminal UI with 8 menu options]*

The interactive menu provides:
- Options 1-4: Run individual agents
- Option 5: Run all agents sequentially
- Option 6: Reset system (clear all data)
- Option 7: Display system status
- Option 8: Exit

#### Agent 1: Email Extraction

*[Screenshot will be added showing Agent 1 search parameters and email extraction process]*

**Search Parameters Used:**
- Email Subject: `GradingL19`
- Max Emails: `30`
- Results: 8 homework emails found (L11-L18)

#### Excel Output Files

##### Excel1.xlsx - Email Extraction Data

*[Screenshot will be added showing Excel1.xlsx with 7 columns]*

| email_id | received_time | email_subject | sender_email | github_url | thread_id | status |
|----------|---------------|---------------|--------------|------------|-----------|--------|
| abc123... | 2025-12-01 | AI Development Expert course - Homework - L17 | student@gmail.com | https://github.com/... | thread_xyz | Ready |

**Columns:**
- `email_id`: SHA-256 hash (unique identifier)
- `received_time`: Email timestamp
- `email_subject`: Full subject line
- `sender_email`: Student email address
- `github_url`: Extracted GitHub repository URL
- `thread_id`: Gmail thread ID for replies
- `status`: Ready or Missing: [field]

##### Excel2.xlsx - Repository Analysis

*[Screenshot will be added showing Excel2.xlsx with grade calculations]*

| email_id | github_url | total_files | total_lines | compliant_lines | grade | status |
|----------|------------|-------------|-------------|-----------------|-------|--------|
| abc123... | https://... | 10 | 1500 | 1200 | 80.0 | Ready |

**Grade Formula:**
```
compliant_files = count(files with ≤150 lines)
grade = 100 * (compliant_files / total_files)
```

##### Excel3.xlsx - AI Feedback

*[Screenshot will be added showing Excel3.xlsx with persona-based feedback]*

| email_id | grade | grade_category | persona | response | api_attempts | status |
|----------|-------|----------------|---------|----------|--------------|--------|
| abc123... | 95.0 | Excellent | Trump | "Tremendous work! ..." | 1 | Ready |

**Persona Assignment:**
- **90-100**: Trump (Enthusiastic, superlatives)
- **70-90**: Shahar Hason (Israeli comedian style)
- **55-70**: Bruce Lee (Martial arts philosophy)
- **0-55**: Dudi Amsalem (Direct politician style)

#### Gmail Integration

##### Inbox - Homework Submissions

*[Screenshot will be added showing Gmail inbox with 8 homework emails]*

Homework emails received with subjects:
- AI Development Expert course - Homework - L11 - GradingL19
- AI Development Expert course - Homework - L12 - GradingL19
- ... (L13-L18)

##### Drafts - AI-Generated Feedback

*[Screenshot will be added showing Gmail Drafts folder with generated replies]*

Draft emails created for each submission:
- Subject: Re: AI Development Expert course - Homework - L17
- Threaded replies (using thread_id)
- Personalized feedback with student name
- Not sent automatically (manual review required)

### Performance Metrics

**Processing Statistics:**
- Total emails processed: 8
- Repositories successfully cloned: 8
- AI feedback generated: 8
- Gmail drafts created: 8
- Success rate: 100%

**Execution Time:**
- Agent 1 (Email Extraction): ~10 seconds
- Agent 2 (Repository Analysis): ~45 seconds (5 concurrent workers)
- Agent 3 (AI Feedback): ~60 seconds (with API delays)
- Agent 4 (Draft Creation): ~15 seconds
- **Total Pipeline Time**: ~2 minutes 10 seconds

### Search Term Recommendations

Based on testing, the following search terms work best:

**Most Effective:**
- `GradingL19` - Finds exactly 8 emails (L11-L18)
- `Homework` - Finds all homework-related emails

**Less Effective:**
- `AI Development Expert course` - Too generic, requires max_emails ≥30

**Pro Tip:** Use specific, unique identifiers in email subjects for reliable extraction.

---

## 📝 License

MIT License - See [LICENSE](LICENSE) file for details

---

## 👤 Author

**Hadar Wayn**
- Project: L19 AI Agents Auto Homework Grading System
- Date: December 2025
- Architecture: Claude Code Agents with Dual Execution Modes

---

## 🙏 Acknowledgments

- **Claude Code** by Anthropic for agent architecture
- **Gemini AI** by Google for LLM feedback generation
- **Gmail API** for email automation
- **Rich** library for beautiful terminal UI

---

## 📚 Additional Resources

- [Claude Code Documentation](https://docs.anthropic.com/claude-code)
- [Gmail API Guide](https://developers.google.com/gmail/api)
- [Gemini API Docs](https://ai.google.dev/docs)
- [PRD.md](docs/PRD.md) - Product Requirements Document
- [tasks.json](docs/tasks.json) - Task Tracking

---

**Made with ❤️ using Claude Code Agents**
