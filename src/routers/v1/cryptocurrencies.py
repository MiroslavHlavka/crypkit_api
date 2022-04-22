import aiopg.sa
from fastapi import APIRouter, Depends, Path
from starlette.status import HTTP_200_OK, HTTP_201_CREATED

from src.models.cryptocurrency import Cryptocurrency
from src.models.schemas.responses.cryptocurrency import (
    CryptocurrencyBaseSchema, CryptocurrencyCreateSchema,
    CryptocurrencyIdSchema, CryptocurrencyUpdateSchema)
from src.routers import get_coingecko_service, get_psql_engine
from src.services.coingecko import CoingeckoService

router: APIRouter = APIRouter()


@router.post(
    "/cryptocurrency/",
    tags=["cryptocurrency"],
    response_model=CryptocurrencyIdSchema,
    description="Create single cryptocurrency",
    status_code=HTTP_201_CREATED,
    responses={
        HTTP_201_CREATED: {
            "description": "Cryptocurrency has been successfully created.",
        }
    },
)
async def create(
    cryptocurrency: CryptocurrencyCreateSchema,
    db_engine: aiopg.sa.Engine = Depends(get_psql_engine),
    coingecko: CoingeckoService = Depends(get_coingecko_service),
) -> CryptocurrencyIdSchema:
    async with db_engine.acquire() as db_connection:
        cryptocurrency_model = Cryptocurrency(db_connection)
        return await cryptocurrency_model.create(cryptocurrency, coingecko)


@router.delete(
    "/cryptocurrency/{id}",
    tags=["cryptocurrency"],
    response_model=CryptocurrencyIdSchema,
    description="Delete cryptocurrency",
    status_code=HTTP_201_CREATED,
    responses={
        HTTP_200_OK: {
            "description": "Successfully deleted.",
        }
    },
)
async def delete(
    id: str = Path(..., description="An id of cryptocurrency."),
    db_engine: aiopg.sa.Engine = Depends(get_psql_engine),
) -> CryptocurrencyIdSchema:
    async with db_engine.acquire() as db_connection:
        cryptocurrency_model = Cryptocurrency(db_connection)
        return await cryptocurrency_model.delete(id)


@router.patch(
    "/cryptocurrency/",
    tags=["cryptocurrency"],
    response_model=CryptocurrencyBaseSchema,
    description="Update cryptocurrency",
    status_code=HTTP_201_CREATED,
    responses={
        HTTP_200_OK: {
            "description": "Successfully updated.",
        },
    },
)
async def update(
    id: str,
    cryptocurrency: CryptocurrencyUpdateSchema,
    db_engine: aiopg.sa.Engine = Depends(get_psql_engine),
) -> CryptocurrencyBaseSchema:
    async with db_engine.acquire() as db_connection:
        cryptocurrency_model = Cryptocurrency(db_connection)
        return await cryptocurrency_model.update(id, cryptocurrency)


@router.get(
    "/cryptocurrency/{id}/",
    tags=["cryptocurrency"],
    response_model=CryptocurrencyBaseSchema,
    description="Get single cryptocurrency by id.",
    responses={
        HTTP_200_OK: {
            "description": "Successfully returned cryptocurrency.",
        }
    },
)
async def get(
    id: str = Path(..., description="An id of a cryptocurrency"),
    db_engine: aiopg.sa.Engine = Depends(get_psql_engine),
) -> CryptocurrencyBaseSchema:
    async with db_engine.acquire() as db_connection:
        cryptocurrency_model = Cryptocurrency(db_connection)
        return await cryptocurrency_model.get(id)
