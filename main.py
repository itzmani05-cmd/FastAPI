from fastapi import FastAPI

app = FastAPI()

@app.get("/")  
def home():
    return {"message": "Welcome to FastAPI!"}

@app.get("/message")  
def say_hello(name: str):
    return {"message": message}


