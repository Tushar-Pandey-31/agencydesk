
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    database_url: str = (
        "postgresql+psycopg://agencydesk:dev_only_change_me"
        "@localhost:5432/agencydesk"
    )
    jwt_secret: str = "local-development-secret-change-before-deployment"
    access_token_minutes: int = 30
    upload_dir: str = "../uploads"
    max_upload_bytes: int = 10 * 1024 * 1024

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
    )


settings = Settings()
