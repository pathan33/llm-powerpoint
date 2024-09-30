import os

from dotenv import load_dotenv

load_dotenv()

_basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    """
    Configuration class for storing environment variables and API keys.
    """
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

    # PATHS
    BASEDIR = _basedir

    TEMPLATES_PATH = os.path.join(_basedir, "templates")
    POWERPOINTS_PATH = os.path.join(_basedir, "powerpoints")
