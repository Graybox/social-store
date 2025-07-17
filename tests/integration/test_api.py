import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from fastapi.testclient import TestClient
from vedic_time_engine.app.main import app
from vedic_time_engine.app.core import sun_moon
from vedic_time_engine.app.core.sun_moon import EphemerisCalculator

client = TestClient(app)


def test_vedic_time_endpoint(monkeypatch):
    def fake_get_sun_moon_longitudes(self, jd):
        return 100.0, 200.0

    def fake_get_sunrise_sunset(lat, lon, date_str, tz_str):
        return "06:00", "18:00"

    monkeypatch.setattr(EphemerisCalculator, "get_sun_moon_longitudes", fake_get_sun_moon_longitudes)
    monkeypatch.setattr(sun_moon, "get_sunrise_sunset", fake_get_sunrise_sunset)

    response = client.get(
        "/vedic-time?date=2025-07-17&lat=19.0760&long=72.8777&tz=Asia/Kolkata&lang=en"
    )
    assert response.status_code == 200
    data = response.json()

    assert "vedic_time" in data
    assert "sun" in data
    assert "location" in data

    assert "weekday" in data["vedic_time"]
    assert "sunrise" in data["sun"]

    assert isinstance(data["festivals"], list)
    assert isinstance(data["adhik_maas"], bool)
