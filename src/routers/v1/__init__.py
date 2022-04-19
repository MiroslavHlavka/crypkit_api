from fastapi.routing import APIRouter

from src.routers.v1.cryptocurrencies import router as cryptocurrencies_router

router: APIRouter = APIRouter(prefix="/v1")
router.include_router(cryptocurrencies_router)
