from app.agents.market_agent import MarketAgent
from app.agents.competition_agent import CompetitionAgent
from app.agents.swot_agent import SWOTAgent
from app.agents.verdict_agent import FinalVerdictAgent
from app.utils.logger import logger

class MCPOrchestrator:
    def __init__(self, context):
        self.context = context
        self.market_agent = MarketAgent()
        self.competition_agent = CompetitionAgent()
        self.swot_agent = SWOTAgent()
        self.verdict_agent = FinalVerdictAgent()

    async def run(self):
        logger.info("MCP Orchestrator started")

        # Phase 1: Market
        self.context = await self.market_agent.run(self.context)

        if self.context.market_score < 0.35:
            self.context.stop_reason = "Low market demand"
            return self.context

        # Phase 2–3
        self.context = await self.competition_agent.run(self.context)
        self.context = await self.swot_agent.run(self.context)

        #  Phase 4: Final Verdict
        self.context = await self.verdict_agent.run(self.context)

        logger.info("MCP Orchestrator completed Phase 4 flow")
        return self.context
