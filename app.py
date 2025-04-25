from flask import Flask, render_template, request, send_file, redirect, flash
import os
from werkzeug.utils import secure_filename
from src.agents import cv_reader, cv_analyzer, web_generator
from src.agents import reader_task, analyze_task, website_task
from crewai import Crew, Process
import pdfplumber

UPLOAD_FOLDER = 'uploads'
OUTPUT_FOLDER = 'src/ai-agent-output'
ALLOWED_EXTENSIONS = {'pdf'}

app = Flask(__name__)
app.secret_key = 'supersecretkey'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def read_pdf(file_path: str) -> str:
    with pdfplumber.open(file_path) as pdf:
        return "\n".join([page.extract_text() for page in pdf.pages])

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'cv_file' not in request.files:
            flash('No file selected')
            return redirect(request.url)
        file = request.files['cv_file']
        if file.filename == '':
            flash('No file selected')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
            # Read the PDF file
            cv_text = read_pdf(file_path)
            crew = Crew(
                agents=[cv_reader, cv_analyzer, web_generator],
                tasks=[reader_task, analyze_task, website_task],
                process=Process.sequential
            )
            crew.kickoff(inputs={"cv_text": cv_text})
            # Get the result HTML file
            result_html = os.path.join(OUTPUT_FOLDER, 'step_3_website.html')
            if os.path.exists(result_html):
                return render_template('result.html', website_file='step_3_website.html')
            else:
                flash('Failed to generate website. Please try again :)')
                return redirect(request.url)
        else:
            flash('Invalid file type! Please upload a PDF file.')
            return redirect(request.url)
    return render_template('index.html')

@app.route('/download/<filename>')
def download_file(filename):
    file_path = os.path.join(OUTPUT_FOLDER, filename)
    return send_file(file_path, as_attachment=True)

@app.route('/preview/<filename>')
def preview_file(filename):
    file_path = os.path.join(OUTPUT_FOLDER, filename)
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    return content

if __name__ == '__main__':
    app.run(debug=True)
ذ