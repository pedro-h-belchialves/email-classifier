import google.generativeai as genai
from app.services.ai.base_provider import AIProvider
from app.config import GEMINI_API_KEY


class GeminiProvider(AIProvider):

    def __init__(self):
        genai.configure(api_key=GEMINI_API_KEY)
        self.model = genai.GenerativeModel("gemini-pro")

    def generate(self, prompt: str) -> str:
        response = self.model.generate_content(prompt)
        return response.text