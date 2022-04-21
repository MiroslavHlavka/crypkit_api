from typing import Union

import aiopg.sa
from fastapi import APIRouter, Depends, Path
from starlette.responses import Response
from starlette.status import (HTTP_200_OK, HTTP_201_CREATED,
                              HTTP_404_NOT_FOUND, HTTP_409_CONFLICT)

from src.models.cryptocurrency import Cryptocurrency
from src.models.schemas.responses.common import (RESPONSE_404_NOT_FOUND_BY_ID,
                                                 RESPONSE_409_CONFLICT)
from src.models.schemas.responses.cryptocurrency import (
    CryptocurrencyBaseSchema, CryptocurrencyCreateSchema,
    CryptocurrencyIdSchema, CryptocurrencyUpdateSchema)
from src.routers import get_psql_engine, get_coingecko_service
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
        },
        HTTP_409_CONFLICT: {
            "description": "Cryptocurrency already exists.",
        },
    },
)
async def create(
    cryptocurrency: CryptocurrencyCreateSchema,
    db_engine: aiopg.sa.Engine = Depends(get_psql_engine),
    coingecko: CoingeckoService = Depends(get_coingecko_service),
) -> Union[CryptocurrencyIdSchema, Response]:
    async with db_engine.acquire() as db_connection:
        cryptocurrency_model = Cryptocurrency(db_connection)
        result = await cryptocurrency_model.create(cryptocurrency, coingecko)

        if not result:
            return RESPONSE_409_CONFLICT

        return result


@router.delete(
    "/cryptocurrency/{id}",
    tags=["cryptocurrency"],
    response_model=CryptocurrencyIdSchema,
    description="Delete cryptocurrency",
    status_code=HTTP_201_CREATED,
    responses={
        HTTP_200_OK: {
            "description": "Successfully deleted.",
        },
        HTTP_404_NOT_FOUND: {
            "description": "Cryptocurrency have not been found.",
            "content": {
                "application/json": {
                    "example": RESPONSE_404_NOT_FOUND_BY_ID("bitcoin").body,
                },
            },
        },
    },
)
async def delete(
    id: str = Path(..., description="An id of cryptocurrency."),
    db_engine: aiopg.sa.Engine = Depends(get_psql_engine),
) -> Union[CryptocurrencyIdSchema, Response]:
    async with db_engine.acquire() as db_connection:
        cryptocurrency_model = Cryptocurrency(db_connection)
        result = await cryptocurrency_model.delete(id)

        if not result:
            return RESPONSE_404_NOT_FOUND_BY_ID(id)

        return result


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
) -> Union[CryptocurrencyBaseSchema, Response]:
    async with db_engine.acquire() as db_connection:
        cryptocurrency_model = Cryptocurrency(db_connection)
        result = await cryptocurrency_model.update(id, cryptocurrency)

        if not result:
            return RESPONSE_404_NOT_FOUND_BY_ID(id)

        return result


@router.get(
    "/cryptocurrency/{id}/",
    tags=["cryptocurrency"],
    response_model=CryptocurrencyBaseSchema,
    description="Get single cryptocurrency by id.",
    responses={
        HTTP_200_OK: {
            "description": "Successfully returned cryptocurrency.",
        },
        HTTP_404_NOT_FOUND: {
            "description": "Cryptocurrency have not been found.",
            "content": {
                "application/json": {
                    "example": RESPONSE_404_NOT_FOUND_BY_ID("bitcoin").body,
                },
            },
        },
    },
)
async def get(
    id: str = Path(..., description="An id of a cryptocurrency"),
    db_engine: aiopg.sa.Engine = Depends(get_psql_engine),
) -> Union[CryptocurrencyBaseSchema, Response]:
    async with db_engine.acquire() as db_connection:
        cryptocurrency_model = Cryptocurrency(db_connection)
        result = await cryptocurrency_model.get(id)

        if not result:
            return RESPONSE_404_NOT_FOUND_BY_ID(id)

        return result
