from fastapi import APIRouter


metrics_router = APIRouter()


@metrics_router.get("/")
async def read_root():
    return {"Hello": "World"}