from fastapi import FastAPI, Request, Depends, HTTPException
from fastapi.responses import JSONResponse
import models
from models import User, Loan
from database import SessionLocal, engine
from sqlalchemy.orm import Session
from helpers import monthlyPayment, remainingBalance, formatCurrency, formatPercent
from requests import UserRequest, LoanRequest, LoanSerializer, LoanScheduleRequest, LoanSummaryRequest
import json

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

@app.post("/user")
async def create_user(user_request: UserRequest, db: Session = Depends(get_db)):
    """
    Creates a new user with the given user_id if the user id does not already exist.
    
    :param user_request: A model containing the ID of the user to create.
    :param db: The database to write to (provided)l
    :return: The newly created user.
    """
    if db.query(User).filter(User.id == user_request.id).first():
        raise HTTPException(status_code=400, detail="User with this ID already exists")

    user = User()
    user.id = user_request.id

    db.add(user)
    db.commit()

    return JSONResponse(content={"item": json.dumps(user)}, status_code=201)

@app.get("/user/{user_id}/loans")
async def get_loans_for_user(user_id: str, db: Session = Depends(get_db)):
    """
    Retrieve all loans associated with the given user_id.
    
    :param user_id: The id of the user to retrieve all loans for.
    :param db: The database to write to (provided).
    :return: A list of all loans associated with the given user.
    """
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=400, detail="User with this ID does not exist")
    
    loans = db.query(Loan).filter(Loan.owner == user.id).all()

    return JSONResponse(content={"items": [LoanSerializer.from_orm(loan).dict() for loan in loans]}, status_code=200)

@app.post("/loan")
async def create_loan(loan_request: LoanRequest, db: Session = Depends(get_db)):
    """
    Creates a loan for a given user.
    
    :param loan_request: A model describing the new loan to be created in form {
        amount: float
        interest_rate: float
        loan_term: int
        owner: str
    }.
    :param db: The database to write to (provided).
    :return: The newly created loan.
    """
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

    return JSONResponse(content={"item": dict(LoanSerializer.from_orm(loan))}, status_code=201)

@app.get("/loan/{loan_id}")
async def get_loan(loan_id: int, db: Session = Depends(get_db)):
    """
    Retrieves a loan by its loan id. The loan amount and the interest rate have been formatted into currency format
    and percentage to the third decimal place, respectively.
    
    :param loan_id: The id of the loan to retrieve.
    :param db: The database to write to (provided).
    :return: The requested loan.
    """
    loan = db.query(Loan).filter(Loan.id == loan_id).first()
    if not loan:
        raise HTTPException(status_code=400, detail="Loan with this ID does not exist")
    
    loan_dict = dict(LoanSerializer.from_orm(loan))
    loan_dict['amount'] = formatCurrency(loan_dict['amount'])
    loan_dict['interest_rate'] = formatPercent(loan_dict['interest_rate'])
    
    return JSONResponse(content={"item": loan_dict}, status_code=200)

@app.get("/loan/{loan_id}/schedule")
async def get_loan_schedule(loan_id: int, db: Session = Depends(get_db)):
    """
    Retrieves a loan by its loan id and returns its schedule
    
    :param loan_id: The id of the loan to retrieve.
    :param db: The database to write to (provided).
    :return: The schedule of the requested loan.
    """
    loan = db.query(Loan).filter(Loan.id == loan_id).first()
    if not loan:
        raise HTTPException(status_code=400, detail="Loan with this ID does not exist")

    loan_amount = loan.amount
    i = loan.interest_rate
    loan_term = loan.loan_term

    schedule = []

    monthly_payment = monthlyPayment(loan_amount, i, loan_term)

    for month in range(1, loan_term+1):
        rem_balance = remainingBalance(loan_amount, i, monthly_payment, month)
        data = {}
        data["Month"] = month
        data["Remaining balance"] = formatCurrency(rem_balance)
        data["Monthly payment"] = formatCurrency(monthly_payment)
        schedule.append(data)

    return schedule


@app.get("/loan/{loan_id}/summary/{month}")
async def get_loan_summary(loan_id: int, month: int, db: Session = Depends(get_db)):
    """
    Retrieves a loan by its loan id and returns its summary for a given month.
    
    :param loan_id: The id of the loan to retrieve.
    :param db: The database to write to (provided).
    :return: The summary for the requested loan for the requested month.
    """
    loan = db.query(Loan).filter(Loan.id == loan_id).first()

    if not loan:
        raise HTTPException(status_code=400, detail="Loan with this ID does not exist")
    
    loan_amount = loan.amount
    i = loan.interest_rate
    loan_term = loan.loan_term

    if month > loan_term:
        raise HTTPException(status_code=400, detail="Please eneter a month in the valid range for this loan term")

    monthly_payment = monthlyPayment(loan_amount, i, loan_term)
    rem_balance = remainingBalance(loan_amount, i, monthly_payment, month)

    resp = {}
    resp["Current balance"] = formatCurrency(rem_balance)
    resp["Principal paid"] = formatCurrency(loan_amount - rem_balance)
    resp["Interest paid"] = formatCurrency(monthly_payment*month + rem_balance - loan_amount)
    return resp