# agents/cv_analyzer_agent.py
from . import Agent , basic_llm

cv_analyzer_agent = Agent(
    role='CV Analyzer Agent',
    goal='Extract skills, experience, education and projects from the CV text.',
    backstory='You are a professional recruiter who knows how to read and understand CVs.',
    llm= basic_llm,
    verbose=True
)
