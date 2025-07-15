# 서비스 : 로직처리

from sqlalchemy.orm import Session

from app.schemas.user import UserRegister

class AuthService:
    def __init__(self, db: Session):
        self.db = db

    def register_user(self, user_data: UserRegister):
        pass
        

