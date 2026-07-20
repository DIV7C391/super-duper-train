from pydantic import BaseModel

class user_create(BaseModel):
    name:str
    email:str

class user_response(BaseModel):
    id:int
    name:str
    email:str