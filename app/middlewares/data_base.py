from app.config import engine


class DbMiddleware(BaseMiddleware):
    Session = sessionmaker(bind=engine)


    async def pre_process(self, *args):
        conn = engine.connect()


    async def post_process(self, *args):
        session = Session(bind=conn)
        try:
            UserQuery.create_table(session, from_id, name, telegeram_user,
                                   curtime)
            session.commit()
        except Exception:
            session.rollback()
        finally:
            session.close()
