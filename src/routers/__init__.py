import aiopg.sa
from starlette.requests import Request


def get_psql_engine(request: Request) -> aiopg.sa.Engine:
    return request.app.state.psql
