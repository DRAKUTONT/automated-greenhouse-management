from aiogram import Router
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram.filters import Command, Text

from greenhouse_management.greenhouse_management_system import GreenhouseManagementSystem
from telegram_bot.keyboards.reply_keyboards.main_keyboards import create_main_keyboard

router = Router()


class InputParameters(StatesGroup):
    t_parameter = State()
    h_parameter = State()
    hb_parameter = State()


@router.message(Command(commands="start"))
async def start(message: Message, state: FSMContext):
    await message.answer(text='Перед началом работы необходимо, чтобы Вы указали обязательные параметры')
    await message.answer(text='Введите параметр T')

    await state.set_state(InputParameters.t_parameter)


@router.message(InputParameters.t_parameter)
async def t_parameter(message: Message, state: FSMContext):
    try:
        await state.update_data(T=int(message.text.lower()))
        await message.answer(text='Введите параметр H')
        await state.set_state(InputParameters.h_parameter)
    except Exception:
        await message.answer(text='Введите корректное значение')


@router.message(InputParameters.h_parameter)
async def h_parameter(message: Message, state: FSMContext):
    try:
        await state.update_data(H=int(message.text.lower()))
        await message.answer(text='Введите параметр Hb')
        await state.set_state(InputParameters.hb_parameter)
    except Exception:
        await message.answer(text='Введите корректное значение')


@router.message(InputParameters.hb_parameter)
async def hb_parameter(message: Message, state: FSMContext, greenhouse_management_system: GreenhouseManagementSystem):
    try:
        await state.update_data(Hb=int(message.text.lower()))
        await message.answer(text='Параметры выставлены ✅')
        user_data = await state.get_data()
        greenhouse_management_system.set_parameters(user_data)
        await state.clear()
    except Exception:
        await message.answer(text='Введите корректное значение')


@router.message(Text(text=['Назад']))
async def back(message: Message):
    await message.answer('<-', reply_markup=create_main_keyboard())
