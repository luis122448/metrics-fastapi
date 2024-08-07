from fastapi import FastAPI
from router.project_router import project_router
from router.metrics_router import metrics_router
from config.database_config import engine, Base

app = FastAPI()

app.title = "Metrics API"
app.version = "0.1"
app.description = "API for metrics management"
app.docs_url = "/docs"

Base.metadata.create_all(bind=engine)

app.include_router(project_router)
app.include_router(metrics_router)
