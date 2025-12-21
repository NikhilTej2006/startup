from app.mcp.context import StartupContext
from app.services.llm_router import LLMRouter
from app.utils.logger import logger
import json

class SWOTAgent:
    name = "swot_agent"

    async def run(self, context: StartupContext) -> StartupContext:
        logger.info("SWOT Agent started")
        context.current_agent = self.name

        market = context.market or {}
        competition = context.competition or {}

        prompt = f"""
You are a senior startup strategist.

Perform a deep SWOT analysis using ONLY the information provided.
Do NOT invent facts. If something is unclear, state assumptions explicitly.

Startup Idea:
{context.idea}

Domain:
{context.domain}

Market Analysis:
{market}

Competition Analysis:
{competition}

Return STRICT JSON ONLY:

{{
  "strengths": [],
  "weaknesses": [],
  "opportunities": [],
  "threats": [],
  "confidence_level": 0.0
}}
"""

        try:
            response = await LLMRouter.generate(prompt, agent=self.name)
            data = json.loads(response)

        except Exception as e:
            logger.error(f"SWOT agent fallback triggered: {e}")
            data = {
                "strengths": [],
                "weaknesses": [],
                "opportunities": [],
                "threats": [],
                "confidence_level": None,
                "error": "LLM unavailable"
            }

        context.swot = data
        context.completed_agents.append(self.name)

        logger.info("SWOT Agent completed")
        return context
