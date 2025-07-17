"""Festival determination utilities."""

from __future__ import annotations

from typing import List

from ..i18n import get_translation


def get_festivals(
    tithi_index: int,
    nakshatra_index: int,
    paksha: str,
    maasa: str,
    lang: str = "en",
) -> List[str]:
    """Return a list of festivals for the given Panchang elements.

    Parameters
    ----------
    tithi_index:
        Index of the current tithi (0-based).
    nakshatra_index:
        Index of the current nakshatra (0-based).
    paksha:
        Either ``"Shukla"`` or ``"Krishna"``.
    maasa:
        Name of the lunar month (unused for the sample rules).
    lang:
        Target language for festival names.
    """

    festivals: List[str] = []

    # Janmashtami: Krishna Ashtami with Rohini nakshatra
    if paksha == "Krishna" and tithi_index == 7 and nakshatra_index == 3:
        festivals.append(get_translation("festival.janmashtami", lang))

    # Vinayaka Chaturthi: Shukla Chaturthi
    if paksha == "Shukla" and tithi_index == 3:
        festivals.append(get_translation("festival.vinayaka_chaturthi", lang))

    return festivals


def calculate_festivals(*args, **kwargs):
    """Backward-compatible placeholder for festival calculations."""

    return get_festivals(*args, **kwargs)

