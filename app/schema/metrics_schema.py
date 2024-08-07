from typing import Optional, Any
from pydantic import BaseModel
from datetime import datetime


class MetricsSchema(BaseModel):
    id: Optional[int] = None
    project_id: int
    metrics_type: str
    name: str
    value_integer: Optional[int] = None
    value_float: Optional[float] = None
    value_string: Optional[str] = None
    value_date: Optional[datetime] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        json_encoders = {
            datetime: lambda v: v.isoformat(),
        }
        model_config = {
            "json_schema_extra": {
                "examples": [{
                    "id": 0,
                    "project_id": 0,
                    "metrics_type": "integer",
                    "name": "metrics-sample",
                    "value_integer": 1,
                    "value_float": 0,
                    "value_string": "",
                    "value_date": "2021-09-01T00:00:00"
                }]
            }
        }


class BasicMetricsSchema(BaseModel):
    project_id: int
    metrics_type: str
    value_integer: Optional[int] = None
    value_float: Optional[float] = None
    value_string: Optional[str] = None
    value_date: Optional[datetime] = None

    class Config:
        json_encoders = {
            datetime: lambda v: v.isoformat(),
        }
        model_config = {
            "json_schema_extra": {
                "examples": [{
                    "project_id": 0,
                    "metrics_type": "INTEGER",
                    "value_integer": "",
                    "value_float": "",
                    "value_string": "",
                    "value_date": ""
                }]
            }
        }
