# 회원가입, 로그인, 로그아웃 API

from fastapi import APIRouter, Depends, status

from app.db.database import get_db
from app.schemas.user import UserRegister
from sqlalchemy.orm import Session

from app.service.auth_service import AuthService


router = APIRouter(prefix="/auth")

@router.post("/register", status_code= status.HTTP_201_CREATED)
async def register(user_data: UserRegister, db: Session = Depends(get_db)) :
    """회원가입"""
    auth_service = AuthService(db)
    res = auth_service.register_user(user_data)
    return res
