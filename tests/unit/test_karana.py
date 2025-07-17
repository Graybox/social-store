import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from vedic_time_engine.app.core.karana import get_karana_index


def test_karana_index():
    assert get_karana_index(90, 60) == 5
