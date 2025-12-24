from app.mcp.context import StartupContext
from app.services.llm_router import generate
from app.utils.logger import logger
from app.utils.llm_utils import extract_json

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
            response = await generate(
                agent_name=self.name,
                system="You are a senior startup strategist performing SWOT analysis.",
                prompt=prompt
            )
            logger.debug(f"{self.name} LLM response: {response}")

            data = extract_json(response) or {}
            data.setdefault("strengths", [])
            data.setdefault("weaknesses", [])
            data.setdefault("opportunities", [])
            data.setdefault("threats", [])
            data.setdefault("confidence_level", None)

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

        # Update context
        context.swot = data
        if not hasattr(context, "completed_agents") or context.completed_agents is None:
            context.completed_agents = []
        context.completed_agents.append(self.name)

        logger.info("SWOT Agent completed")
        return context
