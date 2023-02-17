from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command, Text

from greenhouse_management.greenhouse_management_system import GreenhouseManagementSystem
from telegram_bot.keyboards.reply_keyboards.devices_keyboard import create_window_device_keyboard, \
    create_humidifier_device_keyboard, create_sprinklers_device_keyboard, create_emergency_management_keyboard, \
    create_sprinkler_device_keyboard
from telegram_bot.utils.formatting import formatting_sensor_data_for_user, formatting_device_data_for_user
from greenhouse_management.exceptions.temperature_exception import TemperatureParameterException
from greenhouse_management.exceptions.humidity_exception import HumidityParameterException
from greenhouse_management.exceptions.soil_humidity_exception import SoilHumidityParameterException

router = Router()


@router.message(Text(text=['Проветривание', '/window_device']))
async def window_device_handler(message: Message, greenhouse_management_system: GreenhouseManagementSystem):
    current_status = 'Открыто' if greenhouse_management_system.is_window_work() else 'Закрыто'
    await message.answer(f'Текущий статус: {current_status}',
                         reply_markup=create_window_device_keyboard(greenhouse_management_system.is_window_work()))


@router.message(Text(text=['Включить привод']))
async def enable_window_device_handler(message: Message, greenhouse_management_system: GreenhouseManagementSystem):
    try:
        greenhouse_management_system.set_window_state(state=True)
        await message.answer('Окно открыто', reply_markup=create_window_device_keyboard(True))

    except TemperatureParameterException:
        await message.answer('Невозможно выполнить данное действие, так как параметр T не соответсвует требованиям')


@router.message(Text(text=['Выключить привод']))
async def disable_window_device_handler(message: Message, greenhouse_management_system: GreenhouseManagementSystem):
    greenhouse_management_system.set_window_state(state=False)
    await message.answer('Окно закрыто', reply_markup=create_window_device_keyboard(False))


@router.message(Text(text=['Система увлажнения', '/humidifier_device']))
async def humidifier_device_handler(message: Message, greenhouse_management_system: GreenhouseManagementSystem):
    current_status = 'Включено' if greenhouse_management_system.is_humidifier_work() else 'Выключено'
    await message.answer(f'Текущий статус: {current_status}', reply_markup=create_humidifier_device_keyboard(
        greenhouse_management_system.is_humidifier_work()))


@router.message(Text(text=['Включить увлажнитель']))
async def enable_humidifier_device_handler(message: Message, greenhouse_management_system: GreenhouseManagementSystem):
    try:
        greenhouse_management_system.set_humidifier_state(state=True)
        await message.answer('Увлажнитель включен', reply_markup=create_humidifier_device_keyboard(True))

    except HumidityParameterException:
        await message.answer('Невозможно выполнить данное действие, так как параметр H не соответсвует требованиям')


@router.message(Text(text=['Выключить увлажнитель']))
async def disable_humidifier_device_handler(message: Message, greenhouse_management_system: GreenhouseManagementSystem):
    greenhouse_management_system.set_humidifier_state(state=False)
    await message.answer('Увлажнитель выключен', reply_markup=create_humidifier_device_keyboard(False))


@router.message(Text(text=['Система полива', '/sprinklers_device']))
async def sprinklers_device_handler(message: Message, greenhouse_management_system: GreenhouseManagementSystem):
    data = formatting_device_data_for_user(data=greenhouse_management_system.get_sprinklers_state(),
                                           device_name='Полив', enable_name='включен', disable_name='выключен')

    text = '\n'.join([f'{key}: {value}' for key, value in data.items()])
    await message.answer(text, reply_markup=create_sprinklers_device_keyboard())


@router.message(Text(startswith='Полив №'))
async def sprinkler_device_handler(message: Message, greenhouse_management_system: GreenhouseManagementSystem):
    device_id = int(message.text[-1]) - 1
    if -1 < device_id > 5:
        await message.answer('Некорректный номер полива')
    else:
        device_status = 'Включено' if greenhouse_management_system.is_sprinkler_work(
            device_id=device_id) else 'Выключено'
        await message.answer(f'Статус: {device_status}',
                             reply_markup=create_sprinkler_device_keyboard(sprinkler_id=device_id + 1,
                                                                           is_work=greenhouse_management_system.is_sprinkler_work(
                                                                               device_id)))


@router.message(Text(startswith='Включить полив №'))
async def enable_sprinkler_device_handler(message: Message, greenhouse_management_system: GreenhouseManagementSystem):
    device_id = int(message.text[-1]) - 1
    if -1 < device_id > 5:
        await message.answer('Некорректный номер полива')
    else:
        try:
            greenhouse_management_system.set_sprinkler_state(state=True, device_id=device_id)
            await message.answer(f'Полив №{device_id + 1} включен',
                                 reply_markup=create_sprinkler_device_keyboard(sprinkler_id=device_id + 1,
                                                                               is_work=True))
        except SoilHumidityParameterException:
            await message.answer(
                'Невозможно выполнить данное действие, так как параметр Hb не соответсвует требованиям')


@router.message(Text(startswith='Выключить полив №'))
async def disable_sprinkler_device_handler(message: Message, greenhouse_management_system: GreenhouseManagementSystem):
    device_id = int(message.text[-1]) - 1
    if -1 < device_id > 5:
        await message.answer('Некорректный номер полива')
    else:
        greenhouse_management_system.set_sprinkler_state(state=False, device_id=device_id)
        await message.answer(f'Полив №{device_id + 1} выключен',
                             reply_markup=create_sprinkler_device_keyboard(sprinkler_id=device_id + 1, is_work=False))


@router.message(Text(text=['Экстренное управление', '/emergency_management']))
async def emergency_management_handler(message: Message, greenhouse_management_system: GreenhouseManagementSystem):
    current_status = 'Включено' if greenhouse_management_system.get_emergency_mode_status() else 'Выключено'
    await message.answer(f'Экстренное управление: {current_status}', reply_markup=create_emergency_management_keyboard(
        greenhouse_management_system.get_emergency_mode_status()))


@router.message(Text(text='Включить экстренное управление'))
async def enable_emergency_management_handler(message: Message,
                                              greenhouse_management_system: GreenhouseManagementSystem):
    greenhouse_management_system.enable_emergency_mode()
    await message.answer(f'Экстренное управление включено', reply_markup=create_emergency_management_keyboard(True))


@router.message(Text(text='Выключить экстренное управление'))
async def disable_emergency_management_handler(message: Message,
                                               greenhouse_management_system: GreenhouseManagementSystem):
    greenhouse_management_system.disable_emergency_mode()
    await message.answer(f'Экстренное управление выключено', reply_markup=create_emergency_management_keyboard(False))
