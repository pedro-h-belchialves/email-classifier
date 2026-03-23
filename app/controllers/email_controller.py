from fastapi import APIRouter, HTTPException
from app.schemas.email_schema import EmailRequest, EmailResponse
from app.services.use_cases import ClassifyEmailUseCase
from app.utils.logger import get_logger

logger = get_logger(__name__)

router = APIRouter()

@router.post("/classify", response_model=EmailResponse)
def classify_email(request: EmailRequest):
    try:
        use_case = ClassifyEmailUseCase()

        result = use_case.execute(request.content)

        return result
    except Exception as e:
        logger.error(f"Error processing email: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail=f"Erro ao processar email: {str(e)}"
        )