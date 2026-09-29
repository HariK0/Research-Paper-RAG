from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from app.config import get_settings
from app.database import database_is_ready

settings = get_settings()
app = FastAPI(title=settings.app_name, version="0.1.0")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/api/health", tags=["health"])
@app.get("/api/v1/health", tags=["health"])
def health() -> dict[str, str]:
    return {"status": "ok", "environment": settings.app_env}


@app.get("/api/health/ready", tags=["health"])
def readiness() -> dict[str, str]:
    if not database_is_ready():
        raise HTTPException(status_code=503, detail="Database is not ready")
    return {"status": "ready", "database": "connected"}
