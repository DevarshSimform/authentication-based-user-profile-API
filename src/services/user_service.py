from sqlalchemy.orm import Session

from ..schemas.user_schema import UserResponse, UserRetrieveResponse
from ..repositories.auth_repo import AuthRepository
from ..repositories.user_repo import UserRepository


class UserService:

    def __init__(self, db: Session):
        self.auth_repo = AuthRepository(db)
        self.user_repo = UserRepository(db)

    
    def get_users(self) -> list[UserResponse]:
        return self.user_repo.get_all_users()


    def get_user(self, user_id) -> UserRetrieveResponse:
        user = self.user_repo.get_user_by_id(user_id)
        if not user:
            pass
        return user
    
    
    def update_user(self, user_id, user) -> UserResponse:
        if not self.user_repo.is_user_exist_by_id(user_id):
            pass
        return self.user_repo.update_user_by_id(user_id, user)
    
    
    def disable_user(self, user_id):
        if not self.user_repo.get_user_by_id(user_id):
            pass
        return self.user_repo.disable_user_by_id(user_id)

    
    def enable_user(self, user_id):
        if not self.user_repo.get_user_by_id(user_id):
            pass
        return self.user_repo.enable_user_by_id(user_id)


    def delete_user(self, user_id) -> dict:
        if not self.user_repo.is_user_exist_by_id(user_id):
            pass
        return self.user_repo.delete_user_by_id(user_id)
