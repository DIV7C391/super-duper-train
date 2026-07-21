from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

import crud
import schemas

from database import engine, get_db, Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

#creating user endpoint
@app.post("/users",response_model=schemas.user_response)
def create_user(user: schemas.user_create, db: Session = Depends(get_db)):
    return crud.create_user(db, user)

#get all users endpoint
@app.get("/users",response_model=list[schemas.user_response])
def get_users(db: Session = Depends(get_db)):
    return crud.get_all(db)

#get one user with the user id
@app.get("/users/{user_id}",response_model=schemas.user_response)
def get_user(user_id: int,db: Session = Depends(get_db)):
    user = crud.get_one(db, user_id)
    return user

#update user endpoint
@app.put("/users/{user_id}",response_model=schemas.user_response)
def update_user(user_id: int,user: schemas.user_create,db: Session = Depends(get_db)):
    updated_user = crud.update_user(db,user_id,user)
    return updated_user

#delete user endpoint
@app.delete("/users/{user_id}")
def delete_user(user_id: int,db: Session = Depends(get_db)):
    deleted_user = crud.delete_user(db,user_id)

    if not deleted_user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )



