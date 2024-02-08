from asyncpg import UniqueViolationError
from utils.db_api.schemas.user import User


async def add_user(user_id: int, name: str, update_name: str = None):
    try:
        user = User(user_id=user_id, name=name, update_name=update_name)
        await user.create()
    except UniqueViolationError:
        print('Пользователь не добавлен')


async def select_all_users():
    users = await User.query.gino.all()
    return users
