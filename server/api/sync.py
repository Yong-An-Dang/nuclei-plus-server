from fastapi import APIRouter

router = APIRouter(prefix="/sync", tags=["sync"])


@router.post("/")
async def sync():
    return {"Hello": "World"}
