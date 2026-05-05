from fastapi import FastAPI
from app.api.v1.routers import gists

app = FastAPI(title="GitHub Gists API")

app.include_router(gists.router, prefix="/api/v1")


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/ready")
def readiness_check():
    return {"status": "ready"}