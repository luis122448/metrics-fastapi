from fastapi import FastAPI
from app.router.project_metrics_router import project_metrics_router
from app.router.metrics_router import metrics_router
from app.config.database_config import engine, Base

app = FastAPI()

app.title = "Metrics API"
app.version = "0.1"
app.description = "API for metrics management"
app.docs_url = "/docs"

Base.metadata.create_all(bind=engine)

app.include_router(project_metrics_router)
app.include_router(metrics_router)
