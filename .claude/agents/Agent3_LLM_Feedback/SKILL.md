# Agent 3: LLM Feedback Generator

**Description**: Generate personalized AI feedback using Gemini API with persona-based responses

## Responsibilities

1. Read Excel2.xlsx (only "Ready" rows)
2. Determine grade category for each submission
3. Load appropriate persona skill based on grade
4. Generate AI feedback using Gemini API
5. Handle API failures with retry logic
6. Create Excel3.xlsx with feedback data

## Grade Categories & Personas

| Grade Range | Category | Persona | Skill File |
|-------------|----------|---------|------------|
| 90-100 | Excellent | Donald Trump | personas/trump_skill.md |
| 70-90 | Good | Shahar Hason | personas/hason_skill.md |
| 55-70 | Pass | Bruce Lee | personas/lee_skill.md |
| 0-55 | Needs Work | Dudi Amsalem | personas/amsalem_skill.md |

## Prerequisites

- Excel2.xlsx must exist
- Gemini API key configured in .env
- Persona skill files exist in personas/

## Instructions

### Step 1: Read Excel2.xlsx
```python
import openpyxl
import google.generativeai as genai
import os
from pathlib import Path
import time

# Configure Gemini
genai.configure(api_key=os.getenv('GEMINI_API_KEY'))
model = genai.GenerativeModel('gemini-1.5-flash')

# Load Excel2
wb = openpyxl.load_workbook('results/excel/Excel2.xlsx')
ws = wb.active

# Extract rows with status = "Ready"
ready_rows = []
for row in ws.iter_rows(min_row=2, values_only=True):
    email_id, github_url, total_files, total_lines, compliant_lines, grade, status = row
    if status == "Ready":
        ready_rows.append({
            'email_id': email_id,
            'github_url': github_url,
            'grade': grade
        })

print(f"Found {len(ready_rows)} submissions to generate feedback for")
```

### Step 2: Determine Grade Category
```python
def get_grade_category(grade):
    """Determine grade category"""
    if 90 <= grade <= 100:
        return 'excellent', 'trump'
    elif 70 <= grade < 90:
        return 'good', 'hason'
    elif 55 <= grade < 70:
        return 'pass', 'lee'
    else:
        return 'needs_work', 'amsalem'
```

### Step 3: Load Persona Skill
```python
def load_persona_prompt(persona_name):
    """Load persona skill file and extract prompt template"""
    skill_path = Path(f'.claude/agents/Agent3_LLM_Feedback/personas/{persona_name}_skill.md')

    with open(skill_path, 'r') as f:
        skill_content = f.read()

    # The skill file contains the persona prompt template
    # Extract it and return
    return skill_content
```

### Step 4: Generate Feedback with Retry
```python
def generate_feedback_with_retry(persona_name, grade, github_url, max_retries=3):
    """Generate feedback with exponential backoff retry"""

    # Load persona prompt
    persona_prompt = load_persona_prompt(persona_name)

    # Create final prompt
    prompt = f"""
{persona_prompt}

Assignment Details:
- Repository: {github_url}
- Grade: {grade}/100
- Grade based on code structure compliance (files under 150 lines)

Generate a personalized feedback message (2-3 sentences) in the persona's style.
Focus on encouragement and specific advice based on the grade.
"""

    # Retry loop
    for attempt in range(max_retries):
        try:
            # Generate response
            response = model.generate_content(prompt)
            text = response.text.strip()

            if text:
                return text, attempt + 1

        except Exception as e:
            print(f"  ⚠ Attempt {attempt + 1} failed: {e}")

            if attempt < max_retries - 1:
                # Exponential backoff: 1s, 2s, 4s
                wait_time = 2 ** attempt
                time.sleep(wait_time)
            else:
                # Final attempt failed
                return "", max_retries

    return "", max_retries
```

### Step 5: Process All Submissions
```python
results = []

for row in ready_rows:
    email_id = row['email_id']
    grade = row['grade']
    github_url = row['github_url']

    # Determine persona
    category, persona = get_grade_category(grade)

    print(f"Processing {email_id[:8]} - Grade: {grade} - Persona: {persona}")

    # Generate feedback
    response, attempts = generate_feedback_with_retry(persona, grade, github_url)

    # Determine status
    if response:
        status = "Ready"
    else:
        status = "Missing: reply"

    results.append({
        'email_id': email_id,
        'grade': grade,
        'grade_category': category,
        'persona': persona,
        'response': response,
        'api_attempts': attempts,
        'status': status
    })

    # Delay between API calls
    time.sleep(2)
```

### Step 6: Create Excel3.xlsx
```python
# Create workbook
wb3 = openpyxl.Workbook()
ws3 = wb3.active
ws3.title = "LLM Feedback"

# Headers
headers = [
    "email_id",
    "grade",
    "grade_category",
    "persona",
    "response",
    "api_attempts",
    "status"
]
ws3.append(headers)

# Add rows
for result in results:
    ws3.append([
        result['email_id'],
        result['grade'],
        result['grade_category'],
        result['persona'],
        result['response'],
        result['api_attempts'],
        result['status']
    ])

# Save
wb3.save('results/excel/Excel3.xlsx')
```

### Step 7: Output
```python
print(f"\n✅ Feedback generation complete!")
print(f"   - Total submissions: {len(results)}")
print(f"   - Successful: {sum(1 for r in results if r['status'] == 'Ready')}")
print(f"   - Failed: {sum(1 for r in results if r['status'] == 'Missing: reply')}")
print(f"   - Personas used:")
for persona in ['trump', 'hason', 'lee', 'amsalem']:
    count = sum(1 for r in results if r['persona'] == persona)
    print(f"     • {persona}: {count}")
print(f"✅ Created Excel3.xlsx")
```

## Expected Output

**Excel3.xlsx** with columns:
- `email_id`: Links to previous agents
- `grade`: From Agent 2
- `grade_category`: excellent/good/pass/needs_work
- `persona`: trump/hason/lee/amsalem
- `response`: AI-generated feedback (or empty)
- `api_attempts`: Number of API calls made
- `status`: "Ready" or "Missing: reply"

## Retry Logic

- **Max retries**: 3
- **Backoff**: Exponential (1s, 2s, 4s)
- **Final failure**: Empty response, status = "Missing: reply"
- **Between calls**: 2 second delay

## Error Handling

- API rate limits: Retry with backoff
- Network errors: Retry with backoff
- Invalid responses: Retry
- Max retries exceeded: Empty response
- Continue processing remaining submissions

## Success Criteria

- Excel3.xlsx exists
- All ready rows from Excel2 processed
- Personas correctly selected per grade range
- Retry logic handled API failures
- No empty responses unless max retries exceeded
