from sqlalchemy import Column, Integer, String
from database import Base #base class is imported from databse.py
from sqlalchemy import Boolean, ForeignKey


class user(Base):
    __tablename__="users"
    id=Column(Integer, primary_key=True)
    name=Column(String)


class Task(Base):
    __tablename__="tasks"
    id=Column(Integer,primary_key=True)
    title=Column(String)
    completed=Column(Boolean, default=False)

    user_id=Column(Integer, ForeignKey(user.id))