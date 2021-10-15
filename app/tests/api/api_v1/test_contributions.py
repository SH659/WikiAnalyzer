import pytest as pytest
from httpx import AsyncClient

from core.settings import settings


@pytest.mark.asyncio
async def test_get_user_contributions(client: AsyncClient):
    r = await client.post(f"{settings.API_V1_STR}/contributions",
                          json={'user': "Jimbo Wales"})
    assert r.status_code == 200


@pytest.mark.asyncio
async def test_get_user_contributions_over_time(client: AsyncClient):
    r = await client.post(f"{settings.API_V1_STR}/contributions/stats_over_time",
                          json={'user': "Jimbo Wales", "interval": 86400})
    assert r.status_code == 200
