from app.mcp.context import StartupContext
from app.services.llm_router import generate
from app.utils.logger import logger
from app.utils.json_utils import extract_json

import json

class ExecutionAgent:
    name = "execution_agent"

    async def run(self, context: StartupContext) -> StartupContext:
        logger.info("Execution Agent started")
        context.current_agent = self.name

        prompt = f"""
You are a startup execution coach.

Create a 90-day execution plan based on the MVP.

MVP:
{context.mvp}

Tech Stack:
{context.tech_stack}

Return STRICT JSON ONLY:

{{
  "month_1": [],
  "month_2": [],
  "month_3": [],
  "key_risks": [],
  "mitigations": []
}}
"""

        try:
            response = await generate(
                agent_name=self.name,
                system="You plan startup execution.",
                prompt=prompt
            )
            data = extract_json(response)

        except Exception as e:
            logger.error(f"Execution fallback: {e}")
            data = {"error": "LLM unavailable"}

        context.execution_plan = data
        context.completed_agents.append(self.name)

        logger.info("Execution Agent completed")
        return context
