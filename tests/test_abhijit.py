import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from vedic_time_engine.app.core.abhijit import get_abhijit_muhurta


def test_standard_day():
    assert get_abhijit_muhurta("06:00", "18:00") == ("11:36", "12:24")


def test_uneven_day_length():
    start, end = get_abhijit_muhurta("05:30", "20:30")
    assert start == "12:36" and end == "13:24"
