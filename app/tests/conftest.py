import asyncio
from typing import Generator

import pytest
from httpx import AsyncClient

from main import app


@pytest.fixture(scope="session")
def event_loop():
    loop = asyncio.get_event_loop_policy().new_event_loop()
    asyncio.set_event_loop(loop)
    yield loop


@pytest.fixture(scope="session")
async def client(event_loop) -> Generator:
    async with AsyncClient(app=app, base_url="http://test") as ac:
        yield ac
