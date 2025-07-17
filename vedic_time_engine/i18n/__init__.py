import json
from functools import lru_cache
from pathlib import Path

_I18N_DIR = Path(__file__).parent

@lru_cache(maxsize=None)
def _load_language(lang: str) -> dict:
    """Load translation dictionary for a given language."""
    path = _I18N_DIR / f"{lang}.json"
    if not path.exists():
        return {}
    with open(path, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return {}


def get_translation(key: str, lang: str = "en") -> str:
    """Return the translated string for the given key and language."""
    translations = _load_language(lang)
    return translations.get(key, key)
