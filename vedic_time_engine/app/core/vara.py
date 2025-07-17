"""Vara (weekday) related helpers."""

from __future__ import annotations

import json
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

from dateutil import parser

from ..i18n.lang import get_translation as _translate, load_language


_TRANSLATIONS: dict[str, dict[str, str]] = {}


def get_translation(key: str, lang: str) -> str:
    """Return localized string for ``key`` in ``lang``.

    If the language file or key is missing, ``key`` itself is returned.
    """

    if lang not in _TRANSLATIONS:
        try:
            _TRANSLATIONS[lang] = load_language(lang)
        except FileNotFoundError:
            _TRANSLATIONS[lang] = {}

    return _translate(key, lang)


_EN_WEEKDAYS = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday",
]


def get_weekday_name(date_str: str, lang: str, tz: str) -> str:
    """Return localized weekday name for ``date_str`` in timezone ``tz``."""

    # Step 1: parse the provided date string robustly
    dt = parser.parse(date_str)
    # Use only the date component
    dt = datetime(dt.year, dt.month, dt.day)

    # Step 2: localize this date to the requested timezone at midnight
    tzinfo = ZoneInfo(tz)
    local_dt = dt.replace(tzinfo=tzinfo)

    # Step 3: compute weekday index where Monday=0
    index = local_dt.weekday()

    # Step 4: get translation using ``weekday.{index}`` key
    key = f"weekday.{index}"
    name = get_translation(key, lang)

    # Fallback to English weekday name if translation missing
    if name == key:
        name = _EN_WEEKDAYS[index]

    return name


def calculate_vara(*args, **kwargs):
    """Placeholder for future vara calculations."""

    pass

