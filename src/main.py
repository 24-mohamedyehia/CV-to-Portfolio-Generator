# main.py
from agents import cv_reader, cv_analyzer, web_generator
from agents import reader_task, analyze_task, website_task
from crewai import Crew , Process
import pdfplumber
import os

def read_pdf(file_path: str) -> str:
    '''Read PDF file content'''
    with pdfplumber.open(file_path) as pdf:
        return "\\n".join([page.extract_text() for page in pdf.pages])


cv_text = read_pdf('./1727444550333.pdf')

output_dir = "src/ai-agent-output"
os.makedirs(output_dir, exist_ok=True)


crew = Crew(
agents=[cv_reader, 
        cv_analyzer, 
        web_generator],

tasks=[reader_task,
        analyze_task,
        website_task],

process=Process.sequential
)

crew_results = crew.kickoff(inputs={"cv_text": cv_text})

crew_results