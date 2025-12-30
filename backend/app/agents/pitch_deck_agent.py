from app.mcp.context import StartupContext
from app.services.llm_router import generate
from app.utils.json_utils import extract_json
from app.utils.logger import logger
import json

class PitchDeckAgent:
    name = "pitch_deck_agent"

    async def run(self, context: StartupContext) -> StartupContext:
        logger.info("Pitch Deck Agent started")
        context.current_agent = self.name

        prompt = f"""
You are a venture capital pitch expert.

Generate a pitch deck STRUCTURE using the startup data below.
Do NOT invent traction or revenue.

Startup Idea:
{context.idea}

Domain:
{context.domain}

Strategy:
{context.strategy}

Financials:
{context.financials}

Roadmap:
{context.roadmap}

Return STRICT JSON ONLY:

{{
  "slides": [
    {{"title": "Problem", "content": ""}},
    {{"title": "Solution", "content": ""}},
    {{"title": "Market Opportunity", "content": ""}},
    {{"title": "Product & MVP", "content": ""}},
    {{"title": "Business Model", "content": ""}},
    {{"title": "Go-To-Market", "content": ""}},
    {{"title": "Competition", "content": ""}},
    {{"title": "Roadmap", "content": ""}},
    {{"title": "Financials", "content": ""}},
    {{"title": "Ask", "content": ""}}
  ]
}}
"""

        response = await generate(
            agent_name=self.name,
            system="You are a startup pitch deck generator.",
            prompt=prompt
        )

        data = extract_json(response)
        context.pitch_deck = data
        context.completed_agents.append(self.name)

        logger.info("Pitch Deck Agent completed")
        return context
