from fastapi import APIRouter
from app.models.request_models import StartupIdeaRequest
from app.models.response_models import StartupIdeaResponse
from app.mcp.context import StartupContext
from app.mcp.orchestrator import MCPOrchestrator

router = APIRouter()

@router.post("/validate", response_model=StartupIdeaResponse)
async def validate_startup(data: StartupIdeaRequest):
    context = StartupContext(
        idea=data.idea,
        domain=data.domain,
        target_users=data.target_users
    )

    orchestrator = MCPOrchestrator(context)
    final_context = await orchestrator.run()

    return StartupIdeaResponse(
        status="success",
        context=final_context.dict()
    )
