import os
import requests

TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

def web_search(query: str, k: int = 5):
    url = "https://api.tavily.com/search"
    payload = {
        "api_key": TAVILY_API_KEY,
        "query": query,
        "search_depth": "basic",
        "max_results": k
    }
    response = requests.post(url, json=payload)
    return response.json()
