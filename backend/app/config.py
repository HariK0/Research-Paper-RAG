from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "Research Paper RAG Assistant"
    app_env: str = "development"
    database_url: str = "postgresql+psycopg://rag_user:change-me@localhost:5432/research_rag"
    chroma_url: str = "http://localhost:8001"

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


@lru_cache
def get_settings() -> Settings:
    return Settings()
