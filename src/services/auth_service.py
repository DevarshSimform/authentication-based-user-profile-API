from sqlalchemy.orm import Session

from ..schemas.auth_schema import RegisterUser, RegisterUserResponse, LoginUser, Token
from ..repositories.auth_repo import AuthRepository
from ..repositories.user_repo import UserRepository
from ..utils.auth_util import create_access_token
from ..exceptions import UserNotFound, UserCreationException



class AuthService:

    def __init__(self, db: Session):
        self.auth_repo = AuthRepository(db)

    def create(self, user: RegisterUser) -> RegisterUserResponse:
        if self.auth_repo.is_user_exist_in_db(user.email, user.username):
            raise UserNotFound()
        return self.auth_repo.create(user)

    def login_user(self, user: LoginUser) -> Token:
        user = self.auth_repo.authenticate_user(user)
        if not user:
            raise UserNotFound()
        access_token = create_access_token(data={"sub": user.email})
        return Token(
            access_token=access_token, token_type="bearer"
        )