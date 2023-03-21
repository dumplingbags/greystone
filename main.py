from fastapi import FastAPI, Request, Depends, HTTPException
import models
from models import User, Loan
from database import SessionLocal, engine
from sqlalchemy.orm import Session
from pydantic import BaseModel
from helpers import monthlyPayment, remainingBalance

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
    loan_id: int

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
        loan_term=loan_request.loan_term,
        owner=loan_request.owner)

    db.add(loan)
    db.commit()

    l = db.query(Loan).filter(Loan.id == loan.id).first()
    if not l:
            raise HTTPException(status_code=400, detail="Loan has not been created")

    return {
        "code": "success",
        "message": "loan created"
    }

@app.get("/loan_schedule/{loan_id}")
async def get_loan_schedule(loan_id: int, db: Session = Depends(get_db)):

    loan = db.query(Loan).filter(Loan.id == loan_id).first()

    if not loan:
            raise HTTPException(status_code=400, detail="User with this ID does not exist")

    loan_amount = loan.amount
    i = loan.interest_rate
    loan_term = loan.loan_term

    schedule = []

    monthly_payment = monthlyPayment(loan_amount, i, loan_term)

    for month in range(1, loan_term+1):
        rem_balance = remainingBalance(loan_amount, i, monthly_payment, month)
        data = {}
        data["Month"] = month
        data["Remaining balance"] = round(rem_balance, 2)
        data["Monthly payment"] = round(monthly_payment, 2)
        schedule.append(data)

    return schedule


@app.get("/loan_summary/{loan_id}/{month}")
async def get_loan_summary(loan_id: int, month: int, db: Session = Depends(get_db)):
    loan = db.query(Loan).filter(Loan.id == loan_id).first()

    if not loan:
            raise HTTPException(status_code=400, detail="User with this ID does not exist")

    loan_amount = loan.amount
    i = loan.interest_rate
    loan_term = loan.loan_term

    monthly_payment = monthlyPayment(loan_amount, i, loan_term)
    rem_balance = remainingBalance(loan_amount, i, monthly_payment, month)

    resp = {}
    resp["Current balance"] = round(rem_balance, 2)
    resp["Principal paid"] = round(loan_amount - rem_balance, 2)
    resp["Interest paid"] = round(monthly_payment*month + rem_balance - loan_amount, 2)
    return resp