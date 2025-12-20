from services.city_extractor_fallback import extract_city

tests = [
    "Какая погода в Москве?",
    "Погода сегодня в Санкт-Петербурге",
    "Что там на улице?",
    "Погода в Омске",
]

for t in tests:
    print(t, "->", extract_city(t))