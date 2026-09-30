from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI()

class User(BaseModel):
    name:str
    age:int
    
@app.post("/create-user")
def create_user(name:str,age:int):
    return{
        "name":name,
        "age":age
    }
    
@app.post("/create-users")
def create_user(user:dict):
    return{
     "message":"User Created",
     "data":user
    }
    
    #Validation
@app.post("/create-users-validate")
def create_user(user:User):
    return{
     "message":"User Created",
     "data":user
    }
    