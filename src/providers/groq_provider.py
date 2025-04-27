
from crewai import LLM
import os
from dotenv import load_dotenv
load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")

"""
Here is the list of available models:

llama-3.3-70b-versatile
qwen-qwq-32b

"""

basic_llm = LLM(
    model="groq/llama-3.3-70b-versatile",
    temperature=0,
    api_key=groq_api_key
)
