from app.mcp.context import StartupContext
from app.services.llm_router import generate
from app.utils.logger import logger
from app.utils.json_utils import extract_json

class StrategyAgent:
    name = "strategy_agent"

    async def run(self, context: StartupContext) -> StartupContext:
        logger.info("Strategy Agent started")
        context.current_agent = self.name

        prompt = f"""
You are a senior startup strategist.

Your task:
- Define a clear strategic direction
- Identify the best niche
- Recommend positioning

Use ONLY provided data. Do not invent facts.

Startup Idea:
{context.idea}

Domain:
{context.domain}

Market:
{context.market}

Competition:
{context.competition}

SWOT:
{context.swot}

Verdict:
{context.verdict}

Return STRICT JSON ONLY:

{{
  "focus_niche": "",
  "positioning_statement": "",
  "core_strategy": "",
  "recommended_actions": []
}}
"""

        try:
            raw = await generate(
                agent_name=self.name,
                system="You are a startup strategy expert.",
                prompt=prompt
            )
            data = extract_json(raw)

        except Exception as e:
            logger.error(f"Strategy agent fallback: {e}")
            data = {
                "focus_niche": None,
                "positioning_statement": None,
                "core_strategy": None,
                "recommended_actions": [],
                "error": "LLM unavailable"
            }

        context.strategy = data
        context.completed_agents.append(self.name)

        logger.info("Strategy Agent completed")
        return context
