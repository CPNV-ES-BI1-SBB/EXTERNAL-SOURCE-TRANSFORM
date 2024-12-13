from fastapi import FastAPI
from app.routes import main as router

app = FastAPI(title="Transform", version="0.0.1")
app.include_router(router.api_router)