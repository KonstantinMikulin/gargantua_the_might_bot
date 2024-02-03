from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardButton, InlineKeyboardMarkup)
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder


# FSM inline keyboard
inline_button_male = InlineKeyboardButton(
    text='Male',
    callback_data='male'
)
inline_button_female = InlineKeyboardButton(
    text='Female',
    callback_data='female'
)

kb_builder = InlineKeyboardBuilder()
kb_builder.row(inline_button_male, inline_button_female)

inline_gender_keyboard = kb_builder.as_markup()
