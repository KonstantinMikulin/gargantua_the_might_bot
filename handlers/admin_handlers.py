from aiogram import Bot, Router
from aiogram.filters import Command
from aiogram.types import Message

router = Router()


@router.message(Command(commands='delmenu'))
async def del_main_menu(message: Message, bot: Bot):
    await bot.delete_my_commands()
    await message.answer(text='Кнопка "Menu" удалена')


# @router.message(Command(commands='delete_menu'))
# async def process_main_menu_delete(message: Message, bot):
#     await bot.delete_my_commands()
#     await message.answer(text='Удалили меню. Для возвращения /restore_menu',
#                          reply_markup=ReplyKeyboardRemove())
