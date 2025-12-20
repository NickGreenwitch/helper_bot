from services.city_data import FIXED_MAP


def normalize_city(word: str) -> str:
    word_lower = word.lower()
    #Фиксрованный словарь
    if word_lower in FIXED_MAP:
        return FIXED_MAP[word_lower]

    rules = [
        ("еже", "еж"),   # воронежe → воронеж
        ("ани", "ань"),  # казани → казань
        ("ени", "ень"),  # тюмени → тюмень
        ("ске", "ск"),   # омске → омск
        ("ске", "ск"),   # томске → томск
        ("ска", "ск"),   # новосибирска → новосибирск
        ("а", ""),       # новосибирска → новосибирск (fallback)
        ("у", "а"),      # москву → москва
        ("ой", "а"),     # самарой → самара
    ]

    for old, new in rules:
        if word_lower.endswith(old):
            word_lower = word_lower[:-len(old)] + new
            break

    return word_lower.title()