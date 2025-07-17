
"""Utilities for Abhijit Muhurta calculations."""

from datetime import datetime, timedelta
from typing import Tuple


def get_abhijit_muhurta(sunrise: str, sunset: str) -> Tuple[str, str]:
    """Return the start and end time of Abhijit Muhurta.

    Parameters
    ----------
    sunrise : str
        Local sunrise time in ``"HH:MM"`` 24‑hour format.
    sunset : str
        Local sunset time in ``"HH:MM"`` 24‑hour format.

    Returns
    -------
    Tuple[str, str]
        Start and end time of Abhijit Muhurta in ``"HH:MM"`` format.
    """

    sunrise_dt = datetime.strptime(sunrise, "%H:%M")
    sunset_dt = datetime.strptime(sunset, "%H:%M")

    midpoint = sunrise_dt + (sunset_dt - sunrise_dt) / 2
    start_dt = midpoint - timedelta(minutes=24)
    end_dt = midpoint + timedelta(minutes=24)

    return start_dt.strftime("%H:%M"), end_dt.strftime("%H:%M")


def calculate_abhijit(*args, **kwargs):
    """Calculate abhijit."""
    pass
