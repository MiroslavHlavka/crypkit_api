from fastapi import APIRouter
from llconfig import Config

from src.config import init_config

system_router = APIRouter()
config: Config = init_config()


@system_router.get("/ping")
async def ping() -> str:
    return "pong"


@system_router.get("/")
async def root() -> dict:
    return {
        "service": config["SERVICE_NAME"],
        "environment": config["ENV"],
    }
