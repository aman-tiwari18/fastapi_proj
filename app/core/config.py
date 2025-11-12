from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql://user:rootpassword123@localhost/fastapi_db"
    SECRET_KEY: str = "supersecretkey"
    ALGORITHM: str = "HS256"

    class Config:
        env_file = ".env"  # Optional: load from .env file

settings = Settings()
