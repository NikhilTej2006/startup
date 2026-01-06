from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config import settings
from app.api.v1.validate import router as validate_router
from app.api.v1.health import router as health_router

app = FastAPI(title=settings.APP_NAME)

# ✅ CORS MIDDLEWARE (REQUIRED FOR FRONTEND)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173", 
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],   # allows OPTIONS, POST, GET, etc
    allow_headers=["*"],
)

# ✅ ROUTERS
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
