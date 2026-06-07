"""Application configuration"""

from functools import lru_cache
from typing import List
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application settings"""

    # Basic app config
    APP_NAME: str = "Global Flooring Opportunities Center"
    APP_ENV: str = "development"
    APP_DEBUG: bool = True
    APP_SECRET_KEY: str = "your-secret-key-here"

    # API server config
    API_HOST: str = "0.0.0.0"
    API_PORT: int = 8000
    API_WORKERS: int = 4

    # Database config
    DATABASE_URL: str = "postgresql://postgres:postgres@localhost:5432/flooring_db"
    DATABASE_POOL_SIZE: int = 20
    DATABASE_MAX_OVERFLOW: int = 40
    DATABASE_ECHO: bool = False

    # Redis config
    REDIS_URL: str = "redis://localhost:6379/0"
    REDIS_TTL: int = 3600

    # JWT config
    JWT_SECRET: str = "your-jwt-secret-key"
    JWT_ALGORITHM: str = "HS256"
    JWT_EXPIRATION: int = 86400

    # CORS config
    CORS_ORIGINS: List[str] = [
        "http://localhost:3000",
        "http://localhost:8000",
    ]

    class Config:
        env_file = ".env"
        case_sensitive = True


@lru_cache()
def get_settings() -> Settings:
    """Get settings instance"""
    return Settings()
