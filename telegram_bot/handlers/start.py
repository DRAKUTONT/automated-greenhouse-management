from aiogram import Router
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.filters import Command

router = Router()  # [1]


@router.message(Command(commands=["start"]))  # [2]
async def start(message: Message):
    await message.answer('hello')