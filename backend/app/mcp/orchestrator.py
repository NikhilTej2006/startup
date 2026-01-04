from app.agents.market_agent import MarketAgent
from app.agents.competition_agent import CompetitionAgent
from app.agents.swot_agent import SWOTAgent
from app.agents.verdict_agent import FinalVerdictAgent
from app.agents.strategy_agent import StrategyAgent
from app.agents.financial_agent import FinancialAgent
from app.agents.roadmap_agent import RoadmapAgent
from app.agents.mvp_agent import MVPAgent
from app.agents.tech_stack_agent import TechStackAgent
from app.agents.execution_agent import ExecutionAgent
from app.agents.pitch_deck_agent import PitchDeckAgent
from app.agents.fundability_agent import FundabilityAgent
from app.agents.red_flag_agent import RedFlagAgent
from app.agents.failure_mode_agent import FailureModeAgent
from app.agents.stress_test_agent import StressTestAgent
from app.agents.survivability_agent import SurvivabilityAgent
from app.agents.investment_committee_agent import InvestmentCommitteeAgent
from app.agents.vc_cross_examination_agent import VCCrossExaminationAgent

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

        self.context = await self.competition_agent.run(self.context)
        self.context = await self.swot_agent.run(self.context)
        self.context = await self.verdict_agent.run(self.context)
        self.context = await StrategyAgent().run(self.context)
        self.context = await FinancialAgent().run(self.context)
        self.context = await RoadmapAgent().run(self.context)
        self.context = await MVPAgent().run(self.context)
        self.context = await TechStackAgent().run(self.context)
        self.context = await ExecutionAgent().run(self.context)
        self.context = await PitchDeckAgent().run(self.context)
        self.context = await FundabilityAgent().run(self.context)
        self.context = await RedFlagAgent().run(self.context)
        self.context = await FailureModeAgent().run(self.context)
        self.context = await StressTestAgent().run(self.context)
        self.context = await SurvivabilityAgent().run(self.context)
        self.context = await InvestmentCommitteeAgent().run(self.context)
        self.context = await VCCrossExaminationAgent().run(self.context)
        logger.info("MCP Orchestrator completed") 
        return self.context
