from fastapi import APIRouter, Depends, Form, HTTPException, UploadFile, status
from sqlalchemy.orm import Session
from app.core.dependencies import get_current_user
from app.db.database import get_db
from app.service.post_service import PostService

router = APIRouter(prefix="/posts")

@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_post(title:str = Form(...) , 
                      content:str = Form(...), 
                      image:UploadFile = Form(...),
                      current_user:dict = Depends(get_current_user),
                       db: Session = Depends(get_db) ) :
    
    post_service = PostService(db)
    res = await post_service.create_post(title, content, image, current_user)
    return res
