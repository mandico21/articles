import datetime

from aiogram import types
from aiogram.dispatcher.filters import CommandStart
from sqlalchemy.orm import sessionmaker

from app.config import engine
from app.loader import dp
from app.moduls.db_api.db_commands import UserQuery

Session = sessionmaker(bind=engine)


@dp.message_handler(CommandStart())
async def command_start_handler(msg: types.Message):
    conn = engine.connect()
    session = Session(bind=conn)
    from_id = msg.from_user.id
    name = msg.from_user.full_name
    telegeram_user = msg.from_user.username
    curtime = datetime.datetime.now()
    try:
        UserQuery.create_table(session, from_id, name, telegeram_user, curtime)
        session.commit()
        await msg.answer(f'Я записала, {name}!')
    except Exception:
        session.rollback()
        await msg.answer('Ой, что-то пошло не так(')
        raise RuntimeError('Film creation failure')
    finally:
        session.close()

    await msg.answer(f'Hello, {msg.from_user.full_name}!')
