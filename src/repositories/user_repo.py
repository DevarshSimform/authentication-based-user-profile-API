from sqlalchemy.orm import Session

from ..models.user_model import User
from ..schemas.auth_schema import RegisterUser, RegisterUserResponse
from ..schemas.user_schema import UserUpdate


class UserRepository:
    
    def __init__(self, db: Session):
        self.db = db

    
    def is_user_exist_by_id(self, id):
        return True if self.db.query(User).filter_by(id = id).first() else False
    
    def get_all_users(self):
        return self.db.query(User).all()
    
    def get_user_by_id(self, id):
        return self.db.query(User).filter_by(id = id).first()
    
    def get_user_by_username(self, username):
        return self.db.query(User).filter_by(username = username).first()
    
    def disable_user_by_id(self, id):
        db_user = self.db.query(User).filter(User.id == id).first()
        db_user.disabled = True
        self.db.commit()
        self.db.refresh(db_user)
        return db_user
    
    def enable_user_by_id(self, id):
        db_user = self.db.query(User).filter(User.id == id).first()
        db_user.disabled = False
        self.db.commit()
        self.db.refresh(db_user)
        return db_user
    
    def update_user_by_id(self, id, user: UserUpdate):
        db_user = self.db.query(User).filter_by(id = id)
        db_user.update(user.model_dump(exclude_unset=True))
        self.db.commit()
        return db_user.first()

    def delete_user_by_id(self, id):
        db_user = self.db.query(User).filter_by(id = id)
        db_user.delete()
        self.db.commit()
        return {"detail": "User deleted successfully"}
