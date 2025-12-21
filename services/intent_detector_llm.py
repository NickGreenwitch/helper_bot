import json
import os
import requests
from pathlib import Path
from dotenv import load_dotenv

# --- env ---
BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env")

API_KEY = os.getenv("OPENROUTER_API_KEY")
API_URL = "https://openrouter.ai/api/v1/chat/completions"

TOPICS_PATH = BASE_DIR / "data" / "topics.json"

MODEL = "arcee-ai/trinity-mini:free"  # можешь заменить

def load_topics() -> dict:
    with open(TOPICS_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def detect_intent(text: str) -> dict:
    topics = load_topics()

    topics_json = json.dumps(topics, ensure_ascii=False, indent=2)

    prompt = f"""
Ты — классификатор пользовательских запросов.

Тебе дан список тем (intent).
Нужно выбрать ОДНУ наиболее подходящую тему.

Ответь СТРОГО в JSON:
{{
  "intent": string,
  "confidence": number
}}

Темы:
{topics_json}

Текст пользователя:
"{text}"
"""

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": "Ты классификатор интентов."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0
    }

    try:
        r = requests.post(API_URL, headers=headers, json=payload, timeout=15)
        r.raise_for_status()

        content = r.json()["choices"][0]["message"]["content"]
        data = json.loads(content)

        return {
            "intent": data.get("intent", "unknown"),
            "confidence": round(float(data.get("confidence", 0)), 2)
        }

    except Exception as e:
        print(f"[INTENT LLM ERROR] {e}")
        return {
            "intent": "unknown",
            "confidence": 0.0
        }