from fastapi import FastAPI, Depends, HTTPException,Header, Query, Path, Cookie, Body, Form, File, UploadFile

app = FastAPI()


def common_logic():
    return {
        "message": "Common Logic executed"
    }


@app.get("/home")
def home(data=Depends(common_logic)):
    return data

def verify_token(token:str=Header(None)):
    if token != "mysecrettoken":
        raise HTTPException(status_code=401, detail="Unauthorized")
    return {"message": "Authorized access"}
    

@app.get("/secured-data")
def secured_data(user=Depends(verify_token)):
    return {
        "message": "This is secured data",
        "user": user
    }
