# 회원가입, 로그인, 로그아웃 API

from fastapi import APIRouter, Depends

from app.db.database import get_db
from app.schemas.user import UserRegister
from sqlalchemy.orm import Session


router = APIRouter(prefix="/auth")

@router.post("/register")
async def register(user_data: UserRegister, db: Session = Depends(get_db)) :
    """회원가입"""
    