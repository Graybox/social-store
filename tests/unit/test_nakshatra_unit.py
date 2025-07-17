import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from vedic_time_engine.app.core.nakshatra import get_nakshatra_index


def test_nakshatra_index():
    assert get_nakshatra_index(100) == 7
