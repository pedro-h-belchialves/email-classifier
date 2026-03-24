from fastapi import APIRouter, HTTPException, UploadFile, File
import tempfile

from app.schemas.email_schema import EmailRequest, EmailResponse
from app.services.use_cases import ClassifyEmailUseCase
from app.utils.logger import get_logger
from app.services.parsers.file_parser import FileParser

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

@router.post("/classify-file", response_model=EmailResponse)
async def classify_email(file: UploadFile = File(...)):
    try:
        use_case = ClassifyEmailUseCase()

        with tempfile.NamedTemporaryFile(delete=False) as temp:
                temp.write(await file.read())
                temp_path = temp.name

        parser = FileParser()
        text = parser.parse(temp_path, file.filename)

        result = use_case.execute(text)

        return result
    except Exception as e:
        logger.error(f"Error processing email: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail=f"Erro ao processar email: {str(e)}"
        )