"""Nakshatra calculation utilities."""

from __future__ import annotations

import json
from functools import lru_cache
from pathlib import Path


I18N_DIR = Path(__file__).resolve().parents[2] / "i18n"


@lru_cache(maxsize=None)
def _load_translations(lang: str) -> dict:
    """Load translation dictionary for ``lang`` from JSON files."""

    file_path = I18N_DIR / f"{lang}.json"
    if not file_path.exists():
        return {}
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return {}


def get_translation(key: str, lang: str = "en") -> str:
    """Return the localized string for ``key`` or the key if missing."""

    translations = _load_translations(lang)
    return translations.get(key, key)


def get_nakshatra_index(moon_lon: float) -> int:
    """Return the 0-based nakshatra index for ``moon_lon`` in degrees."""

    segment = 360.0 / 27.0
    return int((moon_lon % 360.0) // segment)


def get_nakshatra_name(index: int, lang: str = "en") -> str:
    """Return the localized name of the nakshatra at ``index``."""

    wrapped_index = index % 27
    key = f"nakshatra.{wrapped_index}"
    return get_translation(key, lang)


def calculate_nakshatra(*args, **kwargs):
    """Calculate nakshatra (placeholder)."""

    pass
