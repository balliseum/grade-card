import secrets

# from pydantic import BaseSettings --> deprecated
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "GRADE-CARD"
    SECRET_KEY: str = secrets.token_urlsafe(32)
    SQLALCHEMY_DATABASE_URI: str = "sqlite:///./sql_app.db"

    # TODO SQLALCHEMY_DATABASE_URI: str = "postgresql://localhost:5432/grade-card"

    class Config:
        env_file = ".env"


settings = Settings()
