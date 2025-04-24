from crewai import Task
from agents import cv_reader_agent , cv_analyzer_agent , web_generator_agent
import os


output_dir = "./ai-agent-output"
os.makedirs(output_dir, exist_ok=True)
