import os
import sys
import pytest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from vedic_time_engine.app.core.ghati import get_ghati_vighati

def test_five_hours_since_sunrise():
    assert get_ghati_vighati("06:00", "11:00") == (12, 30)

def test_before_sunrise_clamped():
    assert get_ghati_vighati("06:00", "05:00") == (0, 0)

def test_exact_ghati_boundary():
    assert get_ghati_vighati("06:00", "06:24") == (1, 0)

def test_single_minute():
    assert get_ghati_vighati("06:00", "06:01") == (0, 2)
