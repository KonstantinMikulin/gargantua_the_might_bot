import asyncio
import logging

from aiogram import Bot, Dispatcher

from config_data.config import Config, load_config
from handlers import admin_handlers, user_handlers, other_handlers
from keyboards.set_menu import set_main_menu
from fsm.fsm_profile import storage
from infrastructure.database.utils.connect_to_pg import get_pg_pool
from middlewares.database import DataBaseMiddleware
from infrastructure.database.utils.create_tables import create_tables

logger = logging.getLogger(__name__)


async def main():
    logging.basicConfig(level=logging.INFO,
                        format='%(filename)s:%(lineno)d #%(levelname)-8s '
                        '[%(asctime)s] - %(name)s - %(message)s')
    logger.info('Starting bot')
    config: Config = load_config()
    bot = Bot(token=config.tg_bot.token)
    dp = Dispatcher(storage=storage)

    db_pool = await get_pg_pool(
        db_name=config.pg.db_name,
        host=config.pg.host,
        port=config.pg.port,
        user=config.pg.username,
        password=config.pg.password
    )

    async with db_pool.acquire() as connect:
        try:
            await create_tables(connect)
        except Exception as e:
            logger.exception(e)
            await db_pool.close()

    dp.include_router(admin_handlers.router)
    dp.include_router(user_handlers.router)
    dp.include_router(other_handlers.router)

    dp.update.middleware(DataBaseMiddleware())

    await set_main_menu(bot)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, _db_pool=db_pool)


if __name__ == '__main__':
    asyncio.run(main())
