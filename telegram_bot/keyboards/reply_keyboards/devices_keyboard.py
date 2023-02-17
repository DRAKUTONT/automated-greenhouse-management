from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def create_window_device_keyboard(is_work: bool = False) -> ReplyKeyboardMarkup:
    builder = ReplyKeyboardBuilder()

    if is_work:
        builder.row(KeyboardButton(text='Выключить привод'), width=1)

    else:
        builder.row(KeyboardButton(text='Включить привод'), width=1)

    builder.row(KeyboardButton(text='Назад'), width=1)

    markup = builder.as_markup()
    markup.resize_keyboard = True

    return markup


def create_humidifier_device_keyboard(is_work: bool = False) -> ReplyKeyboardMarkup:
    builder = ReplyKeyboardBuilder()

    if is_work:
        builder.row(KeyboardButton(text='Выключить увлажнитель'), width=1)

    else:
        builder.row(KeyboardButton(text='Включить увлажнитель'), width=1)

    builder.row(KeyboardButton(text='Назад'), width=1)

    markup = builder.as_markup()
    markup.resize_keyboard = True

    return markup


def create_sprinklers_device_keyboard() -> ReplyKeyboardMarkup:
    builder = ReplyKeyboardBuilder()

    builder.row(KeyboardButton(text=f'Полив №1'),
                KeyboardButton(text=f'Полив №2'),
                KeyboardButton(text=f'Полив №3'),
                width=3)

    builder.row(KeyboardButton(text=f'Полив №4'),
                KeyboardButton(text=f'Полив №5'),
                KeyboardButton(text=f'Полив №6'),
                width=3)

    builder.row(KeyboardButton(text='Назад'), width=1)

    markup = builder.as_markup()
    markup.resize_keyboard = True

    return markup


def create_sprinkler_device_keyboard(sprinkler_id: int, is_work: bool = False) -> ReplyKeyboardMarkup:
    builder = ReplyKeyboardBuilder()

    if is_work:
        builder.row(KeyboardButton(text=f'Выключить полив №{sprinkler_id}'), width=1)

    else:
        builder.row(KeyboardButton(text=f'Включить полив №{sprinkler_id}'), width=1)

    builder.row(KeyboardButton(text='Назад'), width=1)

    markup = builder.as_markup()
    markup.resize_keyboard = True

    return markup


def create_emergency_management_keyboard(is_work: bool = False) -> ReplyKeyboardMarkup:
    builder = ReplyKeyboardBuilder()

    if is_work:
        builder.row(KeyboardButton(text='Выключить экстренное управление'), width=1)

    else:
        builder.row(KeyboardButton(text='Включить экстренное управление'), width=1)

    builder.row(KeyboardButton(text='Назад'), width=1)

    markup = builder.as_markup()
    markup.resize_keyboard = True

    return markup


def create_parameters_keyboard():
    builder = ReplyKeyboardBuilder()

    builder.row(KeyboardButton(text='T'),
                KeyboardButton(text='H'),
                KeyboardButton(text='Hb'),
                width=3)

    builder.row(KeyboardButton(text='Назад'), width=1)

    markup = builder.as_markup()
    markup.resize_keyboard = True

    return markup