from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

DATABASE_URL = "sqlite:///terrario.db"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread":False}
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