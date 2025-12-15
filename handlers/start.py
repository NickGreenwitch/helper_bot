from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart

start_router = Router()

@start_router.message(CommandStart())
async def start_handler(message: Message):
    await message.answer(
        "Привет! 👋\n"
        "Я голосовой помощник.\n"
        "Отправь мне голосовое сообщение."
    )