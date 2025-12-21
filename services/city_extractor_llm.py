import requests
import json
import os
from services.city_normalizer import normalize_city
from dotenv import load_dotenv

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
dotenv_path = os.path.join(BASE_DIR, ".env")

load_dotenv(dotenv_path)

API_KEY = os.getenv("OPENROUTER_API_KEY")
API_URL = "https://openrouter.ai/api/v1/chat/completions"
print(API_KEY)

def extract_city(text: str) -> str | None:
    prompt = f"""
Ты — сервис извлечения данных.
Извлеки город из запроса пользователя о погоде.
Ответь строго в JSON формате:
{{"city": string | null}}

Текст: "{text}"
"""

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "arcee-ai/trinity-mini:free",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0
    }

    try:
        response = requests.post(API_URL, headers=headers, json=payload, timeout=10)
        response.raise_for_status()
        result = response.json()
        text_response = result["choices"][0]["message"]["content"]
        city = json.loads(text_response).get("city")
        print(f"[LLM raw] '{city}'") # <- покажет что вернула модель
        return normalize_city(city)
    except Exception as e:
        print(f"[LLM API error] {e}")
        return None