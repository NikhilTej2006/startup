from pydantic import BaseModel
from typing import Optional, List, Dict

class StartupContext(BaseModel):
    idea: str
    domain: Optional[str] = None
    target_users: Optional[str] = None

    market_score: Optional[float] = None
    competition_score: Optional[float] = None
    risk_score: Optional[float] = None

    swot: Optional[Dict] = None
    tech_stack: Optional[Dict] = None
    mvp_plan: Optional[Dict] = None
    pitch: Optional[Dict] = None

    current_agent: Optional[str] = None
    completed_agents: List[str] = []
    stop_reason: Optional[str] = None
