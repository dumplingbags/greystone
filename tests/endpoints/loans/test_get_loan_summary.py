import pytest
from httpx import AsyncClient

from main import app
from loan_inputs import LoanSummaryResponse, MissingLoanResponse, InvalidMonthResponse

@pytest.mark.asyncio
async def test_get_schedule():
    async with AsyncClient(base_url="http://localhost:8000") as client:
        response = await client.get("/loan/1/summary/2")
    assert response.status_code == 200
    assert response.json() == LoanSummaryResponse

@pytest.mark.asyncio
async def test_get_schedule_missing_loan():
    async with AsyncClient(base_url="http://localhost:8000") as client:
        response = await client.get("/loan/101/summary/2")
    assert response.status_code == 400
    assert response.json() == MissingLoanResponse

@pytest.mark.asyncio
async def test_get_schedule_invalid_month():
    async with AsyncClient(base_url="http://localhost:8000") as client:
        response = await client.get("/loan/1/summary/500")
    assert response.status_code == 400
    assert response.json() == InvalidMonthResponse