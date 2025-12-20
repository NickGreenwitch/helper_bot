from city_extractor_llm import extract_city

tests = [
    "Какая погода в Москве?",
    "Погода сегодня в Санкт-Петербурге",
    "Что там на улице?",
    "Прогноз погоды для Новосибирска",
    "Переведи слово 'cat'"
]

for t in tests:
    city = extract_city(t)
    print(f"Текст: {t}")
    print(f"Извлечён город: {city}")
    print("-" * 30)