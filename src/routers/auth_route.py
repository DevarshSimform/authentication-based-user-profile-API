from fastapi import APIRouter, Depends, Form
from sqlalchemy.orm import Session
from typing import Annotated

from ..schemas.auth_schema import RegisterUser, RegisterUserResponse, Token, LoginUser
from ..configurations.database import get_db
from ..services.auth_service import AuthService



router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.post("/register", response_model=RegisterUserResponse)
def register_user(
    user: RegisterUser, 
    db: Session = Depends(get_db)
):
    service = AuthService(db)
    return service.create(user)


@router.post("/login", response_model=Token)
def login_user(user: Annotated[LoginUser, Form()], db: Session = Depends(get_db)) -> Token:
    service = AuthService(db)
    return service.login_user(user)