from aiogram.types import User

from aiogram_dialog import DialogManager


async def user_name_getter(dialog_manager: DialogManager, event_from_user: User, **kwargs) -> dict:
    return {'username': event_from_user.first_name}
