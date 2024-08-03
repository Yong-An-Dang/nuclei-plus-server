from fastapi import FastAPI

from server.api import openai, sync
from server.sql import models
from server.sql.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# http://127.0.0.1:8000/redoc
# http://127.0.0.1:8000/docs
app = FastAPI()

app.include_router(openai.router)
app.include_router(sync.router)
