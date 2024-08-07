from model.metrics_model import MetricsModel
from model.project_model import ProjectModel
from schema.project_schema import ProjectSchema
from schema.api_response_schema import ApiResponseObject, ApiResponseList


class ProjectService:

    def __init__(self, sql_connection) -> None:
        self.sql_connection = sql_connection

    def get_project(self):
        object_response = ApiResponseList(status=1.0, message="Success")
        result = self.sql_connection.query(ProjectModel).all()
        object_response.list = [metric.to_dict() for metric in result]
        return object_response

    def create_project(self, project: ProjectSchema):
        object_response = ApiResponseObject(status=1.0, message="Success")
        new_project = ProjectModel(name=project.name)
        self.sql_connection.add(new_project)
        self.sql_connection.commit()
        self.sql_connection.refresh(new_project)
        object_response.object = new_project.to_dict()
        return object_response

    def update_project(self, project_id: int, name: str):
        object_response = ApiResponseObject(status=1.0, message="Success")
        project = self.sql_connection.query(ProjectModel).filter(ProjectModel.id == project_id).first()
        project.name = name
        self.sql_connection.commit()
        self.sql_connection.refresh(project)
        object_response.object = project.to_dict()
        return object_response

    def delete_project(self, project_id: int):
        object_response = ApiResponseObject(status=1.0, message="Success")
        project = self.sql_connection.query(ProjectModel).filter(ProjectModel.id == project_id).first()
        self.sql_connection.delete(project)
        self.sql_connection.commit()
        return object_response
