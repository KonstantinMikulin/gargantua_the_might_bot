import asyncio

from config_data import config_db
from utils.db_api import quick_commands as commands
from utils.db_api.db_gino import db


async def db_test():
    await db.set_bind(config_db.POSTGRES_URI)
    await db.gino.drop_all()
    await db.gino.create_all()

    await commands.add_user(1, 'Vlad', 'Not')
    await commands.add_user(7598434, 'Konstantin', 'Kostya')
    await commands.add_user(12, 'Dan', 'Daniel')
    await commands.add_user(1010205, 'Mark', '123')
    await commands.add_user(15, 'Anna', 'Beloved Anna')

    users = await commands.select_all_users()
    print(users)

    count = await commands.count_users()
    print(count)

    user = await commands.select_user(1)
    print(user)

    await commands.update_user_name(1, 'Vlad Efanov')
    user = await commands.select_user(1)
    print(user)


asyncio.run(db_test())
