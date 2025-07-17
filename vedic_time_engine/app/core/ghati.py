"""Utility functions for Ghati/Vighati time calculations."""

from typing import Tuple


def get_ghati_vighati(sunrise: str, current_time: str) -> Tuple[int, int]:
    """Return the ghati and vighati elapsed since ``sunrise``.

    Parameters
    ----------
    sunrise : str
        Local sunrise time in ``"HH:MM"`` 24‑hour format.
    current_time : str
        Local current time in ``"HH:MM"`` 24‑hour format.

    Returns
    -------
    Tuple[int, int]
        Number of ghatis and vighatis elapsed since ``sunrise``. Both values
        are clamped to the range 0–59.
    """

    def to_minutes(value: str) -> int:
        hours, minutes = map(int, value.split(":"))
        return hours * 60 + minutes

    sunrise_min = to_minutes(sunrise)
    current_min = to_minutes(current_time)

    total_minutes = current_min - sunrise_min
    if total_minutes < 0:
        total_minutes = 0

    ghati = (total_minutes // 24) % 60
    leftover_minutes = total_minutes % 24
    vighati = int(leftover_minutes * 60 / 24) % 60

    return ghati, vighati


def calculate_ghati(*args, **kwargs):
    """Calculate ghati."""
    pass
