from pydantic import BaseModel
from typing import Optional, Dict, Any, List

class StartupContext(BaseModel):
    # Input
    idea: str
    domain: str
    target_users: str

    # Phase outputs
    market: Optional[Dict[str, Any]] = None
    competition: Optional[Dict[str, Any]] = None
    swot: Optional[Dict[str, Any]] = None
    verdict: Optional[Dict[str, Any]] = None

    # Scores & control
    market_score: Optional[float] = None
    competition_score: Optional[float] = None 
    stop_reason: Optional[str] = None

    # Execution metadata
    current_agent: Optional[str] = None
    completed_agents: List[str] = []

    class Config:
        extra = "forbid"
