"""Tithi (lunar day) calculations."""

from ...i18n import get_translation


def get_tithi_index(moon_lon: float, sun_lon: float) -> int:
    """Return the tithi index based on longitudinal difference."""
    difference = (moon_lon - sun_lon) % 360
    index = int(difference // 12)
    return index


def get_tithi_name(index: int, lang: str = "en") -> str:
    """Return the localized name for the given tithi index."""
    index = index % 30
    return get_translation(f"tithi.{index}", lang)


def calculate_tithi(*args, **kwargs):
    """Backward-compatible placeholder for tithi calculation."""
    return get_tithi_index(*args, **kwargs)
