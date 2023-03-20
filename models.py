from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Numeric
from sqlalchemy.orm import relationship

from database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    loans = relationship("Loan", back_populates="owner")

class Loan(Base):
    __tablename__ = "loans"

    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Numeric, index=True)
    interest_rate = Column(Numeric, index=True)
    loan_term = Column(Integer, index = True)
    owner = Column(String, ForeignKey("users.id"))

    owner = relationship("User", back_populates="loans")