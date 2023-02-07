import asyncio
from aiogram import Bot, Dispatcher
from telegram_bot.handlers import start
import logging


async def main():
    logging.basicConfig()
    bot = Bot(token="5819137091:AAHb8sZIKAq17I9bChUywEzYgYUP30Mi2og")
    dp = Dispatcher()

    dp.include_router(start.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
