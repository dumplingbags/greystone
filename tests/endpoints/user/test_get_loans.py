import pytest
from httpx import AsyncClient

from main import app
from user_inputs import UserLoansResponse, UserLoansMissingResponse

@pytest.mark.asyncio
async def test_get_user_loans():
    async with AsyncClient(base_url="http://localhost:8000") as client:
        response = await client.get("/user/shaneoh/loans")
    assert response.status_code == 200
    assert response.json() == UserLoansResponse

@pytest.mark.asyncio
async def test_get_user_missing_user():
    async with AsyncClient(base_url="http://localhost:8000") as client:
        response = await client.get("/user/bob/loans")
    assert response.status_code == 400
    assert response.json() == UserLoansMissingResponse