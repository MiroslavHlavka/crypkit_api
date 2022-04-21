from typing import Callable, List

from pydantic import BaseModel, Field
from starlette.responses import Response
from starlette.status import HTTP_404_NOT_FOUND, HTTP_409_CONFLICT


class ErrorResponse(BaseModel):
    code: int = Field(..., description="Error status code")
    message: str = Field(..., description="Error message")
    errors: List[str]

    def response(self) -> Response:
        return Response(
            content=self.json(),
            media_type="application/json",
            status_code=self.code,
        )


RESPONSE_404_NOT_FOUND_BY_ID: Callable[
    [str], Response
] = lambda pk_id: ErrorResponse.construct(
    code=HTTP_404_NOT_FOUND,
    message=f"Cryptocurrency with id '{pk_id}' has not been found.",
).response()


RESPONSE_409_CONFLICT = ErrorResponse.construct(
    code=HTTP_409_CONFLICT,
    message="Cryptocurrency already exists.",
).response()
