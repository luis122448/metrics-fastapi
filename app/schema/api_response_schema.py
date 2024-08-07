from pydantic import BaseModel
from typing import Optional, Any, List, Dict
from datetime import date, datetime


class ApiResponseObject(BaseModel):
    status: float
    message: str
    object: Optional[Any] = None
    log_message: Optional[str] = None
    log_user: Optional[str] = None

    class Config:
        json_encoders = {
            datetime: lambda v: v.isoformat(),
        }
        model_config = {
            "json_schema_extra": {
                "examples": [{
                    "status": 1.2,
                    "message": "Error Unauthorized",
                    "object": ""
                }]
            }
        }


class ApiResponseList(BaseModel):
    status: float
    message: str
    list: Optional[List[Dict[str, Any]]] = None
    log_message: Optional[str] = None
    log_user: Optional[str] = None

    class Config:
        json_encoders = {
            datetime: lambda v: v.isoformat(),
        }
        model_config = {
            "json_schema_extra": {
                "examples": [{
                    "status": 1.2,
                    "message": "Error Unauthorized",
                    "list": ""
                }]
            }
        }


class ApiResponseAuth(BaseModel):
    status: float
    message: str
    object: Optional[Any] = None

    class Config:
        json_encoders = {
            datetime: lambda v: v.isoformat(),
        }
        model_config = {
            "json_schema_extra": {
                "examples": [{
                    "status": 1.2,
                    "message": "Error Unauthorized",
                    "object": ""
                }]
            }
        }
