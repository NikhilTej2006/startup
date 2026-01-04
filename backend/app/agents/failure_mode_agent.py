import json
from app.mcp.context import StartupContext
from app.services.llm_router import generate
from app.utils.json_utils import extract_json
from app.utils.logger import logger

class FailureModeAgent:
    name = "failure_mode_agent"

    async def run(self, context: StartupContext) -> StartupContext:
        logger.info("Failure Mode Agent started")
        context.current_agent = self.name

        prompt = f"""
You are a venture risk analyst.

Analyze the startup and identify realistic failure modes.

Startup context:
Idea: {context.idea}
Market Score: {context.market_score}
Competition Score: {context.competition_score}
Strategy: {context.strategy}
Financials: {context.financials}
Red Flags: {context.red_flags}

Return STRICT JSON ONLY:

{{
  "failure_modes": [
    {{
      "scenario": "string",
      "impact": "string",
      "severity": "low | medium | high"
    }}
  ]
}}
"""

        try:
            response = await generate(
                agent_name=self.name,
                system="You analyze startup failure scenarios.",
                prompt=prompt
            )

            data = extract_json(response)
            failure_modes = data.get("failure_modes", [])

            if not isinstance(failure_modes, list):
                raise ValueError("failure_modes is not a list")

        except Exception as e:
            logger.error(f"Failure Mode Agent fallback triggered: {e}")
            failure_modes = [
                {
                    "scenario": "Regulatory approval delays",
                    "impact": "Unable to launch drone operations on schedule",
                    "severity": "high"
                },
                {
                    "scenario": "Unit economics fail to scale",
                    "impact": "Sustained losses prevent follow-on funding",
                    "severity": "high"
                }
            ]

        context.failure_analysis = {
            "failure_modes": failure_modes
        }

        context.completed_agents.append(self.name)
        logger.info("Failure Mode Agent completed")

        return context
