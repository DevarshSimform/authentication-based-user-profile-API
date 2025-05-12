from pydantic import BaseModel, EmailStr, Field
from ..models.user_model import RoleEnum
from datetime import datetime


class RegisterUser(BaseModel):
    username: str
    email: EmailStr
    password: str
    confirm_password: str
    firstname: str
    lastname: str
    role: RoleEnum = RoleEnum.user


class RegisterUserResponse(BaseModel):
    username: str
    email: EmailStr
    firstname: str
    lastname: str
    bio: str | None
    profile_picture_url: str | None


class LoginUser(BaseModel):
    email: EmailStr = Field(alias="username")
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str
