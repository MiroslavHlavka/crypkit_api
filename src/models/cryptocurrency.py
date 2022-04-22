from typing import Union

import psycopg2
from fastapi import HTTPException
from sqlalchemy import delete, insert, select, update

from src.models.base_model import BaseModel
from src.models.schemas.cryptocurrency import \
    cryptocurrency as cryptocurrency_table
from src.models.schemas.responses.cryptocurrency import (
    CryptocurrencyBaseSchema, CryptocurrencyCreateSchema,
    CryptocurrencyIdSchema, CryptocurrencyUpdateSchema)
from src.services.coingecko import CoingeckoService


class Cryptocurrency(BaseModel):
    async def create(
        self, cryptocurrency: CryptocurrencyCreateSchema, coingecko: CoingeckoService
    ) -> Union[CryptocurrencyIdSchema, None]:
        """Insert data into database."""

        coingecko_cryptocurrency = await coingecko.get_cryptocurrency(cryptocurrency.id)
        if coingecko_cryptocurrency and coingecko_cryptocurrency["symbol"] == cryptocurrency.symbol:
            raise HTTPException(
                status_code=409,
                detail=f"Symbol {cryptocurrency.symbol} is already used on "
                f"coingecko",
            )

        query = (
            insert(cryptocurrency_table)
            .values(
                id=cryptocurrency.id,
                symbol=cryptocurrency.symbol,
                name=cryptocurrency.name,
                description=cryptocurrency.description,
                created_at=cryptocurrency.created_at,
            )
            .returning(cryptocurrency_table.c.id)
        )
        try:
            result = await self.conn.execute(query)
        except psycopg2.Error as e:
            raise HTTPException(
                status_code=500,
                detail=f"Database error: {e}",
            )

        row = await result.fetchone()

        return CryptocurrencyIdSchema(id=row.id)

    async def update(
        self, id: str, cryptocurrency: CryptocurrencyUpdateSchema
    ) -> Union[CryptocurrencyBaseSchema, None]:
        """Update data into database."""
        query = (
            update(cryptocurrency_table)
            .values(
                id=cryptocurrency.id,
                symbol=cryptocurrency.symbol,
                name=cryptocurrency.name,
                description=cryptocurrency.description,
                created_at=cryptocurrency.created_at,
            )
            .where(cryptocurrency_table.c.id == id)
            .returning(cryptocurrency_table)
        )
        try:
            result = await self.conn.execute(query)
        except psycopg2.Error:
            raise HTTPException(
                status_code=500,
                detail=f"Database error: {e}",
            )

        row = await result.fetchone()

        if not row:
            raise HTTPException(
                status_code=404,
                detail=f"Cryptocurrency {id} not found",
            )

        return CryptocurrencyBaseSchema(**row)

    async def delete(
        self,
        id: str,
    ) -> Union[CryptocurrencyIdSchema, None]:
        """Delete row with matching id.

        `DELETE FROM table`!
        """
        query = (
            delete(cryptocurrency_table)
            .where(cryptocurrency_table.c.id == id)
            .returning(cryptocurrency_table.c.id)
        )

        result = await self.conn.execute(query)
        row = await result.fetchone()

        if not row:
            raise HTTPException(
                status_code=404,
                detail=f"Cryptocurrency {id} not found",
            )

        return CryptocurrencyIdSchema(id=row.id)

    async def get(self, id: str) -> Union[CryptocurrencyBaseSchema, None]:
        """Get cryptocurrency."""

        query = select(cryptocurrency_table).where(cryptocurrency_table.c.id == id)
        result = await self.conn.execute(query)
        row = await result.fetchone()

        if not row:
            raise HTTPException(
                status_code=404,
                detail=f"Cryptocurrency {id} not found",
            )

        return CryptocurrencyBaseSchema(**row)
