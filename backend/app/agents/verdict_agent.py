from app.mcp.context import StartupContext
from app.services.llm_router import generate
from app.utils.logger import logger
from app.utils.llm_utils import extract_json

class FinalVerdictAgent:
    name = "verdict_agent"

    async def run(self, context: StartupContext) -> StartupContext:
        logger.info("Final Verdict Agent started")
        context.current_agent = self.name

        prompt = f"""
You are a startup investment committee.

Use the data below to give a FINAL verdict.
Do not invent data.

Startup Idea:
{context.idea}

Domain:
{context.domain}

Market:
{context.market or {}}

Competition:
{context.competition or {}}

SWOT:
{context.swot or {}}

Return STRICT JSON ONLY:

{{
  "verdict": "GO | NO_GO | PIVOT",
  "confidence_score": 0.0,
  "reasoning": "",
  "next_steps": []
}}
"""

        try:
            response = await generate(
                agent_name=self.name,
                system="You are a startup investment decision-maker.",
                prompt=prompt
            )
            logger.debug(f"{self.name} LLM response: {response}")

            data = extract_json(response) or {}
            data.setdefault("verdict", "NO_GO")
            data.setdefault("confidence_score", 0.0)
            data.setdefault("reasoning", "LLM unavailable or invalid response")
            data.setdefault("next_steps", [])

        except Exception as e:
            logger.error(f"Verdict agent fallback triggered: {e}")
            data = {
                "verdict": "NO_GO",
                "confidence_score": 0.0,
                "reasoning": "LLM unavailable – decision based on incomplete data",
                "next_steps": [],
                "error": "LLM unavailable"
            }

        # Update context
        context.verdict = data
        if not hasattr(context, "completed_agents") or context.completed_agents is None:
            context.completed_agents = []
        context.completed_agents.append(self.name)

        logger.info("Final Verdict Agent completed")
        return context
