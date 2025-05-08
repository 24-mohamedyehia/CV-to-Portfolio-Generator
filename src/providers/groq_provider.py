from crewai import LLM
import os
from dotenv import load_dotenv
load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")

"""
Here is the list of available models:

llama-3.3-70b-versatile
gemma2-9b-it
llama3-70b-8192

"""

llama_3_3_70B_llm = LLM(
    model="groq/llama-3.3-70b-versatile",
    temperature=0,
    api_key=groq_api_key,
)

llama_4_llm = LLM(
    model="groq/meta-llama/llama-4-scout-17b-16e-instruct",
    temperature=0,
    api_key=groq_api_key
)
