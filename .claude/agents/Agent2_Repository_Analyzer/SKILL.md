# Agent 2: Repository Analyzer

**Description**: Clone GitHub repositories, analyze Python files, calculate grades based on 150-line compliance

## Responsibilities

1. Read Excel1.xlsx (only "Ready" rows)
2. Clone repositories using multi-threading (5 workers)
3. Find all Python files (.py)
4. Count lines in each file
5. Calculate grade: 100 * (compliant_lines / total_lines)
6. Create Excel2.xlsx with grade data

## Prerequisites

- Excel1.xlsx must exist in results/excel/
- Git must be installed
- temp/repos/ directory exists

## Instructions

### Step 1: Read Excel1.xlsx
```python
import openpyxl
import git
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
import time

# Load Excel1
wb = openpyxl.load_workbook('results/excel/Excel1.xlsx')
ws = wb.active

# Extract rows with status = "Ready"
ready_rows = []
for row in ws.iter_rows(min_row=2, values_only=True):
    email_id, received_time, subject, sender, hashed, github_url, thread_id, status = row
    if status == "Ready":
        ready_rows.append({
            'email_id': email_id,
            'github_url': github_url
        })

print(f"Found {len(ready_rows)} repositories to analyze")
```

### Step 2: Multi-threaded Repository Cloning
```python
def analyze_repository(email_id, github_url):
    """Analyze a single repository"""
    try:
        # Create unique directory for this repo
        repo_dir = Path(f"temp/repos/{email_id[:8]}")

        # Clone repository (timeout: 60 seconds)
        print(f"Cloning {github_url}...")
        repo = git.Repo.clone_from(github_url, repo_dir, depth=1)

        # Find all Python files
        python_files = list(repo_dir.rglob("*.py"))

        # Count lines
        total_lines = 0
        compliant_lines = 0
        file_count = 0

        for py_file in python_files:
            try:
                with open(py_file, 'r', encoding='utf-8') as f:
                    lines = len(f.readlines())
                    total_lines += lines

                    # Compliant if <= 150 lines
                    if lines <= 150:
                        compliant_lines += lines

                    file_count += 1
            except Exception:
                continue

        # Calculate grade
        if total_lines > 0:
            grade = round(100 * (compliant_lines / total_lines), 2)
        else:
            grade = 0

        return {
            'email_id': email_id,
            'github_url': github_url,
            'total_files': file_count,
            'total_lines': total_lines,
            'compliant_lines': compliant_lines,
            'grade': grade,
            'status': 'Ready'
        }

    except git.GitCommandError:
        return {
            'email_id': email_id,
            'github_url': github_url,
            'total_files': 0,
            'total_lines': 0,
            'compliant_lines': 0,
            'grade': 0,
            'status': 'Failed: clone'
        }
    except Exception as e:
        return {
            'email_id': email_id,
            'github_url': github_url,
            'total_files': 0,
            'total_lines': 0,
            'compliant_lines': 0,
            'grade': 0,
            'status': f'Failed: {str(e)[:50]}'
        }

# Process repositories in parallel (5 workers)
results = []
with ThreadPoolExecutor(max_workers=5) as executor:
    futures = {
        executor.submit(analyze_repository, row['email_id'], row['github_url']): row
        for row in ready_rows
    }

    for future in as_completed(futures):
        result = future.result()
        results.append(result)
        print(f"  ✓ {result['email_id'][:8]} - Grade: {result['grade']}")
```

### Step 3: Create Excel2.xlsx
```python
# Create workbook
wb2 = openpyxl.Workbook()
ws2 = wb2.active
ws2.title = "Repository Analysis"

# Headers
headers = [
    "email_id",
    "github_url",
    "total_files",
    "total_lines",
    "compliant_lines",
    "grade",
    "status"
]
ws2.append(headers)

# Add rows
for result in results:
    ws2.append([
        result['email_id'],
        result['github_url'],
        result['total_files'],
        result['total_lines'],
        result['compliant_lines'],
        result['grade'],
        result['status']
    ])

# Save
wb2.save('results/excel/Excel2.xlsx')
```

### Step 4: Output
```python
print(f"\n✅ Analysis complete!")
print(f"   - Total repositories: {len(results)}")
print(f"   - Successful: {sum(1 for r in results if r['status'] == 'Ready')}")
print(f"   - Failed: {sum(1 for r in results if 'Failed' in r['status'])}")
print(f"   - Average grade: {sum(r['grade'] for r in results) / len(results):.2f}")
print(f"✅ Created Excel2.xlsx")
```

## Grading Formula

```
Grade = 100 × (compliant_lines / total_lines)

Where:
- compliant_lines = sum of lines in files with ≤ 150 lines
- total_lines = sum of all lines in all .py files
```

## Example

```
Repository contains:
- main.py: 45 lines ✅ (compliant)
- utils.py: 200 lines ❌ (non-compliant)
- helpers.py: 80 lines ✅ (compliant)

Total lines = 45 + 200 + 80 = 325
Compliant lines = 45 + 80 = 125
Grade = 100 × (125 / 325) = 38.46
```

## Expected Output

**Excel2.xlsx** with columns:
- `email_id`: Links to Agent 1
- `github_url`: Repository URL
- `total_files`: Count of .py files
- `total_lines`: Sum of all lines
- `compliant_lines`: Lines in files ≤150
- `grade`: 0-100 score
- `status`: "Ready" or error message

## Error Handling

- Clone timeout (60s): Set status = "Failed: clone"
- Repository not found: Set status = "Failed: clone"
- No Python files: grade = 0, status = "Ready"
- File read errors: Skip file, continue
- Thread failures: Isolated per repository

## Success Criteria

- Excel2.xlsx exists
- All ready rows from Excel1 processed
- Grades calculated correctly
- Multi-threading completed without crashes
