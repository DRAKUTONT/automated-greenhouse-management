import asyncio
import logging
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from aiogram import Bot, Dispatcher
from telegram_bot.handlers import start, sensors_handler, devices_handler
from greenhouse_management.greenhouse_management_system import GreenhouseManagementSystem


async def update_data(greenhouse_management_system: GreenhouseManagementSystem):
    greenhouse_management_system.update_data()


async def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    )

    greenhouse_management_system = GreenhouseManagementSystem(30, 60, 70)
    # greenhouse_management_system.clear_database()
    # greenhouse_management_system.fill_database()

    bot = Bot(token="5819137091:AAHb8sZIKAq17I9bChUywEzYgYUP30Mi2og")
    dp = Dispatcher()

    dp.include_router(start.router)
    dp.include_router(sensors_handler.router)
    dp.include_router(devices_handler.router)

    # scheduler = AsyncIOScheduler(timezone='Europe/Moscow')
    # scheduler.add_job(update_data, trigger="interval", seconds=1, args=(greenhouse_management_system,))
    # scheduler.start()

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, greenhouse_management_system=greenhouse_management_system)


if __name__ == "__main__":
    asyncio.run(main())
