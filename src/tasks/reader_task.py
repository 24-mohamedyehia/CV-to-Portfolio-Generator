from . import Task , os , output_dir , cv_reader_agent

reader_task = Task(
    description="Read the CV and extract the text content.",
    expected_output="Plain text of the CV.",
    output_file=os.path.join(output_dir, "step_1_cv_text.txt"),
    agent=cv_reader_agent
)
