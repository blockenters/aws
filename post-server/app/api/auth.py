# 회원가입, 로그인, 로그아웃 API

from fastapi import APIRouter, Depends, status

from app.db.database import get_db
from app.schemas.user import UserLogin, UserRegister
from sqlalchemy.orm import Session

from app.service.auth_service import AuthService


router = APIRouter(prefix="/auth")

@router.post("/login" , status_code=status.HTTP_200_OK)
async def login(user_data: UserLogin, db: Session = Depends(get_db)):
    auth_service = AuthService(db)
    res = auth_service.login_user(user_data)
    return res


@router.post("/register", status_code= status.HTTP_201_CREATED)
async def register(user_data: UserRegister, db: Session = Depends(get_db)) :
    """회원가입"""
    auth_service = AuthService(db)
    res = auth_service.register_user(user_data)
    return res

