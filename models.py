from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from database import Base


class User(Base):
    __tablename__="users"
    id=Column(Integer,primary_key=True,index=True)
    name=Column(String)
class Conversation(Base):    
    __tablename__="Conversations"
    id=Column(Integer,primary_key=True)
    topic=Column(String)
    user_id=Column(Integer,ForeignKey("users.id"))
