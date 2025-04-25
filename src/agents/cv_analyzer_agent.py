# agents/cv_analyzer_agent.py
from crewai import Agent, Task
import os
from src.agents.llms import basic_llm
output_dir = "src/ai-agent-output"

cv_analyzer = Agent(
    role='CV Analyzer Agent',
    goal='Extract skills, experience, education and projects from the CV text.',
    backstory='You are a professional recruiter who knows how to read and understand CVs.',
    llm= basic_llm,
    verbose=True
)

analyze_task = Task(
    description="Analyze the CV plan text",
    expected_output="JSON with skills, experience, education, and projects.",
    output_file=os.path.join(output_dir, "step_2_analysis.json"),
    agent=cv_analyzer
)