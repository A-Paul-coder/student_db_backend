from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "Student Database AI System"
    debug: bool = True

    database_url: str = "sqlite:///./students.db"

    gemini_api_key: str

    qdrant_url: str = "http://localhost:6333"
    qdrant_collection: str = "student_information"

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )


settings = Settings()
