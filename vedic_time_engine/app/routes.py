"""API route definitions."""

from datetime import datetime
from zoneinfo import ZoneInfo

from fastapi import APIRouter, HTTPException, Query

from .core.abhijit import get_abhijit_muhurta
from .core.calendar import get_lunar_maasa, get_paksha
from .core.choghadiya import get_choghadiya_blocks
from .core.festivals import get_festivals
from .core.ghati import get_ghati_vighati
from .core.karana import get_karana_index, get_karana_name
from .core.nakshatra import get_nakshatra_index, get_nakshatra_name
from .core.rahukalam import get_rahukalam
from .core.sun_moon import (
    EphemerisCalculator,
    get_sunrise_sunset,
    to_julian_day,
)
from .core.tithi import get_tithi_index, get_tithi_name
from .core.vara import get_weekday_name
from .core.yoga import get_yoga_index, get_yoga_name
from .schemas import Location, VedicTimeResponse

router = APIRouter()

@router.get("/")
async def root() -> dict:
    """Root endpoint."""
    return {"message": "Vedic Time Engine"}


@router.get("/vedic-time", response_model=VedicTimeResponse)
def get_vedic_time(
    date: str = Query(..., regex="^\d{4}-\d{2}-\d{2}$"),
    lat: float = Query(...),
    long: float = Query(...),
    tz: str = Query(...),
    lang: str = Query("en"),
) -> VedicTimeResponse:
    """Return computed Vedic time details for the given parameters."""

    try:
        jd = to_julian_day(date)
        sun_lon, moon_lon = EphemerisCalculator().get_sun_moon_longitudes(jd)

        t_idx = get_tithi_index(moon_lon, sun_lon)
        t_name = get_tithi_name(t_idx, lang)
        n_idx = get_nakshatra_index(moon_lon)
        n_name = get_nakshatra_name(n_idx, lang)
        y_idx = get_yoga_index(sun_lon, moon_lon)
        y_name = get_yoga_name(y_idx, lang)
        k_idx = get_karana_index(moon_lon, sun_lon)
        k_name = get_karana_name(k_idx, lang)
        weekday_name = get_weekday_name(date, lang, tz)

        sunrise, sunset = get_sunrise_sunset(lat, long, date, tz)

        ghati, vighati = get_ghati_vighati(sunrise, sunrise)

        weekday_index = datetime.strptime(date, "%Y-%m-%d").replace(
            tzinfo=ZoneInfo(tz)
        ).weekday()

        day_choghadiya = get_choghadiya_blocks(
            sunrise, sunset, weekday_index, lang, True
        )
        night_choghadiya = get_choghadiya_blocks(
            sunrise, sunset, weekday_index, lang, False
        )
        rahu_start, rahu_end = get_rahukalam(sunrise, sunset, weekday_index)
        abhijit_start, abhijit_end = get_abhijit_muhurta(sunrise, sunset)

        paksha = get_paksha(t_idx)
        maasa = get_lunar_maasa(sun_lon, moon_lon)
        festivals = get_festivals(t_idx, n_idx, paksha, maasa, lang)

        response = {
            "date": date,
            "location": {"lat": lat, "long": long, "tz": tz},
            "sun": {"sunrise": sunrise, "sunset": sunset},
            "vedic_time": {
                "weekday": weekday_name,
                "tithi": {"name": t_name},
                "nakshatra": n_name,
                "yoga": y_name,
                "karana": k_name,
                "ghati": ghati,
                "vighati": vighati,
            },
            "choghadiya": {
                "day": day_choghadiya,
                "night": night_choghadiya,
            },
            "rahukalam": {"start": rahu_start, "end": rahu_end},
            "abhijit_muhurta": {"start": abhijit_start, "end": abhijit_end},
            "festivals": festivals,
            "adhik_maas": False,
        }

        return response
    except Exception as exc:  # pragma: no cover - unexpected failures
        raise HTTPException(status_code=500, detail=str(exc))
