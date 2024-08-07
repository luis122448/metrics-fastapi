from fastapi import APIRouter, status
from starlette.responses import JSONResponse
from config.database_config import SessionLocal
from schema.metrics_schema import MetricsSchema
from schema.api_response_schema import ApiResponseList, ApiResponseObject
from service.metrics_service import MetricsService

metrics_router = APIRouter()


@metrics_router.get('/metrics/{project_id}', tags=["METRICS"], response_model=ApiResponseList)
def get_metrics(project_id: int):
    sql_connection = SessionLocal()
    result = MetricsService(sql_connection).get_metrics(project_id).dict()
    return JSONResponse(content=result, status_code=status.HTTP_200_OK)


@metrics_router.post('/metrics', tags=["METRICS"], response_model=ApiResponseObject)
def create_metrics(metrics: MetricsSchema):
    sql_connection = SessionLocal()
    result = MetricsService(sql_connection).create_metrics(metrics).dict()
    return JSONResponse(content=result, status_code=status.HTTP_200_OK)


@metrics_router.put('/metrics/{metrics_id}', tags=["METRICS"], response_model=ApiResponseObject)
def update_metrics(metrics_id: int, metrics: MetricsSchema):
    sql_connection = SessionLocal()
    result = MetricsService(sql_connection).update_metrics(metrics_id, metrics).dict()
    return JSONResponse(content=result, status_code=status.HTTP_200_OK)


@metrics_router.delete('/metrics/{metrics_id}', tags=["METRICS"], response_model=ApiResponseObject)
def delete_metrics(metrics_id: int):
    sql_connection = SessionLocal()
    result = MetricsService(sql_connection).delete_metrics(metrics_id).dict()
    return JSONResponse(content=result, status_code=status.HTTP_200_OK)