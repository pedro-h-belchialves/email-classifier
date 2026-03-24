from openai import OpenAI
from app.services.ai.base_provider import AIProvider
from app.config import OPENAI_API_KEY

class OpenAIProvider(AIProvider):

    def __init__(self):
        self.client = OpenAI(api_key=OPENAI_API_KEY)

    def generate(self, prompt: str) -> str:
        response = self.client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {"role": "system", "content": "Você é um assistente que classifica emails."},
                {"role": "user", "content": prompt}
            ]
        )

        return response.choices[0].message.content