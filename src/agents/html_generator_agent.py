import os
import pdfplumber
from crewai import Agent, Task
from crewai.tools import tool
from src.providers import basic_llm

output_dir = "src/ai-agent-output"

# Define tools for reading PDF files
@tool
def read_pdf(file_path: str) -> str:
    '''this tool used for reading a PDF file and returns its content as a string or text'''
    with pdfplumber.open(file_path) as pdf:
        return "\\n".join([page.extract_text() for page in pdf.pages])

html_generator = Agent(
    role="Professional Portfolio websites Generator",
    goal="Generate a fully responsive, beautiful, and modern portfolio website from provided CV data and CSS theme.",
    backstory=(
        "You are a top-notch frontend developer and designer. "
        "Your task is to create stunning, elegant, and professional portfolios that impress recruiters and clients. "
        "You use Bootstrap, TailwindCSS, and write clean semantic HTML. "
        "You care about colors, fonts, margins, responsiveness, and accessibility."
    ),
    tools=[read_pdf],
    llm=basic_llm,
    verbose=True,
    max_iter=2,
    max_rpm=29
)

html_generator_task = Task(
    description="\n".join([
        "Your job is to carefully read and analyze the uploaded CV {cv_pdf} and generate a single HTML file that includes all sections of the CV.",
        "- <head> includes Bootstrap and Tailwind CSS via CDN.",
        "- <style> block contains the theme CSS inline, using the design specifications (colors, fonts, layout).",
        "- <body> sections: About Me, Skills, Experience, Education, Projects, Contact.",
        "- Each section should be styled consistently with the theme colors and fonts.",
        "- Use responsive layout (mobile, tablet, desktop friendly).",
        "- Add basic JavaScript at the bottom for smooth scroll and navbar link highlighting.",
        "- Ensure the final page is self-contained, no external CSS except Bootstrap/Tailwind.",
        "Important Notes:",
        "- Use the actual CV data from the JSON file for real content. Do not use placeholder text or Lorem Ipsum.",
        "- Use the provided theme colors and fonts from the CSS file.",
        "- Follow the section layout and design guidelines based on the theme.",
        "- Make sure to include all relevant sections from the CV data: skills, experience, education, projects, etc.",
        "- Add appropriate icons for contact information and social media links."
    ]),
    expected_output="A professional single HTML file with embedded CSS and JS, following the design specifications and using the actual CV data.",
    output_file=os.path.join(output_dir, "final_portfolio.html"),
    agent=html_generator
)