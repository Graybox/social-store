import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from vedic_time_engine.app.core.tithi import get_tithi_index


def test_tithi_calc():
    assert get_tithi_index(120, 108) == 1
