# agents/cv_reader_agent.py
from . import Agent , basic_llm 

cv_reader_agent = Agent(
    role=  "CV Reader Agent",
    goal=  "Extract text content from the uploaded CV",
    backstory= "Expert at reading and extracting content from CVs",
    llm=  basic_llm,
    verbose= True
)

