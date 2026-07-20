from sqlalchemy.orm import Session
from models import User
from schemas import user_create

#adding the user to the database program 
def create_user(db:Session, user:user_create):
    db_user=User(name=user.name, email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

#get all users function
def get_all(db:Session):
    return db.query(User).all()

#get one user with the user id
def get_one(db:Session, user_id:int):
    return (db.query(User).filter(User.id==user_id).first())

#update the user detail
def update_user(db:Session, user_id:int, user:user_create):
    db_user=(db.query(User).filter(User.id==user_id).first())

    db_user.name=user.name
    db_user.email=user.email
    db.commit()
    db.refresh(db_user)
    return db_user

#delete the user
def delete_user(db:Session,user_id:int):
    db_user=(db.query(User).filter(User.id==user_id).first())
    db.delete(db_user)
    db.commit()
    return db_user