from pydantic import BaseModel
from typing import Literal

class EmailRequest(BaseModel):
    content: str


class EmailResponse(BaseModel):
    category: Literal["produtivo", "improdutivo"]
    suggested_response: str