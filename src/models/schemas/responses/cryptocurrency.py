from datetime import datetime

from pydantic import BaseModel, Field, constr


class CryptocurrencyIdSchema(BaseModel):
    id: constr(max_length=255) = Field(None, description="Unique id of cryptocurrency")


class CryptocurrencyBaseSchema(CryptocurrencyIdSchema, BaseModel):
    symbol: constr(max_length=10) = Field(description="symbol")
    name: str = Field(description="Name of cryptocurrency")
    description: str = Field(description="Description of cryptocurrency")
    created_at: datetime = Field(
        description="A datetime when cryptocurrency was created"
    )


class CryptocurrencyCreateSchema(CryptocurrencyBaseSchema):
    """Cryptocurrency create schema"""


class CryptocurrencyUpdateSchema(CryptocurrencyBaseSchema):
    """Cryptocurrency update schema"""
