import json
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parents[1]

PROMPT_DIR = BASE_DIR / "app" / "prompts"


def load_prompt(filename):
    """
    Load a JSON prompt file.
    """

    file_path = PROMPT_DIR / filename

    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)

    return data["system_prompt"]


def build_prompt(filename, student_profile, career_goal):
    """
    Combine the selected AI prompt with
    the student's profile and career goal.
    """

    system_prompt = load_prompt(filename)

    prompt = f"""
{system_prompt}

STUDENT PROFILE:

{json.dumps(
    student_profile,
    indent=2,
    ensure_ascii=False
)}

CAREER GOAL:

{career_goal}
"""

    return prompt
