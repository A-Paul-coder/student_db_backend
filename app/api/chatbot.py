from fastapi import APIRouter

from pydantic import BaseModel

from langchain_core.messages import HumanMessage

from app.ai.graph import graph


router = APIRouter(
    prefix="/chat",
    tags=["AI Chatbot"]
)


class ChatRequest(BaseModel):

    message: str


class ChatResponse(BaseModel):

    answer: str


@router.post(
    "/",
    response_model=ChatResponse
)
def chat(request: ChatRequest):

    result = graph.invoke(
        {
            "messages": [
                HumanMessage(
                    content=request.message
                )
            ]
        }
    )

    answer = result["messages"][-1].content

    return {
        "answer": answer
    }