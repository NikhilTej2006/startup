from groq import Groq
from app.config import settings
import asyncio
from app.utils.logger import logger  # use your logger instead of print

client = Groq(api_key=settings.GROQ_API_KEY)

async def generate(agent_name: str, system: str, prompt: str) -> str:
    """
    Async wrapper for Groq LLM chat completion.
    Returns the assistant's reply as a string.
    Handles errors gracefully and always returns a string.
    """
    loop = asyncio.get_event_loop()

    try:
        response = await loop.run_in_executor(
            None,
            lambda: client.chat.completions.create(
                model="meta-llama/llama-4-maverick-17b-128e-instruct",  # best LLaMA-4 instruct model
                messages=[
                    {"role": "system", "content": system},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.3,
                max_tokens=8192  # ensure enough output length
            )
        )

        # Validate response safely
        if response and hasattr(response, "choices") and response.choices:
            content = getattr(response.choices[0].message, "content", "")
            if content:
                return content.strip()

        # fallback empty string if response is invalid
        logger.warning(f"[LLMRouter] Empty response from {agent_name}")
        return ""

    except Exception as e:
        # Log detailed error but return empty string
        logger.error(f"[LLMRouter] Error generating response for {agent_name}: {e}")
        return ""
