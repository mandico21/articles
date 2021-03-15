from pathlib import Path

import sqlalchemy
from environs import Env

env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")
SKIP_UPDATES = env.bool("SKIP_UPDATES", False)
WORK_PATH: Path = Path(__file__).parent.parent

SUPERUSER_IDS = env.list("SUPERUSER_IDS")
IP = env.str("ip")
DBUSER = env.str("DBUSER")
DBPASS = env.str("DBPASS")
DBBASE = env.str("DBBASE")

engine = sqlalchemy.create_engine(
    f'postgresql://{DBUSER}:{DBPASS}@{IP}/{DBBASE}',
    execution_options={
        "isolation_level": "REPEATABLE_READ"
    }
)
