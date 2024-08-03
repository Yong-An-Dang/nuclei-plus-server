from fastapi import APIRouter

router = APIRouter(prefix="/openai", tags=["openai"])


@router.post("/chat")
async def chat():
    return {"message": "Hello Chat"}
