from fastapi import APIRouter, Depends, Form, File, HTTPException, UploadFile, status
from sqlalchemy.orm import Session
from app.core.dependencies import get_current_user
from app.db.database import get_db
from app.service.post_service import PostService

router = APIRouter(prefix="/posts")

@router.get("/my", status_code=status.HTTP_200_OK)
async def get_my_posts(page = 1, 
                       size = 10, 
                       current_user = Depends(get_current_user),
                       db = Depends(get_db)):
    """내가 작성한 포스트 리스트 가져오기"""
    post_service = PostService(db)
    posts = post_service.get_user_posts(current_user, page, size)
    return posts


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_post(title:str = Form(...) , 
                      content:str = Form(...), 
                      image:UploadFile = File(...),
                      current_user:dict = Depends(get_current_user),
                       db: Session = Depends(get_db) ) :
    
    post_service = PostService(db)
    res = await post_service.create_post(title, content, image, current_user)
    return res
