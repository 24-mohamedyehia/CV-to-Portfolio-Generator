from . import Task , os , output_dir , web_generator_agent

website_task = Task(
    description="Use extracted data to build a simple portfolio webpage.",
    expected_output="HTML code or website content in JSON format.",
    output_file=os.path.join(output_dir, "step_3_website.json"),
    agent=web_generator_agent
)