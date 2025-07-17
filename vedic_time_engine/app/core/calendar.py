"""Utilities for high level calendar calculations."""

from typing import List
import os
from dotenv import load_dotenv
import swisseph as swe


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


def is_adhik_maas(start_jd: float, end_jd: float) -> bool:
    """Return ``True`` if the period has no solar sign change.

    Parameters
    ----------
    start_jd : float
        Julian Day of the start of the lunar month (likely a New Moon).
    end_jd : float
        Julian Day of the end of the lunar month (next New Moon).

    Returns
    -------
    bool
        ``True`` if the Sun does not enter a new zodiac sign between
        ``start_jd`` and ``end_jd``; ``False`` otherwise.
    """

    load_dotenv()
    swe.set_ephe_path(os.getenv("SWISSEPH_PATH", "ephe/"))

    flags = swe.FLG_SWIEPH
    jd = start_jd
    lon, _ = swe.calc_ut(jd, swe.SUN, flags)
    prev_sign = int(lon[0] // 30)

    step = 1.0
    while jd < end_jd:
        jd += step
        lon, _ = swe.calc_ut(min(jd, end_jd), swe.SUN, flags)
        current_sign = int(lon[0] // 30)
        if current_sign != prev_sign:
            return False

    return True


def calculate_calendar(*args, **kwargs):
    """Legacy compatibility wrapper."""
    pass
