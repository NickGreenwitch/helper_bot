import request

GEOCODING_URL = "https://geocoding-api.open-meteo.com/v1/search"
def get_coordinates(city:str)->dict|None:
    params = {
        "name": city,
        "count": 1,
        "language": "ru",
        "format":"json"
    }

    response = request.get(GEOCODING_URL, params=params, timeout=10)
    response.raise_for_status()
    data=response.json()

    if "results" not in data or not data["results"]:
        return None
    result = data["results"][0]

    return {
        "name": result["name"],
        "latitude": result["latitude"],
        "longitude": result["longitude"],
        "contry": result.get("country")
    }