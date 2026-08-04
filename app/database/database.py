from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
import os

DATABASE_URL = os.getenv('DATABASE_URL')

engine = create_engine(
    DATABASE_URL
)

# Para comunicar com o mysql : msql+pymysql://usuario:senha@db:3306/terrarium

SessionLocal = sessionmaker(
    autocommit = False,
    autoflush=False,
    bind=engine
)

db = SessionLocal()

Base = declarative_base()

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()