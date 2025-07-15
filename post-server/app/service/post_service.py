
from sqlalchemy.orm import Session
from fastapi import HTTPException, status, UploadFile
from app.db.database import execute_insert
from app.service.s3_service import s3_service

class PostService :
    def __init__(self, db:Session):
        self.db = db

    async def create_post(self, title, content, image, current_user):
        """포스트 생성"""
        # 1. S3에 이미지 업로드 
        image_url = await s3_service.upload_file(image)

        # 2. image_url이 있으니까, db에 인서트 한다.
        sql = """insert into posts
                (title, content, image_url, user_id)
                values
                ( :title , :content, :image_url, :user_id);"""
        execute_insert(sql, {"title":title, 
                             "content": content,
                               "image_url" : image_url,
                                "user_id" :  current_user['id']  })
        # 3. 리턴
        return {'status' : 'success'}
