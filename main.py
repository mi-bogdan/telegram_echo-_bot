import logging
from aiogram import Bot, Dispatcher
from core.settings import settings
from core.handlers.basic import echo


async def start_bot(bot: Bot):
    await bot.send_message(settings.bots.admin_id, text=f'<b>Бот запущен!</b>')


async def stop_bot(bot: Bot):
    await bot.send_message(settings.bots.admin_id, text='<b>Бот остановлен!</b>')

# Настройка логирования
logging.basicConfig(level=logging.INFO)

# Инициализация бота и диспетчера
bot = Bot(token=settings.bots.bot_token, parse_mode='HTML')
dp = Dispatcher()
dp.startup.register(start_bot)
dp.shutdown.register(stop_bot)
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
