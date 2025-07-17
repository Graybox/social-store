import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from vedic_time_engine.app.core.yoga import get_yoga_index


def test_yoga_index():
    assert get_yoga_index(30, 60) == 6
