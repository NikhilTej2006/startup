from fastapi import FastAPI
from app.config import settings
from app.api.v1.validate import router as validate_router
from app.api.v1.health import router as health_router

app = FastAPI(title=settings.APP_NAME)

app.include_router(
    validate_router,
    prefix=settings.API_V1_PREFIX,
    tags=["Startup Validation"]
)

app.include_router(
    health_router,
    prefix=settings.API_V1_PREFIX,
    tags=["Health"]
)
