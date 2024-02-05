from dataclasses import dataclass
from environs import Env


# Database config
@dataclass
class DatabaseConfig:
    database: str
    db_host: str
    db_user: str
    db_password: str


# Class for bot config
@dataclass
class TgBot:
    token: str
    admin_ids: int


# Main config
@dataclass
class Config:
    tg_bot: TgBot
    db: DatabaseConfig | None = None


# Func for loading all necessary config
def load_config(path: str | None = None) -> Config:
    env: Env = Env()
    env.read_env(path)

    return Config(tg_bot=TgBot(token=env('BOT_TOKEN'), admin_ids=env('ADMIN_IDS')))
