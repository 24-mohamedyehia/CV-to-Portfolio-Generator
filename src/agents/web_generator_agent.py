# agents/web_generator_agent.py
from . import Agent , basic_llm

web_generator_agent = Agent(
    role='Website Generator',
    goal='Generate a modern portfolio website using extracted CV data',
    backstory='You are a talented frontend developer who creates beautiful portfolios.',
    llm= basic_llm,
    verbose=True
)