from .languages import DEFAULT_LANGUAGE
from .languages import SUPPORTED_LANGUAGES


def get_default_locale() -> str:
    return DEFAULT_LANGUAGE


def normalize_locale(locale: str | None) -> str:
    if not locale:
        return DEFAULT_LANGUAGE

    normalized = locale.replace("-", "_")

    if normalized in SUPPORTED_LANGUAGES:
        return normalized

    language = normalized.split("_")[0].lower()

    for supported in SUPPORTED_LANGUAGES:
        if supported.lower().startswith(language):
            return supported

    return DEFAULT_LANGUAGE
