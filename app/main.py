from fastapi import FastAPI
from app.controllers import router as email_router

app = FastAPI()

app.include_router(email_router)