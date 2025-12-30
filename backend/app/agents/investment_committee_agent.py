import json
from app.mcp.context import StartupContext
from app.services.llm_router import generate
from app.utils.json_utils import extract_json
from app.utils.logger import logger

class InvestmentCommitteeAgent:
    name = "investment_committee_agent"

    async def run(self, context: StartupContext) -> StartupContext:
        logger.info("Investment Committee Agent started")
        context.current_agent = self.name

        prompt = f"""
You are a Tier-1 VC Investment Committee.

You MUST base your decision strictly on the provided data.
DO NOT invent traction, revenue, or partnerships.

Startup Idea:
{context.idea}

Market Score:
{context.market_score}

Competition:
{context.competition}

SWOT:
{context.swot}

Verdict:
{context.verdict}

Strategy:
{context.strategy}

Financials:
{context.financials}

Roadmap:
{context.roadmap}

Failure Modes:
{context.failure_analysis}

Stress Test:
{context.stress_test}

Survivability:
{context.survivability}

Return STRICT JSON ONLY:

{{
  "committee_decision": "INVEST | PASS | CONDITIONAL_INVEST",
  "investment_rationale": "",
  "key_concerns": [],
  "required_milestones": [],
  "suggested_check_size_usd": 0,
  "ownership_expectation_percent": 0,
  "confidence_level": 0.0
}}
"""

        try:
            response = await generate(
                agent_name=self.name,
                system="You are a VC investment committee making funding decisions.",
                prompt=prompt
            )
            data = extract_json(response)

        except Exception as e:
            logger.error(f"Investment committee fallback: {e}")
            data = {
                "committee_decision": "PASS",
                "investment_rationale": "Insufficient confidence due to execution and risk profile.",
                "key_concerns": ["High competition", "Execution risk"],
                "required_milestones": [],
                "suggested_check_size_usd": 0,
                "ownership_expectation_percent": 0,
                "confidence_level": 0.0
            }

        context.investment_committee = data
        context.completed_agents.append(self.name)

        logger.info("Investment Committee Agent completed")
        return context
