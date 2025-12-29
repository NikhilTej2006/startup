from app.mcp.context import StartupContext
from app.services.llm_router import generate
from app.utils.logger import logger
from app.utils.json_utils import extract_json

class RoadmapAgent:
    name = "roadmap_agent"

    async def run(self, context: StartupContext) -> StartupContext:
        logger.info("Roadmap Agent started")
        context.current_agent = self.name

        prompt = f"""
You are a startup execution planner.

Create a practical roadmap from idea to early traction.

Startup Idea:
{context.idea}

Strategy:
{context.strategy}

Financials:
{context.financials}

Return STRICT JSON ONLY:

{{
  "milestones": [
    {{
      "title": "",
      "description": "",
      "timeframe_months": "",
      "success_metric": ""
    }}
  ],
  "execution_risks": [],
  "overall_timeline_summary": ""
}}
"""

        try:
            raw = await generate(
                agent_name=self.name,
                system="You are a startup execution roadmap expert.",
                prompt=prompt
            )
            data = extract_json(raw)

        except Exception as e:
            logger.error(f"Roadmap agent fallback: {e}")
            data = {
                "milestones": [],
                "execution_risks": [],
                "overall_timeline_summary": None,
                "error": "LLM unavailable"
            }

        context.roadmap = data
        context.completed_agents.append(self.name)

        logger.info("Roadmap Agent completed")
        return context
