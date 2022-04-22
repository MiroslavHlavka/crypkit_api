import logging
import uvicorn
from llconfig import Config
from src.config import init_config
from src.routers import v1
from src.routers.system import system_router
from src.utils import postgresql
from starlette_exporter import PrometheusMiddleware, handle_metrics

from fastapi import FastAPI

logger = logging.getLogger(__name__)

config: Config = init_config()

app = FastAPI(
    title="Crypkit API",
    description="Service for managing cryptocurrencies",
    docs_url="/-/docs",
)
app.include_router(system_router)
app.include_router(v1.router)


@app.on_event("startup")
async def start_api():
    """Initialize API.

    Load configuration, initialize logging, etc.
    """
    try:
        # init postgresql engine
        app.state.psql = await postgresql.get_postgresql_connection(config)

        # init prometheus
        app.add_middleware(PrometheusMiddleware)
        app.add_route("/metrics", handle_metrics)
        # TODO: init sentry, metrics, logging etc here

    except Exception:
        logger.exception("Failed to finish fastapi.startup event")
        raise
    else:
        logger.info("Startup successfully finished")


@app.on_event("shutdown")
def stop():
    """Shutdown event. Just log it."""
    logger.info("Shutting down")


if __name__ == "__main__":
    uvicorn.run("__main__:app", host=config["HOST"], port=config["PORT"], debug=config["DEBUG"],
                reload=config["DEBUG"])
