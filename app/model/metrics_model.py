from config.database_config import Base
from sqlalchemy import Column, Float, Integer, String, DateTime, PrimaryKeyConstraint, Index, ForeignKeyConstraint
from datetime import datetime


class MetricsModel(Base):
    __tablename__ = "TBL_METRICS"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    project_id = Column(Integer, nullable=False)
    metrics_type = Column(String(50), nullable=False)
    name = Column(String(50))
    value_integer = Column(Integer)
    value_float = Column(Float)
    value_string = Column(String(50))
    value_date = Column(DateTime)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)

    # __table_args__ = (
    #     PrimaryKeyConstraint('id', 'project_id', name='PK_METRICS'),
    #     Index('IDX_METRICS_PROJECT_TYPE_NAME', 'id', 'project_id'),
    # )

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
