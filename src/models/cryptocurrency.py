from typing import Union

import psycopg2
from sqlalchemy import delete, insert, select, update

from src.models.base_model import BaseModel
from src.models.schemas.cryptocurrency import \
    cryptocurrency as cryptocurrency_table
from src.models.schemas.responses.cryptocurrency import (
    CryptocurrencyBaseSchema, CryptocurrencyCreateSchema,
    CryptocurrencyIdSchema, CryptocurrencyUpdateSchema)


class Cryptocurrency(BaseModel):
    async def create(
        self, cryptocurrency: CryptocurrencyCreateSchema
    ) -> Union[CryptocurrencyIdSchema, None]:
        """Insert data into database."""
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
        except psycopg2.Error:
            return None

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
            return None

        row = await result.fetchone()

        if not row:
            return None

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
            return None

        return CryptocurrencyIdSchema(id=row.id)

    async def get(self, id: str) -> Union[CryptocurrencyBaseSchema, None]:
        """Get cryptocurrency."""

        query = select(cryptocurrency_table).where(cryptocurrency_table.c.id == id)
        result = await self.conn.execute(query)
        row = await result.fetchone()

        if not row:
            return None

        return CryptocurrencyBaseSchema(**row)
