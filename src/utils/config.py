import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")
    DEFAULT_MODEL = "llama-3.3-70b-versatile"

    @classmethod
    def validate(cls):
        if not cls.GROQ_API_KEY:
            raise ValueError("CRITICAL ERROR: GROQ_API_KEY is missing from your environment setup.")