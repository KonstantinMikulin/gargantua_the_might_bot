from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import KeyboardButton, Message, ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from config_data.config import Config, load_config

config: Config = load_config()

bot = Bot(token=config.tg_bot.token)
dp = Dispatcher()

kb_builder = ReplyKeyboardBuilder()

button_1 = KeyboardButton(text='Button one!')
button_2 = KeyboardButton(text='Button two!')


kb_builder.row(button_1, button_2, width=2)
keyboard: ReplyKeyboardMarkup = kb_builder.as_markup(
    resize_keyboard=True,
    one_time_keyboard=True,
    input_field_placeholder='Choose you answer'
)


@dp.message(CommandStart())
async def process_start_cmd(message: Message):
    await message.answer(
        text='Here you go',
        reply_markup=keyboard
    )


if __name__ == '__main__':
    dp.run_polling(bot)
