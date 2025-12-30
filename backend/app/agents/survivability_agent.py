from app.mcp.context import StartupContext
from app.services.llm_router import generate
from app.utils.json_utils import extract_json
from app.utils.logger import logger
import json

class SurvivabilityAgent:
    name = "survivability_agent"

    async def run(self, context: StartupContext) -> StartupContext:
        logger.info("Survivability Agent started")
        context.current_agent = self.name

        prompt = f"""
Estimate startup survivability.

Financials:
{context.financials}

Red Flags:
{context.red_flags}

Return STRICT JSON:
{{
  "survivability": {{
    "estimated_runway_months": 0,
    "survival_probability": 0.0,
    "resilience_rating": "low | medium | high"
  }}
}}
"""

        try:
            response = await generate(
                agent_name=self.name,
                system="You estimate startup survival.",
                prompt=prompt
            )
            data = extract_json(response)

        except Exception as e:
            logger.error(f"Survivability fallback: {e}")
            data = {
                "survivability": {
                    "estimated_runway_months": 0,
                    "survival_probability": 0.0,
                    "resilience_rating": "low"
                }
            }

        context.survivability = data["survivability"]
        context.completed_agents.append(self.name)
        return context
