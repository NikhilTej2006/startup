from app.mcp.context import StartupContext
from app.services.llm_router import generate
from app.utils.logger import logger
from app.utils.json_utils import extract_json

import json

class TechStackAgent:
    name = "tech_stack_agent"

    async def run(self, context: StartupContext) -> StartupContext:
        logger.info("Tech Stack Agent started")
        context.current_agent = self.name

        prompt = f"""
You are a startup CTO.

Design a scalable yet MVP-friendly tech stack.

Startup Idea:
{context.idea}

MVP Features:
{context.mvp}

Return STRICT JSON ONLY:

{{
  "frontend": "",
  "backend": "",
  "database": "",
  "ai_ml": "",
  "cloud": "",
  "devops": "",
  "reasoning": ""
}}
"""

        try:
            response = await generate(
                agent_name=self.name,
                system="You are a pragmatic startup CTO.",
                prompt=prompt
            )
            data = extract_json(response)

        except Exception as e:
            logger.error(f"Tech stack fallback: {e}")
            data = {"error": "LLM unavailable"}

        context.tech_stack = data
        context.completed_agents.append(self.name)

        logger.info("Tech Stack Agent completed")
        return context
