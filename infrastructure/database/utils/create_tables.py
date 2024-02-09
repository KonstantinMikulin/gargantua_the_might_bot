from asyncpg import Connection

from infrastructure.database.database.db import DB


async def create_tables(connect: Connection) -> None:
    db = DB(connect)
    await db.users.create_table()
