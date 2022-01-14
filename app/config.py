import os

from dotenv import load_dotenv
from pydantic import BaseSettings

load_dotenv()


class Settings(BaseSettings):
    """Stores all project settings."""
    POSTGRES_DATABASE_URL: str = os.getenv('POSTGRES_DATABASE_URL')
