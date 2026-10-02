from fastapi import FastAPI,File,HTTPException, UploadFile
from fastapi.staticfiles import StaticFiles
import os
import shutil

app=FastAPI()

#Step-1 Ensure Uploads folder exists
UPLOAD_DIR="uploads"
if not os.path.exists(UPLOAD_DIR):
    os.makedirs(UPLOAD_DIR)


#step-2 static file setup
app.mount("/files",StaticFiles(directory=UPLOAD_DIR),name="files")

#step-3 Upload File API
@app.post("/upload")
def upload_file(file:UploadFile=File(...)):
    filename=file.filename  
    file_path=os.path.join(UPLOAD_DIR,filename)
    
    if not filename:
        raise HTTPException(status_code=400,details="File not selected")
    
    with open (file_path,"wb") as buffer:
        shutil.copyfileobj(file.file,buffer)
        
        return{
            "message":"File uploaded successfully",
            "filename":filename,
            "file_url":f"http://127.0.0.1:8000/files/{filename}"
            
        }
        
#step-4 file url api
@app.get("/file/{filename}")
def get_file(filename:str):
    file_path=os.path.join(UPLOAD_DIR,filename)
    
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404,details="File not found")
    
    return {
          "file_url":f"http://127.0.0.1:8000/files/{filename}"
    }

@app.get("/")
def home():
    return{"message":"File Upload API with FastAPI"}
        
            
          