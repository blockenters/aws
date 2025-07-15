
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    db_host: str  
    db_port: int 
    db_name: str 
    db_user: str  
    db_password: str  

    # JWT
    secret_key: str
    algorithm: str
    access_token_expire_minutes: int

    @property
    def database_url(self):
        return f"mysql+pymysql://{self.db_user}:{self.db_password}@{self.db_host}:{self.db_port}/{self.db_name}"

    class Config:
        env_file = ".env"

settings = Settings()
