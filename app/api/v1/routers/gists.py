# app/api/v1/routers/gists.py
from fastapi import APIRouter, HTTPException
from app.services.github_service import fetch_user_gists
from app.schemas.gist import GistResponse

router = APIRouter()


# Homepage / Root endpoint
@router.get("/")
@router.get("/home")
def home():
    return {
        "message": "Welcome to GitHub Gists API",
        "version": "1.0.0",
        "endpoints": {
            "get_user_gists": "/api/v1/{username}",
            "health_check": "/api/v1/health"
        }
    }


# /health
@router.get("/health")
def health_check():
    return {
        "status": "ok"
    }


# /ready
@router.get("/ready")
def readiness_check():
    return {
        "status": "ready"
    }

# /username
@router.get("/users/{username}", response_model=list[GistResponse])
def get_gists(username: str):
    gists = fetch_user_gists(username)

    if gists is None:
        raise HTTPException(status_code=404, detail="User not found")

    return gists