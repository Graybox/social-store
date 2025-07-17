"""Pydantic schemas for API inputs and outputs."""

from typing import Any, Dict, List

from pydantic import BaseModel


class Location(BaseModel):
    """Geographic location details."""

    lat: float
    long: float
    tz: str


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
                "location": {"lat": 12.97, "long": 77.59, "tz": "Asia/Kolkata"},
                "sun": {"sunrise": "06:00", "sunset": "18:30"},
                "vedic_time": {
                    "weekday": "Thursday",
                    "tithi": {"name": "Shukla Paksha Pratipada"},
                    "nakshatra": "Ashwini",
                    "yoga": "Shubha",
                    "karana": "Bava",
                    "ghati": 10,
                    "vighati": 20,
                },
                "choghadiya": {
                    "day": [
                        {"start": "06:00", "end": "07:30", "type": "Udveg"}
                    ],
                    "night": [
                        {"start": "19:00", "end": "20:30", "type": "Rog"}
                    ],
                },
                "rahukalam": {"start": "13:30", "end": "15:00"},
                "abhijit_muhurta": {"start": "12:00", "end": "12:48"},
                "festivals": ["Guru Purnima"],
                "adhik_maas": False,
            }
        }
