"""Utilities for Sun and Moon longitude calculations using Swiss Ephemeris."""

from __future__ import annotations

import os
from datetime import datetime, timedelta
from typing import Tuple

from dotenv import load_dotenv
import swisseph as swe
import pytz


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


def _jd_to_datetime_utc(jd: float) -> datetime:
    """Convert Julian Day ``jd`` to a timezone-aware UTC ``datetime``."""

    epoch = datetime(1970, 1, 1, tzinfo=pytz.utc)
    return epoch + timedelta(days=jd - 2440587.5)


def get_sunrise_sunset(lat: float, lon: float, date_str: str, tz_str: str) -> Tuple[str, str]:
    """Return local sunrise and sunset times for ``date_str`` at ``lat``/``lon``.

    Times are formatted as ``"HH:MM"`` in the timezone ``tz_str``. On error the
    returned values default to ``"00:00"``.
    """

    jd = to_julian_day(date_str)
    location = (lon, lat, 0)
    timezone = pytz.timezone(tz_str)

    sunrise_str = "00:00"
    sunset_str = "00:00"

    try:
        res_rise, tret_rise = swe.rise_trans(
            jd, swe.SUN, swe.CALC_RISE | swe.BIT_DISC_CENTER, location
        )
        if res_rise >= 0:
            dt_utc = _jd_to_datetime_utc(tret_rise[0])
            sunrise_str = dt_utc.astimezone(timezone).strftime("%H:%M")
    except Exception:
        pass

    try:
        res_set, tret_set = swe.rise_trans(
            jd, swe.SUN, swe.CALC_SET | swe.BIT_DISC_CENTER, location
        )
        if res_set >= 0:
            dt_utc = _jd_to_datetime_utc(tret_set[0])
            sunset_str = dt_utc.astimezone(timezone).strftime("%H:%M")
    except Exception:
        pass

    return sunrise_str, sunset_str

