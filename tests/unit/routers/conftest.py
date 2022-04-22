import pytest_asyncio
from httpx import AsyncClient

from run_api import app


@pytest_asyncio.fixture
async def async_app_client():
    async with AsyncClient(app=app, base_url="http://api") as client:
        yield client
