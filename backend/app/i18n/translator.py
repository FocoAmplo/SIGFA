import json
from pathlib import Path

from .locale import get_default_locale
from .locale import normalize_locale


class Translator:

    def __init__(
        self,
        locale: str | None = None,
    ):
        self.locale = normalize_locale(locale)
        self.default_locale = get_default_locale()
        self.base_path = Path(__file__).resolve().parent

    def translate(
        self,
        key: str,
        locale: str | None = None,
    ) -> str:
        selected_locale = normalize_locale(locale or self.locale)
        messages = self._load_messages(selected_locale)

        if key in messages:
            return messages[key]

        default_messages = self._load_messages(self.default_locale)

        return default_messages.get(key, key)

    def _load_messages(
        self,
        locale: str,
    ) -> dict:
        path = self.base_path / f"{locale}.json"

        if not path.exists():
            return {}

        with path.open("r", encoding="utf-8") as file:
            return json.load(file)
