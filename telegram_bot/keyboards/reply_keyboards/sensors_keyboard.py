from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder


def create_temp_and_hum_keyboard() -> ReplyKeyboardMarkup:
    builder = ReplyKeyboardBuilder()

    builder.row(KeyboardButton(text='Таблица с данными температуры и влажности'),
                KeyboardButton(text='Таблица с данными средней температуры и влажности'),
                width=2)

    builder.row(KeyboardButton(text='Графики датчиков температуры и влажности'),
                KeyboardButton(text='График средних значений'),
                width=2)

    builder.row(KeyboardButton(text='Назад'), width=1)

    markup = builder.as_markup()
    markup.resize_keyboard = True

    return markup


def create_soil_hum_keyboard() -> ReplyKeyboardMarkup:
    builder = ReplyKeyboardBuilder()

    builder.row(KeyboardButton(text='Таблица с данными влажности почвы'),
                KeyboardButton(text='График каждого датчика влажности почвы'),
                width=2)

    builder.row(KeyboardButton(text='Назад'), width=1)

    markup = builder.as_markup()
    markup.resize_keyboard = True

    return markup