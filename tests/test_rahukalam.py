import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from vedic_time_engine.app.core.rahukalam import get_rahukalam


def test_monday_standard_day():
    start, end = get_rahukalam("06:00", "18:00", 0)
    assert (start, end) == ("07:30", "09:00")


def test_sunday_last_segment():
    start, end = get_rahukalam("06:00", "18:00", 6)
    assert (start, end) == ("16:30", "18:00")


def test_wednesday_custom_sunrise():
    start, end = get_rahukalam("05:30", "17:30", 2)
    assert (start, end) == ("11:30", "13:00")
