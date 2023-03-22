from pydantic import BaseModel, Field

class UserRequest(BaseModel):
    id: str = Field(description="The ID of the user to create.")

class UserSerializer(BaseModel):
    id: str

class LoanRequest(BaseModel):
    amount: float = Field(description="The total amount of the loan.")
    interest_rate: float = Field(description="The interest rate of the loan.")
    loan_term: int = Field(description="The loan term (in months).")
    owner: str = Field(description="the ID of the user that owns this loan.")

class LoanSerializer(BaseModel):
    id: int
    amount: float
    interest_rate: float
    loan_term: int
    owner: str

    class Config:
        orm_mode = True

class LoanScheduleRequest(BaseModel):
    loan_id: int = Field(description="the ID of the loan.")

class LoanSummaryRequest(BaseModel):
    loan_id: str = Field(description="the ID of the loan.")
    month: int = Field(description="the number term of the loan that the summary is requested for.")
