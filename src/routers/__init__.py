import aiopg.sa
from starlette.requests import Request
from src.services.coingecko import CoingeckoService


def get_psql_engine(request: Request) -> aiopg.sa.Engine:
    return request.app.state.psql


def get_coingecko_service() -> CoingeckoService:
    return CoingeckoService()
