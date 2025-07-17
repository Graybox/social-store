"""FastAPI application entry point."""

from fastapi import FastAPI

from .routes import router

app = FastAPI(
    title="Vedic Time Engine API",
    version="1.0.0",
    description=(
        "An API that provides Vedic calendar calculations (Panchang) for any date "
        "and location. Returns tithi, nakshatra, etc., in multiple languages."
    ),
    terms_of_service="https://example.com/terms",
    contact={"name": "Vedic Time Team", "email": "contact@example.com"},
    license_info={"name": "MIT", "url": "https://opensource.org/licenses/MIT"},
)

app.include_router(router)
