# 서비스 : 로직처리

from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.db.database import execute_query, execute_insert
from app.schemas.user import UserLogin, UserRegister

from app.core.security import create_access_token, get_password_hash, verify_password

class AuthService:
    def __init__(self, db: Session):
        print("AuthService")
        self.db = db

    def get_user_by_id(self, user_id):
        sql = """select *
                from users
                where id = :user_id  ;"""
        
        print(type(user_id))

        user_result = execute_query(sql, {"user_id" : user_id} )

        if not user_result:
            return None
        
        user = user_result[0]
        return {"id" : user[0], 
                "username" : user[1], 
                "email" : user[2], 
                "created_at":user[4]}

        

    def login_user(self, user_data: UserLogin):
        # 회원가입 한 사람인지 체크 
        sql = """select *
                from users
                where email = :email ;"""
        user_result = execute_query(sql, {"email" : user_data.email}  )

        if not user_result :
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
        
        user = user_result[0]

        user_dict = {"id" : user[0],
                     "username" : user[1],
                     "email" : user[2],
                     "password_hash": user[3]}
        if not verify_password(user_data.password, user_dict['password_hash'] ):
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
        
        # 비번도 맞으면, jwt 토큰 발행.
        access_token = create_access_token({'sub': str(user_dict['id'])})
        return { "access_token": access_token, "token_type": "bearer" }

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

