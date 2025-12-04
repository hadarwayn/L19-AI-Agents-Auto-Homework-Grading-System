"""
Agent 3 Feedback Generator

Generates personalized AI feedback using Gemini API with persona-based responses.

Author: Hadar Wayn
Date: December 2025
"""

import time
from pathlib import Path
import google.generativeai as genai
from rich.console import Console

console = Console()


def generate_feedback(email_id: str, grade: float, github_url: str, gemini_api_key: str) -> dict:
    """Generate personalized feedback for a submission"""
    # Determine grade category and persona
    category, persona = _get_grade_category(grade)

    console.print(f"[*] Processing {email_id[:8]} - Grade: {grade}% - Persona: {persona}")

    # Configure Gemini
    genai.configure(api_key=gemini_api_key)
    model = genai.GenerativeModel('gemini-2.5-flash')

    # Generate feedback with retry
    response, attempts = _generate_with_retry(model, persona, grade, github_url)

    # Determine status
    if response:
        status = "Ready"
        console.print(f"  [+] Generated feedback ({attempts} attempt(s))")
    else:
        status = "Missing: reply"
        console.print(f"  [!] Failed to generate feedback")

    return {
        'email_id': email_id,
        'grade': grade,
        'grade_category': category,
        'persona': persona,
        'response': response,
        'api_attempts': attempts,
        'status': status
    }


def _get_grade_category(grade: float) -> tuple:
    """Determine grade category and assigned persona"""
    if 90 <= grade <= 100:
        return 'excellent', 'trump'
    elif 70 <= grade < 90:
        return 'good', 'hason'
    elif 55 <= grade < 70:
        return 'pass', 'lee'
    else:
        return 'needs_work', 'amsalem'


def _load_persona_prompt(persona_name: str) -> str:
    """Load persona skill file content"""
    skill_path = Path(f'.claude/agents/Agent3_LLM_Feedback/personas/{persona_name}_skill.md')

    if not skill_path.exists():
        raise FileNotFoundError(f"Persona skill file not found: {skill_path}")

    with open(skill_path, 'r', encoding='utf-8') as f:
        return f.read()


def _generate_with_retry(model, persona_name: str, grade: float, github_url: str, max_retries: int = 3) -> tuple:
    """Generate feedback with exponential backoff retry"""
    # Load persona prompt
    try:
        persona_prompt = _load_persona_prompt(persona_name)
    except FileNotFoundError as e:
        console.print(f"  [!] {e}")
        return "", max_retries

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

    # Retry loop with exponential backoff
    for attempt in range(max_retries):
        try:
            # Generate response
            response = model.generate_content(prompt)
            text = response.text.strip()

            if text:
                return text, attempt + 1

        except Exception as e:
            console.print(f"  [!] Attempt {attempt + 1} failed: {str(e)[:50]}")

            if attempt < max_retries - 1:
                # Exponential backoff: 1s, 2s, 4s
                wait_time = 2 ** attempt
                time.sleep(wait_time)
            else:
                # Final attempt failed
                return "", max_retries

    return "", max_retries
