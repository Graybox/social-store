"""API route definitions."""

from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def root() -> dict:
    """Root endpoint."""
    return {"message": "Vedic Time Engine"}
