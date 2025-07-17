"""Utilities for Sun and Moon longitude calculations using Swiss Ephemeris."""

from __future__ import annotations

import os
from datetime import datetime
from typing import Tuple

from dotenv import load_dotenv
import swisseph as swe


load_dotenv()
swe.set_ephe_path(os.getenv("SWISSEPH_PATH", "ephe/"))


def to_julian_day(date_str: str) -> float:
    """Convert a ``YYYY-MM-DD`` date string to Julian Day at 0h UT."""

    dt = datetime.strptime(date_str, "%Y-%m-%d")
    return swe.julday(dt.year, dt.month, dt.day, 0.0, swe.GREG_CAL)


class EphemerisCalculator:
    """Wrapper to obtain Sun and Moon geocentric longitudes."""

    def get_sun_moon_longitudes(self, jd: float) -> Tuple[float, float]:
        """Return the Sun and Moon ecliptic longitudes for ``jd`` (UT)."""

        flags = swe.FLG_SWIEPH
        sun_pos, _ = swe.calc_ut(jd, swe.SUN, flags)
        moon_pos, _ = swe.calc_ut(jd, swe.MOON, flags)
        return sun_pos[0], moon_pos[0]

