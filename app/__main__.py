from aiogram import Dispatcher
from aiogram.utils import executor

from app import utils, config
from app.config import engine
from app.loader import dp

# Конфигурация модулей с помощью импорта
from app import middlewares, filters, handlers
from app.moduls.db_api.base import Base


async def on_startup(dispatcher: Dispatcher):
    await utils.setup_default_commands(dispatcher)
    await utils.notify_admins(config.SUPERUSER_IDS)
    print("Чистим базу")
    Base.metadata.drop_all(engine)
    print("Готово")
    print("Создание БД")
    Base.metadata.create_all(engine)
    print("Удачно")


if __name__ == '__main__':
    utils.setup_logger("INFO", ["sqlalchemy.engine", "aiogram.bot.api"])
    executor.start_polling(
        dp, on_startup=on_startup, skip_updates=config.SKIP_UPDATES
    )
