from model import Todo
import motor.motor_asyncio
from book_model import Book
from posts.post_model import Post
from auth.auth_model import User, UserLogin
from auth.jwt_handler import generate_token

client = motor.motor_asyncio.AsyncIOMotorClient(
    "mongodb+srv://alfy:12345@commerce.edz8uwx.mongodb.net/?retryWrites=true&w=majority")
database = client.Todolist
collection = database.todo
book_collection = database.books
post_collection = database.posts
user_collection = database.users


async def fetch_one_todo(title):
    document = await collection.find_one({"title": title})
    return document


async def fetch_all_todos():
    todos = list()
    cursor = collection.find({})
    async for document in cursor:
        todos.append(Todo(**document))
    return todos


async def create_a_todo(todo):
    document = todo
    result = await collection.insert_one(document)
    return document


async def update_a_todo(title, description, keywords):
    await collection.update_one({"title": title}, {"$set": {
        "description": description,
        "keywords": keywords
    }})
    document = await collection.find_one({"title": title})
    return document


async def delete_a_todo(title):
    await collection.delete_one({"title": title})
    return True


# books models
async def create_a_book(book: Book):
    document = book
    response = await book_collection.insert_one(book)
    return document

# update a book


async def update_a_book(title,  author, description, tags, no_of_pages):
    await book_collection.update_one({"title": title}, {"$set": {
        "description": description,
        "author": author,
        "no_of_pages": no_of_pages,
        "title": title,
        "tags": tags,
    }})
    document = await book_collection.find_one({"title": title})
    print(document)
    return document


# create a post
async def create_a_post(post: Post):
    document = post
    await post_collection.insert_one(document)
    return document

# register a user


async def register(user: User):
    document = user
    print(document)
    token = generate_token(user["email"])
    await user_collection.insert_one(document)
    return token

# login
async def login(user: UserLogin):
    document = await user_collection.find_one({"email": user["email"]})
    if document:
        return generate_token(document["email"])
    else:
        return {"message":"Invalid user credentials"}
