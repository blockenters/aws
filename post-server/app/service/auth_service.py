# 서비스 : 로직처리

from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.db.database import execute_query, execute_insert
from app.schemas.user import UserRegister

from app.core.security import get_password_hash

class AuthService:
    def __init__(self, db: Session):
        self.db = db

    def register_user(self, user_data: UserRegister):
        sql = """select *
                from users
                where email = :email ;"""
        existing_user = execute_query(sql, {"email":user_data.email})

        if existing_user :
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)

        # 유저 등록
        # 비번 암호화 부터 한다. 
        hashed_password = get_password_hash(user_data.password)

        sql = """insert into users
                (username, email, password_hash)
                VALUES
                ( :username, :email, :password_hash);"""
        
        execute_insert(sql, {"username" : user_data.username, "email":user_data.email, "password_hash" :  hashed_password })
        
        return { "message": "User registered successfully" }

