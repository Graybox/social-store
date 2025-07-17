"""Calendar related utilities."""

from __future__ import annotations

import os
from dotenv import load_dotenv
import swisseph as swe

from .sun_moon import EphemerisCalculator


load_dotenv()
swe.set_ephe_path(os.getenv("SWISSEPH_PATH", "ephe/"))


def calculate_calendar(*args, **kwargs):
    """Calculate calendar."""
    pass


def is_adhik_maas(start_jd: float, end_jd: float) -> bool:
    """Return ``True`` if the interval [``start_jd``, ``end_jd``] has no solar
    ingress.

    Parameters
    ----------
    start_jd : float
        Julian Day of the first new moon.
    end_jd : float
        Julian Day of the next new moon.
    """

    calc = EphemerisCalculator()
    start_lon = calc.get_sun_moon_longitudes(start_jd)[0]
    end_lon = calc.get_sun_moon_longitudes(end_jd)[0]

    start_sign = int(start_lon // 30)
    end_sign = int(end_lon // 30)

    if start_sign != end_sign:
        return False

    jd = start_jd + 1.0
    current_sign = start_sign
    while jd < end_jd:
        sun_lon = calc.get_sun_moon_longitudes(jd)[0]
        sign = int(sun_lon // 30)
        if sign != current_sign:
            return False
        jd += 1.0

    return True
