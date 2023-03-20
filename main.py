from fastapi import FastAPI
import models
from database import SessionLocal, engine
from sqlalchemy.orm import Session

app = FastAPI()

models.Base.metadata.create_all(bind=engine)



@app.get("/")
async def root():
    return {"message": "Hello World"}