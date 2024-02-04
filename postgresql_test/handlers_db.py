from aiogram import Router, F
from aiogram.filters import Command, CommandStart
from aiogram.types import Message

router = Router()


@router.message(CommandStart())
async def process_start_cmd(message: Message) -> None:
    await message.answer(
        text='Let`s store some!'
    )


@router.message(Command(commands='save'))
async def process_save_cmd(message: Message) -> None:
    await message.answer(
        text='Send data'
    )
