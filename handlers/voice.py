from aiogram import Router
from aiogram.types import Message
from pathlib import Path
from services.intent_detector import detect_intent
from services.speech_to_text import transcribe

voice_router = Router()

VOICE_DIR = Path("voices")
VOICE_DIR.mkdir(exist_ok=True)

@voice_router.message()
async def voice_handler(message: Message):
    if not message.voice:
        await message.answer("Отправь голосовое сообщение.")
        return
    #1 Скачиваем голосовое сообщение
    file = await message.bot.get_file(message.voice.file_id)
    ogg_path = VOICE_DIR /f"{message.voice.file_id}.ogg"
    await message.bot.download_file(file.file_path, ogg_path)

    #2 Распознаем речь
    text = transcribe(ogg_path)

    #3 Определяем тему
    intent_data = detect_intent(text)

    #4 Ответ пользователю 

    await message.answer(
        f"Ты сказал:\n{text}\n\n"
        f"📌 Тема: {intent_data['intent']}\n"
        f"🔎 Уверенность: {intent_data['confidence']}"
    )