from app.model.metrics_model import MetricsModel
from app.model.project_metrics_model import ProjectMetricsModel
from app.schema.project_metrics_schema import ProjectMetricsSchema
from app.schema.api_response_schema import ApiResponseObject, ApiResponseList


class ProjectMetricsService:

    def __init__(self, sql_connection) -> None:
        self.sql_connection = sql_connection

    def get_project_metrics(self):
        object_response = ApiResponseList(status=1.0, message="Success")
        result = self.sql_connection.query(ProjectMetricsModel).all()
        object_response.list = [metric.to_dict() for metric in result]
        return object_response

    def create_project_metrics(self, project_metrics: ProjectMetricsSchema):
        object_response = ApiResponseObject(status=1.0, message="Success")
        new_project_metrics = ProjectMetricsModel(name=project_metrics.name)
        self.sql_connection.add(new_project_metrics)
        self.sql_connection.commit()
        self.sql_connection.refresh(new_project_metrics)
        object_response.object = new_project_metrics.to_dict()
        return object_response

    def update_project_metrics(self, project_metrics_id: int, name: str):
        object_response = ApiResponseObject(status=1.0, message="Success")
        project_metrics = self.sql_connection.query(ProjectMetricsModel).filter(ProjectMetricsModel.id == project_metrics_id).first()
        project_metrics.name = name
        self.sql_connection.commit()
        self.sql_connection.refresh(project_metrics)
        object_response.object = project_metrics.to_dict()
        return object_response

    def delete_project_metrics(self, project_metrics_id: int):
        object_response = ApiResponseObject(status=1.0, message="Success")
        project_metrics = self.sql_connection.query(ProjectMetricsModel).filter(ProjectMetricsModel.id == project_metrics_id).first()
        self.sql_connection.delete(project_metrics)
        self.sql_connection.commit()
        return object_response
