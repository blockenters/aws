
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    db_host: str = "localhost"
    db_port: int = 3306
    db_name: str = "your_database_name"
    db_user: str = "your_username"
    db_password: str = "your_password"

    # JWT
    secret_key: str = "your_secret_key_here_make_it_long_and_random"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30

    # aws
    aws_access_key_id: str = "your_aws_access_key_id"
    aws_secret_access_key: str = "your_aws_secret_access_key"
    aws_region: str = "your_aws_region"
    s3_bucket_name: str = "your_s3_bucket_name"

    @property
    def database_url(self):
        return f"mysql+pymysql://{self.db_user}:{self.db_password}@{self.db_host}:{self.db_port}/{self.db_name}"

    class Config:
        env_file = ".env"

settings = Settings()
