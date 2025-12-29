from app.mcp.context import StartupContext
from app.services.llm_router import generate
from app.utils.logger import logger
from app.utils.json_utils import extract_json

class FinancialAgent:
    name = "financial_agent"

    async def run(self, context: StartupContext) -> StartupContext:
        logger.info("Financial Agent started")
        context.current_agent = self.name

        prompt = f"""
You are a startup financial analyst.

Provide a realistic early-stage financial plan.
Base estimates on similar startups.

Startup Idea:
{context.idea}

Strategy:
{context.strategy}

Market:
{context.market}

Competition:
{context.competition}

Return STRICT JSON ONLY:

{{
  "initial_funding_required_usd": 0,
  "burn_rate_per_month_usd": 0,
  "expected_revenue_year_1_usd": 0,
  "expected_revenue_year_3_usd": 0,
  "major_costs": [],
  "recommended_funding_sources": []
}}
"""

        try:
            raw = await generate(
                agent_name=self.name,
                system="You are a startup financial planner.",
                prompt=prompt
            )
            data = extract_json(raw)

        except Exception as e:
            logger.error(f"Financial agent fallback: {e}")
            data = {
                "initial_funding_required_usd": None,
                "burn_rate_per_month_usd": None,
                "expected_revenue_year_1_usd": None,
                "expected_revenue_year_3_usd": None,
                "major_costs": [],
                "recommended_funding_sources": [],
                "error": "LLM unavailable"
            }

        context.financials = data
        context.completed_agents.append(self.name)

        logger.info("Financial Agent completed")
        return context
