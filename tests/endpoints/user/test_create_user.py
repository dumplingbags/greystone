import pytest
from httpx import AsyncClient

from main import app

from user_inputs import ExistingUserResponse

@pytest.mark.asyncio
async def test_create_existing_user():
    async with AsyncClient(base_url="http://localhost:8000") as client:
        payload = {"id": "shaneoh"}
        headers = {"Content-Type": "application/json"}
        response = await client.post("/user", json=payload, headers=headers)
    assert response.status_code == 400
    assert response.json() == ExistingUserResponse