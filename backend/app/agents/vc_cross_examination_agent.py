import json
from app.mcp.context import StartupContext
from app.services.llm_router import generate
from app.utils.json_utils import extract_json
from app.utils.logger import logger

class VCCrossExaminationAgent:
    name = "vc_cross_examination_agent"

    async def run(self, context: StartupContext) -> StartupContext:
        logger.info("VC Cross Examination Agent started")
        context.current_agent = self.name

        prompt = f"""
You are a hostile VC partner panel.

Your job:
- Attack assumptions
- Expose weaknesses
- Identify deal breakers
- Simulate real VC grilling

Startup Data:
Idea: {context.idea}
Verdict: {context.verdict}
Strategy: {context.strategy}
Financials: {context.financials}
Roadmap: {context.roadmap}
Red Flags: {context.red_flags}
Failure Modes: {context.failure_analysis}
Stress Test: {context.stress_test}
Survivability: {context.survivability}
Pitch Deck: {context.pitch_deck}
Fundability: {context.fundability}
Tech Stack: {context.tech_stack}
Investment Committee Decision: {context.investment_committee}

Rules:
- Be aggressive but realistic
- No motivational language
- No advice
- Only pressure and evaluation

Return STRICT JSON ONLY:

{{
  "cross_examination_questions": [],
  "deal_breaker_questions": [],
  "weak_answers_detected": [],
  "founder_survivability_score": 0.0,
  "final_partner_sentiment": "BULLISH | NEUTRAL | BEARISH"
}}
"""

        try:
            response = await generate(
                agent_name=self.name,
                system="You are a VC partner cross-examining founders.",
                prompt=prompt
            )
            data = extract_json(response)

        except Exception as e:
            logger.error(f"VC cross-examination fallback: {e}")
            data = {
                "cross_examination_questions": [],
                "deal_breaker_questions": [],
                "weak_answers_detected": ["Execution risk", "Regulatory uncertainty"],
                "founder_survivability_score": 0.0,
                "final_partner_sentiment": "BEARISH"
            }

        context.vc_cross_examination = data
        context.completed_agents.append(self.name)

        logger.info("VC Cross Examination Agent completed")
        return context
