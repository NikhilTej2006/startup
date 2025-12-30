from pydantic import BaseModel
from typing import Optional, List, Dict, Any


class StartupContext(BaseModel):
    # ---- INPUT ----
    idea: str
    domain: str
    target_users: Optional[str] = None

    # ---- ANALYSIS PHASES (1–4) ----
    market: Optional[Dict[str, Any]] = None
    competition: Optional[Dict[str, Any]] = None
    swot: Optional[Dict[str, Any]] = None
    verdict: Optional[Dict[str, Any]] = None

    market_score: Optional[float] = None
    competition_score: Optional[float] = None

    # ---- STRATEGY & EXECUTION PHASES (5–6) ----
    strategy: Optional[Dict[str, Any]] = None
    financials: Optional[Dict[str, Any]] = None
    roadmap: Optional[Dict[str, Any]] = None

    #---MVP and TechStack Phase (7)----
    mvp: Optional[Dict[str, Any]] = None
    tech_stack: Optional[Dict[str, Any]] = None
    execution_plan: Optional[Dict[str, Any]] = None

     # PHASE 8 — Investor Intelligence
    pitch_deck: Optional[Dict[str, Any]] = None
    investor_qna: Optional[Dict[str, Any]] = None
    fundability: Optional[Dict[str, Any]] = None
    red_flags: Optional[Dict[str, Any]] = None

    # PHASE 9 — Failure Analysis
    failure_analysis: Optional[List[Dict[str, Any]]] = None
    stress_test: Optional[Dict[str, Any]] = None
    survivability: Optional[Dict[str, Any]] = None
    # ---- SYSTEM ----
    completed_agents: List[str] = []
    current_agent: Optional[str] = None
