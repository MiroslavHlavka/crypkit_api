import pytest


@pytest.mark.asyncio
async def test_root(async_app_client):
    response = await async_app_client.get("/")
    assert response.status_code == 200
    assert response.json() == {'environment': 'local', 'service': 'crypkit-service'}


@pytest.mark.asyncio
async def test_ping(async_app_client):
    response = await async_app_client.get("/ping")
    assert response.status_code == 200
    assert response.json() == "pong"
