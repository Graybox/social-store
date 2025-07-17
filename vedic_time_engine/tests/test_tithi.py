import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from vedic_time_engine.app.core.tithi import get_tithi_index, get_tithi_name


def test_get_tithi_index_basic():
    assert get_tithi_index(0, 0) == 0
    assert get_tithi_index(13, 0) == 1
    assert get_tithi_index(359, 0) == 29


def test_get_tithi_name_fallback():
    # With empty translations, returns key
    assert get_tithi_name(0, "en") == "tithi.0"
    assert get_tithi_name(5, "en") == "tithi.5"

