from pydantic import BaseModel
from typing import Optional

class StartupIdeaRequest(BaseModel):
    idea: str
    domain: Optional[str] = None
    target_users: Optional[str] = None
