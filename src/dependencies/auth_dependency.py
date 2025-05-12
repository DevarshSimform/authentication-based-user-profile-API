from typing import Annotated

from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from ..schemas.auth_schema import Token
from ..configurations.database import get_db
from ..utils.auth_util import get_payload
from ..repositories.auth_repo import AuthRepository
from ..models.user_model import User


oauth2_schema = OAuth2PasswordBearer(tokenUrl="/auth/login")


def get_current_user(
    token: Annotated[Token, Depends(oauth2_schema)],
    db: Session = Depends(get_db)
):
    payload = get_payload(token)
    email: str = payload.get("sub")
    if email is None:
        pass
    
    auth_repo = AuthRepository(db)
    user = auth_repo.get_user_by_email(email)
    if not user:
        pass

    return user, db