import os
from dotenv import load_dotenv 
from langchain_openai import ChatOpenAI

load_dotenv()

llm = ChatOpenAI(
  base_url=os.getenv("TOGETHER_BASE_URL"),
  api_key=os.getenv("TOGETHER_API_KEY"),
  model=os.getenv("GEMMA_4")
)