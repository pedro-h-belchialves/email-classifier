from app.config import AI_PROVIDER
from app.services.ai.openai_provider import OpenAIProvider
from app.services.ai.gemini_provider import GeminiProvider
from app.services.ai.anthropic_provider import AnthropicProvider



def get_ai_provider():
    if AI_PROVIDER == "openai":
        return OpenAIProvider()

    elif AI_PROVIDER == "gemini":
        return GeminiProvider()

    elif AI_PROVIDER == "anthropic":
        return AnthropicProvider()

    else:
        raise ValueError(f"Provider inválido: {AI_PROVIDER}")