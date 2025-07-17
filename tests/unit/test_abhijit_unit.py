import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from vedic_time_engine.app.core.abhijit import get_abhijit_muhurta


def test_abhijit_standard_day():
    assert get_abhijit_muhurta("06:00", "18:00") == ("11:36", "12:24")
