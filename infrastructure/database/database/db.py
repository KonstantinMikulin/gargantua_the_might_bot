from asyncpg import Connection

from infrastructure.database.database.users import _UsersDB


class DB:
    def __init__(self, connect: Connection) -> None:
        self.users = _UsersDB(connect=connect)
