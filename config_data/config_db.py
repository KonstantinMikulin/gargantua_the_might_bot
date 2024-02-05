import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = str(os.getenv('BOT_TOKEN'))

ip = os.getenv('ip')
PG_USER = str(os.getenv('DB_USER'))
PG_PASSWORD = str(os.getenv('DB_PASSWORD'))
DATABASE = str(os.getenv('DATABASE'))
POSTGRES_URL = f'postgresql://{PG_USER}:{PG_PASSWORD}@{ip}/{DATABASE}'
