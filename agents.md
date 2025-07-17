# 🧠 Agent Integration Guide: Vedic Time Engine

This document serves as a comprehensive guide for integrating intelligent developer agents (like GitHub Copilot, OpenAI Codex, Replit AI, etc.) with the **Vedic Time Engine** codebase.

It outlines standards, incremental prompt strategies, context-anchored development practices, and caution flags to ensure consistent and accurate contributions by agents.

---

## 🗂️ Project Overview

* **Domain**: Astronomical + Vedic calendar computation
* **Stack**: Python, FastAPI, Swiss Ephemeris, Docker, JSON i18n
* **Structure**: Modular, single-responsibility components (per Panchang element)
* **Goal**: Generate accurate, local, language-specific Vedic calendar data via API

---

## 🧱 File Structure Expectations

Agents must respect and retain the following structure:

```
vedic_time_engine/
├── app/
│   ├── core/               # Tithi, Nakshatra, Yoga, etc. calculators
│   ├── i18n/               # Language JSONs
│   ├── notifications/      # Optional pluggable features
│   ├── schemas.py          # Pydantic schemas
│   ├── routes.py           # FastAPI endpoints
│   └── main.py             # FastAPI app entry
├── ephe/                   # Swiss Ephemeris .se1/.se2 files
├── tests/
├── Dockerfile
├── .env
├── requirements.txt
├── README.md
```

---

## 🎯 Prompt Strategy for Agents

Each development step should be invoked with **minimal context scope**. Agents should:

1. **Limit target** to one prompt/task at a time (e.g., “implement tithi index”) ✅
2. **Preserve interfaces** and existing file layouts ✅
3. **Reference `spec.md` or Prompt Book** for logic ✅
4. **Never remove other functions or imports** unless explicitly stated ❌
5. **Always use translation lookups** for display strings ❗

---

## 🧩 Critical Integration Patterns

| Concern           | Expectation                                                            |
| ----------------- | ---------------------------------------------------------------------- |
| Swiss Ephemeris   | Use `swe.calc_ut`, `swe.set_ephe_path` with `.env` config              |
| Timezone handling | All time calculations must use `pytz` or `zoneinfo` to remain tz-aware |
| Localization      | Use `get_translation(key, lang)`; fallback = key                       |
| API schemas       | Must match `VedicTimeResponse` structure from `schemas.py`             |
| Caching           | Pure functions only via `@lru_cache`; args must be immutable and typed |
| Sunrise logic     | Use `swe.rise_trans()`; convert UTC JD → tz-local datetime string      |

---

## ⚠️ Agent Pitfalls & Safeguards

### 🔴 DO NOT

* Do not hardcode festival names, tithi labels, weekday names
* Do not use datetime without tz-awareness (`datetime.now()` is forbidden)
* Do not re-implement ephemeris math manually
* Do not refactor imports, files, or move functions unless instructed

### 🟢 DO

* Use translation keys (`"tithi.0"`, `"nakshatra.3"`, etc.)
* Encapsulate each logic (e.g., `get_tithi_index`) as **pure**, testable function
* Follow the file/module assigned in Prompt Book (e.g., `karana.py` for Karana logic)
* Respect caching boundaries (only for pure functions)
* Format output as per API schema even if computed values are mocked in tests

---

## ✅ Examples of Good Agent Behavior

* Prompt: *"Implement get_yoga_index using sun/moon longitude"*

  * ✅ Creates `get_yoga_index` inside `yoga.py`
  * ✅ Uses `(sun + moon) % 360 // 13.333` logic
  * ✅ Returns index 0–26

* Prompt: *"Add unit test for karana index logic"*

  * ✅ Creates `test_karana.py` in `tests/unit/`
  * ✅ Tests known inputs: `moon=90, sun=60 → karana=5`

* Prompt: *"Export choghadiya blocks to JSON"*

  * ✅ Uses correct start/end logic with weekday sequence
  * ✅ Returns list of dicts with localized `type`

---

## 🛡️ Safe Default Behaviors

* If a translation key is missing: return the key itself
* If ephemeris fails: return placeholder values with error flag
* If API fails: return HTTP 500 with clear error message (via `HTTPException`)
* If current time is needed in tests: use fixed date (`2025-07-17`) or mock

---

## 🧪 Agent Checklist Before Commit

* [ ] Did I write this inside the correct module (e.g., `tithi.py`, not `main.py`)?
* [ ] Did I use all required arguments and return correct types?
* [ ] Did I avoid any timezone/ephemeris/global hardcodes?
* [ ] Did I respect the Prompt Book interface/structure?
* [ ] Did I check if the output is compatible with the API schema?

---

## 📎 References

* `vedic-engine.md` – Master spec
* `Prompt Book` (Chapters 1–11) – Granular implementation plan
* `/docs` or `/openapi.json` – Live API schema if running

---

This guide is required reading for any intelligent agent contributing to the Vedic Time Engine codebase.

Use with discipline. Adjust only what's scoped. Return only what’s asked. 🙏
