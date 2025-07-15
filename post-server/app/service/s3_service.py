
import boto3
from fastapi import HTTPException, UploadFile, status
from app.core.config import settings
import uuid

class S3Service:
    def __init__(self):
        self.s3_client = boto3.client('s3',
                                      aws_access_key_id=settings.aws_access_key_id,
                                      aws_secret_access_key= settings.aws_secret_access_key,
                                      region_name=settings.aws_region)
        self.bucket_name = settings.s3_bucket_name

    async def upload_file(self, file: UploadFile):
        """파일을 s3에 업로드하고 url을 리턴"""
        try:
            # 파일명 검증
            if not file.filename :
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
            
            # 파일 확장자가 이미지파일인지 검증 
            allowed_extenstions = ['jpg', 'jpeg', 'png', 'gif']
            if file.filename.split('.')[-1]  not in allowed_extenstions :
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
            
            # 파일명을 유니크하게 만들어서 s3에 올려야한다.
            new_filename = str(uuid.uuid4()) + '.' + file.filename.split('.')[-1]
            self.s3_client.upload_fileobj(
                file.file,
                self.bucket_name,
                new_filename,
                ExtraArgs={'ContentType' : file.content_type, 'ACL': 'public-read'} 
            )

            return f"https://{self.bucket_name}.s3.{settings.aws_region}.amazonaws.com/{new_filename}"

        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)


s3_service = S3Service()
