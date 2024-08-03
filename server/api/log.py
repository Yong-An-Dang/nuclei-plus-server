from fastapi import APIRouter

router = APIRouter(prefix="/log", tags=["http_log"])


@router.get("/http")
async def http_get():
    return {"Hello": "World"}

@router.post("/http")
async def http_post():
    return {"Hello": "World"}
