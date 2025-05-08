# agent/__init__.py
from .reader_analyzer_agent import reader_analyzer, json_extraction_task
from .html_generator_agent import html_generator, html_generator_task
from src.providers import llama_3_3_70B_llm , llama_4_llm