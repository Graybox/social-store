"""Karana calculations.

This module provides utilities to determine the current karana based on the
ecliptic longitudes of the Moon and the Sun. The names returned are
internationalised using a simple JSON based lookup.
"""

from __future__ import annotations

import json
from functools import lru_cache
from pathlib import Path

from ..i18n.lang import get_translation as _translate, load_language


KARANA_SEQUENCE = [
    "kimstughna",
    *(
        [name.lower() for name in ("Bava", "Balava", "Kaulava", "Taitila", "Garaja", "Vanija", "Vishti")] * 8
    ),
    "shakuni",
    "chatushpada",
    "nagava",
]


def get_karana_index(moon_lon: float, sun_lon: float) -> int:
    """Return the karana index for the given Moon/Sun longitudes.

    The index ranges from ``0`` to ``59`` where ``0`` represents the first half
    of Shukla Pratipada.
    """

    return int(((moon_lon - sun_lon) % 360) // 6)


@lru_cache(maxsize=None)
def _load_translations(lang: str) -> dict[str, str]:
    """Load translation JSON for ``lang``.

    If the file or key is missing, an empty dictionary is used and the requested
    key will be returned verbatim.
    """

    try:
        return load_language(lang)
    except FileNotFoundError:
        return {}


def get_translation(key: str, lang: str = "en") -> str:
    """Retrieve the translated string for ``key``.

    Falls back to ``key`` if the translation is unavailable.
    """

    return _translate(key, lang)


def get_karana_name(index: int, lang: str = "en") -> str:
    """Return the localized karana name for ``index`` (0–59)."""

    if not 0 <= index < 60:
        raise ValueError("karana index must be in range 0..59")

    name = KARANA_SEQUENCE[index]
    return get_translation(f"karana.{name}", lang)


def calculate_karana(*args, **kwargs):
    """Legacy placeholder for karana calculations."""

    pass
