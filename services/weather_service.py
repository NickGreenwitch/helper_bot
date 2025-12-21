from services.speech_to_text import transcribe
from services.city_extractor_fallback import extract_city
from services.geocoding import get_coordinates
from services.weather import get_current_weather
from pathlib import Path

def get_weather(audio_path: Path) -> dict|None:
    """
    Получает погоду из аудио-сообщения.
    1. Преобразует аудио в текст
    2. Извлекает город
    3. Получает координаты
    4. Получает текущую погоду
    """
    # ---------- Распознаём текст ----------
    try:
        text = transcribe(audio_path)
    except Exception as e:
        print(f"[ERROR] Speech to text failed: {e}")
        return None

    # ---------- Извлекаем город ----------
    city = extract_city(text)
    if not city:
        print("[INFO] Город не определён")
        return None

    # ---------- Получаем координаты ----------
    coords = get_coordinates(city)
    if not coords:
        print(f"[INFO] Не удалось найти координаты для города {city}")
        return None

    # ---------- Получаем текущую погоду ----------
    weather = get_current_weather(coords["latitude"], coords["longitude"])

    return {
        "city": coords["name"],
        "country": coords.get("contry"),
        "temperature": weather["temperature"],
        "windspeed": weather["windspeed"],
        "time": weather["time"]
    }