
from passlib.context import CryptContext
from datetime import datetime, timedelta, timezone
from app.core.config import settings

from jose import jwt, JWTError

pwd_context = CryptContext(schemes=["bcrypt"])

def get_password_hash(password) :
    return pwd_context.hash(password)

def verify_password(plain_password, hashed_password):
    """비번 검증"""
    return pwd_context.verify(plain_password, hashed_password)


def create_access_token(data):
    """JWT 토큰 생성"""
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=settings.access_token_expire_minutes)
    to_encode.update({'exp':expire})
    return jwt.encode(to_encode, settings.secret_key, algorithm=settings.algorithm)

def verify_token(token):
    try : 
        payload = jwt.decode(token, settings.secret_key, algorithms=[settings.algorithm])

        print("sub : " + str(payload.get("sub")))

        user_id = int(payload.get("sub"))
        return user_id
    except (JWTError, ValueError):
        return None