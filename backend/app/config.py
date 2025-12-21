from pydantic_settings import BaseSettings
class Settings(BaseSettings):
    APP_NAME: str = "Startup Idea Validator Backend"
    API_V1_PREFIX: str = "/api/v1"
    DEBUG: bool = True

settings = Settings()
