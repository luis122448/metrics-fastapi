import asyncio
from fastapi import APIRouter, status, WebSocket, Depends, WebSocketDisconnect
from starlette.responses import JSONResponse
from config.database_config import SessionLocal
from schema.metrics_schema import MetricsSchema, CreateMetricsSchema, UpdateMetricsSchema
from schema.api_response_schema import ApiResponseList, ApiResponseObject
from service.metrics_service import MetricsService

metrics_router = APIRouter()


@metrics_router.get('/metrics/{project_id}', tags=["METRICS"], response_model=ApiResponseList)
def get_metrics(project_id: int):
    sql_connection = SessionLocal()
    result = MetricsService(sql_connection).get_metrics(project_id).dict()
    return JSONResponse(content=result, status_code=status.HTTP_200_OK)


@metrics_router.post('/metrics', tags=["METRICS"], response_model=ApiResponseObject)
def create_metrics(metrics: CreateMetricsSchema):
    sql_connection = SessionLocal()
    result = MetricsService(sql_connection).create_metrics(metrics).dict()
    return JSONResponse(content=result, status_code=status.HTTP_200_OK)


@metrics_router.put('/metrics', tags=["METRICS"], response_model=ApiResponseObject)
def update_metrics(metrics: UpdateMetricsSchema):
    sql_connection = SessionLocal()
    result = MetricsService(sql_connection).update_metrics(metrics).dict()
    return JSONResponse(content=result, status_code=status.HTTP_200_OK)


@metrics_router.patch('/metrics', tags=["METRICS"], response_model=ApiResponseObject)
def update_metrics(metrics: UpdateMetricsSchema):
    sql_connection = SessionLocal()
    result = MetricsService(sql_connection).update_metrics_by_increment(metrics).dict()
    return JSONResponse(content=result, status_code=status.HTTP_200_OK)


@metrics_router.delete('/metrics/{metrics_id}', tags=["METRICS"], response_model=ApiResponseObject)
def delete_metrics(metrics_id: int):
    sql_connection = SessionLocal()
    result = MetricsService(sql_connection).delete_metrics(metrics_id).dict()
    return JSONResponse(content=result, status_code=status.HTTP_200_OK)


@metrics_router.websocket('/metrics/websocket/{project_id}')
async def websocket_endpoint(websocket: WebSocket, project_id: int):
    sql_connection = SessionLocal()
    try:
        await websocket.accept()
        metrics_service = MetricsService(sql_connection)
        while True:
            metrics = metrics_service.get_metrics(project_id)
            await websocket.send_json(metrics.dict())
            await asyncio.sleep(1)
    except WebSocketDisconnect:
        print(f"WebSocket connection closed for project_id: {project_id}")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        try:
            await websocket.close()
        except RuntimeError as close_error:
            print(f"Error during WebSocket close: {close_error}")
        finally:
            sql_connection.close()
