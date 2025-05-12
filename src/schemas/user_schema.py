from pydantic import BaseModel, EmailStr
from ..models.user_model import RoleEnum
from datetime import datetime


class UserResponse(BaseModel):
    email: EmailStr
    username: str
    firstname: str
    lastname: str
    bio: str | None
    profile_picture_url: str | None


class UserRetrieveResponse(UserResponse):
    id: int
    disabled: bool
    created_at: datetime
    updated_at: datetime | None
    last_login: datetime | None


class DisableUserResponse(UserResponse):
    disabled: bool


class UserUpdate(BaseModel):
    firstname: str
    lastname: str
    bio: str | None
    profile_picture_url: str | None
