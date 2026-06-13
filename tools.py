import requests
import os
from langchain.tools import tool
from langchain_tavily import TavilySearch

@tool(
    "calculator",
    description=(
        "Performs arithmetic and mathematical calculations. "
        "Use this tool for evaluating math expressions, basic arithmetic, "
        "scientific calculations, or solving numeric problems. "
        "Input should be a valid mathematical expression as a string "
        "(e.g., '25 * 4 + 10', 'sqrt(16)', '100 / 5'). "
        "Do NOT use for general reasoning, factual queries, or web lookups."
    )
)
def calc(expression: str) -> str:
    """Evaluate mathematical expressions."""
    return str(eval(expression))


@tool(
    "web_search",
    description=(
        "Searches the web for up-to-date or factual information. "
        "Use this tool when the question requires recent data, external knowledge, "
        "current events, factual lookups, company/product information, "
        "documentation, or anything not guaranteed to be in memory. "
        "Input should be a concise search query "
        "(e.g., 'latest LangChain version', 'weather in Hyderabad'). "
        "Do NOT use for math calculations or simple reasoning."
    )
)
def web_search(query: str):
    response = TavilySearch(
        max_results=3,
        topic="general",
        tavily_api_key=os.getenv("TAVILY_API_KEY")
        
    )
    return response.invoke(query)


@tool(
    "weather",
    description=(
        "Fetches real-time weather information for a specific location. "
        "Use this tool when the user asks about current weather conditions, "
        "temperature, humidity, rain, wind, or weather forecasts for a city or place. "
        "Input should be a location name as a string "
        "(e.g., 'Hyderabad', 'New York', 'London'). "
        "Use for weather-related questions like "
        "'What's the weather in Mumbai?' or "
        "'Is it raining in Bangalore?'. "
        "Do NOT use for general knowledge, math, or non-weather queries."
    )
)
def get_weather(location: str) -> str:
    url = f"https://wttr.in/{location}?format=j1"
    response = requests.get(url, timeout=10)

    response.raise_for_status()
    data = response.json()

    return data

# calc.invoke("2+2")
# web_search.invoke("HDFC")
# get_weather.invoke("Hyderabad")
