
from src.agents import cv_reader_agent , cv_analyzer_agent , web_generator_agent
from src.tasks import reader_task , analyze_task , website_task
from crewai import Crew , Process
import pdfplumber

def read_pdf(file_path: str) -> str:
    '''Read PDF file content'''
    with pdfplumber.open(file_path) as pdf:
        return "\\n".join([page.extract_text() for page in pdf.pages])
    

cv_text = read_pdf('./CV_ML_engnieers.pdf')


crew = Crew(
    agents=[cv_reader_agent, 
            cv_analyzer_agent, 
            web_generator_agent],

    tasks=[reader_task,
            analyze_task,
            website_task],

    process=Process.sequential
)

crew_results = crew.kickoff(inputs={"cv_text": cv_text})

crew_results