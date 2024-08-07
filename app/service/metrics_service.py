from model.metrics_model import MetricsModel
from schema.metrics_schema import MetricsSchema
from schema.api_response_schema import ApiResponseObject, ApiResponseList


class MetricsService:

    def __init__(self, sql_connection) -> None:
        self.sql_connection = sql_connection

    def get_metrics(self, project_id: int):
        object_response = ApiResponseList(status=1.0, message="Success")
        result = self.sql_connection.query(MetricsModel).filter(MetricsModel.project_id == project_id).all()
        object_response.list = [metric.to_dict() for metric in result]
        return object_response
    
    def create_metrics(self, metrics: MetricsSchema):
        object_response = ApiResponseObject(status=1.0, message="Success")
        new_metrics = MetricsModel(**metrics.dict())
        self.sql_connection.add(new_metrics)
        self.sql_connection.commit()
        self.sql_connection.refresh(new_metrics)
        object_response.object = new_metrics.to_dict()
        return object_response

    def update_metrics(self, metrics_id: int, metrics: MetricsSchema):
        object_response = ApiResponseObject(status=1.0, message="Success")
        metrics_new = self.sql_connection.query(MetricsModel).filter(MetricsModel.id == metrics_id).first()
        if metrics_new is None:
            object_response.status = 0.0
            object_response.message = "Metrics not found"
            return object_response
        elif metrics_new.metrics_type != 'INTEGER':
            metrics_new.value_integer = metrics.value_integer
        elif metrics_new.metrics_type != 'STRING':
            metrics_new.value_string = metrics.value_string
        elif metrics_new.metrics_type != 'FLOAT':
            metrics_new.value_float = metrics.value_float
        elif metrics_new.metrics_type != 'DATE':
            metrics_new.value_date = metrics.value_date
        self.sql_connection.commit()
        self.sql_connection.refresh(metrics_new)
        object_response.object = metrics_new.to_dict()
        return object_response

    def delete_metrics(self, metrics_id: int):
        object_response = ApiResponseObject(status=1.0, message="Success")
        metrics = self.sql_connection.query(MetricsModel).filter(MetricsModel.id == metrics_id).first()
        self.sql_connection.delete(metrics)
        self.sql_connection.commit()
        return object_response
