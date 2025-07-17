import importlib
from vedic_time_engine.app.core.nakshatra import get_nakshatra_index, get_nakshatra_name


def test_get_nakshatra_index_basic():
    assert get_nakshatra_index(0) == 0
    assert get_nakshatra_index(13.333333) == 0  # still in first nakshatra
    assert get_nakshatra_index(13.3334) == 1


def test_get_nakshatra_index_wrap():
    assert get_nakshatra_index(360) == 0
    assert get_nakshatra_index(-0.1) == 26


def test_get_nakshatra_name_fallback():
    # translations are empty so fallback to key
    assert get_nakshatra_name(0, "en") == "nakshatra.0"
