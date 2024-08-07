from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from config.database_config import SessionLocal
from schema.project_schema import ProjectSchema
from schema.api_response_schema import ApiResponseObject, ApiResponseList
from service.project_service import ProjectService

project_router = APIRouter()


@project_router.get("/project", tags=["Project"], response_model=ApiResponseList)
async def get_project():
    sql_connection = SessionLocal()
    result = ProjectService(sql_connection).get_project().dict()
    return JSONResponse(content=result, status_code=status.HTTP_200_OK)


@project_router.post("/project", tags=["Project"], response_model=ApiResponseObject)
async def create_project(project: ProjectSchema):
    sql_connection = SessionLocal()
    result = ProjectService(sql_connection).create_project(project).dict()
    return JSONResponse(content=result, status_code=status.HTTP_200_OK)

