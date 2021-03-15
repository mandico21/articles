from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    user_id = Column("user_id", Integer, primary_key=True)
    name = Column("name", String(150), nullable=False)
    telegeram_user = Column("telegeram_user", String(150), nullable=True)
    date_created = Column('date_created', DateTime, nullable=False)


    def __init__(self, user_id, name,telegeram_user, date_created):
        self.user_id = user_id
        self.name = name
        self.telegeram_user = telegeram_user
        self.date_created = date_created

