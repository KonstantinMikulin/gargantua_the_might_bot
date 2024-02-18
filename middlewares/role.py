from typing import Awaitable, Callable, Any

from aiogram import BaseMiddleware
from aiogram.types import Update, User
from asyncpg import Pool

from infrastructure.database.database.db import DB
from infrastructure.database.models.users import UsersModel


class DataBaseMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[Update, dict[str, Any]], Awaitable[None]],
        event: Update,
        data: dict[str, Any]
    ) -> Any:
        db: DB = data.get('db')
        user: User = data.get('event_from_user')
        user_record: UsersModel = await db.users.get_user_record(user_id=user.id)
        data['role'] = user_record.role

        await handler(event, data)
