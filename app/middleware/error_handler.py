import logging
from starlette.middleware.base import BaseHTTPMiddleware, DispatchFunction
from fastapi import FastAPI, HTTPException, Request, Response, status
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException as StarletteHTTPException

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class ExceptionHandlerMiddleware(BaseHTTPMiddleware):

    def __init__(self, app: FastAPI) -> None:
        super().__init__(app)

    async def dispatch(self, request: Request, call_next: DispatchFunction) -> Response | JSONResponse:
        try:
            return await call_next(request)
        except HTTPException as e:
            return JSONResponse({
                "status": 1.2,
                "message": e.detail
            }, status_code=e.status_code)
        except Exception as e:
            return JSONResponse({
                "status": 1.2,
                "message": str(e)
            }, status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)


async def http_exception_handler(request: Request, e: StarletteHTTPException):
    return JSONResponse({
        "status": 1.2,
        "message": e.detail
    }, status_code=e.status_code)

