from fastapi import FastAPI, HTTPException, Depends, Header
from jose import jwt  # type: ignore
from datetime import datetime, timedelta, timezone

app=FastAPI();

SECRET_KEY="mySecretKey"

ALGORITHM="HS256"

#Create Token
def create_token(data:dict):
    to_encode=data.copy()
    expire=datetime.now(timezone.utc)+timedelta(minutes=15)
    to_encode.update({"exp":expire})
    encoded_jwt=jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)
    return encoded_jwt

#Login Api
@app.post("/login")
def Login(username:str,password:str):
    if username != "admin" or password != "admin":
        raise HTTPException(status_code=401,detail="Invalid username or password")
    token=create_token({"sub":username})
    return {"access_token": token, "token_type": "bearer"}

#Token verification
def verify_token(token:str=Header(None)):
    try:
        payload=jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
        return payload
    except:
        raise HTTPException(status_code=401,detail="Invalid or expire token")


#protected route
@app.get("/secure")
def secure_data(user=Depends(verify_token)):
    return {"message":"Secure Data Accessed","user":user}
        