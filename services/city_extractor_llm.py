import request
import json

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "mistral"

def extract_city(text: str)->str|None:
    prompt = f"""
Ты - сервис извлечения данных.
Твоя задача - извлечь город из пользовательского запроса о погоде.
Ответь СТРОГО в JSON, без текста и пояснений.

Формат:
{{
    "city": string| null
}}

Текст:
"{text}"
"""