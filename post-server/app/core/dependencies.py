


from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from sqlalchemy.orm import Session

from app.core.security import verify_token
from app.db.database import get_db
from app.service.auth_service import AuthService

security = HTTPBearer()

def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security) , 
                     db : Session = Depends(get_db)):
    """현재 로그인한 유저의 정보 가져오기"""
    token = credentials.credentials
    
    user_id = verify_token(token)

    auth_service = AuthService(db)
    user = auth_service.get_user_by_id(user_id)
    
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)

    return user

