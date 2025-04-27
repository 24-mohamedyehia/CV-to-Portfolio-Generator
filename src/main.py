# main.py
from agents import reader_analyzer, json_extraction_task
from crewai import Crew , Process

crew = Crew(
agents=[
    reader_analyzer
],

tasks=[
    json_extraction_task
],

process=Process.sequential  
)

cv_pdf = 'D:\my_laptob\Projects\CV-to-Portfolio-Generator\CV_ML_engnieers.pdf'

crew_results = crew.kickoff(inputs={"cv_pdf": cv_pdf})
