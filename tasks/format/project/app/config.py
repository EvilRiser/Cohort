import logging
from functools import lru_cache
from pydantic_settings import BaseSettings
from dotenv import load_dotenv, find_dotenv

env_file = find_dotenv(".env.dev")
load_dotenv(env_file)

log = logging.getLogger("uvicorn")


class Settings(BaseSettings):
    environment: str = "dev"
    testing: bool = bool(0)

# BaseSettings also automatically reads from environment variables for these config settings.
# In other words, environment: str = "dev" is equivalent to environment: str = os.getenv("ENVIRONMENT", "dev").


@lru_cache()
def get_settings() -> BaseSettings:
    log.info("Loading config settings from the environment...")
    return Settings()
