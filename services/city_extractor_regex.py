import re
from services.city_normalizer import normalize_city
from services.city_data import KNOWN_CITIES, STOP_WORDS



def extract_city(text: str) -> str | None:
    text_lower = text.lower()

    # ---------- 1. Поиск по списку ----------
    for city, normalized in KNOWN_CITIES.items():
        if re.search(rf"\b{re.escape(city)}\b", text_lower):
            return normalized

    # ---------- 2. Regex-кандидаты ----------
    patterns = [
        r"в\s+([а-яё\-]+)",
        r"для\s+([а-яё\-]+)",
        r"погода\s+в\s+([а-яё\-]+)",
    ]

    for pattern in patterns:
        match = re.search(pattern, text_lower)
        if not match:
            continue

        candidate = match.group(1)

        # ---------- 3. Фильтрация ----------
        if len(candidate) < 3:
            continue

        if candidate in STOP_WORDS:
            continue

        if not re.fullmatch(r"[а-яё\-]+", candidate):
            continue

        return normalize_city(candidate)

    return None