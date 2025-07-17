import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from vedic_time_engine.app.core.vara import get_weekday_name


def test_get_weekday_name():
    assert get_weekday_name("2025-07-17", "en", "UTC") == "Thursday"
