# Vedic Time Engine

## Overview
A FastAPI service for calculating Vedic time (Panchang) elements for a given date and location. It computes values such as Tithi, Nakshatra, Yoga and more, with responses available in multiple languages.

## Project Structure
- **app/** – FastAPI application modules and routes.
- **i18n/** – Translation JSON files.
- **tests/** – Unit and integration tests.
- **ephe/** – Swiss Ephemeris data files (not included).
- **docs/** – Documentation such as `openapi.yaml`.
- **.github/workflows/** – Continuous integration workflows.

## API Usage
Example request:
```bash
GET /vedic-time?date=2025-07-17&lat=19.0760&long=72.8777&tz=Asia/Kolkata&lang=en
```
Truncated response:
```json
{
  "date": "2025-07-17",
  "location": {"lat": 19.0760, "long": 72.8777, "tz": "Asia/Kolkata"},
  "sun": {"sunrise": "05:59", "sunset": "18:52"},
  "vedic_time": {"tithi": {"name": "Pratipada"}, "nakshatra": "Ashwini", ...}
}
```

## Installation
```bash
pip install -r requirements.txt
```
Run locally:
```bash
uvicorn vedic_time_engine.app.main:app --reload --port 8080
```

### Widget
In another terminal install the widget dependencies and start its dev server:

```bash
cd vedic-time-widget
npm install
VITE_ENGINE_BASE_URL=http://localhost:8080 npm run dev
```
The widget will fetch data from the running API.

### Docker
Place Swiss Ephemeris data in `ephe/` before building or mount it at runtime.
```bash
docker build -t vedic-time .
docker run -p 8080:8080 vedic-time
```

## Contributing
Pull requests are welcome. Please open an issue to discuss changes.

## License
MIT
