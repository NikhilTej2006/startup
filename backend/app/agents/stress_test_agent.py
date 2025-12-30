from app.mcp.context import StartupContext
from app.services.llm_router import generate
from app.utils.json_utils import extract_json
from app.utils.logger import logger
import json

class StressTestAgent:
    name = "stress_test_agent"

    async def run(self, context: StartupContext) -> StartupContext:
        logger.info("Stress Test Agent started")
        context.current_agent = self.name

        prompt = f"""
Apply shocks to this startup:
- Funding delay
- Demand drop
- Cost overrun

Financials:
{context.financials}

Return STRICT JSON:
{{
  "stress_test": {{
    "funding_delay": "impact",
    "demand_drop": "impact",
    "cost_overrun": "impact"
  }}
}}
"""

        try:
            response = await generate(
                agent_name=self.name,
                system="You stress test startups.",
                prompt=prompt
            )
            data =extract_json(response)

        except Exception as e:
            logger.error(f"StressTest fallback: {e}")
            data = {
                "stress_test": {
                    "funding_delay": "unknown",
                    "demand_drop": "unknown",
                    "cost_overrun": "unknown"
                }
            }

        context.stress_test = data["stress_test"]
        context.completed_agents.append(self.name)
        return context
