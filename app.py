import json
from pathlib import Path
import streamlit as st

BASE_DIR = Path(__file__).resolve().parent

st.set_page_config(
    page_title="AspiraPath AI",
    page_icon="🚀",
    layout="wide"
)

st.title("🚀 AspiraPath AI")
st.subheader("From Aspiration to Achievable")
st.write(
    "A constraint-aware GenAI career navigator that helps women "
    "turn career aspirations into realistic action plans."
)

# -------------------------------
# Load sample profile
# -------------------------------

profile_file = (
    BASE_DIR /
    "app" /
    "sample_data" /
    "sample_student_profile.json"
)

with open(profile_file, "r", encoding="utf-8") as file:
    default_profile = json.load(file)

# -------------------------------
# Student Profile
# -------------------------------

st.sidebar.header("👩 Student Profile")

education = st.sidebar.text_input(
    "Education",
    default_profile["education"]
)

skills = st.sidebar.text_input(
    "Current Skills",
    ", ".join(default_profile["current_skills"])
)

target_role = st.sidebar.text_input(
    "Target Career",
    default_profile["target_role"]
)

budget = st.sidebar.number_input(
    "Learning Budget (₹)",
    min_value=0,
    value=default_profile["budget_inr"],
    step=1000
)

hours_per_week = st.sidebar.number_input(
    "Available Hours / Week",
    min_value=1,
    value=default_profile["hours_per_week"]
)

timeline = st.sidebar.number_input(
    "Target Timeline (Months)",
    min_value=1,
    value=default_profile["timeline_months"]
)

language = st.sidebar.selectbox(
    "Preferred Language",
    ["English", "Telugu"]
)

# -------------------------------
# Profile object
# -------------------------------

student_profile = {
    "education": education,
    "current_skills": [
        skill.strip()
        for skill in skills.split(",")
        if skill.strip()
    ],
    "target_role": target_role,
    "budget_inr": budget,
    "hours_per_week": hours_per_week,
    "timeline_months": timeline,
    "language": language
}

# -------------------------------
# Career Goal
# -------------------------------

st.header("🎯 Career Aspiration")

career_goal = st.text_area(
    "Tell us about your career goal",
    placeholder="Example: I want to become an AI Engineer but I don't know where to start."
)

# -------------------------------
# AI Modules
# -------------------------------

st.header("🤖 AI Career Modules")

module = st.selectbox(
    "Choose a module",
    [
        "Career Analysis",
        "Skill Gap Analysis",
        "Career Roadmap",
        "Weekly Planner",
        "Portfolio Project",
        "Career Readiness",
        "What-If Simulator",
        "Alternative Careers"
    ]
)

# -------------------------------
# Prompt mapping
# -------------------------------

prompt_mapping = {
    "Career Analysis": "career_analysis.json",
    "Skill Gap Analysis": "skill_gap.json",
    "Career Roadmap": "career_roadmap.json",
    "Weekly Planner": "weekly_planner.json",
    "Portfolio Project": "project_generator.json",
    "Career Readiness": "readiness_score.json",
    "What-If Simulator": "what_if_simulator.json",
    "Alternative Careers": "alternative_career.json"
}

# -------------------------------
# Generate Prompt
# -------------------------------

if st.button("🚀 Generate Career Guidance"):

    prompt_file = (
        BASE_DIR /
        "app" /
        "prompts" /
        prompt_mapping[module]
    )

    with open(prompt_file, "r", encoding="utf-8") as file:
        prompt_data = json.load(file)

    system_prompt = prompt_data["system_prompt"]

    final_prompt = f"""
{system_prompt}

STUDENT PROFILE:

{json.dumps(student_profile, indent=2, ensure_ascii=False)}

CAREER GOAL:

{career_goal}

Provide the response in {language}.
"""

    st.success("Career guidance prompt generated successfully!")

    st.subheader("Generated AI Prompt")

    st.code(
        final_prompt,
        language="text"
    )

# -------------------------------
# Privacy Notice
# -------------------------------

st.divider()

st.caption(
    "🔒 Privacy: Do not enter passwords, bank details, government ID numbers "
    "or other unnecessary sensitive information."
)

st.caption(
    "⚠️ AspiraPath AI provides career guidance and does not guarantee "
    "employment, salary, admission or certification."
)
