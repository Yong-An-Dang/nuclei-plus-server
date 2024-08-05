from fastapi import APIRouter

from server.services.openai import agent_chat
from server.sql.schemas import ChatRequestBody

router = APIRouter(prefix="/openai", tags=["openai"])


@router.post("/chat")
async def chat(chat_msg: ChatRequestBody):
    return agent_chat(chat_msg)
