from aiogram_dialog import Dialog, DialogManager, StartMode, Window, setup_dialogs
from aiogram_dialog.widgets.text import Const, Format

from dialogs.getters import user_name_getter
from states.states import StartSG


start_dialog = Dialog(
    Window(
        Format(text='Hello, {username}'),
        getter= user_name_getter,
        state=StartSG.start
    ),
)

