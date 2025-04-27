# agents/cv_reader_agent.py
from crewai import Agent, Task 
from crewai.tools import tool
from pydantic import BaseModel , Field
from typing import List, Optional
import pdfplumber
import os
from src.agents.llms import basic_llm

# Define output directory
output_dir = "src/ai-agent-output"

# Define tools for reading PDF files
@tool
def read_pdf(file_path: str) -> str:
    '''this tool reads a PDF file and returns its content as a string.'''
    with pdfplumber.open(file_path) as pdf:
        return "\\n".join([page.extract_text() for page in pdf.pages])

# Define Agent for reading PDF files
reader_analyzer = Agent(
    role=  "CV Reader Analyzer Agent",
    goal=  '\n'.join([
        "Extract clean and complete structured data from CV in PDF format",
        "To provide a list of a JSON file with the extracted data"
    ]),
    backstory= "You're an AI expert in reading CVs (PDF format) and converting them into organized JSON format, perfect for using in web generation.",
    llm=  basic_llm,
    verbose= True,
    tools= [read_pdf]
)

# Define Task for JSON data extraction
json_extraction_task = Task(
    description='\n'.join([
        "Your job is to carefully read and analyze the uploaded CV {cv_pdf} and extract the following structured data as a JSON dictionary:",
        "name: Full name of the person.",
        "contact: Object with keys (email, phone, linkedin, github, twitter, website if available).",
        "location: City and country where the person is based (if available).",
        "summary: Short personal statement or career summary.",
        "skills: List of technical and soft skills.",
        "experience: List of past jobs, each one should include:",
        "company: Company name.",
        "position: Job title.",
        "duration: Full string of date range (e.g. Jan 2020 – Mar 2023).",
        "location: City and country of the company (if available).",
        "description: Description of responsibilities and achievements.",
        "education: List of education entries, each one should include:",
        "degree: Degree or certificate.",
        "university: Name of institution.",
        "year: Graduation year or duration string.",
        "location: City and country of the institution (if available).",
        "certifications: List of certificates, each one should include:",
        "name: Certificate title.",
        "issuer: Organization that issued it.",
        "date: Issuance date (if available).",
        "languages: List of languages and proficiency levels.",
        "projects: List of personal/professional projects, each one should include:",
        "name: Project title.",
        "description: What it does and its impact.",
        "tech_stack: List of technologies used.",
        "publications: List of publications (if any), each one should include:",
        "title: Title of the publication.",
        "publisher: Where it was published.",
        "date: Publication date.",

        "volunteer_work: List of volunteer activities, each one should include:",
        "organization: Organization name.",
        "role: Volunteer role or title.",
        "duration: Full string of date range.",
        "description: Brief description of activities.",

        "awards: List of awards or honors, each one should include:",
        "name: Award name.",
        "issuer: Organization giving the award.",
        "date: Award date (if available).",
        "interests: List of hobbies or interests.",

        "references: (Optional) List of references if provided, each one should include:",
        "name: Referee's full name.",
        "position: Referee's position.",
        "contact_info: Email or phone of the referee.",
        "field: The person's area of expertise or career field, based on their experience and education."

        "Return the result in a clean JSON format matching this structure exactly"
    ]),
    expected_output="A JSON object containing a list of all extracted data. ",
    output_file=os.path.join(output_dir, "step_1_cv_data.json"),
    output_json= None,
    agent=reader_analyzer
)


