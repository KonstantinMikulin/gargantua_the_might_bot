import os
import logging
import asyncio

from aiogram import Bot, Dispatcher

import handlers_db
from db import BaseModel, create_new_async_engine, get_session_maker, proceed_schemas

from sqlalchemy.engine import URL

logger = logging.getLogger(__name__)


async def main():
    logging.basicConfig(
        level=logging.INFO,
        format='%(filename)s:%(lineno)d #%(levelname)-8s '
               '[%(asctime)s] - %(name)s - %(message)s'
    )
    logger.info('Starting bot')
    bot = Bot(token=os.getenv('token'))
    dp = Dispatcher()

    dp.include_router(handlers_db.router)

    postgres_url = URL.create(
        'postgresql+asyncpg',
        username=os.getenv('db_user'),
        host='localhost',
        password=os.getenv('db_pass'),
        database=os.getenv('db_name'),
        port=os.getenv('db_port')
    )
    async_engine = create_new_async_engine(postgres_url)
    session_maker = get_session_maker(async_engine)

    await proceed_schemas(async_engine, BaseModel.metadata)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
