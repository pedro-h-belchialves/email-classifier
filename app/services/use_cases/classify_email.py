from app.services.ai.factory import get_ai_provider
from app.utils.json_parser import extract_json
from app.schemas.email_schema import EmailResponse


class ClassifyEmailUseCase:

    def __init__(self):
        self.ai_provider = get_ai_provider()

    def execute(self, content: str):
        prompt = f"""
        Classifique o seguinte email como produtivo ou improdutivo
        e gere uma resposta apropriada.

        Email:
        {content}

        Responda apenas em JSON válido:
        {{
            "category": "produtivo ou improdutivo",
            "suggested_response": "resposta aqui"
        }}
        """

        response = self.ai_provider.generate(prompt)

        parsed = extract_json(response)

           validated = EmailResponse(**parsed)

        return validated