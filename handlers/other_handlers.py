from aiogram import Router
from aiogram.types import Message
from aiogram.filters import StateFilter
from aiogram.fsm.state import default_state

from lexicon.lexicon import LEXICON_RU

router = Router()


@router.message(StateFilter(default_state))
async def process_any(message: Message):
    await message.answer(text=LEXICON_RU['other_answers'])
