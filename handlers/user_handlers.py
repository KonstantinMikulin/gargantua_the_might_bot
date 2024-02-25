import logging

from aiogram import Router, F
from aiogram.filters import Command, CommandStart, StateFilter
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.state import default_state
from aiogram.fsm.context import FSMContext

from aiogram_dialog import DialogManager, StartMode

from lexicon.lexicon import LEXICON_RU, LEXICON_FSM
from keyboards.keyboards import inline_gender_keyboard
from fsm.fsm_profile import FSMProfile, user_dict
from states.states import StartSG

from infrastructure.database.database.db import DB
from infrastructure.database.models.users import UsersModel

logger = logging.getLogger(__name__)
router = Router()


# command for starting bot
@router.message(CommandStart(), StateFilter(default_state))
# async def process_start_cmd(message: Message, db: DB) -> None:
async def process_start_cmd(message: Message, dialog_manager: DialogManager) -> None:
    await dialog_manager.start(state=StartSG.start, mode=StartMode.RESET_STACK)
    
    # await db.users.add(user_id=message.from_user.id, language=message.from_user.language_code)
    # user_record: UsersModel = await db.users.get_user_record(user_id=message.from_user.id)
    # logger.debug('my_user_record %s', user_record)


@router.message(Command(commands='help'), StateFilter(default_state))
async def process_help_cmd(message: Message) -> None:
    await message.answer(text=LEXICON_RU[message.text])


@router.message(Command(commands='profile'), StateFilter(default_state))
async def process_profile_command(message: Message, state: FSMContext) -> None:
    await message.answer(text=LEXICON_RU[message.text])
    await state.set_state(FSMProfile.fill_name)


# handler for /cancel when FSM is off
@router.message(Command(commands='cancel'), StateFilter(default_state))
async def process_cancel_command(message: Message):
    await message.answer(
        text=LEXICON_RU[message.text]
    )


# handler for /cancel when FSM is on
@router.message(Command(commands='cancel'), ~StateFilter(default_state))
async def process_cancel_command_state(message: Message, state: FSMContext) -> None:
    await message.answer(text=LEXICON_FSM[message.text])
    await state.clear()


# handler if name was sent correct and changing state to fill_age
@router.message(StateFilter(FSMProfile.fill_name), F.text.isalpha())
async def process_name_sent(message: Message, state: FSMContext) -> None:
    await state.update_data(name=message.text)
    await message.answer(text=LEXICON_FSM['age'])
    await state.set_state(FSMProfile.fill_age)


# handler if name was not correct
@router.message(StateFilter(FSMProfile.fill_name))
async def warning_not_name(message: Message):
    await message.answer(
        text=LEXICON_FSM['not_name']
    )


# handler if age was sent correct and changing state to fill_gender
@router.message(StateFilter(FSMProfile.fill_age), lambda x: x.text.isdigit() and 18 <= int(x.text) <= 120)
async def process_age_sent(message: Message, state: FSMContext) -> None:
    await state.update_data(age=message.text)
    await message.answer(
        text=LEXICON_FSM['gender'],
        reply_markup=inline_gender_keyboard
    )
    await state.set_state(FSMProfile.fill_gender)


# handler if age was not correct
@router.message(StateFilter(FSMProfile.fill_age))
async def warning_not_age(message: Message):
    await message.answer(
        text=LEXICON_FSM['not_age']
    )


# handler for choosing gender and switch state to fill_weight
@router.callback_query(StateFilter(FSMProfile.fill_gender), F.data.in_(['male', 'female']))
async def process_gender_press(callback: CallbackQuery, state: FSMContext) -> None:
    await state.update_data(gender=callback.data)
    await callback.message.delete()
    await callback.message.answer(text=LEXICON_FSM['weight'])
    await state.set_state(FSMProfile.fill_weight)


# handler if button with genders was not pressed
@router.message(StateFilter(FSMProfile.fill_gender))
async def warning_not_gender(message: Message):
    await message.answer(
        text=LEXICON_FSM['not_gender']
    )


# handler if weight was correct, store data and stop FSM
@router.message(StateFilter(FSMProfile.fill_weight), lambda x: x.text.isdigit() and 20 <= int(x.text) <= 700)
async def process_weight_sent(message: Message, state: FSMContext) -> None:
    await state.update_data(weight=message.text)
    user_dict[message.from_user.id] = await state.get_data()
    await state.clear()
    await message.answer(text=LEXICON_FSM['profile_done'])


# handler if weight was not correct
@router.message(StateFilter(FSMProfile.fill_weight))
async def warning_not_weight(message: Message):
    await message.answer(
        text=LEXICON_FSM['not_weight']
    )


@router.message(Command(commands='showdata'), StateFilter(default_state))
async def process_showdata_sent(message: Message) -> None:
    if message.from_user.id in user_dict:
        await message.answer(
            text=f'Name: {user_dict[message.from_user.id]["name"]}\n'
                 f'Age: {user_dict[message.from_user.id]["age"]}\n'
                 f'Gender: {user_dict[message.from_user.id]["gender"]}\n'
                 f'Weight: {user_dict[message.from_user.id]["weight"]}'
        )
    else:
        await message.answer(text='To fill - /profile')
