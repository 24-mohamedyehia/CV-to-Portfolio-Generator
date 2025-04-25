# agents/web_generator_agent.py
from crewai import Agent, Task
import os
from src.agents.llms import basic_llm
output_dir = "src/ai-agent-output"

web_generator = Agent(
    role='Website Generator',
    goal='Generate a modern portfolio website using extracted CV data',
    backstory='You are a talented frontend developer who creates beautiful portfolios.',
    llm= basic_llm,
    verbose=True
)

website_task = Task(
    description= '/n'.join(["Use extracted data to build a professional portfolio webpage.",
                            "You have to use Bootstrap CSS framework for a better UI."]),
    expected_output="A professional HTML page for the protofolio webpage",
    output_file=os.path.join(output_dir, "step_3_website.html"),
    agent=web_generator
)