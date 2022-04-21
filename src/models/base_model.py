import abc

from aiopg.sa import SAConnection

from src.services.coingecko import CoingeckoService


class BaseModel(abc.ABC):
    """Base model class.

    Provides connection to SQL server.
    """

    def __init__(self, conn: SAConnection):
        self.conn = conn

    @abc.abstractmethod
    async def create(self, id: str, coingecko: CoingeckoService) -> None:
        """Insert/update data into database."""
        raise NotImplementedError()

    @abc.abstractmethod
    async def delete(self, id: str) -> None:
        """Delete row with matching id.

        :param:`ids` is empty as SQLAlchemy will run havoc with
        `DELETE FROM table`!
        """
        raise NotImplementedError()

    @abc.abstractmethod
    async def get(self, id: str) -> str:
        """Get rows with matching ids."""
        raise NotImplementedError()
