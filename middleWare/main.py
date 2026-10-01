from fastapi import FastAPI, Request
import time
import asyncio
app=FastAPI()

@app.get("/")
def get_users():
    return{"message":"Hello World"}

# @app.middleware("http")
# async def my_middleware(request: Request, call_next):
#     print("Before request")
#     response=await call_next(request)
#     print("After request")
#     return response

#Logging middleware
@app.middleware("http")
async def log_requests(request: Request, call_next):
    start_time=time.time()
    response=await call_next(request)
    process_time=time.time()-start_time
    print(f"path:{request.url.path} | Time:{process_time}")
    return response

#Async Wait Function
def task():
    time.sleep(30)
    print("Task Completed")

task() 
   
async def task1():
    await asyncio.sleep(30)
    print("Task Completed")

task1()

  

    
    