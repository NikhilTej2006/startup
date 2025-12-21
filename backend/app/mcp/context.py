from pydantic import BaseModel, Field
from typing import Any, Dict, List, Optional

class StartupContext(BaseModel):
    idea: str
    domain: str

    # agent tracking
    current_agent: Optional[str] = None
    completed_agents: List[str] = Field(default_factory=list)

    # market agent
    market: Optional[Dict[str, Any]] = None
    market_score: Optional[float] = None

    # competition agent
    competition: Optional[Dict[str, Any]] = None
    competition_score: Optional[float] = None

    # swot agent (future)
    swot: Optional[Dict[str, Any]] = None
