from app.services.gemini import gemini_generate
from app.services.hf import hf_generate
from app.utils.logger import logger

class LLMRouter:

    @staticmethod
    # app/services/llm_router.py

    async def generate(prompt: str, agent: str):
        try:
            logger.info(f"LLMRouter → Gemini for {agent}")
            return await gemini_generate(prompt)

        except Exception as e:
            logger.warning(f"LLM unavailable for {agent}: {e}")
            raise RuntimeError("LLM temporarily unavailable")
