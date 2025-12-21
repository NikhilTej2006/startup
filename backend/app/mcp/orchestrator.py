from app.mcp.context import StartupContext
from app.utils.logger import logger
from app.agents.market_agent import MarketAgent

class MCPOrchestrator:
    def __init__(self, context: StartupContext):
        self.context = context
        self.market_agent = MarketAgent()

    async def run(self) -> StartupContext:
        logger.info("MCP Orchestrator started")

        # Phase 2: Market Agent
        self.context = await self.market_agent.run(self.context)

        # Early stop logic (simple for now)
        if self.context.market_score is not None and self.context.market_score < 0.35:
            self.context.stop_reason = "Low market demand"
            logger.warning("MCP stopped: Low market demand")

        logger.info("MCP Orchestrator completed Phase 2 flow")
        return self.context
