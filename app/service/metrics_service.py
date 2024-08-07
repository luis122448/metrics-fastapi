from app.model.metrics_model import MetricsModel


class MetricsService:

    def __init__(self, sql_connection) -> None:
        self.sql_connection = sql_connection

    def get_metrics(self, project_id: int):
        result = self.sql_connection.execute(
            f"SELECT * FROM metrics WHERE project_id = {project_id}")
        return result.fetchall()
    
    def create_metrics(self, project_id: int, metrics_type: str, name: str, value_integer: int, value_float: float, value_string: str, value_date: str):
        new_metrics = MetricsModel(project_id=project_id, metrics_type=metrics_type, name=name, value_integer=value_integer, value_float=value_float, value_string=value_string, value_date=value_date)
        self.sql_connection.add(new_metrics)
        self.sql_connection.commit()
        self.sql_connection.refresh(new_metrics)
        return new_metrics
