"""Yoga calculation utilities."""

from __future__ import annotations

import json
from functools import lru_cache
from pathlib import Path
from typing import Dict

from ..i18n.lang import get_translation as _translate, load_language

I18N_DIR = Path(__file__).resolve().parents[2] / "i18n"


def calculate_yoga(*args, **kwargs):
    """Calculate yoga."""
    pass


@lru_cache(maxsize=None)
def _load_translations(lang: str) -> Dict[str, str]:
    """Return translation dictionary for ``lang``."""

    path = I18N_DIR / f"{lang}.json"
    if path.exists():
        try:
            return load_language(lang)
        except json.JSONDecodeError:
            return {}
    return {}


def get_translation(key: str, lang: str = "en") -> str:
    """Return the translation for ``key`` in ``lang`` if available."""

    return _translate(key, lang)


def get_yoga_index(sun_lon: float, moon_lon: float) -> int:
    """Return the yoga index based on Sun and Moon longitudes."""

    return int(((sun_lon + moon_lon) % 360) // (360.0 / 27.0))


def get_yoga_name(index: int, lang: str = "en") -> str:
    """Return the localized yoga name for ``index``."""

    return get_translation(f"yoga.{index}", lang)
