class ClassifyEmailUseCase:
    def execute(self, content: str):

        if "obrigado" in content.lower():
            return {
                "category": "improdutivo",
                "suggested_response": "Agradecemos sua mensagem!"
            }

        return {
            "category": "produtivo",
            "suggested_response": "Recebemos sua solicitação e iremos analisar."
        }