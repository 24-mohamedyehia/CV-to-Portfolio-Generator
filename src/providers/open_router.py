from crewai import LLM
import os
from dotenv import load_dotenv
load_dotenv()
open_router_api = os.getenv("OPEN_ROUTER_API_KEY")


basic_llm = LLM(
    model="openrouter/deepseek/deepseek-chat-v3-0324:free",
    base_url="https://openrouter.ai/api/v1",
    api_key=open_router_api,
    temperature=0.7
)