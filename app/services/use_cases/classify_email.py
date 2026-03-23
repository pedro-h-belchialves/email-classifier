from app.services.ai.factory import get_ai_provider
from app.utils.json_parser import extract_json
from app.schemas.email_schema import EmailResponse
from app.services.ai.training_data import EXAMPLES
from app.utils.logger import get_logger


logger = get_logger(__name__)


class ClassifyEmailUseCase:

    def __init__(self):
        self.ai_provider = get_ai_provider()
        

    def execute(self, content: str):
        logger.info(f"Classifying email: {content}")

        examples_text = ""

        for example in EXAMPLES:
            examples_text += f"""
        Email: {example["email"]}
        Resposta:
        {{
        "category": "{example["category"]}",
        "suggested_response": "{example["response"]}"
        }}
        """
    
        prompt = f"""
        Você é um assistente especializado em classificação de emails.

        Seu objetivo é classificar emails como:
        - "produtivo" → quando exige ação, resposta ou resolução
        - "improdutivo" → quando é apenas agradecimento, confirmação ou sem ação necessária

        Exemplos:

        {examples_text}

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
        logger.info(f"Ai response: {response}")

        parsed = extract_json(response)
        logger.info(f"Parsed response: {parsed}")

        validated = EmailResponse(**parsed)
        logger.info(f"Validated response: {parsed}")

        return validated
    
 