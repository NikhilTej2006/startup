from pydantic_settings import BaseSettings
class Settings(BaseSettings):
    APP_NAME: str = "Startup Idea Validator Backend"
    API_V1_PREFIX: str = "/api/v1"
    DEBUG: bool = True

    TAVILY_API_KEY: str | None = None
    HF_API_KEY: str
    GROQ_API_KEY: str
    class Config:
        env_file = ".env"
        extra = "forbid"
settings = Settings()
