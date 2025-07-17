"""Utilities for high level calendar calculations."""

from typing import List


MAASA_NAMES: List[str] = [
    "Chaitra",
    "Vaishakha",
    "Jyeshtha",
    "Ashadha",
    "Shravana",
    "Bhadrapada",
    "Ashwin",
    "Kartik",
    "Margashirsha",
    "Pausha",
    "Magha",
    "Phalguna",
]


def get_paksha(tithi_index: int) -> str:
    """Return the paksha name for ``tithi_index``."""

    index = tithi_index % 30
    return "Shukla" if index < 15 else "Krishna"


def get_lunar_maasa(sun_lon: float, moon_lon: float) -> str:
    """Return the lunar month name based on Sun/Moon longitudes."""

    diff = (moon_lon - sun_lon) % 360
    month_index = int(diff // 30)
    return MAASA_NAMES[month_index]


def calculate_calendar(*args, **kwargs):
    """Legacy compatibility wrapper."""
    pass
