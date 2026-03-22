from fastapi import APIRouter
from app.schemas.email_schema import EmailRequest, EmailResponse
from app.services.use_cases import ClassifyEmailUseCase

router = APIRouter()

@router.post("/classify", response_model=EmailResponse)
def classify_email(request: EmailRequest):
    use_case = ClassifyEmailUseCase()

    result = use_case.execute(request.content)

    return result