from services.city_extractor_llm import extract_city as llm_extract 
from services.city_extractor_ner import extract_city as ner_extract
from services.city_extractor_regex import extract_city as regex_extract

def extract_city(text: str)-> str | None:
    #LLM
    try:
        city = llm_extract(text)
        if city:
            print(f"[CITY] LLM → {city}")
            return city
    except Exception as e:
            print(f"[CITY] LLM error: {e}")
    #NER
    try:
        city = ner_extract(text)
        if city:
            print(f"[CITY] NER → {city}")
            return city
    except Exception as e:
        print(f"[CITY] NER error: {e}")
    #Regex
    city = regex_extract(text)
    if city:
        print(f"[CITY] REGEX → {city}")
        return city
    #Не найдено
    print("[CITY] NOT FOUND")
    return None