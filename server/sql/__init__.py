from server.sql import models
from server.sql.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

db = SessionLocal()
