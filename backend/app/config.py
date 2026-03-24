import os
from dotenv import load_dotenv

load_dotenv(os.path.join(os.path.dirname(__file__), "../", ".env"))

AI_PROVIDER = os.getenv("AI_PROVIDER")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")