import pytest
from httpx import AsyncClient

from main import app
from loan_inputs import LoanWithMissingUser, LoanWithMissingUserResponse

@pytest.mark.asyncio
async def test_get_schedule():
    async with AsyncClient(base_url="http://localhost:8000") as client:
        payload = LoanWithMissingUser
        headers = {"Content-Type": "application/json"}
        response = await client.post("/loan", json=payload, headers=headers)
    assert response.status_code == 400
    assert response.json() == LoanWithMissingUserResponse