import os

from dotenv import load_dotenv
from pydantic import BaseModel

load_dotenv()


class Settings(BaseModel):
    """Stores all project settings."""
    POSTGRES_DATABASE_URL: str = os.getenv('POSTGRES_DATABASE_URL')
    # JWT settings.
    authjwt_secret_key: str = os.getenv('authjwt_secret_key')
    authjwt_token_location: set = {os.getenv('authjwt_token_location')}
    authjwt_cookie_csrf_protect: bool = (os.getenv('authjwt_cookie_csrf_protect', 'False') == 'True')
