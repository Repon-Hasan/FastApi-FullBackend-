from fastapi import FastAPI


app=FastAPI()
#Home
@app.get("/")
def home():
    return{"message":"hello from fast Api"}

#About Route
@app.get("/about")
def about():
      return{"message":"hello from AboutApi"}
  
#Dynamic Routes
@app.get("/user/{user_id}")
def get_user(user_id ):
    return {"user_id": f"User id is {user_id}"}

#Dynamic Routes(data types)
@app.get("/userInt/{user_id}")
def get_user(user_id:int):
    return {"user_id":"User id is {user_id}"}

#Query Parameter /users?name=mohit
#/products?price=1000
@app.get("/params")
def get_users(name: str=None):
    return{"Name":name}

@app.get("/products")
def get_users(limit: int=10):
    return{"limit":limit}

#Multiple Query Params
@app.get("/items")
def get_users(name: str=None,price:int=0):
    return{
        "name":name,
        "price":price
    }


    
    