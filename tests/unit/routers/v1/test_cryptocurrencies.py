import pytest


@pytest.mark.parametrize(
    "coin",
    [
        "random_coin",
        "bitcoin",
    ],
)
@pytest.mark.asyncio
async def test_get_nonexistent_coin(async_app_client, coin):
    response = await async_app_client.get(f"/cryptocurrency/{coin}")
    assert response.status_code == 404
