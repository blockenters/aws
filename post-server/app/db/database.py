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

def execute_query(sql, params) :
    """SQL 쿼리 실행 : select """
    with engine.connect() as connection:
        if params :
            result = connection.execute( text(sql), params )
        else :
            result = connection.execute( text(sql))
        return result.fetchall()
    
def execute_insert(sql, params):
    """디비에 인서트"""
    with engine.connect() as connection :
        with connection.begin():
            if params :
                result = connection.execute( text(sql) , params )
            else :
                result = connection.execute( text(sql) )
            return result.lastrowid