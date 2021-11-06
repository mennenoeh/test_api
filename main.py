from typing import Optional
from fastapi import FastAPI, Response
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange

# uvicorn main:app --reload


app = FastAPI()

my_posts = [{"title": "title of post 1", "content": "Content of post 1", "id": 1},
            {"title": "Lieblingsessen", "content": "Pizza", "id": 2}]

class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None

def find_post(id):
    for p in my_posts:
        if p["id"] == id:
            return p

@app.get("/")
async def root():
    return {"message": "welcome to my api!!"}

@app.get("/posts")
def get_posts():
    return {"data": my_posts}

@app.post("/posts")
def create_posts(post: Post):
    post_dict = post.dict()
    post_dict["id"] = randrange(0, 10000000)
    my_posts.append(post_dict)
    return {"data": post_dict}

@app.get("/posts/{id}")
def get_post(id: int):
    post = find_post(id)
    return {"detail": f"hier ist post: {post}"}