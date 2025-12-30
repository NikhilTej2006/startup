from app.mcp.context import StartupContext
from app.services.llm_router import generate
from app.utils.json_utils import extract_json
from app.utils.logger import logger
import json

class FundabilityAgent:
    name = "fundability_agent"

    async def run(self, context: StartupContext) -> StartupContext:
        logger.info("Fundability Agent started")
        context.current_agent = self.name

        prompt = f"""
You are a VC partner scoring startup fundability.

Score based on:
- Market size
- Competition
- Strategy clarity
- Execution readiness
- Financial realism

Startup Context:
Market: {context.market}
Competition: {context.competition}
Strategy: {context.strategy}
Financials: {context.financials}
Execution: {context.execution_plan}

Return STRICT JSON ONLY:

{{
  "fundability_score": 0,
  "strengths": [],
  "concerns": [],
  "investor_type_fit": ["pre-seed", "seed", "series-a"]
}}
"""

        response = await generate(
            agent_name=self.name,
            system="You are a venture capitalist evaluating startups.",
            prompt=prompt
        )

        context.fundability = extract_json(response)
        context.completed_agents.append(self.name)

        logger.info("Fundability Agent completed")
        return context
