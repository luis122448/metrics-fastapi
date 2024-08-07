from config.database_config import Base
from sqlalchemy import Column, Float, Integer, String, DateTime
from datetime import datetime


class ProjectModel(Base):
    __tablename__ = "project"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, onupdate=datetime.utcnow)

    def to_dict(self):
        def convert_datetime(dt):
            return dt.isoformat() if dt else None
        return {
            "id": self.id,
            "name": self.name,
            "created_at": convert_datetime(self.created_at),
            "updated_at": convert_datetime(self.updated_at),
        }
