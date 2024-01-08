from aiogram import Bot
from aiogram.types import Message


# Эхо-обработчик для всех текстовых сообщений
async def echo(message: Message, bot: Bot):
    # Ответ тем же текстом, что был получен
    await message.answer(message.text)
