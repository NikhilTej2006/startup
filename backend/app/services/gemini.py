from google import genai
from app.config import settings

client = genai.Client(api_key=settings.GEMINI_API_KEY)

async def gemini_generate(prompt: str) -> str:
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt
    )
    return response.text
