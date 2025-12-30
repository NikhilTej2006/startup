from app.mcp.context import StartupContext
from app.services.llm_router import generate
from app.utils.json_utils import extract_json
from app.utils.logger import logger
import json

class FailureModeAgent:
    name = "failure_mode_agent"

    async def run(self, context: StartupContext) -> StartupContext:
        logger.info("Failure Mode Agent started")
        context.current_agent = self.name

        prompt = f"""
You are a startup failure analyst.

Based ONLY on the data below, simulate realistic failure scenarios.
Do NOT invent random risks. Be concrete.

Startup:
{context.idea}

Market:
{context.market}

Competition:
{context.competition}

Financials:
{context.financials}

Roadmap:
{context.roadmap}

Return STRICT JSON ONLY:

{{
  "failure_modes": [
    {{
      "scenario": "",
      "impact": "",
      "probability": 0.0,
      "severity": "low | medium | high"
    }}
  ]
}}
"""

        try:
            response = await generate(
                agent_name=self.name,
                system="You are a startup failure simulation engine.",
                prompt=prompt
            )
            data = extract_json(response)

        except Exception as e:
            logger.error(f"Failure mode fallback: {e}")
            data = {"failure_modes": []}

        context.failure_analysis = context.failure_analysis or {}
        context.failure_analysis["failure_modes"] = data["failure_modes"]

        context.completed_agents.append(self.name)
        logger.info("Failure Mode Agent completed")
        return context
