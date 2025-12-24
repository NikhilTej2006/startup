import os
from groq import Groq
from app.utils.logger import logger

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

async def groq_generate(
    prompt: str,
    system: str = "You are a helpful AI agent.",
    model: str = "meta-llama/llama-4-maverick-7b-instruct",
    temperature: float = 0.4,
    max_tokens: int = 1024,
):
    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": system},
                {"role": "user", "content": prompt}
            ],
            temperature=temperature,
            max_tokens=max_tokens
        )

        return response.choices[0].message.content

    except Exception as e:
        logger.error(f"Groq LLM failure: {e}")
        raise
