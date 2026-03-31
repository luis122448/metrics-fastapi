from fastapi import APIRouter
from version import BUILD_VERSION_NUMBER, BUILD_VERSION_DATE

health_router = APIRouter()


@health_router.get("/ready")
async def readiness():
    return {
        "status": "ok",
        "version": BUILD_VERSION_NUMBER,
        "build_date": BUILD_VERSION_DATE,
    }
