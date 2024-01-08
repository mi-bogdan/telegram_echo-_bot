import logging
from aiogram import Bot, Dispatcher
from core.settings import settings
from core.handlers.basic import echo

# Настройка логирования
logging.basicConfig(level=logging.INFO)

# Инициализация бота и диспетчера
bot = Bot(token=settings.bots.bot_token)
dp = Dispatcher()
# регистрируем эхо функцию
dp.message.register(echo)


async def main():
    # Настройка диспетчера и запуск обработчиков
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == '__main__':
    # Запуск основной асинхронной функции
    import asyncio
    asyncio.run(main())
