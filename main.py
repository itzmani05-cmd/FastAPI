from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello"}

my_posts = [
    {"title": "title of post 1", "content": "content of post 1", "id": 1},
    {"title": "title of post 2", "content": "content of post 2", "id": 2},
]

class Post(BaseModel):
    title: str
    content: str

@app.post("/posts")
def create_posts(post: Post):
    new_post = {
        "title": post.title,
        "content": post.content,
        "id": len(my_posts) + 1  
    }
    return {"data": new_post}

