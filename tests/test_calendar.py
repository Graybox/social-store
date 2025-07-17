import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from vedic_time_engine.app.core.calendar import is_adhik_maas
import swisseph as swe


def test_is_adhik_maas_true():
    start_jd = swe.julday(2020, 6, 21, 0)
    end_jd = swe.julday(2020, 7, 20, 0)
    assert is_adhik_maas(start_jd, end_jd) is True


def test_is_adhik_maas_false():
    start_jd = swe.julday(2020, 7, 20, 0)
    end_jd = swe.julday(2020, 8, 18, 0)
    assert is_adhik_maas(start_jd, end_jd) is False
