import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from vedic_time_engine.app.core.calendar import (
    get_paksha,
    get_lunar_maasa,
    is_adhik_maas,
)
import swisseph as swe


def test_get_paksha_shukla_krishna():
    assert get_paksha(5) == "Shukla"
    assert get_paksha(16) == "Krishna"


def test_get_lunar_maasa_example():
    assert get_lunar_maasa(150.0, 200.0) == "Vaishakha"


def test_is_adhik_maas_false_when_sign_changes():
    start = swe.julday(2000, 1, 1, 0)
    end = start + 40  # long enough for a sign change
    assert is_adhik_maas(start, end) is False


def test_is_adhik_maas_true_when_no_sign_change():
    start = swe.julday(2000, 1, 1, 0)
    end = start + 5  # short period, Sun stays in same sign
    assert is_adhik_maas(start, end) is True
