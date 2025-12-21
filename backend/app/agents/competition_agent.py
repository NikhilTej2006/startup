from app.mcp.context import StartupContext
from app.services.search import web_search
from app.services.llm_router import LLMRouter
from app.utils.logger import logger
import json

class CompetitionAgent:
    name = "competition_agent"

    async def run(self, context: StartupContext) -> StartupContext:
        logger.info("Dynamic Competition Agent started")
        context.current_agent = self.name

        query = f"""
        Top startups or companies similar to:
        {context.idea}
        in domain {context.domain}
        """

        search_results = web_search(query, k=7)

        prompt = f"""
You are a senior startup market analyst.

Analyze competition dynamically using evidence.
Avoid assumptions. Base decisions only on signals.

Startup Idea:
{context.idea}

Domain:
{context.domain}

Search Results:
{search_results}

Output STRICT JSON ONLY:

{{
  "competitors": [
    {{
      "name": "",
      "description": "",
      "strength": ""
    }}
  ],
  "market_maturity": "early | growing | saturated",
  "entry_barriers": "low | medium | high",
  "competition_score": 0.0
}}
"""

        try:
            response = await LLMRouter.generate(prompt, agent=self.name)
            data = json.loads(response)

        except Exception as e:
            logger.error(f"Competition agent fallback triggered: {e}")

            # SAFE dynamic fallback (not heuristic)
            data = {
                "competitors": [],
                "market_maturity": "unknown",
                "entry_barriers": "unknown",
                "competition_score": None,
                "error": "LLM unavailable"
            }

        context.competition = data
        context.competition_score = data.get("competition_score")
        context.completed_agents.append(self.name)

        logger.info("Dynamic Competition Agent completed")
        return context
