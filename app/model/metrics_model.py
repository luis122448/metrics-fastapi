from app.config.database_config import Base
from sqlalchemy import Column, Float, Integer, String, DateTime, PrimaryKeyConstraint, Index, ForeignKeyConstraint
from datetime import datetime


class MetricsModel(Base):
    __tablename__ = "METRICS"

    id = Column(Integer, nullable=False)
    project_id = Column(Integer, nullable=False)
    metrics_type = Column(String(50), nullable=False)
    name = Column(String(50))
    value_integer = Column(Integer)
    value_float = Column(Float)
    value_string = Column(String(50))
    value_date = Column(DateTime)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)

    __table_args__ = (
        PrimaryKeyConstraint('project_id', 'metrics_type', name='PK_METRICS'),
        ForeignKeyConstraint(['project_id'], ['PROJECT.id'], name='FK_METRICS_PROJECT_METRICS_ID'),
        Index('IDX_METRICS_PROJECT_TYPE_NAME', 'project_id', 'metrics_type'),
    )

    def to_dict(self):
        def convert_datetime(dt):
            return dt.isoformat() if dt else None
        return {
            "id": self.id,
            "project_id": self.project_id,
            "metrics_type": self.metrics_type,
            "name": self.name,
            "value_integer": self.value_integer,
            "value_float": self.value_float,
            "value_string": self.value_string,
            "value_date": convert_datetime(self.value_date),
            "created_at": convert_datetime(self.created_at),
            "updated_at": convert_datetime(self.updated_at),
        }
