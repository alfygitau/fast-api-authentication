from pydantic import BaseModel, Field


class Post(BaseModel):
    id: int = Field(default=None)
    title: str = Field(default=None)
    content: str = Field(default=None)

    class config:
        schema_extra = {
            "post_example": {
                "title": "this is some title of a post",
                "content": "this is the content of a post"
            }
        }
