import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from vedic_time_engine.app.core.calendar import get_paksha, get_lunar_maasa


def test_get_paksha():
    assert get_paksha(0) == "Shukla"
    assert get_paksha(20) == "Krishna"


def test_get_lunar_maasa():
    assert get_lunar_maasa(150.0, 200.0) == "Vaishakha"
