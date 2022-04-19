from fastapi import APIRouter, Body, Depends, Path, Query
from starlette.status import (
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_409_CONFLICT,
    HTTP_400_BAD_REQUEST,
)

router: APIRouter = APIRouter()


@router.post(
    "/cryptocurrency/",
    tags=["cryptocurrency"],
    #TODO: response_model=,
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
async def create_cryptocurrency(
        db: str,
        # TODO: cryptocurrency: model,
):
    return {"data": {"id": 15}}


@router.get(
    "/cryptocurrency/{id}/",
    tags=["cryptocurrency"],
    # TODO: response_model=,
    description="Get single cryptocurrency by id.",
    responses={
        HTTP_200_OK: {
            "description": "Successfully returned cryptocurrency.",
        },
    },
)
async def get_by_id(
    id: int = Path(..., description="An id of a "),
    # TODO: db: ,
) -> dict:

    return {"data": "sddsd"}
