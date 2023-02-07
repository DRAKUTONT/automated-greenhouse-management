from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder


def create_temp_and_hum_keyboard() -> ReplyKeyboardMarkup:
    builder = ReplyKeyboardBuilder()

    builder.row(KeyboardButton(text='Таблица с данными'), width=1)

    builder.row(KeyboardButton(text='График каждого датчика'),
                KeyboardButton(text='График средних значений'),
                width=2)

    builder.row(KeyboardButton(text='Назад'), width=1)

    markup = builder.as_markup()
    markup.resize_keyboard = True

    return markup


def create_soil_hum_keyboard() -> ReplyKeyboardMarkup:
    builder = ReplyKeyboardBuilder()

    builder.row(KeyboardButton(text='Таблица с данными'),
                KeyboardButton(text='График каждого датчика'),
                width=2)

    builder.row(KeyboardButton(text='Назад'), width=1)

    markup = builder.as_markup()
    markup.resize_keyboard = True

    return markup