from aiogram import Router
from aiogram.types import Message
from services.intent_detector import detect_intent

voice_router = Router()

@voice_router.message()
async def voice_handler(message: Message):
    if not message.voice:
        await message.answer("Отправь голосовое сообщение.")
        return

    # ⚠️ Пока вместо распознанной речи — заглушка
    text = "какая погода в москве"

    intent_data = detect_intent(text)

    await message.answer(
        f"🧠 Распознанный запрос:\n{text}\n\n"
        f"📌 Тема: {intent_data['intent']}\n"
        f"🔎 Уверенность: {intent_data['confidence']}"
    )