import requests
from app.config import settings

HF_API_URL = "https://api-inference.huggingface.co/models/HuggingFaceH4/zephyr-7b-beta"

headers = {
    "Authorization": f"Bearer {settings.HF_API_KEY}"
}

async def hf_generate(prompt: str) -> str:
    payload = {
        "inputs": prompt,
        "parameters": {
            "temperature": 0.7,
            "max_new_tokens": 600
        }
    }

    response = requests.post(HF_API_URL, headers=headers, json=payload, timeout=30)
    response.raise_for_status()

    data = response.json()
    return data[0]["generated_text"]
