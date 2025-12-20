from services.city_extractor_llm import extract_city as llm_extract
from services.city_extractor_regex import extract_city as regex_extract
from services.city_normalizer import normalize_city

def extract_city(text: str) -> str | None:
    """
    Функция извлечения города с fallback:
    1. Сначала LLM
    2. Если не удалось → regex
    """
    # ---------- LLM ----------
    try:
        city = llm_extract(text)
        if city:
            city = normalize_city(city)
            print(f"[CITY] LLM → {city}")
            return city
    except Exception as e:
        print(f"[CITY] LLM error: {e}")

    # ---------- Regex ----------
    try:
        city = regex_extract(text)
        if city:
            print(f"[CITY] REGEX → {city}")
            return city
    except Exception as e:
        print(f"[CITY] REGEX error: {e}")

    # ---------- Не найдено ----------
    print("[CITY] NOT FOUND")
    return None