from pydantic import BaseModel
from typing import Optional, Literal, List

class Verdict(BaseModel):
    decision: Literal["GO", "NO-GO", "ITERATE"]
    confidence: float  # 0.0 – 1.0
    reasoning: str
    key_risks: List[str]
    key_strengths: List[str]
    missing_signals: List[str]
