import pytest
from httpx import AsyncClient

from main import app
from loan_inputs import LoanScheduleResponse, MissingLoanResponse

@pytest.mark.asyncio
async def test_get_schedule():
    async with AsyncClient(base_url="http://localhost:8000") as client:
        response = await client.get("/loan/1/schedule")
    assert response.status_code == 200
    assert response.json() == LoanScheduleResponse

@pytest.mark.asyncio
async def test_get_missing_loan_schedule():
    async with AsyncClient(base_url="http://localhost:8000") as client:
        response = await client.get("/loan/101/schedule")
    assert response.status_code == 400
    assert response.json() == MissingLoanResponse