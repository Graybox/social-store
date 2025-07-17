"""Pydantic schemas for API inputs and outputs."""

from typing import Any, Dict, List

from pydantic import BaseModel, Field


class Location(BaseModel):
    """Geographic location details."""

    lat: float = Field(..., example=19.076)
    long: float = Field(..., example=72.8777)
    tz: str = Field(..., example="Asia/Kolkata")


class VedicTimeResponse(BaseModel):
    """Full response model for the ``/vedic-time`` endpoint."""

    date: str
    location: Location
    sun: Dict[str, str]
    vedic_time: Dict[str, Any]
    choghadiya: Dict[str, List[Dict[str, str]]]
    rahukalam: Dict[str, str]
    abhijit_muhurta: Dict[str, str]
    festivals: List[str]
    adhik_maas: bool

    class Config:
        schema_extra = {
            "example": {
                "date": "2025-07-17",
                "location": {"lat": 19.076, "long": 72.8777, "tz": "Asia/Kolkata"},
                "sun": {"sunrise": "06:02", "sunset": "18:55"},
                "vedic_time": {
                    "weekday": "Thursday",
                    "tithi": {"name": "Shukla Chaturthi"},
                    "nakshatra": "Rohini",
                    "yoga": "Vyatipata",
                    "karana": "Vanija",
                    "ghati": 21,
                    "vighati": 43,
                },
                "choghadiya": {
                    "day": [
                        {"start": "06:02", "end": "07:32", "type": "Char"}
                    ],
                    "night": [
                        {"start": "19:01", "end": "20:31", "type": "Labh"}
                    ],
                },
                "rahukalam": {"start": "09:08", "end": "10:38"},
                "abhijit_muhurta": {"start": "12:13", "end": "13:01"},
                "festivals": ["Vinayaka Chaturthi"],
                "adhik_maas": False,
            }
        }
