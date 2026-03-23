from app.services.ai.factory import get_ai_provider
from app.utils.json_parser import extract_json
from app.schemas.email_schema import EmailResponse


class ClassifyEmailUseCase:

    def __init__(self):
        self.ai_provider = get_ai_provider()

    def execute(self, content: str):
        prompt = f"""
        Você é um assistente especializado em classificação de emails.

        Seu objetivo é classificar emails como:
        - "produtivo" → quando exige ação, resposta ou resolução
        - "improdutivo" → quando é apenas agradecimento, confirmação ou sem ação necessária

        Exemplos:

        Email: "Obrigado pela ajuda!"
        Resposta:
        {{
        "category": "improdutivo",
        "suggested_response": "Agradecemos sua mensagem! Ficamos à disposição."
        }}

        Email: "Preciso de suporte com meu pedido"
        Resposta:
        {{
        "category": "produtivo",
        "suggested_response": "Recebemos sua solicitação e iremos analisá-la o mais breve possível."
        }}

        Email: "Só passando para avisar que deu tudo certo"
        Resposta:
        {{
        "category": "improdutivo",
        "suggested_response": "Ficamos felizes em saber! Qualquer coisa, estamos à disposição."
        }}

        Agora classifique o seguinte email:

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