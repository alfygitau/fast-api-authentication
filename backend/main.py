from fastapi import FastAPI, HTTPException, Body, Depends
from fastapi.middleware.cors import CORSMiddleware

from database import *
from model import Todo
from book_model import Book
from posts.post_model import Post
from auth.auth_model import User, UserLogin

from auth.jwt_bearer import JWTBearer

app = FastAPI()

origins = ["https://localhost:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.get("/")
def read_root():
    return {"message": "Getting started"}

# get all todos


@app.get("/api/todo", tags=["Todos"])
async def get_all_todos():
    response = await fetch_all_todos()
    return response

# get todo by id


@app.get("/api/todo/{title}", tags=["Todos"], response_model=Todo)
async def get_todo_by_title(title):
    response = await fetch_one_todo(title)
    if response:
        return response
    else:
        raise HTTPException(404, "No todo item with the mentioned title")

# create to do


@app.post("/api/todo", tags=["Todos"], response_model=Todo)
async def create_todo(todo: Todo):
    print(todo.dict())
    response = await create_a_todo(todo.dict())
    if response:
        return response
    else:
        raise HTTPException(400, "Something went wrong")

# upate todo


@app.put("/api/todo/{title}", tags=["Todos"], response_model=Todo)
async def update_todo(title: str, description: str = Body(...), keywords: str = Body(...)):
    response = await update_a_todo(title, description, keywords)
    if response:
        return response
    else:
        raise HTTPException(404, "No todo item with the mentioned title")

# delete todo


@app.delete("/api/todo/{title}", tags=["Todos"])
async def delete_todo(title):
    response = await delete_a_todo(title)
    if response:
        return {"message": "Todo successfully deleted"}
    else:
        raise HTTPException(404, "No todo item with the mentioned title")

    # create a book


@app.post("/api/book", tags=["books"], response_model=Book)
async def create_book(book: Book):
    response = await create_a_book(book.dict())
    return response


# update a book
@app.put("/api/{title}", tags=["books"], response_model=Book)
async def update_book(title: str, author: str = Body(...), description: str = Body(...), tags: list[str] = Body(...), no_of_pages: int = Body(...)):
    response = await update_a_book(title, author, description, tags, no_of_pages)
    return response

# create a post


@app.post("/api/post", dependencies=[Depends(JWTBearer())], tags=["posts"], response_model=Post)
async def create_post(post: Post):
    response = await create_a_post(post.dict())
    return response

# register a user


@app.post("/user/register", tags=["user"])
async def signup(user: User):
    response = await register(user.dict())
    return response


# login
@app.post("/user/login", tags=["user"])
async def signin(user: UserLogin):
    response = await login(user.dict())
    return response
