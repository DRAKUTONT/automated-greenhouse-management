from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from telegram_bot.keyboards.reply_keyboards.main_keyboards import create_main_keyboard

router = Router()


@router.message(Command(commands=["start", "help"]))
async def start(message: Message):
    await message.answer("""
    /start - перезапустить бота
    /help - подсказка
    /temp_and_hum - температура и влажность
    /soil_humidity - влажность почвы
    /set_T - установить T
    /set_H - установить H
    /set_Hb - установить Hb
    /emergency_management - экстренное управление""", reply_markup=create_main_keyboard())



