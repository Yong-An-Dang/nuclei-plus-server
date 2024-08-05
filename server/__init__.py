from fastapi import FastAPI

from server.api import openai, sync


# http://127.0.0.1:8000/redoc
# http://127.0.0.1:8000/docs
app = FastAPI()

app.include_router(openai.router)
app.include_router(sync.router)
