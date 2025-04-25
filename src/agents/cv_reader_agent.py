# agents/cv_reader_agent.py
from crewai import Agent, Task 
import os
from src.agents.llms import basic_llm
output_dir = "src/ai-agent-output"

cv_reader = Agent(
    role=  "CV Reader Agent",
    goal=  "Extract text content from the uploaded CV",
    backstory= "Expert at reading and extracting content from CVs",
    llm=  basic_llm,
    verbose= True
)



reader_task = Task(
    description="Read this {cv_text} CV and extract the text content.",
    expected_output="Plain text of the CV.",
    output_file=os.path.join(output_dir, "step_1_cv_text.txt"),
    agent=cv_reader
)
