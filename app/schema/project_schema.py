from typing import Optional, Any
from pydantic import BaseModel
from datetime import datetime


class ProjectSchema(BaseModel):
    id: Optional[int] = None
    name: str
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
                    "name": "project-sample"
                }]
            }
        }
