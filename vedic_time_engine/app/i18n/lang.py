import json
from pathlib import Path

_language_cache: dict[str, dict] = {}


def load_language(lang: str) -> dict:
    """Load the JSON file for the given language code and return as dict."""
    base = Path(__file__).resolve().parents[2] / "i18n" / f"{lang}.json"
    return json.loads(base.read_text(encoding="utf-8"))


def get_translation(key: str, lang: str = "en") -> str:
    """Retrieve the translated string for the given key in the specified language."""
    if lang not in _language_cache:
        try:
            _language_cache[lang] = load_language(lang)
        except FileNotFoundError:
            _language_cache[lang] = {}
    return _language_cache[lang].get(key, key)
