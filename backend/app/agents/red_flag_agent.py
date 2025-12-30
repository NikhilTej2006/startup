from app.mcp.context import StartupContext
from app.services.llm_router import generate
from app.utils.json_utils import extract_json
from app.utils.logger import logger
import json

class RedFlagAgent:
    name = "red_flag_agent"

    async def run(self, context: StartupContext) -> StartupContext:
        logger.info("Red Flag Agent started")
        context.current_agent = self.name

        prompt = f"""
You are a VC performing risk analysis.

Detect RED FLAGS only using given data.
Do not invent.

Startup Context:
Verdict: {context.verdict}
Strategy: {context.strategy}
Financials: {context.financials}
Execution: {context.execution_plan}

Return STRICT JSON ONLY:

{{
  "red_flags": [],
  "severity": "low | medium | high",
  "mitigation_suggestions": []
}}
"""

        response = await generate(
            agent_name=self.name,
            system="You are a startup risk analyst.",
            prompt=prompt
        )

        context.red_flags = extract_json(response)
        context.completed_agents.append(self.name)

        logger.info("Red Flag Agent completed")
        return context
