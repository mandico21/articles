from app.moduls.db_api.base import User


class UserQuery:
    def create_table(session: "Session", user_id: int, name: str, telegeram_user: str, date_created: int):
        u = User(user_id, name, telegeram_user, date_created)
        session.add(u)