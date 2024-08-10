from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from router.project_router import project_router
from router.metrics_router import metrics_router
from config.database_config import engine, Base
from middleware.error_handler import ExceptionHandlerMiddleware, http_exception_handler
from starlette.exceptions import HTTPException as StarletteHTTPException

app = FastAPI()

app.title = "Metrics API"
app.version = "0.1"
app.description = "API for metrics management"
app.docs_url = "/docs"

# Base.metadata.create_all(bind=engine)

# Add middleware
origins = [
    "https://luis122448.com",
    "https://dota-shuffle-angular-production.up.railway.app",
    "https://dota-shuffle-production.up.railway.app",
    "http://localhost:4200",
    "http://localhost:4600",
    "http://localhost:4800",
    "http://localhost:8000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST","PUT", "PATCH", "DELETE"],
    allow_headers=["*"],
)
app.add_middleware(ExceptionHandlerMiddleware)

# Exception Handler
app.add_exception_handler(StarletteHTTPException, http_exception_handler)

# Add routes
app.include_router(project_router)
app.include_router(metrics_router)


@app.websocket("/communicate")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"Message text was: {data}")