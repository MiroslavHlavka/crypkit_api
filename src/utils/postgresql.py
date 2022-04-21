import aiopg.connection
import aiopg.sa
from llconfig import Config


async def get_postgresql_connection(config: Config) -> aiopg.sa.Engine:
    """Open connections to PostgreSQL server."""
    return await postgresql_engine(config)


async def postgresql_engine(
    config: Config,
    timeout: float = aiopg.connection.TIMEOUT,
) -> aiopg.sa.Engine:
    """Create connection engine for PostgreSQL server."""
    return await aiopg.sa.create_engine(
        dsn=f"postgresql://{config['DB_USER']}:{config['DB_PASSWORD']}@{config['DB_HOST']}/{config['DB_DBNAME']}",
        timeout=timeout,
    )
