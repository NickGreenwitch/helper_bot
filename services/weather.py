import requests

WEATHER_URL = "https://api.open-meteo.com/v1/forecast"

def get_current_weather(lat: float, lon: float) -> dict:
    params = {
        "latitude": lat,
        "longitude": lon,
        "current_weather": True,
        "timezone": "auto"
    }

    response = requests.get(WEATHER_URL, params=params, timeout=10)
    response.raise_for_status()

    data = response.json()
    current = data["current_weather"]

    return {
        "temperature": current["temperature"],
        "windspeed": current["windspeed"],
        "time": current["time"]
    }