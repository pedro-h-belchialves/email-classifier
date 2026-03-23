import anthropic
from app.services.ai.base_provider import AIProvider
from app.config import ANTHROPIC_API_KEY
class AnthropicProvider(AIProvider):

    def __init__(self):
        self.client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)

    def generate(self, prompt: str) -> str:
        response = self.client.messages.create(
            model="claude-3-haiku-20240307",
            max_tokens=500,
            messages=[
                {"role": "user", "content": prompt}
            ]
        )

        return response.content[0].text