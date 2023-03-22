import pytest
from httpx import AsyncClient

from main import app
from loan_inputs import LoanResponse, MissingLoanResponse

@pytest.mark.asyncio
async def test_get_loan():
    async with AsyncClient(base_url="http://localhost:8000") as client:
        response = await client.get("/loan/1")
    assert response.status_code == 200
    assert response.json() == LoanResponse

@pytest.mark.asyncio
async def test_get_missing_loan():
    async with AsyncClient(base_url="http://localhost:8000") as client:
        response = await client.get("/loan/101")
    assert response.status_code == 400
    assert response.json() == MissingLoanResponse