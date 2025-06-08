from flask import Flask, render_template, request, send_file, redirect, flash
from werkzeug.utils import secure_filename
from src.agents import html_generator ,html_generator_task
from crewai import Crew, Process
from utils import clean_output
import os

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
            
            crew = Crew(
                agents=[html_generator],
                tasks=[html_generator_task],
                process=Process.sequential,
                verbose=True
            )
            cv_text = file_path
            crew.kickoff(inputs={"cv_pdf": cv_text})
            # Get the result HTML file
            result_html = os.path.join(OUTPUT_FOLDER, 'final_portfolio.html')
            clean_output(result_html)  # Clean the output file

            if os.path.exists(result_html):
                return render_template('result.html', website_file='final_portfolio.html')
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