from app.mcp.context import StartupContext
from app.services.llm_router import generate
from app.utils.logger import logger
from app.utils.json_utils import extract_json
import json

class MVPAgent:
    name = "mvp_agent"

    async def run(self, context: StartupContext) -> StartupContext:
        logger.info("MVP Agent started")
        context.current_agent = self.name

        prompt = f"""
You are a senior startup product manager.

Define a BUILDABLE MVP using the information below.
Focus on speed, validation, and risk reduction.

Startup Idea:
{context.idea}

Target Users:
{context.target_users}

Strategy:
{context.strategy}

Return STRICT JSON ONLY:

{{
  "core_features": [],
  "non_core_features": [],
  "user_roles": [],
  "success_metrics": [],
  "mvp_timeline_weeks": number
}}
"""

        try:
            response = await generate(
                agent_name=self.name,
                system="You design MVPs for early-stage startups.",
                prompt=prompt
            )
            data = extract_json(response)

        except Exception as e:
            logger.error(f"MVP agent fallback: {e}")
            data = {
                "core_features": [],
                "non_core_features": [],
                "user_roles": [],
                "success_metrics": [],
                "mvp_timeline_weeks": None,
                "error": "LLM unavailable"
            }

        context.mvp = data
        context.completed_agents.append(self.name)

        logger.info("MVP Agent completed")
        return context
