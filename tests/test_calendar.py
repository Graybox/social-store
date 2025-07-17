import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from vedic_time_engine.app.core.calendar import get_paksha, get_lunar_maasa


def test_get_paksha_shukla_krishna():
    assert get_paksha(5) == "Shukla"
    assert get_paksha(16) == "Krishna"


def test_get_lunar_maasa_example():
    assert get_lunar_maasa(150.0, 200.0) == "Vaishakha"
