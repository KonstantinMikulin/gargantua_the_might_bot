from typing import Awaitable, Callable, Any

from aiogram import BaseMiddleware
from aiogram.types import Update
from asyncpg import Pool

from infrastructure.database.database.db import DB


class DataBaseMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[Update, dict[str, Any]], Awaitable[None]],
        event: Update,
        data: dict[str, Any]
    ) -> Any:
        pool: Pool = data.get('_db_pool')

        async with pool.acquire() as connect:
            data['db'] = DB(connect)

            await handler(event, data)
