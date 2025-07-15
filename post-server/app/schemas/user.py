# 요청 / 응답에 사용되는 json을 클래스로 저장한다.

from pydantic import BaseModel, EmailStr

class UserRegister(BaseModel):
    username : str
    email : EmailStr
    password : str

class UserLogin(BaseModel):
    email : EmailStr
    password : str