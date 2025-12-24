from app.mcp.context import StartupContext
from app.services.search import web_search
from app.services.llm_router import generate
from app.utils.logger import logger
from app.utils.llm_utils import extract_json

class CompetitionAgent:
    name = "competition_agent"

    async def run(self, context: StartupContext) -> StartupContext:
        logger.info("Dynamic Competition Agent started")
        context.current_agent = self.name

        # Build search query
        query = f"Top startups or companies similar to: {context.idea} in domain {context.domain}"
        search_results = web_search(query, k=7)

        # Build prompt for LLM
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
    {{"name": "", "description": "", "strength": ""}}
  ],
  "market_maturity": "early | growing | saturated",
  "entry_barriers": "low | medium | high",
  "competition_score": 0.0
}}
"""

        try:
            response = await generate(
                agent_name=self.name,
                system="You are a senior startup market analyst performing competition analysis.",
                prompt=prompt
            )
            logger.debug(f"{self.name} LLM response: {response}")

            data = extract_json(response) or {}
            data.setdefault("competitors", [])
            data.setdefault("market_maturity", "unknown")
            data.setdefault("entry_barriers", "unknown")
            data.setdefault("competition_score", None)

        except Exception as e:
            logger.error(f"Competition agent fallback triggered: {e}")
            data = {
                "competitors": [],
                "market_maturity": "unknown",
                "entry_barriers": "unknown",
                "competition_score": None,
                "error": "LLM unavailable"
            }

        # Update context
        context.competition = data
        context.competition_score = data.get("competition_score")
        if not hasattr(context, "completed_agents") or context.completed_agents is None:
            context.completed_agents = []
        context.completed_agents.append(self.name)

        logger.info("Dynamic Competition Agent completed")
        return context
