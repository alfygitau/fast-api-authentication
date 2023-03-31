from pydantic import BaseModel


class Book(BaseModel):
    author: str
    title: str
    description: str
    no_of_pages: int
    tags: list[str]
