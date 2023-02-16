from aiogram import Router
from aiogram.types import Message, FSInputFile
from aiogram.filters import Text

from greenhouse_management.greenhouse_management_system import GreenhouseManagementSystem
from telegram_bot.keyboards.reply_keyboards.sensors_keyboard import create_temp_and_hum_keyboard, create_soil_hum_keyboard


router = Router()


@router.message(Text(text=['Температура и влажность', '/temp_and_hum']))
async def temp_and_hum_handler(message: Message, greenhouse_management_system: GreenhouseManagementSystem):
    data = greenhouse_management_system.get_data()
    text = '\n'.join([f'{key}: {value:.2f}' for key, value in data['ventilation_system'].items()] +
                     [f'{key}: {value:.2f}' for key, value in data['humidification_system'].items()])

    await message.answer(text, reply_markup=create_temp_and_hum_keyboard())


@router.message(Text(text=['График средних значений']))
async def graph_temp_and_hum_average_value_handler(message: Message, greenhouse_management_system: GreenhouseManagementSystem):
    greenhouse_management_system.draw_average_value_graphic()
    await message.answer_photo(FSInputFile('average_values.png'))


@router.message(Text(text=['Графики датчиков температуры и влажности']))
async def graph_temp_and_hum_average_value_handler(message: Message, greenhouse_management_system: GreenhouseManagementSystem):
    greenhouse_management_system.draw_sensors_graphic(sensor_type='temp_and_hum')
    await message.answer_photo(FSInputFile('temp_graphic.png'))
    await message.answer_photo(FSInputFile('hum_graphic.png'))


@router.message(Text(text=['Влажность почвы', '/soil_humidity']))
async def soil_hum_handler(message: Message, greenhouse_management_system: GreenhouseManagementSystem):
    data = greenhouse_management_system.get_data()
    text = '\n'.join([f'{key}: {value:.2f}' for key, value in data['irrigation_system'].items()])
    await message.answer(text, reply_markup=create_soil_hum_keyboard())


@router.message(Text(text=['График каждого датчика влажности почвы']))
async def graph_temp_and_hum_average_value_handler(message: Message, greenhouse_management_system: GreenhouseManagementSystem):
    greenhouse_management_system.draw_sensors_graphic(sensor_type='soil_hum')
    await message.answer_photo(FSInputFile('soil_hum_graphic.png'))


