from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from app.config.database_config import SessionLocal
from app.schema.project_metrics_schema import ProjectMetricsSchema
from app.schema.api_response_schema import ApiResponseObject, ApiResponseList
from app.service.project_metrics_service import ProjectMetricsService

project_metrics_router = APIRouter()


@project_metrics_router.get("/project-metrics", tags=["ProjectMetrics"], response_model=ApiResponseList)
async def get_project_metrics():
    sql_connection = SessionLocal()
    result = ProjectMetricsService(sql_connection).get_project_metrics().dict()
    return JSONResponse(content=result, status_code=status.HTTP_200_OK)


@project_metrics_router.post("/project-metrics", tags=["ProjectMetrics"], response_model=ApiResponseObject)
async def create_project_metrics(project_metrics: ProjectMetricsSchema):
    sql_connection = SessionLocal()
    result = ProjectMetricsService(sql_connection).create_project_metrics(project_metrics).dict()
    return JSONResponse(content=result, status_code=status.HTTP_200_OK)

