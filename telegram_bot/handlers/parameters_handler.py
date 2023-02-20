from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message
from aiogram.filters import Command, Text

from greenhouse_management.greenhouse_management_system import GreenhouseManagementSystem

router = Router()


class InputTParameter(StatesGroup):
    t_parameter = State()


class InputHParameter(StatesGroup):
    h_parameter = State()


class InputHbParameter(StatesGroup):
    hb_parameter = State()


@router.message(Text(text='T'))
async def t_parameter_handler(message: Message, state: FSMContext):
    await message.answer('Введите параметр T')
    await state.set_state(InputTParameter.t_parameter)


@router.message(InputTParameter.t_parameter)
async def input_t_parameter(message: Message, state: FSMContext, greenhouse_management_system: GreenhouseManagementSystem):
    try:
        await state.update_data(T=int(message.text.lower()))
        greenhouse_management_system.set_parameters(await state.get_data())

        await message.answer(text='Параметр выставлен ✅')
        await state.clear()
    except Exception:
        await message.answer(text='Введите корректное значение')


@router.message(Text(text='H'))
async def h_parameter_handler(message: Message, state: FSMContext):
    await message.answer('Введите параметр H')
    await state.set_state(InputHParameter.h_parameter)


@router.message(InputHParameter.h_parameter)
async def input_h_parameter(message: Message, state: FSMContext, greenhouse_management_system: GreenhouseManagementSystem):
    try:
        await state.update_data(H=int(message.text.lower()))
        greenhouse_management_system.set_parameters(await state.get_data())

        await message.answer(text='Параметр выставлен ✅')
        await state.clear()
    except Exception:
        await message.answer(text='Введите корректное значение')


@router.message(Text(text='Hb'))
async def hb_parameter_handler(message: Message, state: FSMContext):
    await message.answer('Введите параметр Hb')
    await state.set_state(InputHbParameter.hb_parameter)


@router.message(InputHbParameter.hb_parameter)
async def input_hb_parameter(message: Message, state: FSMContext, greenhouse_management_system: GreenhouseManagementSystem):
    try:
        await state.update_data(Hb=int(message.text.lower()))
        greenhouse_management_system.set_parameters(await state.get_data())

        await message.answer(text='Параметр выставлен ✅')
        await state.clear()
    except Exception:
        await message.answer(text='Введите корректное значение')
