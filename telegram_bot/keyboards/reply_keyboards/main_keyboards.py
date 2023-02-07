from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def create_main_keyboard() -> ReplyKeyboardMarkup:
    builder = ReplyKeyboardBuilder()

    builder.row(KeyboardButton(text='Температура и влажность'),
                KeyboardButton(text='Влажность почвы'),
                width=2)

    builder.row(KeyboardButton(text='Проветривание'),
                KeyboardButton(text='Система полива'),
                KeyboardButton(text='Система увлажнения'),
                width=3)

    builder.row(KeyboardButton(text='Экстренное управление'),
                KeyboardButton(text='Параметры'),
                width=2)

    markup = builder.as_markup()
    markup.resize_keyboard = True

    return markup