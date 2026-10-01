from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI()


#PUT /users/101?nitify=true

# {
#     "name":"Ripon"
# }
users =[]   
class User(BaseModel):
    name:str
    age:int

@app.post("/users")
def create_user(user:User):
    user.append(user)
    return{
        "message":"User Created",
        "data":user
    }


@app.put("/users/{user_id}")
def updated_user(user_id: int, user: User, notify: bool = False):

    if user_id < len(users):
        users[user_id] = user

        return {
            "message": "User Updated",
            "notify": notify,
            "data": user
        }

    return {
        "error": "User not Found"
    }       
        
class UserData(BaseModel):
        name:str
        age:int
        password:str
    
class UserResponse(BaseModel):
        name:str
        age:int 

@app.get("/users-data", response_model=UserResponse)
def get_user():  
        return {
            "name":"Ripon",
            "age":25,
            "password":"123456"
        }
    
                
         
    