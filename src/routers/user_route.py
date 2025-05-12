from fastapi import APIRouter, Depends, Body
from typing import Annotated
from sqlalchemy.orm import Session

from ..configurations.database import get_db
from ..schemas.user_schema import UserResponse, UserRetrieveResponse, UserUpdate, DisableUserResponse
from ..services.user_service import UserService


router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router.get("/", response_model=list[UserResponse])
def get_users(db: Session = Depends(get_db)) -> list[UserResponse]:
    service = UserService(db)
    return service.get_users()


@router.get("/{user_id}", response_model=UserRetrieveResponse)
def get_user(user_id: int, db: Session = Depends(get_db)) -> UserRetrieveResponse:
    service = UserService(db)
    return service.get_user(user_id)

@router.put("/", response_model=UserRetrieveResponse)
def update_user(user_id: int, user: Annotated[UserUpdate, Body()], db: Session = Depends(get_db)):
    service = UserService(db)
    return service.update_user(user_id, user)

@router.patch("/disable_user", response_model=DisableUserResponse)
def disable_user(user_id: int, db: Session = Depends(get_db)):
    service = UserService(db)
    return service.disable_user(user_id)

@router.patch("/enable_user", response_model=DisableUserResponse)
def enable_user(user_id: int, db: Session = Depends(get_db)):
    service = UserService(db)
    return service.enable_user(user_id)

@router.delete("/")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    service = UserService(db)
    return service.delete_user(user_id)