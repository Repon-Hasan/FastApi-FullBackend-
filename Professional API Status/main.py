from fastapi import FastAPI, HTTPException, Request,status
from fastapi.responses import JSONResponse

app=FastAPI();

@app.post("/create_users",status_code= status.HTTP_201_CREATED)
def create_user():
    return{
        "message":"User Created"
    }


#Custom Status code Response
@app.get("/users")
def get_users():
    return{
        "status":"success",
        "message":"Users List",
        "data":["Ripon","Rifat","Rasel"]
    } 
    
#Error Handling       
@app.get("/users/{user_id}")
def get_user(user_id:int):
    if user_id !=1:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="User Not Found")
    return{
        "user_id":user_id,
        "name":"Ripon HHHHHH"
    }

#Exception Handling
class UserNotFoundException(Exception):
        def __init__(self,name:str):
            self.name=name
            
@app.exception_handler(UserNotFoundException)
def user_not_found_exception_handler(request:Request,exc:UserNotFoundException):
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={
            "message":f"User with name {exc.name} not found"
        }
    )

@app.get("/userD/{name}")
def get_user(name:str):
    if name != "Ripon":
        raise UserNotFoundException(name=name)
    return{
        "name":name,
        "age":25
    }
                
