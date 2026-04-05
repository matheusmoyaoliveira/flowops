from fastapi import FastAPI

from app.core.config import settings

app = FastAPI(
    title=settings.app_name,
    version="0.1.0"
)

@app.get("/")
def read_root():
    return {
        "message": f"{settings.app_name} API is running",
        "environment": settings.app_env
    }

@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "app": settings.app_name,
        "environment": settings.app_env
    }