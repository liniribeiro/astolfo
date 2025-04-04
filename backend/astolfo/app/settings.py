import os
from pathlib import Path
from typing import Any

from pydantic import PostgresDsn, field_validator
from pydantic_core.core_schema import ValidationInfo
from pydantic_settings import BaseSettings

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ENVIRONMENT = os.getenv("ENVIRONMENT", "development")

class Settings(BaseSettings):
    BASE_DIR: str = BASE_DIR
    ENVIRONMENT: str = ENVIRONMENT
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "astolfo"

    POSTGRES_SERVER: str = "localhost"
    POSTGRES_USER: str = "postgres"
    POSTGRES_PORT: int = 5432
    POSTGRES_PASSWORD: str = "postgrespw"
    POSTGRES_DB: str = "astolfo"
    SQLALCHEMY_DATABASE_URI: str | None = None

    @field_validator("SQLALCHEMY_DATABASE_URI", mode="after")
    def assemble_db_connection(cls, v: str | None, values: ValidationInfo) -> Any:
        if isinstance(v, str):
            return v
        return str(PostgresDsn.build(
            scheme="postgresql",
            username=values.data.get("POSTGRES_USER"),
            password=values.data.get("POSTGRES_PASSWORD"),
            host=values.data.get("POSTGRES_SERVER"),
            port=values.data.get("POSTGRES_PORT", 5432),
            path=f"{values.data.get('POSTGRES_DB') or ''}",
        ))

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = True

settings = Settings()