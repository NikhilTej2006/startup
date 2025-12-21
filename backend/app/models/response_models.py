from pydantic import BaseModel
from typing import Any

class StartupIdeaResponse(BaseModel):
    status: str
    context: Any
