from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    APP_NAME: str = "Sistema Na Garagem"
    VERSION: str = "0.1.0"
    DATABASE_URL: str = "sqlite:///data/estetica.db"

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )

settings = Settings()