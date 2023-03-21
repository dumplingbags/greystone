from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Numeric
from sqlalchemy.orm import relationship

from database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(String, primary_key=True, index=True)

class Loan(Base):
    __tablename__ = "loans"

    id = Column(Integer, primary_key=True, autoincrement=True)
    amount = Column(Numeric, index=True)
    interest_rate = Column(Numeric, index=True)
    loan_term = Column(Integer, index = True)
    owner = Column(String, ForeignKey("users.id"))