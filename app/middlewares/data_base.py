from aiogram.dispatcher.middlewares import BaseMiddleware

from app.config import engine


class DbMiddleware(BaseMiddleware):

    def __init__(self, conns):
        self.conns = conns

    async def pre_process(self, obj, data, *args):
        conn = engine.connect()
        data["conn"] = conn

    async def post_process(self, obj, data, *args):
        db = data.get("conn")
        try:
            db.commit()
        except Exception:
            db.rollback()
        finally:
            db.close()
