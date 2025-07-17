"""Utilities for Rahukalam calculations."""

from datetime import datetime, timedelta
from typing import Tuple


_SEGMENT_MAP = {
    0: 2,  # Monday
    1: 7,  # Tuesday
    2: 5,  # Wednesday
    3: 6,  # Thursday
    4: 4,  # Friday
    5: 3,  # Saturday
    6: 8,  # Sunday
}


def get_rahukalam(sunrise: str, sunset: str, weekday_index: int) -> Tuple[str, str]:
    """Return the start and end of Rahukalam for the given day.

    Parameters
    ----------
    sunrise : str
        Local sunrise time in ``"HH:MM"`` format.
    sunset : str
        Local sunset time in ``"HH:MM"`` format.
    weekday_index : int
        Day of the week where Monday is ``0`` and Sunday ``6``.

    Returns
    -------
    Tuple[str, str]
        Start and end time of the Rahukalam period in ``"HH:MM"`` format.
    """

    sunrise_dt = datetime.strptime(sunrise, "%H:%M")
    sunset_dt = datetime.strptime(sunset, "%H:%M")

    day_length = sunset_dt - sunrise_dt
    segment = day_length / 8

    rahukalam_segment = _SEGMENT_MAP.get(weekday_index % 7, 8)
    start_dt = sunrise_dt + segment * (rahukalam_segment - 1)
    end_dt = start_dt + segment

    return start_dt.strftime("%H:%M"), end_dt.strftime("%H:%M")


def calculate_rahukalam(*args, **kwargs):
    """Calculate rahukalam (placeholder)."""

    pass
