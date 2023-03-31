from pydantic import BaseModel, Field, EmailStr


class User(BaseModel):
    fullname: str = Field(default=None)
    email: EmailStr = Field(default=None)
    password: str = Field(default=None)

    class config:
        user_schema = {
            "user_example": {
                "fullname": "alfred kariuki",
                "email": "alfygitau@gmail.com",
                "password": "alfred12345"
            }
        }


class UserLogin(BaseModel):
    email: EmailStr = Field(default=None)
    password: str = Field(default=None)

    class config:
        user_schema = {
            "user_example": {
                "email": "alfygitau@gmail.com",
                "password": "alfred12345"
            }
        }
