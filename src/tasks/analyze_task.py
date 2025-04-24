from . import Task , os , output_dir , cv_analyzer_agent

analyze_task = Task(
    description="Analyze this CV text: {cv_text}",
    expected_output="JSON with skills, experience, education, and projects.",
    output_file=os.path.join(output_dir, "step_2_analysis.json"),
    agent=cv_analyzer_agent
)