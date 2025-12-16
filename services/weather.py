import request

WEATHER_URL = "https://api.open-meteo.com/v1/forecast"

def get_current_weather(lat: float, lon: float)->dict:
    params={
        "latitude": lat,
        "longitude": lon,
        "current": "temperature_2m, wind_speed_10m", "timezone": "auto"
    }

    response = request.get(WEATHER_URL, params=params, timeout=10)
    response.raise_for_status()

    data = response.json()
    current = data["current"]

    return {
        "temperature": current["temperature_2m"],
        "windspeed": current["wind_speed_10m"],
        "time": current["time"]
    }