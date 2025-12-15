from aiogram import Router
from aiogram.types import Message

voice_router = Router()

@voice_router.message()
async def voice_handler(message: Message):
    if message.voice:
        await message.answer("🎤 Я получил голосовое сообщение!")
    else:
        await message.answer("Пожалуйста, отправь голосовое сообщение.")