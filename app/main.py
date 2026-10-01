from fastapi import FastAPI

from app.core.database import Base, engine
from app.api.students import router as student_router
from app.api.chatbot import router as chatbot_router

Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="Student Database AI System",
    description=(
        "Modular Student Database Management "
        "System with Gemini and LangGraph"
    ),
    version="1.0.0"
)


app.include_router(student_router)
app.include_router(chatbot_router)

@app.get("/")
def root():

    return {
        "message": "Student Database AI Backend is running"
    }


@app.get("/health")
def health():

    return {
        "status": "healthy"
    }