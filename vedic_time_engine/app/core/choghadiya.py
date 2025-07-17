"""Utilities for Choghadiya calculations."""

from __future__ import annotations

import json
import os
from datetime import datetime, timedelta
from typing import Dict, List


CYCLE = ["Udveg", "Chal", "Labh", "Amrit", "Kaal", "Shubh", "Rog"]


def get_translation(key: str, lang: str) -> str:
    """Return translation for ``key`` in ``lang`` if available."""
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
    file_path = os.path.join(base_dir, "i18n", f"{lang}.json")
    try:
        with open(file_path, "r", encoding="utf-8") as fh:
            data = json.load(fh)
        return data.get(key, key)
    except (FileNotFoundError, json.JSONDecodeError):
        return key


def get_choghadiya_blocks(
    sunrise: str,
    sunset: str,
    weekday_index: int,
    lang: str,
    is_day: bool,
) -> List[Dict[str, str]]:
    """Return the 8 Choghadiya segments for the given period."""

    sunrise_dt = datetime.strptime(sunrise, "%H:%M")
    sunset_dt = datetime.strptime(sunset, "%H:%M")

    if is_day:
        start_time = sunrise_dt
        end_time = sunset_dt
        start_index = (weekday_index + 6) % len(CYCLE)
    else:
        start_time = sunset_dt
        end_time = sunrise_dt + timedelta(days=1)
        start_index = weekday_index % len(CYCLE)

    duration = end_time - start_time
    segment = duration / 8

    blocks: List[Dict[str, str]] = []
    index = start_index
    current = start_time

    for _ in range(8):
        block_end = current + segment
        block_type = CYCLE[index % len(CYCLE)]
        blocks.append(
            {
                "start": current.strftime("%H:%M"),
                "end": block_end.strftime("%H:%M"),
                "type": get_translation(f"choghadiya.{block_type.lower()}", lang),
            }
        )
        current = block_end
        index = (index + 1) % len(CYCLE)

    return blocks


# Existing placeholder for compatibility

def calculate_choghadiya(*args, **kwargs):
    """Calculate choghadiya."""
    pass
