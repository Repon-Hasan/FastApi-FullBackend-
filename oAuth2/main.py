from fastapi import FastAPI, HTTPException, Depends, Header
from jose import jwt  # type: ignore
from datetime import datetime, timedelta, timezone
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from passlib.context import CryptContext # type: ignore

app=FastAPI();

#JWT CONFIG
SECRET_KEY="mySecretKey"
ALGORITHM="HS256"
ACCESS_TOKEN_EXPIRE_MINUTES=30

#Password hashing
pwd_context=CryptContext(schemes=["bcrypt"], deprecated="auto")

#OAuthSetUp
oauth2_schema=OAuth2PasswordBearer(tokenUrl="login")


#Dummy User Database
fake_users_db={
    "admin":{
        "username":"admin",
        "hashed_password":pwd_context.hash("admin")
    }
}

#hash password
def hash_password(password:str):
    return pwd_context.hash(password)

#verify password
def verify_password(plain_password:str,hashed_password:str):
    return pwd_context.verify(plain_password,hashed_password)


#Create Token
def create_token(data:dict):
    to_encode=data.copy()
    expire=datetime.now(timezone.utc)+timedelta(minutes=15)
    to_encode.update({"exp":expire})
    encoded_jwt=jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)
    return encoded_jwt

#Login Api(Oauth2 Form)
@app.post("/login")
def Login(form_data:OAuth2PasswordRequestForm=Depends()):
    user=fake_users_db.get(form_data.username)
    if not user or not verify_password(form_data.password,user["hashed_password"]):
        raise HTTPException(status_code=401,detail="Invalid username or password")
    access_token=create_token({"sub":form_data.username})
    return {"access_token": access_token, "token_type": "bearer"}

#Token verification
def verify_token(token:str=Depends(oauth2_schema)):
    try:
        payload=jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
        username:str=payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401,detail="Invalid or expire token")
        return username
    except jwt.JWTError:
        raise HTTPException(status_code=401,detail="Invalid or expire token")


#protected route
@app.get("/secure")
def secure_data(username:str=Depends(verify_token)):
    return {"message":"Secure Data Accessed","user":username}
        