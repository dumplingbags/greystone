from fastapi import FastAPI, Request, Depends, HTTPException
import models
from models import User, Loan
from database import SessionLocal, engine
from sqlalchemy.orm import Session
from pydantic import BaseModel

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

class UserRequest(BaseModel):
    id: str

class LoanRequest(BaseModel):
    amount: float
    interest_rate: float
    loan_term: int
    owner: str

class LoanScheduleRequest(BaseModel):
    loan_id: str

class LoanSummaryRequest(BaseModel):
    loan_id: str
    month: int

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/user")
async def create_user(user_request: UserRequest, db: Session = Depends(get_db)):

    if db.query(User).filter(User.id == user_request.id).first():
            raise HTTPException(status_code=400, detail="User with this ID already exists")

    user = User()
    user.id = user_request.id

    db.add(user)
    db.commit()

    return {
        "code": "success",
        "message": "user  created"
    }

@app.post("/loan")
async def create_user(loan_request: LoanRequest, db: Session = Depends(get_db)):

    if not db.query(User).filter(User.id == loan_request.owner).first():
            raise HTTPException(status_code=400, detail="User with this ID does not exist")

    loan = Loan(
        amount=loan_request.amount,
        interest_rate=loan_request.interest_rate,
        loan_term=loan_request.interest_rate,
        owner=loan_request.owner)

    db.add(loan)
    db.commit()

    return {
        "code": "success",
        "message": "loan  created"
    }

@app.get("/loan_schedule")
async def get_loan_schedule(loan_schedule_request: LoanScheduleRequest, db: Session = Depends(get_db)):
    raise HTTPException(status_code=404, detail="This API Endpoint has not been set up yet.")

@app.get("/loan_summary")
async def get_loan_summary(loan_summary_request: LoanSummaryRequest, db: Session = Depends(get_db)):
    raise HTTPException(status_code=404, detail="This API Endpoint has not been set up yet.")