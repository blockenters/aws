from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from app.core.config import settings

# 데이터베이스 생성 
engine = create_engine(settings.database_url)

# 세션 로컬 클래스 생성 
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()